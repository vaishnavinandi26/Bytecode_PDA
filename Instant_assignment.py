#!/usr/bin/env python
# coding: utf-8

# In[31]:


l1=[10,11,13,14]
l2=[]
for x in l1:
    l2.append(x+10)
print(l2)


# In[32]:


l1=[10,11,13,14]
l2=[5,6,7,8,9]
l3=[]
for i,val in enumerate(l1):
    l3.append(l1[i]+l2[i])
print(l3)


# In[27]:


l1=[10,20,23,45,78,90,42,41]
l2=[] 
for num in l1:
    if num>=40:
        l2.append(num)
print(l2)
    


# In[15]:


l1=[10,20,15,45,89,90,11,34]
l2=[]
indexes=[0,1,5,7]
result=[l1[i] for i in indexes]
l2.append(result)
print(l2)


# In[ ]:





# In[4]:


r=range(10)
print(r,type(r))
for val in r:
    print(val)
r=range(0,10)
print(r,type(r))
for val in r:
    print(val)
for val in range(0,10,1):
    print(val)



# In[6]:


r=range(10,21)
print(r,type(r))
for val in r:
    print(val)
r=range(10,21)
print(r,type(r))
for val in r:
    print(val)
for val in range(10,21,1):
    print(val)


# In[7]:


r=range(100,106)
print(r,type(r))
for val in r:
    print(val)
r=range(100,106)
print(r,type(r))
for val in r:
    print(val)
for val in range(100,106,1):
    print(val)


# In[13]:


r=range(-10,-17)
print(r,type(r))
for val in r:
    print(val)
for val in range(-10,-17,-1):
    print(val)


# In[14]:


r=range(10,0)
print(r,type(r))
for val in r:
    print(val)
for val in range(10,0,-1):
    print(val)


# In[15]:


r=range(-10,0)
print(r,type(r))
for val in r:
    print(val)
for val in range(-10,0,-1):
    print(val)


# In[16]:


r=range(-1,-11)
print(r,type(r))
for val in r:
    print(val)
for val in range(-1,-11,-1):
    print(val)


# In[17]:


r=range(10,21,2)
print(r,type(r))
for val in r:
    print(val)


# In[19]:


r=range(100,160)
print(r,type(r))
for val in range(100,160,10):
    print(val)


# In[22]:


r=range(-20,-8,2)
for val in range(-20,-8,2):
    print(val)


# In[14]:


r=range(-1000,-400,100)
for val in range(-1000,-400,100):
    print(val)


# In[15]:


r=range(-4,6,1)
for val in range(-4,6,1):
    print(val)


# In[5]:


r=range(5,-6,-1)
for val in range(5,-6,-1):
    print(val)


# In[ ]:




