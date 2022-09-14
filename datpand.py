# series - список с нумерацией (индексами) /одномерные данные, как массив/один столбец
import pandas as pd
# my_series = pd.Series([1, 3, 5, 7], index=["a", "b", "c", "d"])
# print(my_series) #my_series[1] - вывод конкретного элемента ["a", "b"]
# my_series = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8}) #задать как словарь
# my_series.name = "spisok"
# my_series.index.name = "number"
# print(my_series)
# my_series.index =[]
# DataFrame  таблица
# df = pd.DataFrame({
#     "country": ["Russa", "USA", "Italia"],
#     "population": [30, 50, 15]
# })
# df.index = ["RU", "USA", "IT"]
# df.index.name = "code"
# print(df)
# print(df["country"])
# print(df.loc["RU"], "population") доступ к какому то элементу
# print(df[df.population > 20]["population"])
# df["good country"] = [False, True, True] #добавить ещё
# print(df)
# df.drop(['good country'], axis='columns') #удалить столбец
# df1 = df.drop(columns=['good country']) #удалить столбец
# print(df1)
# df.to_csv('datpand.csv') #сохраним наш датафрейм в csv
# df = pd.read_csv('datpand.csv', sep = ",") #откроем его

# Титаник
# titan = pd.read_csv('titanic.csv') #откроем его
# print(titan.head(n = 5))
# print(titan.groupby(["Sex", "Survived"])['PassengerID'].count())

# pvt = titan.pivot_table(index=["Sex"], columns=["PClass"], values="Name", aggfunc="count") # Сводная таблица/число женщин и мужчин в каждом классе
# print(pvt)
# print(pvt.loc["female", ["1st", "2nd"]])



#визуализация данных matplotlib
import matplotlib.pyplot as plt
# df = pd.read_csv('apple.csv')
# new_df = df.loc['2017-Feb':'2012-Feb', ["Close"]]
# new_df.plot()
# plt.show()

df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
# print(type(df))
# print(df)
# df.info()
# print(df.columns)
# df = df.head(3)
# df.index = ["a", "b", "c"]
# print(df)
# df = df[['Name', 'Age']].head(3)
# print(df)
# print(df.loc["Survived", ["1st", "2nd"]])
# print(df.loc[[5, 10, 15], ['Name', 'Age']]) mistake$$
# print(df.iloc[5:8, :3])
# print(df.iloc[5:8, [1, 5]]) #доступ по индексам
# print(df["Age"] > 30)
#если хотим получить пользователей с определнными данными
# print(df[df["Age"].isin([30, 60])])
# print(df["Age"])
# print(df[(df['Age'] > 10) & (df['Pclass'] == 1)]) # удобная сортировка и задача сразу нескольких критериев
# df["Age"].notna() #маска удаляет незаполеннные элементы
# print(df[df["Age"].notna()]) #удаление не заполненных элементов
# print(df["Age"].isna().sum()) #функция наоборот /не известнет возраст
# print(df.loc[df["Age"].notna(), "Name"]) #имена людей у кого есть возраст (указан)

# сортировка!
# print(df.sort_values("Age").head(10)) #по возрасту
# print(df.sort_values(["Age", "Name"], ascending=[False, True]).head(10)) #сначала сортируем по убываниюв возрасте, а те кто одинаковые то в алфовитном порядке

#объединение датафреймов
# df2 = df.copy(deep=True) # копируем и все значения также deep
# df1 = pd.concat([df, df2]) #по строкам /
# df1 = pd.concat([df, df2], axes=1) #по столбцам
# print(df1.shape)
#хотим добавить Датафрейм ещё один столбец с некоторыми значениями, создаем ещё один ДФ и объед их
# mdf = pd.DataFrame(index=df.index)
# mdf['PassengerId'] = df['PassengerId']
# mdf['evenId'] = df["PassengerId"].apply(lambda x: x % 2 == 0)
# print(pd.merge(df, mdf, how="inner")) #мы объединили два дф

#Аналитические функции / операции над строками, столбцами
# print(df.count())
# print(df["Name"].count())
# print(df.groupby("Sex") ["Age"].mean()) #объединяем данные/ средний возраст м и ж
# print(df.groupby("Sex") ["Age"].describe())
# print(df.groupby(["Sex", "Survived"])["Age"].agg(["mean", "median"])) # агрегаторная функция можем сразу несколько функций применить
# print(df["Sex"].value_counts())
# print(df.corr()) #функция корреляции
#
# визуализация
# df["Age"].plot(kind="hist")
# df['Age'].plot(kind='hist', bins=20)
# df["Age"].plot(kind="hist", xlim=(0, 80))
# df.groupby("Sex")["Age"].plot(kind="hist", xlim=(0, 80))
# plt.show()


# Изменение данных в сериес и датафрейм
# tdf = df.copy(deep=True)
# tdf["Pclass"] = 1 #изменение значений
# print(tdf)
# print(tdf["Pclass"].count())
# print(df["Pclass"].value_counts())
# tdf["isAdult"] = tdf["Age"] >= 18
# print(tdf.head(10))

# tdf["isAdultSurvived"] = tdf["isAdult"]
# tdf.loc[tdf["Survived"] == 0, "isAdultSurvived"] = False
# print(tdf.head())

