import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Method to load and display data from a csv file
def load_merged_data():
    merged_data = pd.read_csv("../merged_data.csv")
    merged_data["Date"] = pd.to_datetime(merged_data["Date"])
    return merged_data


# 1. Make a chart to illustrate if weekly sales are increasing or decreasing over time.
def plot_weekly_sales_trend(merged_data):
    weekly_sales = merged_data.groupby(merged_data["Date"].dt.strftime('%Y-%U'))["Weekly_Sales"].sum()
    plt.plot(weekly_sales)
    plt.title("Weekly Sales Trend")
    plt.xlabel("Week")
    plt.ylabel("Total Sales")
    plt.show()


# 2. Make a chart to show how much each brand sells.
def plot_brand_sales(merged_data):
    brand_sales = merged_data.groupby("Store")["Weekly_Sales"].sum()
    plt.bar(brand_sales.index, brand_sales)
    plt.title("Brand Sales")
    plt.xlabel("Brand")
    plt.ylabel("Total Sales")
    plt.show()


# 3. Determine the top ten selling stores.
def plot_top_ten_stores(merged_data):
    store_sales = merged_data.groupby("Store")["Weekly_Sales"].sum()
    top_ten_stores = store_sales.sort_values(ascending=False).head(10)
    plt.bar(top_ten_stores.index, top_ten_stores)
    plt.title("Top Ten Stores")
    plt.xlabel("Store")
    plt.ylabel("Total Sales")
    plt.show()


# 4. Make a histogram to show the top 10 stores sales.
def plot_top_ten_stores_histogram(merged_data):
    store_sales = merged_data.groupby("Store")["Weekly_Sales"].sum()
    top_ten_stores = store_sales.sort_values(ascending=False).head(10)
    plt.hist(top_ten_stores, bins=10)
    plt.title("Top Ten Stores")
    plt.xlabel("Store")
    plt.ylabel("Total Sales")
    plt.show()


# 5. Create a chart that compares average weekly sales for the top ten selling stores during holidays and non-holidays.
def plot_holiday_vs_non_holiday_sales(merged_data):
    merged_data['IsHolidayWeek'] = merged_data['Holiday'].apply(lambda x: 'Holiday' if x == True else 'Non-Holiday')
    store_sales = merged_data.groupby(['Store', 'IsHolidayWeek'])['Weekly_Sales'].mean().reset_index()
    store_sales = store_sales.sort_values('Weekly_Sales', ascending=False)
    top_stores = store_sales['Store'].unique()[:10]
    top_stores_sales = store_sales[store_sales['Store'].isin(top_stores)]
    plt.figure(figsize=(15, 9))
    sns.barplot(x='Store', y='Weekly_Sales', hue='IsHolidayWeek', data=top_stores_sales)
    plt.title('Average Weekly Sales for Top 10 Selling Stores during Holiday and Non-Holiday Weeks')
    plt.xlabel('Store')
    plt.ylabel('Average Weekly Sales')
    plt.show()


# 6. Create a chart that displays the average weekly sales for each brand department for the top 10 selling stores.
def plot_brand_dept_sales(merged_data):
    top_stores = merged_data.groupby("Store")["Weekly_Sales"].sum().sort_values(ascending=False).head(10).index.tolist()
    top_stores_data = merged_data[merged_data["Store"].isin(top_stores)]
    brand_dept_sales = top_stores_data.groupby(["Store", "Category"])["Weekly_Sales"].mean().reset_index()
    brand_dept_sales = brand_dept_sales.sort_values("Weekly_Sales", ascending=False)
    plt.figure(figsize=(23, 13))
    sns.barplot(x="Store", y="Weekly_Sales", hue="Category", data=brand_dept_sales)
    plt.title("Average Weekly Sales for Each Brand Department for the Top 10 Selling Stores")
    plt.xlabel("Store")
    plt.ylabel('Average Weekly Sales')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=25)
    plt.show()


# 7. Make a line chart to show the relationship between weekly sales and weather Temperature.
def plot_sales_vs_temperature(merged_data):
    temp_sales = merged_data.groupby("Temperature")["Weekly_Sales"].mean()
    plt.plot(temp_sales)
    plt.title("Weekly Sales vs. Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Average Weekly Sales")
    plt.show()


# 8.	Make a line chart to show the relationship between the cost of fuel and weather weekly sales.
def plot_sales_vs_temp_and_fuel(merged_data):
    temp_fuel_sales = merged_data.groupby(["Temperature", "Fuel_Price"])["Weekly_Sales"].mean().reset_index()
    plt.figure(figsize=(15, 10))
    sns.lineplot(x="Temperature", y="Weekly_Sales", hue="Fuel_Price", data=temp_fuel_sales)
    plt.title("Weekly Sales vs. Temperature at Different Fuel Costs")
    plt.xlabel("Temperature")
    plt.ylabel("Average Weekly Sales")
    plt.show()


# Main method to call all the methods
def main():
    merged_data = load_merged_data()
    plot_weekly_sales_trend(merged_data)
    plot_brand_sales(merged_data)
    plot_top_ten_stores(merged_data)
    plot_top_ten_stores_histogram(merged_data)
    plot_holiday_vs_non_holiday_sales(merged_data)
    plot_brand_dept_sales(merged_data)
    plot_sales_vs_temperature(merged_data)
    plot_sales_vs_temp_and_fuel(merged_data)


# Call the main method to run the program
if __name__ == "__main__":
    main()