#this node simulates the camera output, ouputting the object's x,y position on the frame and its depth relative to the camera frame


import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimulatedCameraNode(Node):

    def __init__(self):
        super().__init__('simulated_camera_node')
        self.publisher_ = self.create_publisher(String, 'object_state', 10)
        timer_period = 0.0166667  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.x = -10.0  # Starting position
        self.y = 0.0   # Fixed y-coordinate
        self.z = 0.0   # Fixed z-coordinate
        self.direction = 1  # Moving in the positive x direction

    def timer_callback(self):
        msg = String()
        if self.x >= 10.0:
            self.direction = -1  # Change direction to negative
        elif self.x <= -10.0:
            self.direction = 1  # Change direction to positive
        self.x += self.direction * 0.1  # Move the object by 0.1 units per timer tick
        msg.data = f'x: {self.x:.4f}, y: {self.y:.4f}, z: {self.z:.4f}'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    simulated_camera_node = SimulatedCameraNode()

    rclpy.spin(simulated_camera_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    simulated_camera_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
