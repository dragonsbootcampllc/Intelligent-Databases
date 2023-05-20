import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

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

    # Prepare the data for XGBoost
    def create_features_targets(data, look_back=1):
        X, y = [], []
        for i in range(look_back, len(data)):
            X.append(data[i - look_back:i])
            y.append(data[i])
        return np.array(X), np.array(y)

    # Define the number of time stepsto look back for each prediction
    look_back = 12

    # Create the features and targets for the training data
    X_train, y_train = create_features_targets(train_data, look_back)

    # Create the features and targets for the testing data
    X_test, y_test = create_features_targets(test_data, look_back)

    # Define the XGBoost model parameters
    xgb_params = {
        'n_estimators': 100,
        'max_depth': 5,
        'learning_rate': 0.1,
        'min_child_weight': 1,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'objective': 'reg:squarederror'
    }

    # Fit the XGBoost model
    model = XGBRegressor(**xgb_params)
    model.fit(X_train, y_train)

    # Make predictions on the testing data
    predictions = model.predict(X_test)

    # Print the accuracy metrics (MAE, MSE, RMSE)
    print("MAE: ", mean_absolute_error(y_test, predictions))
    print("MSE: ", mean_squared_error(y_test, predictions))
    print("RMSE: ", np.sqrt(mean_squared_error(y_test, predictions)))

    # Plot the predictions vs the actual values
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test_data.index[look_back:], y_test, label='Actual')
    ax.plot(test_data.index[look_back:], predictions, label='Predicted')
    ax.legend()
    plt.show()

    # Calculate accuracy as a percentage
    accuracy = 1 - (np.abs(predictions - y_test) / y_test)

    print("Best accuracy satisfied ", "store:", store, "category:", category, "accuracy", accuracy.mean() * 100)


get_best_accuracy()
