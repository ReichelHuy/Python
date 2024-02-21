import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# Đọc dữ liệu khách hàng từ file CSV
data = pd.read_csv('customer_data.csv')

# Xóa các cột không cần thiết
data = data.drop(['CustomerID'], axis=1)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Áp dụng Hierarchical Clustering
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster_labels = cluster.fit_predict(scaled_data)

# Thêm nhãn phân cụm vào dữ liệu gốc
data['Cluster'] = cluster_labels

# In thông tin về các nhóm khách hàng
for cluster_id in range(2):
    cluster_data = data[data['Cluster'] == cluster_id]
    print(f"Cluster {cluster_id} - Số lượng khách hàng: {len(cluster_data)}")
    print(cluster_data.describe())

# Vẽ biểu đồ các nhóm khách hàng
plt.scatter(data['Spend'], data['Frequency'], c=cluster_labels, cmap='viridis')
plt.xlabel('Số tiền đã chi trả')
plt.ylabel('Tần suất mua hàng')
plt.title('Phân loại khách hàng dựa trên hành vi mua sắm')
plt.show()

