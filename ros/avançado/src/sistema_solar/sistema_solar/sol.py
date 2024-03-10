from .Planeta import Planeta
import rclpy

class Sol(Planeta):
    def __init__(self):
        self.declare_parameters(
            namespace='', 
            parameters=[
                ('rd', rclpy.Parameter.Type.DOUBLE),
                ('od', rclpy.Parameter.Type.DOUBLE),
                ('p', rclpy.Parameter.Type.DOUBLE)
            ]
        )
        super.__init__('sol',self.get_param('sol_raio'), self.get_param('sol_orbita_dis'),self.get_param('sol_periodo'),'world')


def main():
    rclpy.init()
    sol = Sol()
    rclpy.spin(sol)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
