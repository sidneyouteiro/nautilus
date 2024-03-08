import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.get_logger().info('Subscriber iniciado')
        self._subscription = self.create_subscription(Twist,'vel', self.subscription_callback, 10)
        self._subscription

    def subscription_callback(self,t_msg):
        self.get_logger().info(
                f'vetor velocidade ({t_msg.linear.x},{t_msg.linear.y},{t_msg.linear.z}) ({t_msg.angular.x},{t_msg.angular.y},{t_msg.angular.z})'
        )


def main(args=None):
    rclpy.init(args=args)

    sub = Subscriber()
    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
