#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   shape.py
@Time    :   2023/08/01
@Author  :   ChenYiTao 
@Version :   3.9.13 64-bit
@Desc    :   地区分布，不分时间
'''

# 模块导入

import shapefile
import matplotlib.pyplot as plt
import pandas as pd
import shapely.geometry as geometry
import warnings
import time

from concurrent.futures import ProcessPoolExecutor, as_completed

# 设置
plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False # 设置显示负号
warnings.filterwarnings('ignore')

# 常量定义
worker_num = 15  # 进程数可设为逻辑CPU数-1

# 读取数据
file_path = r"CD_shape\data\chengdu\chengdu.shp"
sf = shapefile.Reader(file_path, encoding='gbk') # 读取shp文件
shapes = sf.shapes() # .shapes()读取几何数据信息，存放着该文件中所有对象的 几何数据
records = sf.records() # .records()读取属性数据信息，存放着该文件中所有对象的 属性数据
area_num = len(shapes) # 区域数量
fig, ax = plt.subplots()  # 生成一张图和一张子图
trip_df = pd.read_pickle("GPS_data/trip_df.pkl") # 读取出行数据
wuhou_id = -1
jinjiang_id = -1
# 查找records[i][1]为'武侯区'或'锦江区'的id
for i in range(area_num):
    if records[i][1]=='武侯区':
        wuhou_id = i
    elif records[i][1]=='锦江区':
        jinjiang_id = i
wuhou_shapes = shapes[wuhou_id]
jinjiang_shapes = shapes[jinjiang_id]

# 初始化 trip_df_wuhou 和 trip_df_jinjiang 为与trip_df相同的格式
trip_df_wuhou = pd.DataFrame(columns=trip_df.columns)
trip_df_jinjiang = pd.DataFrame(columns=trip_df.columns)

# 函数定义
def process_trip(trip_id):
    """
    判断trip_df中的每个trip是否在某个区县内
    Args:
        trip_id (int): 当前trip的id
    Returns:
        area_id (int): 当前trip所在区县的id
    """
    if trip_df.iloc[trip_id]['passenger']==0:
        return -1
    for j in range(area_num):
        if geometry.Point(trip_df.iloc[trip_id]['start_longitude'], trip_df.iloc[trip_id]['start_latitude']).within(geometry.shape(shapes[j])):
            return j
    return -1

def count_trips():
    """
    统计每个区县的出行次数
    """
    for i in range(area_num): # 画出成都市所有的区县
        pts = shapes[i].points # 获取每个区县的所有点
        x,y = zip(*pts) # 将所有点的x坐标和y坐标分别提取出来
        ax.plot(x, y, '-', lw=1, color='lightskyblue') # 画出 lw表示线宽
        ax.fill(x, y, color='lightcyan', alpha=0.3) # 填充多边形 alpha表示透明度
        id = records[i][0] # 获取id
        name = records[i][1] # 获取区县名称
        # 获取区县的中心点坐标
        bbox = shapes[i].bbox
        x = (bbox[0] + bbox[2]) / 2
        y = (bbox[1] + bbox[3]) / 2
        # 在每个区县的中心点标注区县名称
        ax.text(x, y, name, fontsize=8, ha='center', va='center', color='k')
    plt.show()
    # plt.savefig('CD_shape/chengdu_city.png', dpi=300,bbox_inches='tight') # 保存图片

    # 判断trip_df中的每个trip是否在某个区县内
    area = [0]*len(shapes) # 用于存放每个区县的出行次数
    start_time = time.time()
    # 遍历每个trip,这一段可以用多进程优化
    with ProcessPoolExecutor(max_workers=worker_num) as executor:
        futures = [executor.submit(process_trip, trip_id) for trip_id in range(len(trip_df))]
        for future in as_completed(futures):
            area_id = future.result()
            if area_id!=-1:
                area[area_id]+=1
    end_time = time.time()
    print('time cost: {:.2f}s'.format(end_time-start_time))

    # 保存area
    pd.to_pickle(area, 'CD_shape/area.pkl')

    # 将area画出柱状图
    plt.bar(range(area_num), area)
    plt.xticks(range(area_num), [records[i][1] for i in range(area_num)], rotation=90)
    plt.xlabel('区县')
    plt.ylabel('出行次数')
    plt.title('成都市各区县出行次数')
    plt.show()
    plt.savefig('CD_shape/area.png', dpi=300,bbox_inches='tight') # 保存图片

def process_trip_dis(trip_id):
    """
    判断trip_df中的每个trip在武侯区还是锦江区中
    Args:
        trip_id (int): 当前trip的id
    Returns:
        area_id (int): 当前trip所在区县的id
    """
    cur_row = trip_df.iloc[trip_id]
    if geometry.Point(cur_row['start_longitude'], cur_row['start_latitude']).within(geometry.shape(wuhou_shapes)) and geometry.Point(cur_row['end_longitude'], cur_row['end_latitude']).within(geometry.shape(wuhou_shapes)):
        return wuhou_id,trip_id
    elif geometry.Point(cur_row['start_longitude'], cur_row['start_latitude']).within(geometry.shape(jinjiang_shapes)) and geometry.Point(cur_row['end_longitude'], cur_row['end_latitude']).within(geometry.shape(jinjiang_shapes)):
        return jinjiang_id,trip_id
    else:
      return -1,trip_id
    
# 主函数    
if __name__ == '__main__':
    # 筛选出武侯区和锦江区的数据,分别记为trip_df_wuhou和trip_df_jinjiang

    # 遍历trip_df，将武侯区和锦江区的数据分别存入trip_df_wuhou和trip_df_jinjiang
    start_time = time.time()
    # 遍历每个trip,这一段可以用多进程优化
    with ProcessPoolExecutor(max_workers=worker_num) as executor:
        results = executor.map(process_trip_dis, range(len(trip_df)))
        # futures = [executor.submit(process_trip_dis, trip_id) for trip_id in range(len(trip_df))]
        # for future in as_completed(futures):
        #     area_id,trip_id = future.result()
        #     if area_id == wuhou_id:
        #         trip_df_wuhou = pd.concat([trip_df_wuhou, trip_df.iloc[trip_id]], ignore_index=True)
        #     elif area_id == jinjiang_id:
        #         trip_df_jinjiang = pd.concat([trip_df_jinjiang, trip_df.iloc[trip_id]], ignore_index=True)
    for area_id,trip_id in results:
        if area_id == -1:
            continue
        # 以DataFrame取出一行数据
        new_row = trip_df.iloc[trip_id]
        # 将new_row添加到trip_df_wuhou或trip_df_jinjiang中
        if area_id == wuhou_id:
            trip_df_wuhou = trip_df_wuhou.append(new_row, ignore_index=True)
        elif area_id == jinjiang_id:
            trip_df_jinjiang = trip_df_jinjiang.append(new_row, ignore_index=True)
            
    end_time = time.time()
    print('time cost: {:.2f}s'.format(end_time-start_time))

    # 保存trip_df_wuhou和trip_df_jinjiang
    trip_df_wuhou.to_csv('CD_shape/trip_df_wuhou.csv', index=False)
    trip_df_jinjiang.to_csv('CD_shape/trip_df_jinjiang.csv', index=False)