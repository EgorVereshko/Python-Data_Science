import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class LinearModel:
    def __init__(self, num_features):
        self.num_features = num_features
        self.weights = np.zeros(num_features)
        self.bias = 0

    def __call__(self, X):
        return np.dot(X, self.weights) + self.bias


class LinearRegressor(LinearModel):
    def fit(self, X, y, learning_rate=0.00001, epochs=10000):
        error_history = []
        for _ in range(epochs):
            predictions = self(X)
            error = y - predictions
            gradient = -2 * np.dot(X.T, error)
            self.weights -= learning_rate * gradient
            self.bias -= learning_rate * np.mean(error)
            current_error = ((y - predictions) ** 2).sum()
            error_history.append(current_error)
        return error_history

    def predict(self, X):
        return self(X)


class LinearClassifier(LinearModel):
    def fit(self, X, y, learning_rate=0.00001, epochs=1000):
        error_history = []
        for _ in range(epochs):
            predictions = self(X)
            sigmoid = 1 / (1 + np.exp(-predictions))
            error = y - sigmoid
            gradient = -np.dot(X.T, error)
            self.weights -= learning_rate * gradient
            self.bias -= learning_rate * np.mean(error)
            current_error = -np.mean(y * np.log(sigmoid) + (1 - y) * np.log(1 - sigmoid))
            error_history.append(current_error)
        return error_history

    def predict(self, X):
        predictions = self(X)
        sigmoid = 1 / (1 + np.exp(-predictions))
        return np.round(sigmoid)

    def predict_proba(self, X):
        predictions = self(X)
        sigmoid = 1 / (1 + np.exp(-predictions))
        return sigmoid


data = pd.read_csv('Student_Performance.csv')
print(data.head())

Y = data['Performance Index']
X = data.drop('Performance Index', axis=1)
X['Extracurricular Activities'] = X['Extracurricular Activities'].replace({'Yes': 1, 'No': 0})
X = X.to_numpy()

print('Среднее по столбцам', X.mean())
print('Стандартное отклонение по столбцам', X.std())

normalized_X = (X - X.mean()) / X.std()
normalized_Y = (Y - Y.mean()) / Y.std()

num_features = normalized_X.shape[1]
lr = LinearRegressor(num_features=num_features)
history = lr.fit(normalized_X, normalized_Y)

epochs = range(1, len(history) + 1)

plt.plot(epochs, history, 'b', label='MSE')
plt.title('График обучения')
plt.xlabel('Эпохи')
plt.ylabel('MSE')
plt.legend()

print(plt.show())
