#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


np.random.seed(42)  
population_size = 100000
sample_size = 50  
num_samples = 1000  



# In[4]:


#Distribution is exponential
population_data = np.random.exponential(scale=2, size=population_size)




# In[5]:


plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(population_data, bins=50, color='blue', alpha=0.7)
plt.title('Original Population Distribution (Exponential)')
plt.xlabel('Value')
plt.ylabel('Frequency')



# In[6]:


# Collect the sample means
sample_means = [np.mean(np.random.choice(population_data, size=sample_size)) for _ in range(num_samples)]



# In[8]:


# Plot the distribution of sample means
plt.subplot(1, 3, 2)
plt.hist(sample_means, bins=50, color='green', alpha=0.7)
plt.title(f'Distribution of Sample Means\n(n={sample_size}, {num_samples} samples)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')



# In[9]:


larger_sample_size = 500
sample_means_large = [np.mean(np.random.choice(population_data, size=larger_sample_size)) for _ in range(num_samples)]



# In[10]:


plt.subplot(1, 3, 3)
plt.hist(sample_means_large, bins=50, color='red', alpha=0.7)
plt.title(f'Distribution of Sample Means\n(n={larger_sample_size}, {num_samples} samples)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




