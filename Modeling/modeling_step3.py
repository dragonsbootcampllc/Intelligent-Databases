import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import math

# Assuming you have a dataset named "merged_data"
merged_data = pd.read_csv("merged_data.csv")

# Preprocess the data
merged_data['Date'] = pd.to_datetime(merged_data['Date'])
merged_data.set_index('Date', inplace=True)


# Choose a specific store and category to forecast
# run the code untile getting the best accuracy

def get_best_accuracy():
    store = 33
    category = 4
    filtered_data = merged_data[(merged_data['Store'] == store) & (merged_data['Category'] == category)]

    # Split the data into train and test categories (80% and 20%)
    train_data, test_data = train_test_split(filtered_data['Weekly_Sales'], test_size=0.2, shuffle=False)

    # Determine the ARIMA model's parameters (p, d, q) - you can use auto_arima or trial and error
    p, d, q = 1, 2, 2

    # Create and fit the ARIMA
    model = ARIMA(train_data, order=(p, d, q))
    model_fit = model.fit()

    # Make predictions on the testing data
    predictions = model_fit.predict(start=len(train_data), end=len(train_data) + len(test_data) - 1, typ='levels')

    # print the accuracy metrics (MAE, MSE, RMSE)
    print("MAE: ", mean_absolute_error(test_data, predictions))
    print("MSE: ", mean_squared_error(test_data, predictions))
    print("RMSE: ", math.sqrt(mean_squared_error(test_data, predictions)))

    # Plot the predictions vs the actual values
    predictions.plot(legend=True)
    test_data.plot(legend=True)
    plt.show()

    accuracy = 1 - (np.abs(predictions - test_data) / test_data)

    print("Best accuracy satisfied ", "store:", store, "category:", category, "accuracy", accuracy.mean() * 100)


get_best_accuracy()
