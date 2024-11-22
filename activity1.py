import pandas as pd
import numpy as np

sports_challenge = {'name': ['Ronaldo', 'Ronaldhino', 'Messi', 'Neymar'],
                    'score': [6, 4, 3, 7],
                    'year': [2023, 2022, 2021, 2025]}
labels = ['a','s','d','f']

df = pd.DataFrame(sports_challenge , index=labels)
print("Summary of the basic info")
print(df.info())
print(df.head(4))

print("!!!<________________________>!!!")

students_name = {'name': ['Abdullah', 'Malik', 'Ayaan', 'Shaun'],
                 'score': [2, 6, 10, 0],
                 'schools': ['Canmbridge', 'Oxford', 'Jamia Baitussalam', 'Harvard']}
labels = ['a)','b)','c)','d)']

df = pd .DataFrame(students_name , index=labels)
print("This is all the info: ")
print(df.info())
print(df.head(4))

df = pd.read_csv('data.csv')
df["Score"].fillna(130, inplace = True)
print(df.to_string())