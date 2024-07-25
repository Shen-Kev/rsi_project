#this node takes in the camera input and decides where the servo motor should point to keep the object in frame with minimal motion blur and minimal servo lag (understands that servo must move smoothly and can't instantly jump to new position)

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 

class LocalPlannerNode(Node):

    def __init__(self):
        super().__init__('local_planner')
        self.subscription = self.create_subscription(
            Float32,
            'object_location_drone_ref_frame_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(Float32, 'desired_camera_angle_topic', 10)
        timer_period = 0.0166667
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.desired_camera_angle = 123.456


    def timer_callback(self):
        msg = Float32()  # Change message type to Float32
        msg.data = float(self.desired_camera_angle)  # Set the data to a float value
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%f"' % msg.data)

    def listener_callback(self, msg):
        pass
        #self.get_logger().info('Received: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    local_planner = LocalPlannerNode()
    rclpy.spin(local_planner)
    local_planner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
