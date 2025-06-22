import pandas as pd
import csv
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

print(df.shape)

time_spent_alone_6_10 = df[(df['Time_spent_Alone']) > 6]

print(time_spent_alone_6_10.shape)

time_spent_alone_0_5 = df[(df['Time_spent_Alone'] < 5)]
print(time_spent_alone_0_5.shape)
time_spent_alone_0_5.to_csv(filepath_0_5)
time_spent_alone_6_10.to_csv(filepath_6_10)

print(df.head())

cursor = conn.cursor()

csv_data = csv.reader(open('Datasets/personality_datasert.csv', 'r'))

with open('Datasets\personality_datasert.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cursor.execute("INSERT INTO personality2 (Time_spent_Alone, Stage_fear, Social_event_attendance, Going_outside, Drained_after_socializing, \
        Friends_circle_size, Post_frequency,Personality) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )
conn.commit()
cursor.close()




print('Program completed successfully!')
