"""
To forecast weekly sales, we need to create a machine learning model:

Divides the data into training and testing categories (80 percent training data and 20 percent testing data). Create
two separate supervised learning models to forecast weekly sales based on specific characteristics. Compare the
accuracy of the two models (in percentages). Create a clustering model to group together store categories with
similar sales. Which number of Clusters is the best? Why?
"""
# import dependencies
import pandas as pd
import numpy as np
import sklearn as skl
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings

warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans

df = pd.read_csv('merged_data.csv')

train, test = train_test_split(df, test_size=0.2)
# model 1
model = LinearRegression()
# model 2 RandomForestModel

model.fit(train[['Weekly_Sales']], train[['Temperature']])
model.score(test[['Weekly_Sales']], test[['Temperature']])
print("score : ", model.score(test[['Weekly_Sales']], test[['Temperature']]))

model.fit(train[['Weekly_Sales']], train[['Fuel_Price']])
model.score(test[['Weekly_Sales']], test[['Fuel_Price']])

print("score : ", model.score(test[['Weekly_Sales']], test[['Fuel_Price']]))

model2 = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=0)
model2.fit(train[['Weekly_Sales']], train[['Temperature']])
model2.score(test[['Weekly_Sales']], test[['Temperature']])
print("score : ", model2.score(test[['Weekly_Sales']], test[['Temperature']]))
model2.fit(train[['Weekly_Sales']], train[['Fuel_Price']])
model2.score(test[['Weekly_Sales']], test[['Fuel_Price']])
print("score : ", model2.score(test[['Weekly_Sales']], test[['Fuel_Price']]))

kmeans = KMeans(n_clusters=3)
kmeans.fit(df[['Weekly_Sales']])
y_km = kmeans.fit_predict(df[['Weekly_Sales']])
print(y_km)

# print accuracy percentage with two decimal places
print("Accuracy: %.2f%%" % (model.score(test[['Weekly_Sales']], test[['Fuel_Price']]) * 100.0))


