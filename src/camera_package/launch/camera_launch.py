from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_package',
            executable='camera_control', 
            name='sim' #idk if i need to have a name but ill keep it for now 
        ),
        Node(
            package='camera_package',
            executable='servo_cmd',
            name='sim'
        ),
        Node(
            package='camera_package',
            executable='simulated_camera_node',
            name='sim'
        ),
        Node(
            package='camera_package',
            executable='transform',
            name='sim'
        ),
    ])