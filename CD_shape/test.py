import shapefile
import matplotlib.pyplot as plt
import pandas as pd
import shapely.geometry as geometry
import warnings

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
        
if __name__ == '__main__':

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
    # 遍历每个trip,这一段可以用多进程优化
    with ProcessPoolExecutor(max_workers=worker_num) as executor:
        futures = [executor.submit(process_trip, trip_id) for trip_id in range(len(trip_df))]
        for future in as_completed(futures):
            area_id = future.result()
            if area_id!=-1:
                area[area_id]+=1

    # 将area画出柱状图
    plt.bar(range(area_num), area)
    plt.xticks(range(area_num), [records[i][1] for i in range(area_num)], rotation=90)
    plt.xlabel('区县')
    plt.ylabel('出行次数')
    plt.title('成都市各区县出行次数')
    plt.show()

