from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_package',
            #namespace='turtlesim1', no need for namespace since they are different executables
            executable='talker', #this name is defined/taken from the setup.py, on the left side of the equals sign for the entry points
            name='sim'
        ),
        Node(
            package='camera_package',
            #namespace='turtlesim2',
            executable='listener',
            name='sim'
        ),
    ])