# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: container_entity.py
@time: 2021/6/8 16:15
@description:集装箱实体
"""


class Container:

    def __init__(self, name, c_id, c_type, size):

        self.name = name  # 集装箱名称，str类型
        self.ID = c_id  # 集装箱ID，str类型
        self.type = c_type  # 集装箱中转类型，'international'表示国际中转箱，'yangtze'表示长江内支线中转箱，str类型
        self.size = size  # 集装箱尺寸，20尺/40尺，str类型

        self.first_trip_vessel_id = ""  # 一程船ID（Vessel类对象的ID属性），str类型
        self.second_trip_vessel_id = ""  # 二程船ID（Vessel类对象的ID属性），str类型
