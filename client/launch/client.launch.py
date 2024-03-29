from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(package = 'client', node_executable = 'client', output = 'screen')
    ])