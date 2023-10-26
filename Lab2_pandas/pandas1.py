import pandas as pd

df = pd.read_csv("titanic.csv")

# print(df.head(5))

# print(df.info())

# missing_values = df.isna().sum()
# print(missing_values)

# print(df.fillna(0)) # замена пропущенных или неопределенных значений на ноль

# print(df.dropna()) # удаление строк, где есть пропущенные значения

# column = df['PassengerId']
# print(column)

# columns = df[['PassengerId', 'Survived']]
# print(columns)

# index = df.loc[1]
# print(index)

# result = df[(df['Sex'] == 'male') & (df['Age'] > 30)]
# print(result)

# sort = df.sort_values(by=['Pclass'])
# print(sort)

# group = df.groupby('Pclass')['Survived'].mean()
# print(group)

# missing_values = df.isna().sum()
# df.fillna(0)
# print(df.head(10))
# df = df[(df['Age'] > 30)]
# df = df.sort_values(by=['Fare'], ascending=False)
# print(df.head(10))
# df = df.groupby('Pclass')['Age'].mean()
# print(df)