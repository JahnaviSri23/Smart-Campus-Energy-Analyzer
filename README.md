Algorithm Explanation

1.The program first takes energy readings as input and stores them in a list.
2.It then checks each value using a loop and classifies it into efficient, moderate, high, or invalid.
3.A dictionary is used to store these categories separately for better organization.
4.List comprehension is used to filter out only valid (non-negative) readings.
5.The total energy consumption and number of buildings are calculated and stored in a tuple.
6.Finally, based on different conditions like high usage count, balance, and total consumption, the program decides the campus efficiency.

Personalized Logic (My Thinking)

1.First, I thought that negative energy values don’t make sense, so I treated them as invalid.
2.While calculating total energy, I ignored those invalid values to avoid wrong results.
3.For balanced usage, I didn’t keep it too strict — I allowed a small difference of 1 between efficient and moderate readings.
4.I checked energy waste first because if total consumption is too high, it’s a major issue regardless of other conditions.
5.I used a dictionary to separate the readings into categories so it becomes easy to analyze.
6.I used list comprehension to filter valid readings quickly instead of using another loop.
