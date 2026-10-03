import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

df = sns.load_dataset('mpg')

df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())

X = df[['displacement']]   
y = df['mpg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

y_pred_lin = lin_model.predict(X_test)

mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

print("Linear Regression:")
print("MSE:", round(mse_lin, 4))
print("R²:", round(r2_lin, 4))

degrees = [2, 3, 5]
models = {}

print("\nPolynomial Regression:")
print("Degree\tMSE\t\tR²")
print("--------------------------------")

for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
   
    X_train_poly = poly.fit_transform(X_train)
   
    X_test_poly = poly.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    y_pred = model.predict(X_test_poly)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(degree ,"\t" ,round(mse,4),"\t" ,round(r2,4))
    
    models[degree] = (model, poly)

plt.figure(figsize=(8, 6))

plt.scatter(X, y, color='blue', s=20, label='Data')

X_range = pd.DataFrame(np.linspace(X['displacement'].min(), X['displacement'].max(), 100),columns=['displacement'])

y_range_lin = lin_model.predict(X_range)
plt.plot(X_range,y_range_lin, color='red', label='Linear')

colors = ['yellow', 'green', 'orange']

for degree, color in zip(degrees, colors):
    model, poly = models[degree]
    X_range_poly = poly.transform(X_range)
    y_range = model.predict(X_range_poly)
    plt.plot(X_range, y_range, color=color, label=f'Degree {degree}')

plt.xlabel("Displacement")
plt.ylabel("MPG")
plt.title("Polynomial vs Linear Regression")
plt.legend()
plt.show()