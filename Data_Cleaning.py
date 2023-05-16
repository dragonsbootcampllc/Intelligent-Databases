import pandas as pd


# Method to load and display data from a csv file

def load_and_display_data(file_name):
    # Load data from csv file
    data = pd.read_csv(file_name)
    # Display information about the data
    print(f"\n{file_name} information:")
    print(data.info())
    # Display the first 10 rows of the data
    print(f"\nTop 10 rows of the {file_name}:")
    print(data.head(10))
    # Display basic statistics for numeric columns in the data
    print(f"\nBasic statistics for numeric columns in the {file_name}:")
    print(data.describe())
    return data


# Function to display summary statistics for a column in a data set
def display_summary_statistics(data, column_name):
    # Display summary statistics for the column in the data
    print(f"\nSummary statistics for {column_name}:")
    # Display the mean of the column
    # Mean is the average of the column values
    # The mean is calculated by adding all the values in the column and dividing by the number of values
    print(f"Mean: {data[column_name].mean()}")
    # Display the median of the column
    # Median is the middle value of the column
    # The median is calculated by sorting the values in the column and selecting the middle value
    print(f"Median: {data[column_name].median()}")
    # Display the Count of the column
    # Count is the number of values in the column
    # The count is calculated by counting the number of values in the column
    print(f"Count: {data[column_name].count()}")
    # Display the Standard Deviation of the column
    # Standard Deviation is a measure of how spread out the values in the column are
    # The Standard Deviation is calculated by calculating the square root of the variance
    print(f"Standard deviation: {data[column_name].std()}")


# Function to display the minimum and maximum values for a column in a data set
def display_min_max(data, column_name):
    # Display the minimum value in the column
    # The minimum value is the smallest value in the column
    print(f"\nThe minimum of the {column_name} column is {data[column_name].min():.2f}.")
    # Display the maximum value in the column
    # The maximum value is the largest value in the column
    print(f"The maximum of the {column_name} column is {data[column_name].max():.2f}.")


# Function to check for missing data in a data set
def check_missing_data(data, data_name):
    # Display the number of missing values in each column
    print(f"\nNumber of missing values in {data_name}:")
    print(data.isnull().sum())


# Function to check for incorrect values in a data set
# Incorrect values are values that are less than or equal to 0
def check_incorrect_values(data, data_name):
    print(f"\nIncorrect values in {data_name}:")
    # Loop through each column in the data set
    for col in data.columns:
        # Check if the column is numeric
        if data[col].dtype == "float64":
            # Display the column name
            print(col)
            # Display the incorrect values in the column
            # Incorrect values are values that are less than or equal to 0
            print(data[data[col] <= 0][col])
            # Display the number of incorrect values in the column
            print("Number of incorrect values:")
            print(data[data[col] <= 0][col].count())


# Main function to run the program
def main():
    # Load and display the data from the csv files
    # The data is loaded into a Pandas DataFrame
    # call the load_and_display_data function for each csv file
    sales_data = load_and_display_data("data.csv")
    weather_data = load_and_display_data("weather.csv")
    fuel_data = load_and_display_data("fuel_pricing.csv")

    # Display summary statistics for the numeric columns in the data
    # call the display_summary_statistics function for each data set
    for data, column_name in [(sales_data, "Weekly_Sales"), (weather_data, "Temperature"), (fuel_data, "Fuel_Price")]:
        # call the display_summary_statistics function for each data set
        display_summary_statistics(data, column_name)
        # call the display_min_max function for each data set
        display_min_max(data, column_name)

    # Check for missing data in the data sets
    # call the check_missing_data function for each data set
    for data, data_name in [(sales_data, "sales data"), (weather_data, "weather data"), (fuel_data, "fuel data")]:
        # call the check_missing_data function for each data set
        check_missing_data(data, data_name)
        # call the check_incorrect_values function for each data set
        check_incorrect_values(data, data_name)
        # Remove rows with missing data from the data set
        data.dropna(inplace=True)

    # Merge the data sets into a single data set using
    merged_data = pd.merge(pd.merge(sales_data, weather_data), fuel_data)
    # Save the merged data set to a csv file called merged_data.csv without the index column
    merged_data.to_csv("merged_data.csv", index=False)


# Call the main function to run the program
if __name__ == "__main__":
    main()
