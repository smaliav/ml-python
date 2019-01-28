# SIMPLE CAR CLASSIFIER
from sklearn import tree

# [HP, NumOfSeats]
features = [
    [300, 2],
    [450, 2],
    [200, 8],
    [150, 9]
]

# 0 - sports-car, 1 - minivan
labels = [
    0,
    0,
    1,
    1
]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print("Input HP:")
hp = input()
print("Input number of seats:")
numOfSeats = input();

prediction = clf.predict([[hp, numOfSeats]])

if (prediction[0] == 0):
    print("It's a sports car!")
else:
    print("It's a minivan!")
