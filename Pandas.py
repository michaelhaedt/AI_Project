import pandas as pd
import os
import numpy as np  
import matplotlib.pyplot as plt
import jaydebeapi as jdbc
import psycopg2
from pathlib import Path  


try:
    conn = psycopg2.connect(
        host="192.168.0.165",
        port=5432,
        database="IDA",
        user="admin",
        password="1qaz!QAZ"
    )
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()


os.makedirs('Datasets', exist_ok=True)  # Ensure the directory exists

filepath_0_5 = Path('Datasets/time_spent_alone_0_5.csv')
filepath_6_10 = Path('Datasets/time_spent_alone_6_10.csv')  

df = pd.read_csv('Datasets\personality_datasert.csv')

time_spent_alone_6_10 = df[(df['Time_spent_Alone']) > 6]

time_pent_alone_0_5 = df[(df['Time_spent_Alone'] < 5)]

time_pent_alone_0_5.to_csv(filepath_0_5)
time_spent_alone_6_10.to_csv(filepath_6_10)

print(df.head())
print('Program completed successfully!')

#print(df.shape())
#print("hello world")
# If you are seeing weird debugger symbols in your output, it might be due to incorrect usage of print statements.
# For example, `print(df())` should be `print(df)` or `print(df.head())`.
# Also, ensure your file encoding is UTF-8 and your terminal supports Unicode.
# If you are using an IDE, try restarting it or clearing the console.