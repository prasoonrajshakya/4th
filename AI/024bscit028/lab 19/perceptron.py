import os
os.system("cls")

import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def activation(self, x):
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])

        for epoch in range(self.epochs):
            for i in range(len(X)):
                linear_output = np.dot(X[i], self.weights) + self.bias
                prediction = self.activation(linear_output)

                error = y[i] - prediction

                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

    def predict(self, X):
        predictions = []

        for x in X:
            linear_output = np.dot(x, self.weights) + self.bias
            predictions.append(self.activation(linear_output))

        return np.array(predictions)

# AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y_and = np.array([0, 0, 0, 1])

and_model = Perceptron(learning_rate=0.1, epochs=10)
and_model.fit(X, y_and)

and_predictions = and_model.predict(X)

print("AND Gate")
print("Predictions:", and_predictions)
print("Actual:     ", y_and)

# OR gate
y_or = np.array([0, 1, 1, 1])

or_model = Perceptron(learning_rate=0.1, epochs=10)
or_model.fit(X, y_or)

or_predictions = or_model.predict(X)

print("\nOR Gate")
print("Predictions:", or_predictions)
print("Actual:     ", y_or)