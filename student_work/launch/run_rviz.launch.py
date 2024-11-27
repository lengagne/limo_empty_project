from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Déclaration des arguments pour le fichier RViz
    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=os.path.join(
            os.path.dirname(__file__),  # Chemin du fichier de lancement
            '../config/my_rviz_config.rviz'  # Chemin relatif du fichier RViz
        ),
        description='Path to the RViz config file'
    )

    # Node pour lancer RViz2 avec le fichier de configuration
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', LaunchConfiguration('rviz_config')],
        output='screen'
    )

    # Retourne une description de lancement avec l'argument et le nœud RViz
    return LaunchDescription([
        rviz_config_arg,
        rviz_node
    ])
