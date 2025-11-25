#!/usr/bin/env python
# coding: utf-8

# In[2]:


s="hello" 
print(s)
print(type(s)) 


# In[5]:


s="hello" 
print(length(s)) 


# In[6]:


s="hello" 
print(len(s)) 


# In[7]:


s1="hello"
s2="hello"
print(id(s1))
print(id(s2))


# In[8]:


s1="hello"
s2="hello"
print(s1 is s2)


# In[9]:


s1="hello" 
s2="hello" 
s3="hi" 
print(s1 is s2) 
print(s2 is s3) 


# In[10]:


s1="hello" 
s2="hello" 
s3="hi" 
print(s1 == s2) 
print(s2 == s3) 


# In[11]:


print("a"+"bc")


# In[12]:


print("abcd"[2::])


# In[13]:


str1='hello'
str2=','
str3='world'
print(str1[-1:])


# In[14]:


print(r"\nhello")


# In[15]:


print('new''line')


# In[16]:


str1="helloworld"
print(str1[::-1])


# In[17]:


example = "snow world" 
example[3] = 's'                        
print(example) 


# In[18]:


l1=[1,2,3]
print(min(l1))
print(max(l1))


# In[19]:


q="What are you"
print(min(q))
print(max(q))


# In[20]:


example="hello"
print(example.count("l"))


# In[21]:


example="helle"
print(example.find("e"))


# In[22]:


example="helle"
print(example.rfind("e"))


# In[23]:


example="helloworld"
print(example[::0])


# In[24]:


str1="restart" 
char = str1[0] 
str1 = str1.replace(char, '$')                        
print(str1) 


# In[25]:


str1="restart" 
char = str1[0] 
str1 = str1.replace(char, '$')                        
str2 = char + str1[1:] 
print(str2) 


# In[26]:


example="helloworld"                        
print(example[::-1].startswith("d")) 


# In[27]:


print("hello\example\test.txt")


# In[28]:


print("hello\\example\\test.txt")


# In[29]:


print("hello\"example\"test.txt")


# In[30]:


print("hello"\example"\test.txt")


# In[31]:


print("hello"+1+2+3)


# In[32]:


print("D", end = ' ') 
print("C", end = ' ')                        
print("B", end = ' ')                        
print("A", end = ' ') 


# In[33]:


print("Hello".replace("l", "e")) 


# In[35]:


print("abc DEF".capitalize())


# In[34]:


print("abcdef".upper())


# In[36]:


print("ABCDEF".upper())


# In[37]:


print("ABCDEF".lower())


# In[38]:


print("abcdef".center(b))


# In[1]:


print("xyyzxyzxzxyy".count('yy')) 


# In[2]:


print("xyyzxyzxzxyy".count('yy',1)) 


# In[3]:


print("xyyzxyzxzxyy".count('yy',4)) 


# In[4]:


print("xyyzxyzxzxyy".endswith("xyy")) 


# In[5]:


print("ab\tcd\tef") 


# In[6]:


print("a\nb")


# In[7]:


print("abcdef".find("cd"))


# In[8]:


print("ccdcddcd".find("c")) 


# In[9]:


print("Hello {0} and {1}".format('foo', 'bin')) 


# In[10]:


print("Hello {1} and {0}".format('foo', 'bin')) 


# In[11]:


print("Hello {} and {}".format('foo', 'bin')) 


# In[12]:


print("Hello {name1} and {name2}".format('foo', 'bin')) 


# In[13]:


print("Hello {name1} and 
{name2}".format(name1='foo',name2='bin')) 


# In[14]:


print('The sum of {0} and {1} is {2}'.format(2, 10, 12))


# In[15]:


print('ab,12'.isalnum()) 


# In[16]:


print('ab12'.isalnum()) 


# In[17]:


print('ab'.isalnum()) 


# In[18]:


print('a B'.isalnum()) 


# In[19]:


print(".isdigit())


# In[20]:


print('0xa'.isdigit())


# In[21]:


print('my_string'.isidentifier())


# In[22]:


print('abc'.lower())


# In[23]:


print('$my_string'.isidentifier())


# In[24]:


print('a@1,'.lower())


# In[25]:


print('11'.isnumeric())


# In[26]:


print('Hello World'.istitle())


# In[27]:


print('HelloWorld'.istitle())


# In[29]:


s1=''' hello   hi how are you''' 
print(s1) 


# In[30]:


s1=''' hello hi how are you''' 
print(s1.strip()) 


# In[31]:


print('abcdefgh'.partition('cd'))


# In[32]:


print('abcdefcdgh'.partition('cd')) 


# In[33]:


print('abcd'.partition('cd')) 


# In[34]:


print('abcdef12'.replace('cd', '12')) 


# In[35]:


print('abef'.replace('cd', '12')) 


# In[36]:


print('abcdefcdghcd'.split('cd')) 


# In[37]:


print('Ab!2'.swapcase() 


# In[38]:


print('ab cd ef'.title()) 


# In[39]:


print('ab cd-ef'.title()) 


# In[ ]:




