# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: berth_entity.py
@time: 2021/6/8 16:14
@description:泊位实体
"""


class Berth:
    """
    申明泊位实体包含的所有属性以及方法
    """

    def __init__(self, name, b_id, t_id, b_type):

        self.name = name  # 泊位名称="码头name-泊位编号"，str类型
        self.ID = b_id  # 泊位ID="码头ID-泊位编号"，str类型
        self.belong_terminal_id = t_id  # 泊位属于的码头的ID，str类型
        self.type = b_type  # 泊位类型，'M'表示干线船泊位，'F'支线船泊位，str类型
        self.x_coordinates = ""  # 泊位x坐标（从左向右沿码头岸线方向，以码头最左上角箱区的最左上角为(0,0)计算，并且泊位在上、箱区在下的视觉）,float类型
        self.y_coordinates = ""  # 泊位y坐标（从左向右沿码头岸线方向，以码头最左上角箱区的最左上角为(0,0)计算，并且泊位在上、箱区在下的视觉）,float类型
        self.depth = ""  # 泊位水深，float类型，未使用

        self.blocks = []  # 关联箱区


if __name__ == '__main__':
    berth = Berth(1, 2, 3, 4)
    print(berth.name)
