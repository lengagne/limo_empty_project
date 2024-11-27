from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, FindPackageShare
import os

def generate_launch_description():
    # Localisation du dossier de partage de votre paquet
    package_share_directory = FindPackageShare('<votre_package>').find('<votre_package>')

    # Chemin absolu vers le fichier de configuration RViz dans le dossier config du paquet
    rviz_config_file = os.path.join(package_share_directory, 'config', 'rviz2.rviz')

    # Déclaration de l'argument pour le fichier de configuration RViz
    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=rviz_config_file,  # Utilisation du chemin absolu ici
        description='Path to the RViz config file'
    )

    # Node pour lancer RViz2 avec le fichier de configuration spécifié
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', LaunchConfiguration('rviz_config')],
        output='screen'
    )

    return LaunchDescription([
        rviz_config_arg,
        rviz_node
    ])
