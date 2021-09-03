# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: terminal_entity.py
@time: 2021/6/8 16:12
@description:码头实体
"""


class Terminal:
    """
    申明码头实体包含的所有属性以及方法
    """

    def __init__(self, name, t_id, t_type, m_num, f_num):

        self.name = name  # 码头名称，str类型
        self.ID = t_id  # 码头ID，str类型
        self.type = t_type  # 码头类型，'C'表示驳船码头，'G'表示通用码头，str类型

        self.main_line_berth_num = m_num  # 干线泊位数量，int类型
        self.feeder_berth_num = f_num  # 支线泊位数量，int类型
        self.berth_num = m_num + f_num  # 码头的泊位数量=干线泊位数量+支线泊位数量，int类型
        self.berth_list = []  # 码头有的泊位列表

        self.block_num_along_quay_side = ""  # 沿岸线的方向的箱区数量，int类型
        self.block_num_vertical_quay_side = ""  # 垂直岸线方向的箱区数，int类型
        self.block_num = ""  # 码头的箱区数量=沿岸线的方向的箱区数量*垂直岸线方向的箱区数，int类型，TODO：不适用于洋四、五码头
        self.block_length = ""  # 码头单个箱区的长度，float类型，TODO：不适用于洋四、五码头
        self.block_width = ""  # 码头单个箱区的宽度，float类型，TODO：不适用于洋四、五码头
        self.block_list = []  # 码头箱区列表

        self.gate_coordinates = ""  # 码头道口大门坐标（从左向右沿码头岸线方向，以码头最左上角箱区的最左上角为(0,0)计算，并且泊位在上、箱区在下的视觉）,tuple类型

        self.container_handle_time = 15.0  # 单位：分钟，中转箱从船舶，经岸桥、水平运输设备、场桥，最终到堆场的处理时间，或反过来，float类型
        self.yard_handle_time = 5.0  # 单位：分钟，堆场处理集装箱的时间，float类型

