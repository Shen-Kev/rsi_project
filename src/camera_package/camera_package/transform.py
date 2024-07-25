
#just rotation for now, but in the future it could be more complex

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import numpy as np

class TransformNode(Node):
    def __init__(self):
        super().__init__('transform')
        
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'object_location_cam_ref_frame_topic',
            self.object_location_callback,
            10)
        
        self.subscription2 = self.create_subscription(
            Float32MultiArray,
            'measured_camera_position_topic',
            self.camera_position_callback,
            10)
        
        self.publisher_ = self.create_publisher(Float32MultiArray, 'object_location_drone_ref_frame_topic', 10)
        timer_period = 0.0166667
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.object_location_cam_ref_frame = None
        self.measured_camera_position = None

    def timer_callback(self):
        if self.object_location_cam_ref_frame is not None and self.measured_camera_position is not None:
            # Perform the transformation
            object_location_drone_ref_frame = self.transform_to_drone_frame(
                self.object_location_cam_ref_frame, self.measured_camera_position)

            msg = Float32MultiArray()
            msg.data = object_location_drone_ref_frame
            self.publisher_.publish(msg)

    def object_location_callback(self, msg):
        self.object_location_cam_ref_frame = msg.data
        self.get_logger().info('Received object location in camera frame: x: "%f", y: "%f", z: "%f"' % (msg.data[0], msg.data[1], msg.data[2]))

    #idk if this ever gets published...
    def camera_position_callback(self, msg):
        self.measured_camera_position = msg.data
        self.get_logger().info('Received camera position: yaw: "%f", pitch: "%f", roll: "%f"' % (msg.data[0], msg.data[1], msg.data[2]))

    def transform_to_drone_frame(self, object_pos, camera_pos):

        # Create rotation matrices

        #just a rotation matrix in pitch for now
        R_pitch = np.array([
            [np.cos(camera_pos), 0, np.sin(camera_pos)],
            [0, 1, 0],
            [-np.sin(camera_pos), 0, np.cos(camera_pos)]
        ])

        # Transform object position
        object_pos_drone_frame = np.dot(R_pitch, object_pos)

        return object_pos_drone_frame.tolist()

def main(args=None):
    rclpy.init(args=args)
    servo_cmd = TransformNode()
    rclpy.spin(servo_cmd)
    servo_cmd.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
