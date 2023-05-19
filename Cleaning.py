import pandas as pd

# Load sales data
sales_data = pd.read_csv("data.csv")
weather_data = pd.read_csv("weather.csv")
fuel_data = pd.read_csv("fuel_pricing.csv")

# Display information about the sales data
print("Sales data information:")
print(sales_data.info())
print("\nTop 10 rows of the sales data:")
print(sales_data.head(10))
print("\nBasic statistics for numeric columns in the sales data:")
print(sales_data.describe())

# Display information about the weather data
print("\nWeather data information:")
print(weather_data.info())
print("\nTop 10 rows of the weather data:")
print(weather_data.head(10))
print("\nBasic statistics for numeric columns in the weather data:")
print(weather_data.describe())

# Display information about the fuel data
print("\nFuel data information:")
print(fuel_data.info())
print("\nTop 10 rows of the fuel data:")
print(fuel_data.head(10))
print("\nBasic statistics for numeric columns in the fuel data:")
print(fuel_data.describe())

# mean
print("\nMean of the sales data:")
sales_mean = sales_data["Weekly_Sales"].mean()
print(sales_mean)
weather_mean = weather_data["Temperature"].mean()
print(weather_mean)
fuel_mean = fuel_data["Fuel_Price"].mean()
print(fuel_mean)

# median
print("\nMedian of the sales data:")
sales_median = sales_data["Weekly_Sales"].median()
print(sales_median)
weather_median = weather_data["Temperature"].median()
print(weather_median)
fuel_median = fuel_data["Fuel_Price"].median()
print(fuel_median)

# count
print("\nCount of the sales data:")
sales_count = sales_data["Weekly_Sales"].count()
print(sales_count)
weather_count = weather_data["Temperature"].count()
print(weather_count)
fuel_count = fuel_data["Fuel_Price"].count()
print(fuel_count)

# std
print("\nStandard deviation of the sales data:")
sales_std = sales_data["Weekly_Sales"].std()
print(sales_std)
weather_std = weather_data["Temperature"].std()
print(weather_std)
fuel_std = fuel_data["Fuel_Price"].std()
print(fuel_std)

# min
sales_min = sales_data["Weekly_Sales"].min()
print("\nThe minimum of the Weekly_Sales column is {:.2f}.".format(sales_min))
weather_min = weather_data["Temperature"].min()
print("\nThe minimum of the Temperature column is {:.2f}.".format(weather_min))
fuel_min = fuel_data["Fuel_Price"].min()
print("\nThe minimum of the Fuel_Price column is {:.2f}.".format(fuel_min))

# max
sales_max = sales_data["Weekly_Sales"].max()
print("\nThe maximum of the Weekly_Sales column is {:.2f}.".format(sales_max))
weather_max = weather_data["Temperature"].max()
print("\nThe maximum of the Temperature column is {:.2f}.".format(weather_max))
fuel_max = fuel_data["Fuel_Price"].max()
print("\nThe maximum of the Fuel_Price column is {:.2f}.".format(fuel_max))

print("\nMissing data in sales data:")
print(sales_data.isnull().sum())
print("\nMissing data in weather data:")
print(weather_data.isnull().sum())
print("\nMissing data in fuel data:")
print(fuel_data.isnull().sum())

# Show zero and negative values for each column in sales data
print("\nIncorrect values in sales data:")
for col in sales_data.columns:
    if sales_data[col].dtype == "float64":
        print(col)
        print(sales_data[sales_data[col] <= 0][col])
        print("Number of incorrect values:")
        print(sales_data[sales_data[col] <= 0][col].count())

# Show zero and negative values for each column in weather data
print("\nIncorrect values in weather data:")
for col in weather_data.columns:
    if weather_data[col].dtype == "float64":
        print(col)
        print(weather_data[weather_data[col] <= 0][col])
        print("Number of incorrect values:")
        print(weather_data[weather_data[col] <= 0][col].count())

# Show zero and negative values for each column in fuel data
print("\nIncorrect values in fuel data:")
for col in fuel_data.columns:
    if fuel_data[col].dtype == "float64":
        print(col)
        print(fuel_data[fuel_data[col] <= 0][col])
        print("Number of incorrect values:")
        print(fuel_data[fuel_data[col] <= 0][col].count())

sales_data.dropna(inplace=True)
weather_data.dropna(inplace=True)
fuel_data.dropna(inplace=True)

# merge the data sets together
merged_data = pd.merge(sales_data, weather_data)
merged_data = pd.merge(merged_data, fuel_data)

# save the merged data set to a new csv file
merged_data.to_csv("merged_data.csv", index=False)

# see how many null values are in the merged data set
print("\nMissing data in merged data:")
print(merged_data.isnull().sum())

