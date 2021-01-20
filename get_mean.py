#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import statistics as stat


# In[2]:


c = 0
all_files = []
for root, dirs, files in os.walk(".", topdown = False):
    for name in files:
        if name[0:6] == 'mental':
            #print(name)
            all_files.append(name)
            c += 1
print(f'total cases: {c}')
all_files = sorted(all_files)
print(all_files, '\n', len(all_files))


# In[3]:


data = pd.read_csv(all_files[0], header=None)
print(data)


# In[4]:


n = []
d0d = []
d0p = []
d40d = []
d40p = []
d80d = []
d80p = []
d120d = []
d120p = []
d160d = []
d160p = []

for i in range(len(all_files)):
    data = pd.read_csv(all_files[i], sep=' ', header=None)
    data.columns = ["test","degree","trial","type","correct","time"]
    data = data.drop([0,1,2,3,4])
    
    data = data[data.correct != 3]
    #print(data)
    
    deg0 = data[data.degree == 0]
    deg40 = data[data.degree == 40]
    deg80 = data[data.degree == 80]
    deg120 = data[data.degree == 120]
    deg160 = data[data.degree == 160]
    
    deg0d = deg0[deg0.type == 'D']
    deg0p = deg0[deg0.type == 'P']
    
    deg40d = deg40[deg40.type == 'D']
    deg40p = deg40[deg40.type == 'P']
    
    deg80d = deg80[deg80.type == 'D']
    deg80p = deg80[deg80.type == 'P']
    
    deg120d = deg120[deg120.type == 'D']
    deg120p = deg120[deg120.type == 'P']
    
    deg160d = deg160[deg160.type == 'D']
    deg160p = deg160[deg160.type == 'P']
    
    name = all_files[i]
    n.append(name)
    
    a = stat.mean(deg0d['time'])
    b = stat.mean(deg0p['time'])
    d0d.append(a)
    d0p.append(b)
    
    c = stat.mean(deg40d['time'])
    d = stat.mean(deg40p['time'])
    d40d.append(c)
    d40p.append(d)
    
    e = stat.mean(deg80d['time'])
    f = stat.mean(deg80p['time'])
    d80d.append(e)
    d80p.append(f)
    
    g = stat.mean(deg120d['time'])
    h = stat.mean(deg120p['time'])
    d120d.append(g)
    d120p.append(h)
    
    i = stat.mean(deg160d['time'])
    j = stat.mean(deg160p['time'])
    d160d.append(i)
    d160p.append(j)


# In[5]:


dic = {
    "name": n, 
    "degree0D": d0d,
    "degree0P": d0p,
    "degree40D": d40d,
    "degree40P": d40p,
    "degree80D": d80d,
    "degree80P": d80p,
    "degree120D": d120d,
    "degree120P": d120p,
    "degree160D": d160d,
    "degree160P": d160p}

df = pd.DataFrame(dic)
df.to_csv(os.getcwd()+'/mean_data.csv')
df


# In[6]:


df84 = df.drop(66)
df84.to_csv(os.getcwd()+'/mean_data84.csv')
df84


# In[ ]:




