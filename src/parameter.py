# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: parameter.py
@time: 2021/7/1 10:05
@description: 求解器和算法参数信息
"""
# 全局变量
# terminal_type = 'G'  # 通用码头，int类型，二选一
terminal_type = 'C'  # 驳船专用码头，int类型，二选一
block_length = 270.0  # 码头单个箱区的长度，float类型，TODO：不适用于洋四、五码头
block_width = 57.0  # 码头单个箱区的宽度，float类型，TODO：不适用于洋四、五码头
block_vertical_num = 3  # 所有码头箱区垂直于岸线的数量，int类型，TODO：不适用于洋四、五码头
block_capacity = 100  # 单个箱区可容纳集装箱的数量，int类型，TODO：需考虑在场箱等估计容量
berth_to_quay_side = 100.0  # 泊位离最靠近岸边的箱区的大概距离（单位：米），float类型
berth_to_berth = 200.0  # 泊位和泊位之间的距离（单位：米），float类型

vessel_num = 10  # 船舶数量（包括干线船、支线船），int类型

time_horizon = 48 * 60  # 规划期时长（单位：分钟），int类型
time_length = 5  # 单个时期的时长，int类型

container_num = 1000  # 中转箱数量，int类型
container_type_ratio = (3, 1)  # 中转箱数量，第一位数字表示国际中转箱的比例，第二位数字表示长江内支线中转箱的比例

mainline_vessel_duration_time = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # 干线船可能在港时间列表，单位：小时
feeder_Vessel_duration_time = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 支线船可能在港时间列表，单位：小时
duration_time_per_container = [5, 6, 7, 8, 9, 10]  # 船舶单个集装箱在港平均需要的时间，单位：分钟


class AlgorithmParameter:

    def __init__(self):

        self.iterations = 2000
