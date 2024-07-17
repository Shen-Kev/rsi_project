#this node takes in the camera input and decides where the servo motor should point to keep the object in frame with minimal motion blur and minimal servo lag (understands that servo must move smoothly and can't instantly jump to new position)


import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LocalPlannerNode(Node):

    def __init__(self):
        super().__init__('local_planner')
        self.subscription = self.create_subscription(
            String,
            'object_state',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = LocalPlannerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
