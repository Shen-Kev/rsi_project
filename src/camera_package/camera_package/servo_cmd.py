import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 

#NEED TO ADD CONVERT TO DEG FOR SERVO OUT

class ServoCmdNode(Node):
    def __init__(self):
        super().__init__('servo_cmd')
        self.subscription = self.create_subscription(
            Float32,
            'desired_camera_angle_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning


        self.publisher_ = self.create_publisher(Float32, 'measured_camera_position_topic', 10)
        timer_period = 0.0166667
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.measured_camera_position_rad = 3.14 #RADIANS


    def timer_callback(self):
        msg = Float32()  # Change message type to Float32
        msg.data = float(self.measured_camera_position_rad)  # Set the data to a float value
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.data)


    def listener_callback(self, msg):
        pass
        #msg.data = msg.data + 10.0
        #self.get_logger().info('Servo Ouptut: "%f"' % msg.data)
        

def main(args=None):
    rclpy.init(args=args)
    servo_cmd = ServoCmdNode()
    rclpy.spin(servo_cmd)
    servo_cmd.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()