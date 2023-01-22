#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Create Array

# In[2]:


# Creating Arrays 
a = np.array([1,3,5,7])                                                      # create one dimensional array
b = np.array([[1,93,15,7],[2,4,6,8]], dtype = float)                           # create two dimensional array   
c = np.array([[1,3,5,7],[2,4,6,8],[7,9,11,23],[12,19,21,43]], dtype = float) # create 4d array
print("******one*************")
print(a)
print("*******two************")
print(b)
print("*******four***********")
print(c)


# # Initialize Placeholders

# In[3]:


# Initial PlaceHolders zeros
print("*********zeros********")
print(np.zeros((2,4)))                       # create array of zeros 2 D
print("*********ones********")
print(np.ones((2,3,4),dtype=np.int16))       # create array of ones three D
print("*********evenly even********")
do = np.arange(10,25,2)                      # create array of evenly distributed with step 2
print(do)
print("*********evenly odds********")
de = np.arange(1,10,2)
print(de)
print("*********evenly distrbuted********")
print(np.linspace(2,9,4, dtype=np.int16))    # create array of evenly 
print("*********evenly distrbuted********")
print(np.linspace(2,9,4, dtype=np.int16))    # create array of evenly 
print("*********constant array********")
print(np.full((5,3),8,dtype=float))          # create array of constants
print("*********Identity martrix********")
print(np.eye(4))                             # create Identity Matrix
print("*********Radom********")
print(np.random.random((4,4)))               # create Identity Matrix
print("*********Empty********")
print(np.empty((3,2)))                       # create empty array



# # I/O

# In[4]:


# saving & loading on Disk
np.save('my_array',a)
np.savez('array.npz',a,b)
np.load('my_array.npy')


# In[5]:


# svaing & loading Text files

np.savetxt("myfile.txt", a, delimiter=" ")
np.loadtxt("myfile.txt")

print(np.genfromtxt('myfile.txt',delimiter=','))


# # Data Types

# In[6]:


print(np.int64)
print(np.float32)
#print(np.complex)
#print(np.bool)
#rint(np.object)
print(np.string_)
print(np.unicode_)


# # Inspecct Array

# In[7]:


print("********Array Dim***********")
print(b.shape) # Array Dimensions
print("********Array Length***********")
print(len(a))  # Length of Array
print("********Array Number of Dim***********")
print(c.ndim)  # Number of Array Dimensions
print("********Number of Array element***********")
print(c.size)
print("********Array Data type***********")
print(c.dtype)
print("********Array Data type Name***********")
print(c.dtype.name)
print("********Convert an array to different Type***********")
print(b.astype(int))


# # Asking for Help

# In[8]:


np.info(np.ndarray.dtype)


# # Array Mathematics

# In[9]:


# arithmetic Operations 
print(a)
print(b)
g = a - b
print("********Subtract**********")
print(g)
print("********Subract ops*******")
print(np.subtract(a,b))
g = a + b
print("********Add**********")
print(g)
print("********Add ops*******")
print(np.add(a,b))
print("********Division*******")
print(a/b)
print("*******Division ops****")
print(np.divide(b,a))
print("*******Mutiple ********")
print(a * b)
print("*******Mutiple ops******")
print(np.multiply(a,b))
print("****Exponential ops*****")
print(np.exp(b))
print("****Square root ops*****")
print(np.sqrt(b))
print("****Sin ops*********")
print(np.sin(b))
print("****Cos ops*********")
print(np.cos(b))
print("****log ops*********")
print(np.log(b))
print("****ele wise dot ********")
print(b.dot(a))


# # Comparsion

# In[10]:


print("********element wise comparsion************")
print(a==b) # element wise comparsion
print("********element wise comparsion************")
print(a < 2)
print("********Array wise comparsion************")
print(np.array_equal(a,b))


# # Aggregate Functions

# In[11]:


print(a)
print(b)
print("***********sum **********")
print(a.sum())
print("***********min **********")
print(a.min())
print("***********max **********")
print(b.max(axis=0))
print(b.max(axis=1))
print("***********cumulative sum **********")
print(b.cumsum(axis=1))
print("***********mean **********")
print(b.mean())
print("***********median **********")
print(np.median(b))
print("***********corrcoef **********")
print(np.corrcoef(b))
print("***********std **********")
print(np.std(b))


# # Copying Arrays

# In[12]:


print(a.view())
print(np.copy(a))


# # Storing Arrays

# In[13]:


print(b)
print(b.sort(axis=0))
print(b)


# # Subsetting, Slicing, Indexing

# In[14]:


print(a[2])
print(b[1,2])
print("*******Slicing*****************")
print(b[0:1])
print("*******Reversed*****************")
print(a[::-1])
print("*******Select elements less *****************")
print(a[a<6])


# # Array Manipulation

# In[15]:


print("***********Transpose***********")
print(b)
print(np.transpose(b))
print(b.T)
print("***********Flatten Array***********")
print(b.ravel())
print("***********Change Array Shape***********")
print(c.reshape(2,-2))


# # Adding/Removing Elements

# In[16]:


print(a)
c.resize((2,2))
print("*********reszie***********")
print(c)
print("*********append***********")
print(np.append(a,b))
print("*********Insert item***********")
print(np.insert(a,3,8))
print(a)
print("*********Delete item***********")
print(np.delete(a,[1]))


# # Combining Array

# In[30]:


dd = a * 4
print(a)
print(dd)
print("**********Concatenate Array************")
print(np.concatenate((a,dd),axis=0))
print("**********Stack Vertical Array************")
print(np.vstack((a,dd)))
print("**********Stack array Vertical row-wise************")
print(np.r_[a,dd])
print("**********Stack Horizontal Array************")
print(np.hstack((a,dd)))
print("**********Create Stack column-wise************")
print(np.c_[a,dd])
print("**********Spilitting Horizontal Array************")
print(np.hsplit(a,2))
print("**********Spilitting Vertical Array************")
print(np.vsplit(b,2))


# In[ ]:





# In[ ]:




