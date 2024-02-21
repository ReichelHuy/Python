import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
a= np.array([0,1,2,3])  # mảng 1 chiều
a1= np.array([0,3,1,2]) 
print(a.ndim)           # in ra số chiều
b = np.array([[0,5,2,3],[4,5,3,6]]) # mảng 2 chiều
print(b.ndim)       
#(a[0][:4]) # Lấy từ 0 -> 4 mặc định : là 0
#(a[0][2:4]) # Lấy từ 2->4
print(a.shape) # in ra số cột =>Result (4,)
print(len(a)) # in ra số hàng => Result 4
c= np.arange(10) # random ra 1 cái mảng
for i in c:
    print(i)
    
print(a-a1) # cộng trừ từng phần thử
print(a*a1) # nhân các phần tử
