import numpy as np
from matplotlib import pyplot as plt # viết ngắn gọn cái thư viện lại 
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
# x = [3,5]
# y = [9,2]
# plt.plot(x,y) # vẽ đường
# plt.show()    #show
image = np.random.rand(30,30) #rand array 30*30
plt.imshow(image) 
plt.show()