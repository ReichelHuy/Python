import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
data = np.array([[15,1504],[17,1608],[75,7394],[10,831],[50,5507],[35,3011],[90,8612],[80,9036],[5,614],[65,5832]])
area = data[:,0]
price = data[:,1]
plt.xlabel("Dien tich (m2)")
plt.ylabel("Gia nha (tr dong)")
plt.scatter(area,price,color ='red')
regr = linear_model.LinearRegression()
regr.fit(area.reshape(-1,1),price)
plt.plot(area.reshape(-1,1),regr.predict(area.reshape(-1,1)))
#dự đoán giá bất động sản
need_prediction=[19.2,102.5,56.9]
for elem in need_prediction:
    print(regr.predict([[elem]]))