
# coding: utf-8

# # 1

# In[24]:

def mean(values):
    average=sum(values)/len(values)
    return average


# In[33]:

x=input ("Please, input several numbers separated by commas ")
y= mean(x)


# In[34]:

print(y)


# # 2

# In[35]:

n=input("type a number ")


# In[36]:

z=mean(x[-n:])


# In[37]:

print(x[-n:])


# In[38]:

print(z)


# # 3

# In[ ]:

#3-a 


# In[39]:

import random


# In[86]:

from random import randint
n=(randint(1,100))
print(n)


# In[87]:

r1=range(1,51)
r2=range(51,100)


# In[88]:

def checker(number):
    if n in r1:
        return "Loss"
    elif n in r2:
        return "Win"
    else:
        return "Draw"


# In[89]:

checker(n)


# In[ ]:

#3-b (another way-without adding the checher)


# In[90]:

if n in r1:
    print("Loss")
if n in r2:
    print("Win")
if n==100:
    print("Draw")


# # 4 and # 5

# In[117]:

import pandas_datareader.data as web
import datetime


# In[118]:

# for bringing in a balanced form, as the start date was different for them 
start = datetime.datetime(2012,1,1)
end = datetime.date.today()

# Codexis, Inc. = CDXS
# ZIOPHARM Oncology Inc. = ZIOP
# Pfizer Inc. = PFE
# In[119]:

stocks_list=["codexis","ziopharm", "pfizer"]


# In[120]:

print (stocks_list)


# In[121]:

for i in range(3):
    if i==0:
        print (stocks_list[i])
    elif i==1:
        print (stocks_list[i])
    else:
        print (stocks_list[i])


# In[153]:

stocks_list[0] = web.DataReader("CDXS","google", start, end)


# In[123]:

stocks_list[1] = web.DataReader("ZIOP","google", start, end)


# In[124]:

stocks_list[2] = web.DataReader("PFE","google", start, end)


# In[125]:

stocks_list[0]=codexis


# In[126]:

stocks_list[1]=ziopharm


# In[127]:

stocks_list[2]=pfizer


# In[158]:

print stocks_list


# In[129]:

import matplotlib.pyplot as plt 
get_ipython().magic(u'matplotlib inline')


# In[165]:

stocks_list[2].plot()


# In[148]:

import pandas as pd


# In[149]:

stocks = pd.DataFrame({"CDXS": codexis ["High"],
                      "ZIOP": ziopharm["High"],
                      "PFE": pfizer["High"]})
 
stocks.head(7)


# In[150]:

stocks.plot()


# ###### Additional

# In[166]:

pfizer.head(7)


# In[131]:

type(codexis)


# In[132]:

our_list=[]
for number in codexis["Open"]:
           our_list.append(number)


# In[133]:

print(our_list) 


# In[135]:

plt.plot(ziopharm["High"])


# In[136]:

plt.plot(pfizer["High"])


# In[144]:

our_list=[]
for number in ziopharm["Open"]:
           our_list.append(number)


# In[145]:

print(our_list[:7])


# In[146]:

type(our_list)


# In[117]:

particular_list=[]
for number in ziopharm["Open"]:
    if 12<number<=13:
           particular_list.append(number)


# In[118]:

print(particular_list)

