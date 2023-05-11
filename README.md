# Intelligent-Databases
Data Cleaning, Visualization, Modeling
---




# Intelligent Databases Term Project 

	
## You will be given historical sales information for various stores in various geographies. Each store features a variety of categories, each with its own set of weekly sales.

### Note
- Date attributes represents the week
- The term "holiday" relates to whether the week is a special holiday week.

## Question One [Data Cleaning]

Load the sales data from the supplied file"sales .csv", which contains historical sales data from different categories. Load the weather data from the supplied file"weather .csv", shows the average temperature in each retail region over time. Load the fuel pricing data from the supplied file"fuel .csv", which contains historical fuel prices for the region.

Then perform the following functions:

Examine your datasets with Pandas, which displays all columns and their data types, the top ten for each dataset, and basic statistics for numeric columns (Count, mean, std, min, max). Add your comments about the data
Show the missing data and incorrect values for each column, such as zeros or negative sales.
Decide how you want to handle missing and incorrect values and implement it.
Merge all datasets into data frame based on the date and store.

## Question Two [Visualization]


Make a chart to illustrate if weekly sales are increasing or decreasing over time.
Make a chart to show how much each brand sells.
Determine the top ten selling stores.
Make a histogram to show the top 10 stores sales.
Create a chart that compares average weekly sales for the top ten selling stores during holidays and non-holidays.
Create a chart that displays the average weekly sales for each brand department for the top 10 selling stores.
Make a line chart to show the relationship between weekly sales and weather Temperature.
Make a line chart to show the relationship between the cost of fuel and weather weekly sales.





## Question Three [Modeling]

To forecast weekly sales, we need to create a machine learning model:

Divides the data into training and testing categories (80 percent training data and 20 percent testing data).
Create two separate supervised learning models to forecast weekly sales based on specific characteristics.
Compare the accuracy of the two models (in percentages).
Create a clustering model to group together store categories with similar sales. Which number of Clusters is the best? Why?
