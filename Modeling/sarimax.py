import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

# Assuming you have a dataset named "merged_data"
merged_data = pd.read_csv("../merged_data.csv")

# Preprocess the data
merged_data['Date'] = pd.to_datetime(merged_data['Date'])
merged_data.set_index('Date', inplace=True)


# Choose a specific store and category to forecast
# run the code until getting the best accuracy

def get_best_accuracy():
    store = 33
    category = 4
    filtered_data = merged_data[(merged_data['Store'] == store) & (merged_data['Category'] == category)]

    # Split the data into train and test categories (80% and 20%)
    train_data, test_data = train_test_split(filtered_data['Weekly_Sales'], test_size=0.2, shuffle=False)

    # Fit the SARIMA model
    model = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit()

    # Make predictions on the testing data
    predictions = model_fit.forecast(len(test_data))

    # Printthe accuracy metrics (MAE, MSE, RMSE)
    print("MAE: ", mean_absolute_error(test_data, predictions))
    print("MSE: ", mean_squared_error(test_data, predictions))
    print("RMSE: ", np.sqrt(mean_squared_error(test_data, predictions)))

    # Plot the predictions vs the actual values
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test_data.index, test_data.values, label='Actual')
    ax.plot(test_data.index, predictions, label='Predicted')
    ax.legend()
    plt.show()

    # Calculate accuracy as a percentage
    accuracy = 1 - (np.abs(predictions - test_data) / test_data)

    print("Best accuracy satisfied ", "store:", store, "category:", category, "accuracy", accuracy.mean() * 100)


get_best_accuracy()
