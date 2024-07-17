#this node takes in the servo's position (either directly by assuming the servo always follows command at first, or later, using more advanced techniques if needed), and based on where the camera is rigidly mounted to the drone, describes the object's location in terms of the drone/global frame.


#TEST TO SEE IF LAUNCH LAUNCHES EVERYTHING
import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('transform')
        self.get_logger().info('Hello from transform')

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()