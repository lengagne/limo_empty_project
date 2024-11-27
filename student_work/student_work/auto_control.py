
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

import random

class AutoControl(Node):

    def __init__(self):
        
        laser_msg = LaserScan()
        
        super().__init__('auto_control')
        self.msg_cmd = Twist()
        self.publisher_ = self.create_publisher(Twist, 'auto_cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publisher_callback)
        
        self.subscription = self.create_subscription(LaserScan,'/scan',self.listener_scan_callback,10)
        self.subscription  # prevent unused variable warning

    def listener_scan_callback(self, msg):
        self.laser_msg = msg


    def publisher_callback(self):
        if (len (self.laser_msg.ranges) ==0):
                self.get_logger().warn("Pas de donnees LaserScan disponibles")
                return
        
        # on recupere une valeur au hasard et on l'affiche
        random_index = random.randint(0, len(self.laser_msg.ranges)-1)
        random_range = self.laser_msg.ranges[random_index]
        random_intensity = self.laser_msg.intensities[random_index]
        self.get_logger().info(f'Valeur du scan index : {random_index} : range={random_range:.2f}   intensity={random_intensity:.2f}')
        
        # on dit au robot de tourner sur lui meme        
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
