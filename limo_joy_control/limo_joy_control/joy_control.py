
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class LimoJoyControl(Node):

    def __init__(self):
        self.msg_cmd = Twist()
        super().__init__('joy_control')
        self.subscription = self.create_subscription(Joy,'/joy',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        

    def listener_callback(self, msg):
        self.msg_cmd.linear.x = msg.axes[1] * 0.2
        self.msg_cmd.angular.z = -(msg.buttons[1] - msg.buttons[3])*2.0
        self.publisher_.publish(self.msg_cmd)



def main(args=None):
    rclpy.init(args=args)

    limo_joy_control = LimoJoyControl()

    rclpy.spin(limo_joy_control)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    limo_joy_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
