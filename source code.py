#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[23]:


#Program 3 Task 1
val = input("Enter first name:")
val1= input('Enter last name:')
print(val1,"",val)


# In[21]:


#Program 4 Task 1
pi=22/7
rad = float(input('Enter the radius of circle: '))
Volume=(4/3)*(pi*rad**3)
print("Volume is:",Volume)


# In[43]:


#Program 3 Task 2
Name = input("Enter the name: ")[::-1]
print(Name)


# In[28]:


#program 4 Task 2
print("WE ,THE PEOPLE OF INDIA,\n having solemly resolved to constitute India into a SOVEREIGN,!\n\tSOCIALIST, SECULAR, DEMOCRATIC REPULIC\n\t and to secure to all its citizens")


# In[31]:


#Program 2 Task 1
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")


# In[40]:


#program 2 Task 2
n=5
for i in range(n):
    for j in range(i):
        print('*',end="")
    print('')
    
for i in range(n,0,-1):
    for j in range(i):
        print('*',end="")
    print('')


# In[42]:


# Program 1 Task 2
num= input('Enter the comma separated numbers:\n')
list = num.split(',')
print('list',list)


# In[ ]:





# In[ ]:




