# 3. Python Loops and Tuples in Analytical Applications
# Objective:

# This assignment is designed to strengthen your expertise in using Python loops and
# tuples, particularly in data analysis and processing scenarios. By completing these 
# tasks, you will gain practical experience in handling and analyzing data using these fundamental Python concepts.

# Task 1: Stock Market Data Analysis Enhance your skills in data manipulation and 
# analysis using tuples and loops.

# Problem Statement: You have been provided with stock market data, 
# where each data point is a tuple containing a company's stock symbol, the date, and 
# the closing price. Your task is to write a function to find the average closing price
# of a specified stock.


stock_datas = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    
]

def average_closing_price(name, stock_datas):
    total_closing_price = 0
    count = 0
    
    for Stock in stock_datas:
        if Stock[0] == name:  # Check if the stock symbol matches
            total_closing_price += Stock[2]  # Add the closing price
            count += 1  # Increment the count
    return total_closing_price / count  # Calculate and return the average closing price

name = "AAPL"#or MSFT
avg_price = average_closing_price(name, stock_datas)
print(f"Average closing price for {name}: {avg_price}")
