import pandas as pd 
df=pd.read_csv('users(1).csv')
print(df[['age','country']])
print(df.sort_values('age'))
print(df[df['country']=='Germany'].sort_values('age',ascending=False).head(5))
