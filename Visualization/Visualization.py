# Copyright (c) 2023. Salaheldin Mohamed. All rights reserved.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------Data Cleaning--------------------------------------------------- #
# Load sales data
sales_data = pd.read_csv("../RowData/data.csv")
weather_data = pd.read_csv("../RowData/weather.csv")
fuel_data = pd.read_csv("../RowData/fuel_pricing.csv")
merged_data = pd.read_csv("../merged_data.csv")
# ------------------------------------------Data Visualization--------------------------------------------------- #
# 1-Make a chart to illustrate if weekly sales are increasing or decreasing over time.


# Convert 'date' column to datetime
merged_data["Date"] = pd.to_datetime(merged_data["Date"])

# Group the sales Data by week and calculate the total sales for each week
weekly_sales = merged_data.groupby(merged_data["Date"].dt.strftime('%Y-%U'))["Weekly_Sales"].sum()

# Plot the weekly sales
plt.plot(weekly_sales)
plt.title("Weekly Sales Trend")
plt.xlabel("Week")
plt.ylabel("Total Sales")
plt.show()

# --------------------------------------------------------------------------------------------- #
# 2-Make a chart to show how much each brand sells.


# Group the sales data by brand and calculate the total sales for each brad.
brand_sales = merged_data.groupby("Store")["Weekly_Sales"].sum()

# Plot the brand sales
plt.bar(brand_sales.index, brand_sales)
plt.title("Brand Sales")
plt.xlabel("Brand")
plt.ylabel("Total Sales")
plt.show()

# --------------------------------------------------------------------------------------------- #
# 3-Determine the top ten selling stores.

# Group the sales data by store and calculate the total sales for each store.
store_sales = merged_data.groupby("Store")["Weekly_Sales"].sum()

# Sort the store sales in descending order and select the top ten.
top_ten_stores = store_sales.sort_values(ascending=False).head(10)

# Plot the top ten stores
plt.bar(top_ten_stores.index, top_ten_stores)
plt.title("Top Ten Stores")
plt.xlabel("Store")
plt.ylabel("Total Sales")
plt.show()

# --------------------------------------------------------------------------------------------- #
# 4-Make a histogram to show the top 10 stores sales.

# Plot the top ten stores
plt.hist(top_ten_stores, bins=10)
plt.title("Top Ten Stores")
plt.xlabel("Store")
plt.ylabel("Total Sales")
plt.show()

# --------------------------------------------------------------------------------------------- #
# 5-Compare the average weekly sales of the top ten stores in holiday weeks vs. non-holiday weeks.

# create a new column indicating whether a week is a holiday week or not
merged_data['IsHolidayWeek'] = merged_data['Holiday'].apply(lambda x: 'Holiday' if x == True else 'Non-Holiday')

# group the data by store and holiday status, and calculate the average weekly sales for each group
store_sales = merged_data.groupby(['Store', 'IsHolidayWeek'])['Weekly_Sales'].mean().reset_index()

# sort the data by average weekly sales in descending order
store_sales = store_sales.sort_values('Weekly_Sales', ascending=False)

# select the top 10 selling stores
top_stores = store_sales['Store'].unique()[:10]

# filter the data to include only the top 10 selling stores
top_stores_sales = store_sales[store_sales['Store'].isin(top_stores)]

# bar plot to compare the average weekly sales for the top 10 selling stores during holiday & non-holiday weeks.
plt.figure(figsize=(20, 9))
sns.barplot(x='Store', y='Weekly_Sales', hue='IsHolidayWeek', data=top_stores_sales)
plt.title('Average Weekly Sales for Top 10 Selling Stores during Holiday and Non-Holiday Weeks')
plt.xlabel('Store')
plt.ylabel('Average Weekly Sales')
plt.show()

# --------------------------------------------------------------------------------------------- #
# 6-Create a chart that displays the average weekly sales for each brand department for the top 10 selling stores.

# Get the top 10 selling stores
top_stores = merged_data.groupby("Store")["Weekly_Sales"].sum().sort_values(ascending=False).head(10).index.tolist()

# Filter the data to include only the top 10 selling stores
top_stores_data = merged_data[merged_data["Store"].isin(top_stores)]

# calculate the average weekly sales for each brand department for the top 10 selling stores
brand_dept_sales = top_stores_data.groupby(["Store", "Category"])["Weekly_Sales"].mean().reset_index()

# sort the data by average weekly sales in descending order
brand_dept_sales = brand_dept_sales.sort_values("Weekly_Sales", ascending=False)

# bar plot to compare the average weekly sales for each brand department for the top 10 selling stores
plt.figure(figsize=(23, 13))
sns.barplot(x="Store", y="Weekly_Sales", hue="Category", data=brand_dept_sales)
plt.title("Average Weekly Sales for Each Brand Department for the Top 10 Selling Stores")
plt.xlabel("Store")
plt.ylabel('Average Weekly Sales')
# make the legend appear outside the plot area.
plt.legend(bbox_to_anchor=(3.01, 1), loc=2, borderaxespad=0.)
# make legend horizontal
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=25)
plt.show()
# --------------------------------------------------------------------------------------------- #
# 7-Make a line chart to show the relationship between weekly sales and weather Temperature.

# Group the data by temperature and calculate the average weekly sales for each temperature
temp_sales = merged_data.groupby("Temperature")["Weekly_Sales"].mean()

# Plot the relationship between weekly sales and weather temperature
plt.plot(temp_sales)
plt.title("Weekly Sales vs. Temperature")
plt.xlabel("Temperature")
plt.ylabel("Average Weekly Sales")
plt.show()

# --------------------------------------------------------------------------------------------- #
# 8- Make a line chart to show the relationship between fuel cost and weekly sales at different temperatures.

# Group the data by temperature and fuel cost and calculate the average weekly sales for each temperature and fuel cost
temp_fuel_sales = merged_data.groupby(["Temperature", "Fuel_Price"])["Weekly_Sales"].mean().reset_index()

# Plot the relationship between average weekly sales at different fuel costs and temperatures.
plt.figure(figsize=(15, 10))
sns.lineplot(x="Temperature", y="Weekly_Sales", hue="Fuel_Price", data=temp_fuel_sales)
plt.title("Weekly Sales vs. Temperature at Different Fuel Costs")
plt.xlabel("Temperature")
plt.ylabel("Average Weekly Sales")
plt.show()
