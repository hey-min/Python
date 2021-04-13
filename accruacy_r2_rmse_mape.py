# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:59:31 2021

@author: hey-min chhoi

Accuracy Test : R2, RMSE, MAPE

"""

import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd

real = pd.DataFrame()
est = pd.DataFrame()

x = real.values.flatten()
y = est.values.flatten()
    
x = x[~np.isnan(x)]
y = y[~np.isnan(y)]
    
r2 = r2_score(x, y)
rmse = np.sqrt(mean_squared_error(x, y))
mape = mean_absolute_percentage_error(x,y)*100
    

print('r2:{} rmse:{} mape:{}' .format(r2, rmse, mape))
