Solution for Question 12:


---

Part (a): Which histogram matches the data and why?

The given table represents the number of cars in different price intervals. To match the histogram, you need to observe the frequency of cars in each interval. Here are the key points from the data:

From this table:

Most cars fall in the intervals [27, 34) and [34, 46), with 30 and 29 cars, respectively.

The number of cars decreases as prices increase, especially in intervals [46, 58), [58, 70), and [70, 110).


Answer:
The correct histogram is (iii) because:

The heights of the bars (frequencies) decrease as prices increase, matching the trend in the table.

It reflects the concentration of cars in the middle price intervals and a gradual tapering in higher intervals.



---

Part (b): What does np.percentile(prices, 50) evaluate to and why?

Step 1: Understanding the expression
np.percentile(prices, 50) calculates the 50th percentile (median) of the dataset. The median is the value that separates the lower half and upper half of the data when sorted.

Step 2: Distribution Insight
The dataset has 150 cars in total. The median will be the value at the position:

\text{Median Position} = \frac{150 + 1}{2} = 75.5

Step 3: Cumulative Frequency
To locate the median, we calculate the cumulative frequencies from the table: 
| Interval (Price in $1000) | Number of Cars | Cumulative Frequency | 
|---------------------------|----------------|-----------------------| 
| [10, 22)                 | 26             | 26                    | 
| [22, 27)                 | 25             | 51                    | 
| [27, 34)                 | 30             | 81                    | 
| [34, 46)                 | 29             | 110                   | 
| [46, 58)                 | 14             | 124                   | 
| [58, 70)                 | 14             | 138                   | 
| [70, 110)                | 12             | 150                   |

The 75th and 76th cars fall in the [27, 34) interval because the cumulative frequency reaches 81 in this interval.

Step 4: Median Price
Within the interval [27, 34), prices are evenly distributed. The approximate median price will be around the middle of this range:

\text{Median Price} \approx 30 \text{ (thousands of dollars)}.


---

Final Answer:

Part (a): Histogram (iii) matches the data because it correctly reflects the distribution of car prices.

Part (b): np.percentile(prices, 50) evaluates approximately to 30 (thousands of dollars) because it is the median price based on the cumulative frequency.
