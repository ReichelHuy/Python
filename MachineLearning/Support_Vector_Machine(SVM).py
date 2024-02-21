import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
digits = datasets.load_digits()
print(digits.DESCR)
plt.gray()
plt.matshow(digits.images[0])
plt.show()
n = len(digits.images)
data = digits.images.reshape((n,-1))
X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2, shuffle=True)
classifier = svm.SVC()
classifier.fit(X_train,y_train)
predicted = classifier.predict(X_test)
print(metrics.classification_report(y_test, predicted))
