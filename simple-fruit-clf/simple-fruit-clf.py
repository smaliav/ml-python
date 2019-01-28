# SIMPLE FRUIT CLASSIFIER
from sklearn import tree

# 0 - bumpy, 1 - smooth
features = [
    [140, "1"],
    [130, "1"],
    [150, "0"],
    [170, "0"]
]

# 0 - apple, 1 - orange
labels = [
    0,
    0,
    1,
    1
]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print("Input the weight:")
weight = input()
print("Input the type (0 - bumpy, 1 - smooth):")
type = input();

prediction = clf.predict([[weight, type]])

if (prediction[0] == 0):
    print("It's an apple!")
else:
    print("It's an orrange!")
