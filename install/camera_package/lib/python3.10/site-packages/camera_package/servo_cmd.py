#this node takes in where the servo should be and sends that command to the actual servo. for now, it is simulated output.


#TEST TO SEE IF LAUNCH LAUNCHES EVERYTHING
import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('simulated_camera_node')
        self.get_logger().info('Hello from servo_cmd')

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()