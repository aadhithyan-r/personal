import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.metrics import mean_squared_error, r2_score
data = load_diabetes()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred_lin = lin_model.predict(X_test)
ridge_alphas = np.logspace(-3, 3, 50)
ridge_model = RidgeCV(alphas=ridge_alphas, cv=5)
ridge_model.fit(X_train, y_train)
y_pred_ridge = ridge_model.predict(X_test)
lasso_model = LassoCV(cv=5, max_iter=10000)
lasso_model.fit(X_train, y_train)
y_pred_lasso = lasso_model.predict(X_test)

models = {
    "Linear": y_pred_lin,
    "Ridge": y_pred_ridge,
    "Lasso": y_pred_lasso
}
print("\nModel Performance:")
print("----------------------------------")
print("Model\t\tMSE\t\tR²")
print("----------------------------------")

for name, y_pred in models.items():
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"{name}\t\t{mse:.4f}\t{r2:.4f}")
print("\nBest Regression coefficients")
print("Ridge Alpha:", ridge_model.alpha_)
print("Lasso Alpha:", lasso_model.alpha_)
plt.figure()
plt.scatter(y_test, y_pred_lin, label="Linear")
plt.scatter(y_test, y_pred_ridge, label="Ridge")
plt.scatter(y_test, y_pred_lasso, label="Lasso")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Comparison")
plt.legend()
plt.show()