#this node takes in where the servo should be and sends that command to the actual servo. for now, it is simulated output.


#TEST TO SEE IF LAUNCH LAUNCHES EVERYTHING
import rclpy
from rclpy.node import Node

class ServoCmdNode(Node):
    def __init__(self):
        super().__init__('servo_cmd')
        self.get_logger().info('Hello from servo_cmd')

def main(args=None):
    rclpy.init(args=args)
    node = ServoCmdNode()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()