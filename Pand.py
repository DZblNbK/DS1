import pandas as pd

dataSerias = [1, 2, 3, 4, 5]
series = pd.Series(dataSerias)
print(series)


dataFrame = {
    'Название': ['Toyota', 'Honda', 'Ford'],
    'Цена': [2000000, 1800000, 1500000],
    'Год': [2015, 2016, 2017]
}
df = pd.DataFrame(dataFrame)
print(df)

print("=========================")
filtered_df = df[df['Цена'] > 1800000]
print(filtered_df)
print("=========================")
df['Пробег'] = [50000, 30000, 20000]
print(df)
print("=========================")
grouped = df.groupby('Год').mean()
print(grouped)