from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
           Node(
                package='sistema_solar',
                namespace='sol',
                executable='sol',
                name='sol'
            ),
            Node(
               package='sistema_solar',
               namespace='terra',
               executable='terra',
               name='terra'
            ),
            Node(
                package='sistema_solar',
                namespace='lua',
                executable='lua',
                name='lua'
            )
        ])
