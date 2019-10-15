#!/usr/bin/env python
# coding: utf-8

# # Data Science plots

# In[1]:


# to import required library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# read data into table
df=pd.read_excel('sample_data_for_clustermap.xls',index_col='Variables')
df.head()


# # Clustermap

# In[3]:


# log transformation of the dataframe
all_log = np.log(df) 
# replacing -infinity and +infinity with NaN, then drop all those rows whose every entries are NaN
all1 = all_log.replace([np.inf, -np.inf], np.nan).dropna(how="all")
# fill all NaN with 0
all1.fillna("0",inplace=True)
# set all the column as float data type
all_h = all1[all1.columns].astype(float)
# the clustermap plot
sns.clustermap(all_h, method="average",cmap="PuOr_r",cbar_kws={'label': 'log transformed Read count'},linewidths=0.2, linecolor='gray')
# to save the plot
plt.savefig('clustermap.png', dpi=150, bbox_inches='tight')


# In[ ]:




