import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df =  pd.read_excel("Online Retail.xlsx")
df = df.dropna(subset=['CustomerID'])
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['TotalSpend'] = df['Quantity'] * df['UnitPrice']
customer_df = df.groupby('CustomerID').agg({
    'Quantity': 'sum',
    'UnitPrice': 'mean',
    'TotalSpend': 'sum',
    'Country': 'first'
}).reset_index()
threshold = customer_df['TotalSpend'].median()
customer_df['HighValue'] = (customer_df['TotalSpend'] > threshold).astype(int)
le = LabelEncoder()
customer_df['Country'] = le.fit_transform(customer_df['Country'])
X = customer_df[['Quantity', 'UnitPrice', 'Country']]
y = customer_df['HighValue']
model = DecisionTreeClassifier(criterion='entropy', max_depth=4)
model.fit(X, y)
importance = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importance:\n", importance.sort_values(ascending=False))
plt.figure(figsize=(20,8))
plot_tree(model,
        feature_names=X.columns,
        class_names=['Low','High'],
        filled=True)
plt.title("Customer Segmentation using Decision Tree (ID3)")
plt.show()