import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster

import math
from geometry_msgs.msg import TransformStamped

class Planeta(Node):
    def __init__(self, nome, raio, orbita_dis, periodo, planeta_pai):
        super.__init__(nome)
        self.nome = nome
        self.raio = raio
        self.orbita_dis = orbita_dis
        self.periodo = periodo
        self.planeta_pai = planeta_pai
        self.angulo = 0
        self.tranform_broadcaster = TransformBroadcaster()

    def get_param(self,x):
        return self.get_parameter(x).get_parameter_value().double_value

    def atualiza_posicao(self):

        ts = TransformStamped()

        ts.header.stamp = self.get_clock().now().to_msg()
        ts.header.frame_id = self.planeta_pai
        ts.header.child_frame_id = self.name

        ts.transform.translation.x = math.cos(self.angulo) * self.orbita_dis
        ts.transform.translation.y = math.sin(self.angulo) * self.orbita_dis
        ts.transform.translation.z = 0
        ts.transform.translation.w = 1.0

        self.transform_broadcaster.sendTransform(ts)

