from .Planeta import Planeta
import rclpy

class Lua(Planeta):
    def __init__(self):
        self.declare_parameters(
            namespace='', 
            parameters=[
                ('rd', rclpy.Parameter.Type.DOUBLE),
                ('od', rclpy.Parameter.Type.DOUBLE),
                ('p', rclpy.Parameter.Type.DOUBLE)
            ]
        )
        super.__init__('lua',self.get_param('lua_raio'), self.get_param('lua_orbita_dis'),self.get_param('lua_periodo'),'terra')


def main():
    rclpy.init()
    lua = Lua()
    rclpy.spin(lua)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

