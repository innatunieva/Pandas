
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


# # 4

# In[55]:

import pandas_datareader.data as web

# Codexis, Inc. = CDXS
# ZIOPHARM Oncology Inc. = ZIOP
# Pfizer Inc. = PFE
# In[56]:

import pandas_datareader.data as web
import datetime


# In[57]:

start = datetime.datetime(2012,1,1)
end = datetime.date.today()


# In[58]:

codexis = web.DataReader("CDXS","google", start, end)


# In[59]:

ziopharm = web.DataReader("ZIOP","google", start, end)


# In[60]:

pfizer = web.DataReader("PFE","google", start, end)


# In[61]:

codexis.head(7), ziopharm.head(7), pfizer.head(7)


# In[62]:

codexis.head(7)


# In[63]:

ziopharm.head(7)


# In[64]:

pfizer.head(7)


# In[65]:

type(pfizer)


# In[21]:

import matplotlib.pyplot as plt 
get_ipython().magic(u'matplotlib inline')


# In[67]:

plt.plot(codexis["High"])


# In[68]:

plt.plot(ziopharm["High"])


# In[69]:

plt.plot(pfizer["High"])


# In[31]:

import pandas as pd


# In[70]:

stocks = pd.DataFrame({"CDXS": codexis ["High"  ],
                      "ZIOP": ziopharm["High"],
                      "PFE": pfizer["High"]})
 
stocks.head(7)


# In[71]:

stocks.plot()


# In[102]:

our_list=[]
for number in ziopharm["Open"]:
           our_list.append(number)


# In[106]:

print(our_list[:7])


# # 5

# In[117]:

particular_list=[]
for number in ziopharm["Open"]:
    if 12<number<=13:
           particular_list.append(number)


# In[118]:

print(particular_list)


# In[ ]:



