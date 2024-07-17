#this node simulates the camera output, ouputting the object's x,y position on the frame and its depth relative to the camera frame




#TEST TO SEE IF LAUNCH LAUNCHES EVERYTHING
import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('simulated_camera_node')
        self.get_logger().info('Hello from simulated_camera_node')

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
