#this node takes in the camera input and decides where the servo motor should point to keep the object in frame with minimal motion blur and minimal servo lag (understands that servo must move smoothly and can't instantly jump to new position)


#TEST TO SEE IF LAUNCH LAUNCHES EVERYTHING
import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('simulated_camera_node')
        self.get_logger().info('Hello from camera_control')

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()