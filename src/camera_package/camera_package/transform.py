import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray  # Import Float32MultiArray

class TransformNode(Node):
    def __init__(self):
        super().__init__('transform')
        
        self.subscription = self.create_subscription(
            Float32MultiArray,  # Change message type to Float32MultiArray
            'object_location_cam_ref_frame_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            Float32MultiArray,  # Change message type to Float32MultiArray
            'measured_camera_position_topic',
            self.listener_callback,
            10)
        
        self.subscription2

        self.publisher_ = self.create_publisher(Float32MultiArray, 'object_location_drone_ref_frame_topic', 10)
        timer_period = 0.0166667
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.object_location_drone_ref_frame = [234.567, 0.0, 0.0]  # Initialize as a list for XYZ coordinates

        #unchanging values that describe how the camera moves relative to drone position
        #position difference from servo joint to drone reference frame


    def timer_callback(self):
        msg = Float32MultiArray()  # Change message type to Float32MultiArray
        msg.data = self.object_location_drone_ref_frame  # Set the data to the XYZ values
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%f"' % msg.data)


    def listener_callback(self, msg):
        self.get_logger().info('Received coordinates: x: "%f", y: "%f", z: "%f"' % (msg.data[0], msg.data[1], msg.data[2]))
        

def main(args=None):
    rclpy.init(args=args)
    servo_cmd = TransformNode()
    rclpy.spin(servo_cmd)
    servo_cmd.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
