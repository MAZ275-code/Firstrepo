# -*- coding: utf-8 -*-
"""CS620 HW2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZiSLp06e1oYaMUwF61osf1dW3K1cFRy7

###1) Load a data file diamonds.csv from GitHub/course canvas into Pandas DataFrame called “diamond”
"""

import pandas as pd

diamond = pd.read_csv("diamonds.csv")
diamond

"""###2) List the data types of a data frame “diamond”. Also list the last 10 rows/items of it"""

dt = diamond.dtypes
print("Data Types:\n", dt)

lr = diamond.tail(10)
print("Last 10 Rows:\n", lr)

"""###3) Convert the column ‘Price’ values of ‘diamond’ data frame into a NumPy array called “diamond_price” and answer the following:  
###i. What is the middle diamond price/value listed in the “diamond_price” array  
###ii. View the “diamond_price” data in ascending order.  
###iii. The range is the difference between the highest and lowest values within a set of numbers/price/sales. What is the range of the diamond numbers (price) listed in the “diamond_price” array?
"""

import numpy as np

dp = diamond['price'].to_numpy()

mp = np.median(dp)
print("Middle Diamond Price:", mp)

sorted_prices = np.sort(dp)
print("Sorted Prices:\n", sorted_prices)

price_range = np.max(dp) - np.min(dp)
print("Range of Diamond Prices:", price_range)

"""###4) Show the “Premium” type diamonds’ depth, price, and clarity of the data frame “diamond”"""

pdiamonds = diamond[diamond['cut'] == 'Premium'][['depth', 'price', 'clarity']]
print("Premium Diamonds:\n", pdiamonds)

"""###5) Add a new column/attribute called “priceVolatility” in the “diamond” data frame and set its value to 12% of the price. You must use the Lambda function to compute values for “priceVolatility”. Then display the rows 4, 27, and 1221 with selected columns carat, color, and priceVolatility."""

diamond['priceVolatility'] = diamond['price'].apply(lambda x: 0.12 * x)

sr = diamond.loc[[4, 27, 1221], ['carat', 'color', 'priceVolatility']]
print("Selected Rows:\n", sr)

"""###6) Display the summary statistics for clarity “VS1”."""

vs = diamond[diamond['clarity'] == 'VS1'].describe()
print("Summary Statistics for Clarity 'VS1':\n", vs)

"""###7) Add a new column/attribute called “quality” the defines if the diamond is “round diamond” (depth between 54% and 57%) or “princecut diamond” (depth between 68% and 74%). Your code should utilize a user defined/custom function to compute the values for “quality” based on the depth range given."""

def categorize_quality(depth):
    if 54 <= depth <= 57:
        return 'round diamond'
    elif 68 <= depth <= 74:
        return 'princecut diamond'
    else:
        return None

diamond['quality'] = diamond['depth'].apply(categorize_quality)

diamond

"""###8) Fill the missing values of column “quality” by “NaN”."""

diamond['quality'].fillna(value=np.nan, inplace=True)

"""###9) Make a copy of data frame “diamond” called “diamondQ”. Then drop the rows if any of the column in the “diamondQ” has missing values or “NaN”"""

diamondC = diamond.copy()

diamondC.dropna(inplace=True)

diamond

diamondC

