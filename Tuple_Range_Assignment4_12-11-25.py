#!/usr/bin/env python
# coding: utf-8

# In[10]:


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


# In[11]:


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


# In[12]:


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


# In[18]:


r=range(100,160)
print(r,type(r))
for val in range(100,160,10):
    print(val)


# In[19]:


r=range(-20,-8,2)
for val in range(-20,-8,2):
    print(val)


# In[20]:


r=range(-1000,-400,100)
for val in range(-1000,-400,100):
    print(val)


# In[21]:


r=range(-4,6,1)
for val in range(-4,6,1):
    print(val)


# In[22]:


r=range(5,-6,-1)
for val in range(5,-6,-1):
    print(val)


# In[1]:


t1=(1,2,3,4,5,6,7,8,9,10)
print(t1,type(t1))


# In[5]:


t=(1,2,3,4,5,6,7,8,9,10)
print(t[0],t[len(t)//2]-1,t[-1])


# In[19]:


t1=(1,2,3,4,5,6,7,8,9,10)
print(t1[0:3])
print(t1[-3:])
print(t1[2:5])


# In[25]:


t=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(t[1][2])


# In[27]:


t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)


# In[45]:


t1=(1,2,3,1,2)
print(t1.count(1))
print(t[0][0])


# In[28]:


t1=(1,2,3,4,5)
a,b,c,d,e=t1
print(a,b,c,d,e)


# In[42]:


l1=[10,20,30,40,50]
print(l1,type(l1))
l1.append(6)
print(l1,type(l1))
t1=tuple(l1)
print(t1,type(t1))


# In[34]:


t1=((1,2,3),(4,5,6),(7,8,9))
print(t1[0],t1[1],t1[2],type(t1))


# In[3]:


t1=("programming")
print(t1,type(t1))
s="Python"
s=s + t1
print(s)



# In[4]:


dict1={
       (1,2):10,
       (3,4):20,
       (5,6):30,
}
print(dict1)


# In[5]:


t1=((1,2),(3,4),(4,5))
for inner_tuple in t1:
    print("inner tuple:",inner_tuple)
    for element in inner_tuple:
        print("Element:",element)


# In[8]:


tuple_1=(1,2,3,4,5,1,2,3,4,5)
s2=set(tuple_1)
print(tuple_1)
print(s2)


# In[9]:


def tuple_details(t):
    print("Minimum:",min(t))
    print("Maximum:",max(t))
    print("Sum of elements:",sum(t))
t1=(1,2,3,4,5)
tuple_details(t1)s


# In[ ]:




