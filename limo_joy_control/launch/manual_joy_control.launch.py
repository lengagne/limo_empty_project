from launch import LaunchDescription
from launch_ros.actions import Node
 
 
def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='joy',
                executable='joy_node',
                name='joy',
                ),
            
            Node(
                package='limo_joy_control',
                executable='limo_joy_control',
                name='manual_control',
                )            
            ])
