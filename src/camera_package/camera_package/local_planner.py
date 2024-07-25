#this node takes in the camera input and decides where the servo motor should point to keep the object in frame with minimal motion blur and minimal servo lag (understands that servo must move smoothly and can't instantly jump to new position)


#ADD AUTO PAN
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
import math

class LocalPlannerNode(Node):

    def __init__(self):
        super().__init__('local_planner')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'object_location_drone_ref_frame_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(Float32, 'desired_camera_angle_topic', 10)
        self.desired_camera_angle = None

    def listener_callback(self, msg):
        x, y, z = msg.data[0], msg.data[1], msg.data[2]
        self.desired_camera_angle = math.atan2(z, x)
        self.publish_desired_camera_angle()

    def publish_desired_camera_angle(self):
        if self.desired_camera_angle is not None:
            msg = Float32()
            msg.data = self.desired_camera_angle
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing desired camera angle: "%f"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    local_planner = LocalPlannerNode()
    rclpy.spin(local_planner)
    local_planner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
