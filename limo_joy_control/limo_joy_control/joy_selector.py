
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class JoySelector(Node):

    def __init__(self):        
        self.mode = 0
        
        self.msg_cmd_manual = Twist()
        self.msg_cmd_auto = Twist()
        
        self.msg_cmd = Twist()
        super().__init__('joy_selector')
        self.subscription_manual = self.create_subscription(Twist,'/manual_cmd_vel',self.listener_manual_callback,10)
        self.subscription_manual  # prevent unused variable warning

        self.subscription_auto = self.create_subscription(Twist,'/auto_cmd_vel',self.listener_auto_callback,10)
        self.subscription_auto  # prevent unused variable warning
        
        self.subscription = self.create_subscription(Joy,'/joy',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        
    def listener_manual_callback(self, msg):
        self.msg_cmd_manual = msg

    def listener_auto_callback(self, msg):
        self.msg_cmd_auto = msg        

    def listener_callback(self, msg):
        
        if msg.buttons[5]:
            self.mode = 0
        if msg.buttons[7]:
            self.mode = 1
            
        if self.mode == 0:
            self.publisher_.publish(self.msg_cmd_manual)
        elif self.mode ==1:
            self.publisher_.publish(self.msg_cmd_auto)
        

def main(args=None):
    rclpy.init(args=args)

    limo_joy_selector = JoySelector()

    rclpy.spin(limo_joy_selector)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    limo_joy_selector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
