# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:06:09 2021

@author: Kar
"""
import pandas as pd
import numpy as np

#Log Transform Example
data = pd.DataFrame({'value':[2,45, -23, 85, 28, 2, 35, -12]})
data['log+1'] = (data['value']+1).transform(np.log)
print(data)
#Negative Values Handling. Note that the values are different
data['log'] = (data['value']-data['value'].min()+1) .transform(np.log)
print(data)
