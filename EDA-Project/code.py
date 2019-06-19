# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here

data = pd.read_csv(path)
data['Rating'].hist()
data = data[data['Rating']<=5]
data['Rating'].hist()

#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
missing_data = pd.concat([total_null, percent_null], axis=1, keys = ['Total','Percent'])
print(missing_data)

data = data.dropna()
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())
missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1, keys = ['Total','Percent'])
print(missing_data_1)

# code ends here


# --------------

#Code starts here

g = sns.catplot(x="Category", y="Rating", data=data, kind="box", height = 10)
g.set_xticklabels(rotation = 90)
plt.title('Rating vs Category [BoxPlot]')

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#data['Installs'].value_counts()

data['Installs'] = (data['Installs'].str.replace(',','')).str.replace('+','')
data['Installs'] = pd.to_numeric(data['Installs'])
print(data['Installs'].value_counts())

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])

sns.regplot(x = data['Installs'], y = data['Rating']).set_title('Rating vs Installs [RegPlot]')

#Code ends here



# --------------
#Code starts here

data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)
#print(data['Price'].value_counts())

sns.regplot(x = data['Price'], y = data['Rating']).set_title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here

#data['Genres'].value_counts()
data['Genres'] = data['Genres'].str.split(';', n = 1, expand = True)
#data['Genres'].value_counts()

gr_mean = data.groupby(['Genres'], as_index = False)[['Rating']].mean() #.as_index=False
#print(gr_mean.describe())
gr_mean = gr_mean.sort_values(by='Rating', ascending = True)
print(gr_mean)

print(gr_mean.head(1))
print(gr_mean.tail(1))

#Code ends here


# --------------

#Code starts here

data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

sns.regplot(x="Last Updated Days", y="Rating", data=data).set_title('Rating vs Last Updated [RegPlot]')

#Code ends here


