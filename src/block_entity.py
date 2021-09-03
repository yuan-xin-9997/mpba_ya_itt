# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: block_entity.py
@time: 2021/6/8 16:14
@description:箱区实体
"""


class Block:

    def __init__(self, name, b_id, t_id):

        self.name = name  # 箱区名称="码头name-沿着岸线编号-垂直岸线编号-箱区编号"，str类型
        self.ID = b_id  # 箱区ID="码头id-沿着岸线编号-垂直岸线编号-箱区编号"，str类型
        self.belong_terminal_id = t_id  # 箱区属于的码头的ID，str类型
        self.capacity = ""  # 箱区容量（可容纳的集装箱数量），int类型
        self.x_coordinates = ""  # 箱区左上角x坐标（从左向右沿码头岸线方向，以码头最左上角箱区的最左上角为(0,0)计算，并且泊位在上、箱区在下的视觉）,float类型
        self.y_coordinates = ""  # 箱区左上角y坐标（从上到下海边到箱区，以码头最左上角箱区的最左上角为(0,0)计算，并且泊位在上、箱区在下的视觉），float类型

        self.berths = []  # 关联泊位

        self.handing_time = ""  # 箱区的堆场机械平均装卸时间



