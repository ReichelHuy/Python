import numpy as np
import pandas as pd

# Thiết lập số lượng khách hàng
num_customers = 10000

# Tạo dữ liệu khách hàng
np.random.seed(0)

customer_id = np.arange(1, num_customers + 1)
spend = np.random.normal(loc=50, scale=10, size=num_customers)
noise = np.random.normal(loc=0, scale=10, size=num_customers)
frequency = spend + noise

data = pd.DataFrame({'CustomerID': customer_id, 'Spend': spend, 'Frequency': frequency})

# Lưu dữ liệu vào file CSV
data.to_csv('customer_data.csv', index=False)
