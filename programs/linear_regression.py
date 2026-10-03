import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = fetch_california_housing()
X = data.data[:, [2]] # AveRooms
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print("Model Parameters")
print("-----------------")
print("Slope (Coefficient):", model.coef_)
print("Intercept:", model.intercept_)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("R²:", r2)

plt.xlabel("Average Rooms")
plt.ylabel("Median House Value")
plt.title("Simple Linear Regression ")
plt.scatter(X_test[:50], y_test[:50], color='gray')
plt.plot(X_test[:50], y_pred[:50], color='red')
plt.show()