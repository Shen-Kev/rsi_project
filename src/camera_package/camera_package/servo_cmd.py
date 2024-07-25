#this node takes in where the servo should be and sends that command to the actual servo. for now, it is simulated output.


import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 

class ServoCmdNode(Node):
    def __init__(self):
        super().__init__('servo_cmd')
        self.subscription = self.create_subscription(
            Float32,
            'desired_camera_angle_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
       #msg.data += 10
        self.get_logger().info('Servo Ouptut: "%f"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    servo_cmd = ServoCmdNode()
    rclpy.spin(servo_cmd)
    servo_cmd.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()