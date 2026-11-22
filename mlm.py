from sklearn.tree import DecisionTreeClassifier

# Features: [weight in grams, texture (0 = smooth, 1 = bumpy)]
fruits = [[140, 0], [130, 0], [150, 1], [170, 1]]
labels = ["apple", "apple", "orange", "orange"]

model = DecisionTreeClassifier()
model.fit(fruits, labels)          # the model learns from data

prediction = model.predict([[160, 1]])
print("Prediction:", prediction[0])
