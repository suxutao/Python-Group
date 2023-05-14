import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.datasets import make_blobs
from matplotlib import pyplot
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 生成测试聚类分析代码需要的随机数据
# 生成随机数
data,target=make_blobs(n_samples=100000,n_features=10,centers=10)

# 给随机数定义列名
a = []
for i in range(10):
    a.append('X'+str(i))
data = pd.DataFrame(data)
data.columns = a

# 在二维图中绘制样本，每个样本颜色不同
# 每次只能选取2个特征绘图（二维图像）
pyplot.scatter(data[:,1],data[:,0],c=target);
pyplot.show()
# 输出聚类中心
from sklearn.cluster import KMeans
k = 4 # 定义聚类的类别中心个数，即聚成4类
iteration = 500 # 计算聚类中心的最大循环次数
model = KMeans(n_clusters = k,n_jobs = 4,max_iter = iteration)
model.fit(data)
r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
r = pd.concat([r2,r1],axis=1)
r.columns = list(data.columns)+[u'所属类别数目']
# 给每行数据标记所属类别
r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
r.columns = list(data.columns)+[u'所属类别数目']
