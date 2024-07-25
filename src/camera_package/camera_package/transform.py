#this node takes in the servo's position (either directly by assuming the servo always follows command at first, or later, using more advanced techniques if needed), and based on where the camera is rigidly mounted to the drone, describes the object's location in terms of the drone/global frame.



import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 

class TransformNode(Node):
    def __init__(self):
        super().__init__('transform')
        
        self.subscription = self.create_subscription(
            #ITS NOT A FLOAT, IT HAS XYZ JUST LIKE IN SIMULATED_CAMERA_NODE.PY- WILL NEED OT CHNAGE
            Float32,
            'object_location_cam_ref_frame_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            Float32,
            'measured_camera_position_topic',
            self.listener_callback,
            10)
        
        self.subscription2


        #ITS NOT A FLOAT, IT HAS XYZ JUST LIKE IN SIMULATED_CAMERA_NODE.PY- WILL NEED OT CHNAGE
        self.publisher_ = self.create_publisher(Float32, 'object_location_drone_ref_frame_topic', 10)
        timer_period = 0.0166667
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.object_location_drone_ref_frame = 234.567


    def timer_callback(self):
        msg = Float32()  # Change message type to Float32
        msg.data = float(self.encoder_value)  # Set the data to a float value
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%f"' % msg.data)


    def listener_callback(self, msg):
        #msg.data = msg.data + 10.0
        self.get_logger().info('Servo Ouptut: "%f"' % msg.data)
        

def main(args=None):
    rclpy.init(args=args)
    servo_cmd = ServoCmdNode()
    rclpy.spin(servo_cmd)
    servo_cmd.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()