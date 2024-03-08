#!/usr/bin/python3

import random
import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.get_logger().info('Publisher iniciado')
        
        self._publisher = self.create_publisher(Twist, "vel", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)


    def timer_callback(self):
        twist_msg = Twist()

        twist_msg.linear.x = random.uniform(-5,5)
        twist_msg.linear.y = random.uniform(-5,5)
        twist_msg.linear.z = random.uniform(-5,5)

        twist_msg.angular.x = random.uniform(-5,5)
        twist_msg.angular.y = random.uniform(-5,5)
        twist_msg.angular.z = random.uniform(-5,5)

        self._publisher.publish(twist_msg)
        self.get_logger().info(f"({twist_msg.linear.x},{twist_msg.linear.y},{twist_msg.linear.z})({twist_msg.angular.x},{twist_msg.angular.y},{twist_msg.angular.z})")




def main(args=None):
    rclpy.init(args=args)
    
    pub = Publisher()
    rclpy.spin(pub)
    
    pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
