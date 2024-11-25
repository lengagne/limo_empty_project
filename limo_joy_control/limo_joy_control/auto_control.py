
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class AutoControl(Node):

    def __init__(self):
        super().__init__('auto_control')
        self.msg_cmd = Twist()
        self.publisher_ = self.create_publisher(Twist, 'auto_cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publisher_callback)

    def publisher_callback(self):
        self.msg_cmd.linear.x = 0.0
        self.msg_cmd.angular.z = 1.0
        self.publisher_.publish(self.msg_cmd)



def main(args=None):
    rclpy.init(args=args)

    auto_control = AutoControl()

    rclpy.spin(auto_control)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    auto_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
