#!/usr/bin/python3

import random
import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__():
        super().__init__('publisher')
        self.get_logger().info('Publisher iniciado')
        
        self._publisher = self.create_publisher(Twist, "vel", 10)



def main():
    print('Hi from sensor_velocidade.')


if __name__ == '__main__':
    main()
