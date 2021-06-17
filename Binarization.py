# Python code explaining how to Binarize feature values 
   
#Importing Libraries 
import pandas as pd 
  
#Importing Data
data_set = pd.read_csv('data.csv') 
print(data_set.head())
age = data_set.iloc[:, 1].values 
salary = data_set.iloc[:, 2].values 
print ("\nOriginal age data values : \n",  age) 
print ("\nOriginal salary data values : \n",  salary) 

# Binarizing values
from sklearn.preprocessing import Binarizer 
  
x = age 
x = x.reshape(1, -1) 
y = salary 
y = y.reshape(1, -1) 
  
# For age, let threshold be 35, For salary, let threshold be 61000 
binarizer_1 = Binarizer(35) # Age below 35 is binarized to 0
binarizer_2 = Binarizer(61000) # Salary below 61000 is binarized to 0
  
# Transformed features 
print ("\nBinarized age : \n", binarizer_1.fit_transform(x)) 
print ("\nBinarized salary : \n", binarizer_2.fit_transform(y)) 