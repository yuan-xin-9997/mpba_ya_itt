# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: unit_test.py
@time: 2021/6/8 16:08
@description:仅供单元测试使用。
"""
import time
import random
from terminal_entity import Terminal
from berth_entity import Berth
from block_entity import Block
from vessel_entity import Vessel
from container_entity import Container
from parameter import *


def time_it(func):
    """记时装饰器函数"""

    def inner():
        start = time.time()
        func()
        end = time.time()
        print("程序用时：{}".format(end - start))

    return inner


# @time_it
def data_generation():
    """
    生成两种模式的码头、泊位、箱区、船舶、集装箱数据
    :return: 
    """
    # 生成码头对象
    if terminal_type == 'G':  # 通用码头
        terminal_12 = Terminal("洋山一二期码头", 't_12', 'G', 6, 6)
        terminal_3 = Terminal("洋山三期码头", 't_3', 'G', 5, 4)
        terminal_4 = Terminal("洋山四期码头", 't_4', 'G', 5, 4)
        terminal_5 = Terminal("洋山五期码头", 't_5', 'G', 5, 4)
        terminal_list = [terminal_12, terminal_3, terminal_4, terminal_5]
    elif terminal_type == 'C':  # 驳船专用码头
        terminal_12 = Terminal("洋山一二期码头", 't_12', 'G', 9, 0)
        terminal_3 = Terminal("洋山三期码头", 't_3', 'G', 7, 0)
        terminal_4 = Terminal("洋山四期码头", 't_4', 'G', 7, 0)
        terminal_5 = Terminal("洋山五期码头", 't_5', 'C', 0, 15)
        terminal_list = [terminal_12, terminal_3, terminal_4, terminal_5]
    else:
        raise Exception("洋山五期码头类型标识{}错误！".format(terminal_type))
    for terminal in terminal_list:
        terminal.block_length = block_length
        terminal.block_width = block_width
        terminal.block_num_along_quay_side = terminal.berth_num  # 假设：泊位数量=沿岸线的箱区数量
        terminal.block_num_vertical_quay_side = block_vertical_num  # 假设：所有码头垂直岸线的箱区数量均相等
        terminal.block_num = terminal.block_num_along_quay_side * terminal.block_num_vertical_quay_side

    # 生成所有码头的泊位对象
    for terminal in terminal_list:
        accumulated_x = 0.0
        if terminal.main_line_berth_num > 0:
            for m in range(terminal.main_line_berth_num):
                berth_name = terminal.name + '-' + str(m)
                berth_id = terminal.ID + '-' + str(m)
                berth = Berth(berth_name, berth_id, terminal.ID, 'M')
                berth.x_coordinates = accumulated_x
                berth.y_coordinates = - berth_to_quay_side
                terminal.berth_list.append(berth)
                accumulated_x += berth_to_berth
        if terminal.feeder_berth_num > 0:
            for f in range(terminal.feeder_berth_num):
                berth_name = terminal.name + '-' + str(f)
                berth_id = terminal.ID + '-' + str(f)
                berth = Berth(berth_name, berth_id, terminal.ID, 'F')
                berth.x_coordinates = accumulated_x
                berth.y_coordinates = - berth_to_quay_side
                terminal.berth_list.append(berth)
                accumulated_x += berth_to_berth  # 假设：支线泊位均在干线泊位右边（泊位在上，箱区在下的视觉）

    # 生成所有码头的箱区对象
    for terminal in terminal_list:
        block_no = 0
        accumulated_x = 0.0
        for b1 in range(terminal.block_num_along_quay_side):
            accumulated_y = 0.0
            for b2 in range(terminal.block_num_vertical_quay_side):
                block_name = terminal.name + '-' + str(b1) + '-' + str(b2) + '-' + str(block_no)
                block_id = terminal.ID + '-' + str(b1) + '-' + str(b2) + '-' + str(block_no)
                block = Block(block_name, block_id, terminal.ID)
                block.capacity = block_capacity
                block_no += 1
                block.x_coordinates = accumulated_x
                block.y_coordinates = accumulated_y
                accumulated_y += terminal.block_width
                terminal.block_list.append(block)
                terminal.berth_list[b1].blocks.append(block)  # 假设：泊位关联箱区，此语句基于假设“泊位数量=研岸线的箱区数量”
            accumulated_x += terminal.block_length
        # 计算码头道口大门的位置
        terminal.gate_coordinates = (accumulated_x / 2, accumulated_y + terminal.block_width)

    # 生成距离矩阵（码头之间大门的距离），使用Google Earth测量的洋山四个码头道口与道口之间的道路距离（单位：米）
    terminal_distance_matrix = {
        (terminal_12.ID, terminal_12.ID): 0.0,
        (terminal_3.ID, terminal_3.ID): 0.0,
        (terminal_4.ID, terminal_4.ID): 0.0,
        (terminal_5.ID, terminal_5.ID): 0.0,

        (terminal_12.ID, terminal_3.ID): 1630.0,  # 洋一二->洋三
        (terminal_3.ID, terminal_12.ID): 4822.0,  # 洋三->洋一二

        (terminal_12.ID, terminal_4.ID): 4763.0,  # 洋一二->洋四
        (terminal_4.ID, terminal_12.ID): 4730.0,  # 洋四->洋一二

        (terminal_12.ID, terminal_5.ID): 2590.0,  # 洋一二->洋五
        (terminal_5.ID, terminal_12.ID): 4109.0,  # 洋五->洋一二

        (terminal_3.ID, terminal_4.ID): 7306.0,  # 洋三->洋四
        (terminal_4.ID, terminal_3.ID): 7201.0,  # 洋四->洋三

        (terminal_3.ID, terminal_5.ID): 910.0,  # 洋三->洋五
        (terminal_5.ID, terminal_3.ID): 1619.0,  # 洋五->洋三

        (terminal_4.ID, terminal_5.ID): 7906.0,  # 洋四->洋五
        (terminal_5.ID, terminal_4.ID): 6522.0,  # 洋五->洋四

    }

    # 生成距离矩阵（任意箱区之间的距离，取决于是否同一码头，若同一码头直接用曼哈顿距离，否则根据terminal_distance_matrix）
    block_distance_matrix = {}
    for terminal1 in terminal_list:
        # 同一码头内部箱区的距离（不区分方向）
        for b1 in terminal1.block_list:
            for b2 in terminal1.block_list:
                block_distance_matrix[b1.ID, b2.ID] = abs(b1.x_coordinates - b2.x_coordinates) + \
                                                      abs(b2.y_coordinates - b2.y_coordinates)
        # 不同码头间箱区的距离（区分方向）
        for terminal2 in terminal_list:
            if terminal1 != terminal2:
                for b1 in terminal1.block_list:
                    for b2 in terminal1.block_list:
                        block_distance_matrix[b1.ID, b2.ID] = terminal_distance_matrix[terminal1.ID, terminal2.ID] + \
                                                              abs(b1.x_coordinates - terminal1.gate_coordinates[0]) + \
                                                              abs(b1.y_coordinates - terminal1.gate_coordinates[1]) + \
                                                              abs(b2.x_coordinates - terminal2.gate_coordinates[0]) + \
                                                              abs(b2.y_coordinates - terminal2.gate_coordinates[1])

    # 生成泊位和箱区之间的距离矩阵（只定义同一码头的，不区分方向）
    berth_block_distance_matrix = {}
    for terminal in terminal_list:
        for berth in terminal.berth_list:
            for block in terminal.block_list:
                berth_block_distance_matrix[berth.ID, block.ID] = abs(berth.x_coordinates - block.x_coordinates) + \
                                                                  abs(berth.y_coordinates - block.y_coordinates)
                berth_block_distance_matrix[block.ID, berth.ID] = abs(berth.x_coordinates - block.x_coordinates) + \
                                                                  abs(berth.y_coordinates - block.y_coordinates)

    # 生成时期集合
    time_period = []
    assert time_horizon % time_length == 0
    for i in range(int(time_horizon / time_length)):
        time_period.append(i)
    time_period = tuple(time_period)  # tuple类型，元素为时期id，每一时期长度为time_length

    # 生成船舶对象（假设干线船：支线船=1:1）
    assert vessel_num % 2 == 0  # 确保船舶数量为偶数
    vessel_list = []
    mainline_vessel_list = []
    feeder_vessel_list = []
    for v in range(vessel_num):
        if v < vessel_num / 2:  # 干线船
            vessel_name = "干线船-{}".format(v)
            vessel_id = "mainline-vessel-{}".format(v)
            vessel = Vessel(vessel_name, vessel_id, 'M')
            vessel_list.append(vessel)
            mainline_vessel_list.append(vessel)
        else:
            vessel_name = "干线船-{}".format(v)
            vessel_id = "mainline-vessel-{}".format(v)
            vessel = Vessel(vessel_name, vessel_id, 'F')
            vessel_list.append(vessel)
            feeder_vessel_list.append(vessel)

    # 生成集装箱对象
    container_list = []
    international_container_list = []
    yangtze_container_list = []
    for c in range(container_num):
        if c < container_num * (container_type_ratio[0] / (container_type_ratio[0] + container_type_ratio[1])):  # 国际中转箱
            container_name = "国际水水中转箱-{}".format(c)
            container_id = "international-{}".format(c)
            container = Container(container_name, container_id, 'international', '20')
            # 为当前集装箱分配一二程船（随机从mainline_vessel_list中选择两艘不同的船）
            trip_vessel = random.sample(mainline_vessel_list, 2)
            container.first_trip_vessel_id = trip_vessel[0].ID
            container.second_trip_vessel_id = trip_vessel[1].ID
            container_list.append(container)
            international_container_list.append(container)
            # 更新被分配船舶的（container_first_trip和container_second_trip属性）
            trip_vessel[0].container_first_trip.append(container)
            trip_vessel[1].container_second_trip.append(container)
        else:  # 长江内支线中转箱
            container_name = "长江内支线水水中转箱-{}".format(c)
            container_id = "yangtze-{}".format(c)
            container = Container(container_name, container_id, 'yangtze', '20')
            # 为当前集装箱分配一二程船（分别从mainline_vessel_list和feeder_vessel_list各随机选一艘船）
            trip_vessel = [random.choice(mainline_vessel_list), random.choice(feeder_vessel_list)]
            num = random.random()
            if num <= 0.5:
                container.first_trip_vessel_id = trip_vessel[0].ID
                container.second_trip_vessel_id = trip_vessel[1].ID
                # 更新被分配船舶的（container_first_trip和container_second_trip属性）
                trip_vessel[0].container_first_trip.append(container)
                trip_vessel[1].container_second_trip.append(container)
            else:
                container.first_trip_vessel_id = trip_vessel[1].ID
                container.second_trip_vessel_id = trip_vessel[0].ID
                # 更新被分配船舶的（container_first_trip和container_second_trip属性）
                trip_vessel[1].container_first_trip.append(container)
                trip_vessel[0].container_second_trip.append(container)
            container_list.append(container)
            yangtze_container_list.append(container)

    # 生成船舶对象的estimated_arrival_time、requested_departure_time、duration_time、container_volume属性
    for vessel in vessel_list:
        vessel.container_volume = len(vessel.container_first_trip) + len(vessel.container_second_trip)
        if vessel.type == 'M':
            vessel.duration_time = int(
                (0.5 * 60 * random.choice(mainline_vessel_duration_time) +
                 0.5 * vessel.container_volume * random.choice(duration_time_per_container)) / time_length
            )
            assert vessel.duration_time < len(time_period)
        elif vessel.type == 'F':
            vessel.duration_time = int(
                (0.5 * 60 * random.choice(feeder_Vessel_duration_time) +
                 0.5 * vessel.container_volume * random.choice(duration_time_per_container)) / time_length
            )
            assert vessel.duration_time < len(time_period)
        else:
            raise Exception("船舶类型{}错误！".format(vessel.type))
        vessel.estimated_arrival_time = random.choice(time_period[:(len(time_period) - vessel.duration_time)])
        vessel.requested_departure_time = vessel.estimated_arrival_time + vessel.duration_time
        assert vessel.requested_departure_time <= len(time_period) - 1

    # 生成集卡对象（TODO：是否有必要？）
    # TODO：对上述生成的数据做单元测试，如何做？
    print("数据生成成功，见下方！")

    return terminal_list, berth_block_distance_matrix, block_distance_matrix, time_period, vessel_list, container_list


def main():
    """
    主程序
    """
    # 生成数据
    terminal_list, berth_block_distance_matrix, block_distance_matrix, time_period, vessel_list, container_list = \
        data_generation()


if __name__ == '__main__':
    main()
