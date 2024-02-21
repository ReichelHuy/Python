from sklearn.datasets import load_iris
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split
X,y= load_iris(return_X_y=True)
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
predicted=clf.predict(X_test)
print(metrics.classification_report(y_test,predicted))
import graphviz
dot_data = tree.export_graphviz (clf, out_file=None,feature_names= iris.feature_names , class_names=iris.target_names,filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('tree.gv', view=True)