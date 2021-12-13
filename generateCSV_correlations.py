#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [15, 6]

def dataArrayToNormalizedArray(array):
    #newArr = []
    #x = 1
    #while x < range(array):
     #   newArr += [float(((array[x+1]- array[x])/array[x]))]
     #   x += 1
    #return list(newArr)
    return np.diff(array) / a[:,1:] * 100

def pct_change(nparray):
    pct=np.zeros_like(nparray)
    pct[1:]=np.diff(nparray) / np.abs(nparray[:-1])
    #TODO zero divisionerror
    return pct 



# In[9]:


datafolder = 'C:\\Users\\detrading\\Desktop\\stockData\\'
count= 12
import csv
import numpy as np
import time
import scandir
from scipy.stats import pearsonr

ds = scandir.listdir(datafolder)
fileArray = []
for x in ds:
    #scan for healthy file
    fileArray += [x]
while count < (len(fileArray) -1):
    print(fileArray[count], count)
    results = []
    with open(str('C:\\Users\\detrading\\Desktop\\stockData\\'+ fileArray[count])) as file_name:
        csv = np.genfromtxt (str('C:\\Users\\detrading\\Desktop\\stockData\\'+ fileArray[count]), delimiter=",")
        csv = csv[-100:]
        data1 = csv[:,1]
        data1Norm = pct_change(data1)
        #data1Norm = dataArrayToNormalizedArray(data1)
        #print(data1)

    increment = 1
    while increment < (len(fileArray) - 2):
        csv2 = np.genfromtxt (str('C:\\Users\\detrading\\Desktop\\stockData\\'+ fileArray[count + increment]), delimiter=",")
        csv2 = csv2[-100:]
        data2 = csv2[:,1]
        data2Norm = pct_change(data2)
        #print(data2)
        #print(data2Norm)
        #correlate secCol, secCol_2
        #data = np.correlate(data1,secCol_2,"full")
        # calculate the spearmans's correlation between two variables
        data = pearsonr(data1, data2)
        #print(data1, data2)
        
       # f = open('C:\\Users\\detrading\\Desktop\\000_output.csv','w')
        line = str(fileArray[count])+','+str(fileArray[count + increment])+','+ str(data)
        print(line)
        #line = line + '\n'
        #f.write(line) #Give your csv text here.
       # f.close()
        plt.plot(data1Norm, label = "curve 1",  color="black")
        plt.plot(data2Norm, label = "curve 2", color="red")

        plt.grid()
        plt.show()
        
        #with open('C:\\Users\\detrading\\Desktop\\000_output.csv', 'w', newline='') as file:
         #   writer = csv2.writer(file)
         #   writer.writerow([fileArray[count], fileArray[count + increment], data])
        time.sleep(.1)
        increment += 1
        

    count += 1
    
    


# In[ ]:


#foreach csv file
    #foreach file other than this file
        #csvs to arrays
        #correlate arrays
        #output value in csv with mkt names, correlation coefficient
    


# In[ ]:





# In[ ]:




