from launch import LaunchDescription
from launch_ros.actions import Node

#test

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_package',
            executable='local_planner', 
        ),
        Node(
            package='camera_package',
            executable='servo_cmd',
        ),
        Node(
            package='camera_package',
            executable='simulated_camera_node',
        ),
        Node(
            package='camera_package',
            executable='transform',
        ),
    ])