import pandas as pd
import numpy as np

file = pd.read_csv("jamesbond.csv")

#set_index() and reset_index()

#accepts column names or column lists
file.set_index("Film",inplace = True)#sets the index column as Film column


file.reset_index()#changes back the index to the default

file.reset_index(drop = True ,inplace = True)#it drop is true the index is not resetted

file.fillna("Not found" , inplace = True)
#file = file.dropna()
#if you add another index with set_index()  your data will have 2 indexes
#thus there is need to reset first in order to change an index

#retriving rows 
#we use loc()
#file.loc("The Man with the Golden Gun")
#many can be gotten same as python list e.g
#file.loc("Sacred Bond" )


#Catch-All.ix[] method
#selects both index levels or both rows and columns
#file.ix["GoldenEye"]
#file.ix[ ["Lists of what you want"] ]


#sample methods gives a random row
#here n is the randaom niumber of rows that will be return
file.sample(n=5)

#frac can also be used to specifie a certain ration or persentage eg
file.sample(frac =0.24)#outputs 24% of the entire dataframe


#using nlargest() and nsmallest()
#examples
#takes n ehich is number of rows columns
#file.nlargest(4 , "columnname")
#file.nsmallest(5 , "columnname")

#filtrering using where() method
#returns complete dataframes whre true values are return and false ones replaced with null
#file["Actors"] =="Sean Connery" #normal filter
print(file.where(file["Box Office"]>45))

print(file)
