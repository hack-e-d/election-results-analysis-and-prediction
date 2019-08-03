#importing Packages pandas,math,mathplot and lionear regressor

import pandas as pd
import math as math
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Reading the dataset into data frame data

data=pd.read_csv("Year_Analysis.csv")

#Viewing data info

data.info()

#spliting the data into dependant and independant variables

x=data.values[:,0:6]
y=data.values[:,7]
print(x,y)

#Training linear regressor

lm = LinearRegression()
lm.fit(x,y)

#Printing intersept value

print(lm.intercept_)

#Testing prediction

predictions = lm.predict(x)
plt.scatter(y,predictions)

