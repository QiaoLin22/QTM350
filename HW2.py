from  sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import neighbors
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

x = iris.data
y = iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)

classifier1=tree.DecisionTreeClassifier()

classifier2=neighbors.KNeighborsClassifier()

classifier1.fit(x_train,y_train)
classifier2.fit(x_train,y_train)

predictions=classifier1.predict(x_test)

print(accuracy_score(y_test,predictions))

predictions=classifier2.predict(x_test)

print(accuracy_score(y_test,predictions))
