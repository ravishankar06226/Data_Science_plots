
# Data Science plots


```python
# to import required library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
# read data into table
df=pd.read_excel('sample_data_for_clustermap.xls',index_col='Variables')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Shop1</th>
      <th>Shop2</th>
      <th>Shop3</th>
      <th>Shop4</th>
    </tr>
    <tr>
      <th>Variables</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Var1</th>
      <td>3.912188</td>
      <td>4.013982</td>
      <td>192.269645</td>
      <td>184.176530</td>
    </tr>
    <tr>
      <th>Var2</th>
      <td>3.912188</td>
      <td>2.006991</td>
      <td>160.750031</td>
      <td>89.702558</td>
    </tr>
    <tr>
      <th>Var3</th>
      <td>3.912188</td>
      <td>6.020973</td>
      <td>163.901993</td>
      <td>110.696774</td>
    </tr>
    <tr>
      <th>Var4</th>
      <td>5.868282</td>
      <td>11.038450</td>
      <td>220.637298</td>
      <td>138.370968</td>
    </tr>
    <tr>
      <th>Var5</th>
      <td>4.890235</td>
      <td>4.013982</td>
      <td>109.267995</td>
      <td>75.388320</td>
    </tr>
  </tbody>
</table>
</div>



# Clustermap


```python
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
```


![png](output_4_0.png)



```python

```
