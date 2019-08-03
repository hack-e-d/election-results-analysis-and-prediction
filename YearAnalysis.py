#importing Packages pandas,math,mathplot and seaborn

import pandas as pd
import math as math
import matplotlib.pyplot as ploter

#Reading the dataset into data frame data

data=pd.read_csv("Year_Analysis.csv")

#Viewing data info

data.info()

#Bivarient Analysis using pyplot

ploter.scatter(data['Year'],data['Total Votes'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Year")
ploter.ylabel("No of Voters")
ploter.show()

ploter.scatter(data['Year'],data['Winner %'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Year")
ploter.ylabel("Winning %")
ploter.show()

ploter.scatter(data['Year'],data['Runner %'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Year")
ploter.ylabel("Runner %")
ploter.show()

ploter.scatter(data['Year'],data['Margin %'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Year")
ploter.ylabel("Margin %")
ploter.show()

ploter.scatter(data['Year'],data['Winning Party'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Year")
ploter.ylabel("Winning party")
ploter.show()

ploter.scatter(data['Year'],data['Runner Party'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Year")
ploter.ylabel("Runner party")
ploter.show()

