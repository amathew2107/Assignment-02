#!/usr/bin/env python
# coding: utf-8

# In[64]:


pip install requests beautifulsoup4


# In[65]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[66]:


url = 'https://www.geeksforgeeks.org/python-programming-language/?ref=shm'
url


# In[67]:


data = requests.get(url)


# In[68]:


print(data)


# In[69]:


print(data.content)


# In[70]:


soup = BeautifulSoup(data.content,'html.parser')


# In[71]:


print(soup.prettify())


# In[72]:


# Extracting Title
print(soup.title)


# In[73]:


# PName of the tag
print(soup.title.name)


# In[74]:


print(soup.title.parent.name)


# In[75]:


s = soup.find('div',class_='entry-content')
content = soup.find_all('p')
print(content)


# In[76]:


# scrapping by id
sid =soup.find('div',id = 'main')


# In[90]:


print(sid)
print(type(sid))
for sid1 in sid:
    print(sid1.text)


# In[78]:


leftbar = soup.find('ul',class_ ='leftBarList')


# In[91]:


contentLeftBar = soup.find_all('li')
print("\n",contentLeftBar)


# In[92]:


Text = soup.find('div',class_ ='entry_content')
print(Text)
lines =soup.find_all('p')
print(lines)


# In[93]:



for line in lines:
    print(line.text)
   
    #data.append(Text.string)
       


# In[82]:



for link in soup.find_all('a'):
    Links=(link.get('href'))
    print(Links)
      


# In[83]:



Final= []
Final.append([lines,Links,contentLeftBar,sid,content])
df = pd.DataFrame(Final)
df


# In[85]:


df.to_csv('Assignment4.csv')


# In[ ]:





# In[ ]:





# In[ ]:




