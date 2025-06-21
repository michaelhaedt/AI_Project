import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

df = pd.read_csv('Datasets\personality_datasert.csv')



#time_spent_alone_6_10 = df[df['time_spent_alone'] > 6]

#time_pent_alone_0_5 = df[(df['time_spent_alone_0_5'] < 5)]

#time_pent_alone_0_5.to_csv('Datasets\time_spent_alone_0_5.csv', index=False)
#time_spent_alone_6_10.to_csv('Datasets\time_spent_alone_6_10.csv', index=False)

print(df.head())


df.shape
print("hello world")
# If you are seeing weird debugger symbols in your output, it might be due to incorrect usage of print statements.
# For example, `print(df())` should be `print(df)` or `print(df.head())`.
# Also, ensure your file encoding is UTF-8 and your terminal supports Unicode.
# If you are using an IDE, try restarting it or clearing the console.