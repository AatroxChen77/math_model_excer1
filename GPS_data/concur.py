#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   concur.py
@Time    :   2023/07/28
@Author  :   ChenYiTao 
@Version :   3.9.13 64-bit
@Desc    :   并发技术提高程序运行效率
'''

# 模块导入
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed
from geopy.distance import geodesic
import time
import multiprocessing
import warnings

warnings.filterwarnings('ignore')

# 常量定义
worker_num = 15  # 进程数可设为逻辑CPU数-1

# 变量定义
# 读取pkl文件，得到df_selected
df_selected = pd.read_pickle('GPS_data\\df_selected.pkl')

column_names = [
    'taxi_id', 'passenger', 'start_time', 'end_time', 'start_latitude',
    'start_longitude', 'end_latitude', 'end_longitude', 'distance'
]
# 当passenger列为1时，表示载客，为0时表示无客,以此来把轨迹GPS划分为载客轨迹和无客轨迹
# 并记录载客轨迹和无客轨迹的起始时间和终止时间(s)，起始地点和终止地点、轨迹长度(km)(不是位移)
trip_df = pd.DataFrame(columns=column_names)

# 合并df_selected中连续的载客数据或无客数据，形成一条轨迹
groups = [(cur_taxi, group)
          for cur_taxi, group in df_selected.groupby('taxi_id')]


# 函数定义
# 定义一个函数，用来计算两个经纬度之间的距离
def get_distance(point1, point2):
    """
    计算两个经纬度之间的距离
    :param point1: 起点经纬度 (纬度, 经度)
    :param point2: 终点经纬度 (纬度, 经度)
    :return: 距离（km）
    """
    return geodesic(point1, point2).km


def process_group(cur_taxi, group):
    """
    处理一辆出租车的轨迹数据，将其划分为一条条轨迹，每条轨迹记录其载客情况、起始时间、终止时间、起始地点、终止地点、轨迹长度

    Args:
        cur_taxi (int): 当前出租车的id
        group (DataFrame): 当前出租车的轨迹数据

    Returns:
        result_df (DataFrame): 当前出租车的处理结果，是该出租车的每一段(空驶、载客)轨迹的记录
    """

    result_df = pd.DataFrame(columns=column_names)
    last_row = group.iloc[0].to_dict()
    cur_passenger = last_row['passenger']
    cur_distance = 0
    start_latitude = last_row['latitude']
    start_longitude = last_row['longitude']
    start_time = last_row['time_s']

    for i in range(1, group.shape[0]):  # 从第二行开始遍历
        cur_row = group.iloc[i].to_dict()

        if cur_passenger != cur_row['passenger']:
            # 如果载客情况发生了变化则表示本段轨迹记录完成，记录其终止时间、终止地点
            cur_distance += get_distance(
                (cur_row['latitude'], cur_row['longitude']),
                (last_row['latitude'], last_row['longitude']))
            end_time = last_row['time_s']
            end_latitude = last_row['latitude']
            end_longitude = last_row['longitude']
            new_row = pd.DataFrame({'taxi_id': cur_taxi, 'passenger': cur_passenger, 'start_time': start_time, 'end_time': end_time, \
                                    'start_longitude': start_longitude, 'start_latitude': start_latitude,\
                                    'end_longitude': end_longitude, 'end_latitude': end_latitude, 'distance': cur_distance},index=[0])
            result_df = pd.concat([result_df, new_row], ignore_index=True)
            # 重置轨迹的起始时间、起始地点、载客情况、轨迹长度
            # 轨迹的起始时间
            start_time = cur_row['time_s']
            # 轨迹的起始地点
            start_latitude = cur_row['latitude']
            start_longitude = cur_row['longitude']
            # 轨迹的载客情况
            cur_passenger = cur_row['passenger']
            # 轨迹的长度
            cur_distance = 0
        else:  # 如果载客情况没有发生变化，则添加轨迹长度，继续记录轨迹
            cur_distance += get_distance(
                (cur_row['latitude'], cur_row['longitude']),
                (last_row['latitude'], last_row['longitude']))
        last_row = cur_row

    return result_df


# 主函数
if __name__ == '__main__':
    print(df_selected.info(memory_usage='deep'))
    time_start = time.time()
    # 使用spawn方式创建进程池，避免进程间共享资源的问题

    with ProcessPoolExecutor(
            max_workers=worker_num,
            mp_context=multiprocessing.get_context('spawn')) as executor:
        results = executor.map(process_group,
                               [cur_taxi for cur_taxi, group in groups],
                               [group for cur_taxi, group in groups])
        for result in results:
            trip_df = pd.concat([trip_df, result], ignore_index=True)

    # with ProcessPoolExecutor(max_workers=worker_num) as executor:
    #     futures = [executor.submit(process_group, cur_taxi, group) for cur_taxi, group in groups]
    #     for future in as_completed(futures):
    #         trip_df = pd.concat([trip_df, future.result()], ignore_index=True)

    time_end = time.time()
    trip_df.to_pickle('GPS_data\\trip_df.pkl')
    print('time cost', time_end - time_start, 's')
