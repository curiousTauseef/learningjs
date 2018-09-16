from sklearn import tree
#height, weight, shoe-size
x=[[12, 13, 14], [15,16,17], [14,25,32], [23,21,54], [22, 33, 14], [25,16,27], [24,25,33], [33,21,44]]
y = ['male', 'female', 'female', 'male', 'male', 'female', 'male', 'female' ]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
predict = clf.predict([[11,23,15]])
print predict