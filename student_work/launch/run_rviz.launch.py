from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_directory = get_package_share_directory('student_work')
    package_src = os.path.abspath(os.path.join(package_directory,'../../../../src/limo_empty_project/student_work'))
    rviz_config_path = os.path.join( package_src,'config','rviz2.rviz')
    
    ## Argument pour activer le temps simulé
    #use_sim_time_arg = DeclareLaunchArgument(
        #'use_sim_time',
        #default_value='false',
        #description='Use simulation time if true'
    #)

    # Argument pour le fichier de configuration RViz
    #rviz_config_arg = DeclareLaunchArgument(
        #'rviz_config',
        #default_value=os.path.join(
            #os.path.dirname(__file__),          # changer cette ligne
            #'../config/rviz2.rviz'
        #),
        #description='Path to the RViz config file'
    #)

    # Node pour RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path],
        output='screen',
        
    )

    return LaunchDescription([
        #use_sim_time_arg,
        #rviz_config_arg,
        rviz_node
    ])
