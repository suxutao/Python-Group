import numpy as np
from sklearn.neighbors import NearestNeighbors

# 构造数据
X = np.random.randn(5000, 10)
noise = np.random.randint(10, 20,(50,10))
X = np.concatenate((X, noise), axis=0)

# 计算每个数据点与最近的k个邻居的距离
k = 10
neigh = NearestNeighbors(n_neighbors=k)
neigh.fit(X)
distances, indices = neigh.kneighbors(X)

# 对每个数据点计算平均距离并标记为正常或异常点
mean_distances = np.mean(distances, axis=1)
threshold = np.percentile(mean_distances, 95)
is_anomaly = mean_distances > threshold

# 输出结果
print(f"正常点数量：{len(X[~is_anomaly])}")
print(f"异常点数量：{len(X[is_anomaly])}")
