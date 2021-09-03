# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: vessel_entity.py
@time: 2021/6/8 16:13
@description:船舶实体
"""


class Vessel:
    """
    申明船舶实体包含的所有属性以及方法
    """

    def __init__(self, name, v_id, v_type):
        # 船舶信息
        self.name = name  # 船舶名称，str类型
        self.ID = v_id  # 船舶ID，str类型
        self.type = v_type  # 船舶类型，'M'表示远洋班轮船舶、'F'表示内河驳船，str类型
        self.estimated_arrival_time = ""  # 船舶预计到港时期（时期开始时刻到港），int类型
        self.requested_departure_time = ""  # 船舶要求离港时期（时期开始时刻离港），int类型
        self.duration_time = ""  # 船舶在港时期数，int类型（假设：应该正比于箱量）

        # 中转箱信息
        self.container_volume = ""  # 要在码头装卸的集装箱的集装箱箱量，int类型
        self.container_first_trip = []  # 将当前船舶作为一程船的中转箱列表（Container类对象）
        self.container_second_trip = []  # 将当前船舶作为二程船的中转箱列表（Container类对象）

        # 船舶靠泊信息
        self.terminal_id = ""  # 船舶靠泊码头id，str类型
        self.berth_id = ""  # 船舶靠泊泊位id，str类型
