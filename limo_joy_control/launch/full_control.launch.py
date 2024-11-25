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
                remappings=[('cmd_vel','manual_cmd_vel')]
                ),
            
                         
            Node(
                package='limo_joy_control',
                executable='auto_control',
                name='auto_control',
                ),                   
            Node(
                package='limo_joy_control',
                executable='joy_selector',
                name='joy_selector',
                remappings=[('cmd_vel','joy_cmd_vel')]
                ),                            
            
            Node(
                package='limo_joy_control',
                executable='limo_safe_control',
                name='safe_control',
                ),                 
            ])
