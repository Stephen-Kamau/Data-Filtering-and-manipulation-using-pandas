import pandas as pd
import numpy as np


data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

#create a dataframe  with all the coloumns defined
dataframe = pd.DataFrame(data,columns=['color','object','price'])
print(dataframe)


#creating my own array dataframe using arrange method

arr = pd.DataFrame(np.arange(16).reshape((4,4)),index=['red','blue','cyan','green'],columns=['pen','book','ruler','biscuit'])
print(arr)
#note the index declares positions for the rows
#columns gives the column name for the dataframes


#getting elements from the dataframe can be done throug the following methods

#getting values
print(arr.values)

#getting indexes
print(arr.index)
#getting columns
print(arr.columns)

#getting a specific column
#print(arr.object) #same as .....arr['color']........where color is the column name

#selecting a specific row can be done as follows
#use ix attribute to get it

print(arr.ix[2])  #gets row 3...
#multiplr rows can also be selected by adding them to the list attribute
#slicing can also be used for the selcting of specific rows to be returned


#nested dataframes can also be implimented
#the pandas places NAN if the value is not compensated while making them into dataframe
nestdict = { 'red': { 2012: 22, 2013: 33 },
'white': { 2011: 13, 2012: 22, 2013: 16},
'blue': {2011: 17, 2012: 27, 2013: 18}}


print(pd.DataFrame(nestdict))



