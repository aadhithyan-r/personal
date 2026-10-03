import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

data = fetch_california_housing()
X = data.data[:,2] # AveRooms
y = data.target

X_mean = np.mean(X)
X_std = np.std(X)

X = (X - X_mean) / X_std

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

theta0 = 0
theta1 = 0

learning_rate = 0.01
iterations = 5000

n = len(X_train)

cost_history = []

for i in range(iterations):

    y_pred = theta0 + theta1 * X_train

    error = y_train - y_pred

    d_theta0 = (-1/n) * np.sum(error)

    d_theta1 = (-1/n) * np.sum(error * X_train)

    theta0 = theta0 - learning_rate * d_theta0

    theta1 = theta1 - learning_rate * d_theta1

    cost = (1/(2*n)) * np.sum(error**2)

    cost_history.append(cost)

print("\nMODEL PARAMETERS\n")

print("Theta0 (Intercept):", theta0)

print("Theta1 (Slope):", theta1)

y_pred_final = theta0 + theta1 * X_test

mse = np.mean((y_test - y_pred_final)**2)

SS_res = np.sum((y_test - y_pred_final)**2)

SS_tot = np.sum((y_test - np.mean(y_test))**2)

r2 = 1 - (SS_res / SS_tot)

print("\nEVALUATION METRICS\n")

print("Mean Squared Error (MSE):", round(mse, 4))

print("R² Score:", round(r2, 4))

plt.xlabel("Average Rooms")
plt.ylabel("Median House Value")
plt.title("Simple Linear Regression using Gradient descent")
plt.scatter(X_test[:50], y_test[:50], color='gray')
plt.plot(X_test[:50], y_pred_final[:50], color='red')
plt.show(block=False)

plt.figure(figsize=(8,5))
plt.plot(range(iterations), cost_history,color='green')
plt.title("Cost Function Convergence")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.grid(True)
plt.show()

new_total_rooms = 3
new_total_rooms_normalized = (new_total_rooms - X_mean) / X_std

predicted_value = theta0 + theta1 * new_total_rooms_normalized
print("\nPREDICTION\n")
print("Predicted House Value for",new_total_rooms,"rooms =",round(predicted_value, 2))