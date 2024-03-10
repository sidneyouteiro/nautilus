from .Planeta import Planeta
import rclpy

class Terra(Planeta):
    def __init__(self):
        self.declare_parameters(
            namespace='', 
            parameters=[
                ('rd', rclpy.Parameter.Type.DOUBLE),
                ('od', rclpy.Parameter.Type.DOUBLE),
                ('p', rclpy.Parameter.Type.DOUBLE)
            ]
        )
        super.__init__('terra',self.get_param('terra_raio'), self.get_param('terra_orbita_dis'),self.get_param('terra_periodo'),'sol')


def main():
    rclpy.init()
    terra = Terra()
    rclpy.spin(terra)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
