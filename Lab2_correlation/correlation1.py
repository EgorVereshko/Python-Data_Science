import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

brainFrame = pd.read_csv('brainsize.txt', delimiter='\t')

print(brainFrame)

print(brainFrame.head(10))
print(brainFrame.tail(8))

print(brainFrame.describe())

menDf = brainFrame[brainFrame['Gender'] == 'Male']
womenDf = brainFrame[brainFrame['Gender'] == 'Female']

# menMeanSmarts = menDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
# plt.scatter(menMeanSmarts, menDf["MRI_Count"])
# plt.show()
#
# womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
# plt.scatter(womenMeanSmarts, womenDf["MRI_Count"])
# plt.show()
#
# print(brainFrame.fillna(0).drop('Gender', axis=1).corr())
# # Поэтому, когда вы видите значение 1 на диагонали матрицы корреляции, это не совпадение, а естественное свойство
# # матрицы, отражающее корреляцию переменной с самой собой. представлять собой квадратную матрицу корреляции, где
# # значения показывают корреляцию между парами переменных в DataFrame `brainFrame`. Значения корреляции могут
# # варьироваться от -1 до 1, где -1 обозначает полную отрицательную корреляцию, 1 - положительную корреляцию,
# # а 0 - отсутствие корреляции между переменными.
#
# # зеркальное отражение значений в матрице корреляции не является совпадением, а следствием симметрии корреляционной
# # связи между парами переменных.
#
# print(womenDf.fillna(0).drop('Gender', axis=1).corr())
#
# print(menDf.fillna(0).drop('Gender', axis=1).corr())

# wcorr = womenDf.fillna(0).drop('Gender', axis=1).corr()
# sns.heatmap(wcorr)
# plt.savefig('atribute_correlations.png', tight_layout=True)

# wcorr = menDf.fillna(0).drop('Gender', axis=1).corr()
# sns.heatmap(wcorr)
# plt.savefig('atribute_correlations_men.png', tight_layout=True)

# Значение корреляции близкое к нулю указывает на то, что изменение одной переменной не предсказуемо связано с
# изменением другой переменной.

# разделение по полу в анализе корреляции может помочь обнаружить и понять потенциальные различия во взаимосвязи
# между переменными, связанными с полом.

# Чем ближе значение коэффициента корреляции к 1 или -1, тем более сильная корреляция между этой переменной и MRI_Count.
