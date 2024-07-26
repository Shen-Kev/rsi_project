#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from sensor_msgs.msg import Image as ImageMsg
from cv_bridge import CvBridge, CvBridgeError
from softdrone_target_pose_estimator.msg import Keypoints2D, Keypoint2D
import zmq
import base64

class KeypointDetector(Node):
    def __init__(self):
        super().__init__('keypoint_detector')
        self.bridge = CvBridge()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect('tcp://localhost:5555')
        
        self.image_subscription = self.create_subscription(
            ImageMsg,
            '/target_cam/color/image_raw',
            self.image_callback,
            1)
        
        self.kps_publisher = self.create_publisher(Keypoints2D, 'keypoints_out', 10)
        self.annotated_img_publisher = self.create_publisher(ImageMsg, 'annotated_img_out', 10)

    def recv_array(self, socket, flags=0, copy=True, track=False):
        """recv a numpy array"""
        md = socket.recv_json(flags=flags)
        msg = socket.recv(flags=flags, copy=copy, track=track)
        A = np.frombuffer(msg, dtype=md['dtype'])
        return A.reshape(md['shape'])

    def image_callback(self, msg):
        try:
            img = self.bridge.imgmsg_to_cv2(msg, "rgb8")
            self.socket.send(img)
            kps = self.recv_array(self.socket)
            if np.any(kps):
                kps_msg = Keypoints2D()
                kps_msg.header.stamp = msg.header.stamp
                for kp in kps:
                    kp_msg = Keypoint2D()
                    kp_msg.x = kp[0]
                    kp_msg.y = kp[1]
                    kps_msg.keypoints_2D.append(kp_msg)
                self.kps_publisher.publish(kps_msg)

                for kp in kps:
                    img = cv2.circle(img, (kp[0], kp[1]), 2, (255, 0, 0), 2)

                self.annotated_img_publisher.publish(self.bridge.cv2_to_imgmsg(img, "rgb8"))

        except CvBridgeError as e:
            self.get_logger().error(f'CvBridge Error: {e}')

def main(args=None):
    rclpy.init(args=args)
    keypoint_detector = KeypointDetector()
    rclpy.spin(keypoint_detector)
    keypoint_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
