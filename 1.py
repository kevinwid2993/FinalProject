import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

basket = pd.read_csv('nbastats2018-2019.csv')

'''
basket column
(['Height', 'Weight', 'Age', 'Salary', 'Points', 'Blocks',
'Steals', 'Assists', 'Rebounds', 'FT%', 'FTA', 'FG3%', 'FG3A', 'FG%',
'FGA', 'MP', 'G',
'PER', 'OWS', 'DWS', 'WS', 'WS48', 'USG', 'BPM', 'VORP'],
dtype='object')
MP
Minutes Played
G
Games
PER
Player Efficiency Rating
OWS
Offensive Win Shares
DWS
Defensive Win Shares
WS
Win Shares
WS48
Win Shares Per 48 Minutes
USG
Usage Percentage
BPM
Box Plus-Minus
VORP
Value Over Replacement Player
'''

basket = basket.dropna(subset=['Team'])

basket = basket.drop(['Name','Team','Weight','Height','FT%','FG3%','FG%','FGA','FG3A','FTA','MP','G',
'PER', 'OWS',
'DWS', 'WS', 'WS48', 'USG', 'BPM', 'VORP'],axis=1)

basket = basket.fillna(0)
#print(basket.dtypes)
'''
Height        int64
Weight        int64
Age           int64
Salary       object
Points      float64
Blocks      float64
Steals      float64
Assists     float64
Rebounds    float64
FT%         float64
FTA         float64
FG3%        float64
FG3A        float64
FG%         float64
FGA         float64
MP          float64
G             int64
PER         float64
OWS         float64
DWS         float64
WS          float64
WS48        float64
USG         float64
BPM         float64
VORP        float64
dtype: object
'''

basket['Salary'] = basket['Salary'].astype('int64')
#karena di view sebagai object

#distribution plot
# plt.figure(figsize=(20,10))
# plt.subplot(2,3,1)
# plt.scatter(x='Age',y='Salary',data=basket)
# plt.xlabel('Age')
# plt.ylabel('Salary')
# plt.subplot(2,3,2)
# plt.title('Salary Distribution Plot')
# plt.scatter(x='Points',y='Salary',data=basket)
# plt.xlabel('Points')
# plt.ylabel('Salary')
# plt.subplot(2,3,3)
# plt.scatter(x='Blocks',y='Salary',data=basket)
# plt.xlabel('Blocks')
# plt.ylabel('Salary')
# plt.subplot(2,3,4)
# plt.scatter(x='Steals',y='Salary',data=basket)
# plt.xlabel('Steals')
# plt.ylabel('Salary')
# plt.subplot(2,3,5)
# plt.scatter(x='Assists',y='Salary',data=basket)
# plt.xlabel('Assists')
# plt.ylabel('Salary')
# plt.subplot(2,3,6)
# plt.scatter(x='Rebounds',y='Salary',data=basket)
# plt.xlabel('Rebounds')
# plt.ylabel('Salary')

#correlation plot
# bc = basket.corr()
# sns.heatmap(bc,annot=True)
# plt.show()

x = basket.drop(['Salary'],axis=1)
y = basket['Salary']

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(
    x,
    y,
    test_size = .1,
    random_state = 101
)

from sklearn.linear_model import LinearRegression
linmodel = LinearRegression()
linmodel.fit(xtrain,ytrain)

print(linmodel.intercept_)

print(linmodel.coef_)
'''
[ 627686.61477924  472169.83564527   84568.44051308 2035050.59046354
  390478.60074215  655765.3571344 ]
'''

print(xtrain.columns)
'''
['Age', 'Points', 'Blocks', 'Steals', 'Assists', 'Rebounds']
'''

basketcoeff = pd.DataFrame(linmodel.coef_,xtrain.columns,columns=['Coeff'])

print(basketcoeff)
'''
                 Coeff
Age       6.276866e+05
Points    4.721698e+05
Blocks    8.456844e+04
Steals    2.035051e+06
Assists   3.904786e+05
Rebounds  6.557654e+05
'''

#print(linmodel.predict([[25,20,2,2,5,10]]))

import joblib
joblib.dump(linmodel,'modeljoblib')