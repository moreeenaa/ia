import pandas as pd
df= pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'match score']])

print(df.shape)

print(df.head(4))

print(df[['writing score']])

print(df.shape)

print(df.tail(100))
