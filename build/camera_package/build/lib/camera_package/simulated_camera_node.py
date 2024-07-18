#this node simulates the camera output, ouputting the object's x,y position on the frame and its depth relative to the camera frame



import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import random


class SimulatedCameraNode(Node):

    def __init__(self):
        super().__init__('simulated_camera_node')
        self.publisher_ = self.create_publisher(String, 'object_state', 10)
        timer_period = 0.0166667  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        x = random.uniform(-10.0, 10.0)
        y = random.uniform(-10.0, 10.0)
        z = random.uniform(-10.0, 10.0)
        msg.data = f'x: {x:.4f}, y: {y:.4f}, z: {z:.4f}'
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    simulated_camera_node = SimulatedCameraNode()

    rclpy.spin(simulated_camera_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    simulated_camera_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

