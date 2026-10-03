import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
data = load_breast_cancer()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
mle_model = LogisticRegression(penalty='none', max_iter=5000)
mle_model.fit(X_train, y_train)
l2_model = LogisticRegression(penalty='l2', C=1.0, max_iter=5000)
l2_model.fit(X_train, y_train)
l1_model = LogisticRegression(penalty='l1',solver='liblinear', C=1.0)
l1_model.fit(X_train, y_train)
y_pred_mle = mle_model.predict(X_test)
y_pred_l2 = l2_model.predict(X_test)
y_pred_l1 = l1_model.predict(X_test)
print("\n=== Accuracy ===")
print("MLE Accuracy:", accuracy_score(y_test, y_pred_mle))
print("L2 MAP Accuracy:", accuracy_score(y_test, y_pred_l2))
print("L1 MAP Accuracy:", accuracy_score(y_test, y_pred_l1))
print("\n=== Classification Report: MLE ===")
print(classification_report(y_test, y_pred_mle))
print("\n=== Classification Report: L2 MAP ===")
print(classification_report(y_test, y_pred_l2))
print("\n=== Classification Report: L1 MAP ===")
print(classification_report(y_test, y_pred_l1))
plt.figure()
plt.plot(np.abs(mle_model.coef_[0]), label="MLE")
plt.plot(np.abs(l2_model.coef_[0]), label="L2 (MAP)")
plt.plot(np.abs(l1_model.coef_[0]), label="L1 (MAP)")
plt.xlabel("Feature Index")
plt.ylabel("Coefficient Magnitude")
plt.title("Coefficient Comparison: MLE vs MAP")
plt.legend()
plt.grid()
plt.show()