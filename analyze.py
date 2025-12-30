import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel('xiaohongshu_data.csv')

print("=" * 60)
print("1. 基本统计信息")
print("=" * 60)
print(f"\n数据形状: {df.shape[0]} 行, {df.shape[1]} 列")
print(f"\n列名: {list(df.columns)}")
print(f"\n数据类型:\n{df.dtypes}")
print(f"\n前5行数据:\n{df.head()}")
print(f"\n数值列统计描述:\n{df.describe()}")
