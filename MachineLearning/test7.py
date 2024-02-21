import numpy as np
from sklearn.neighbors import KNeighborsClassifier

n_train, n_test, k = map(int, input().split())

train_data = []
train_labels = []

for i in range(n_train):
    x, y, label = map(int, input().split())
    train_data.append([x, y])
    train_labels.append(label)

test_data = []

for i in range(n_test):
    x, y, a = map(int, input().split())
    test_data.append([x, y, a])

knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(train_data, train_labels)

test_data = np.array(test_data)

predicted_labels = knn.predict(test_data[:, :2])

for label in predicted_labels:
    print(label)
