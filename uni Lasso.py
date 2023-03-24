# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cG6b-F3v21ag3RRmUY1ZAfjNIBttVtHV
"""

import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import linear_model

c = pd.read_csv('Company_data.csv')

c.info()

c.describe()

c.isnull()

c.shape

sb.distplot(c['Sales'])
plt.show()

b =c.corr()
sb.heatmap(b, annot=True)
plt.show()

from sklearn.model_selection import train_test_split

x=c.iloc[:,-1]
y=c.iloc[:,:1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

x_train.shape

y_train=y_train.values.reshape(-1,1)

x_train=x_train.values.reshape(-1,1)

x_train.shape

from sklearn.linear_model import Lasso

reg = Lasso(alpha = 0.5)
reg.fit(x_train,y_train)

x_test=x_test.values.reshape(-1,1)

y_pred=reg.predict(x_test)
print(y)

from sklearn.metrics import mean_absolute_error
mb=mean_absolute_error(y_test,y_pred)
print(mb)

from sklearn.metrics import mean_squared_error
ms=mean_squared_error(y_test,y_pred)
print(ms)

from sklearn.metrics import mean_absolute_error
msr=np.sqrt(mean_squared_error(y_test,y_pred))
print(msr)

from sklearn.metrics import r2_score
r2=r2_score(y_test,y_pred)
print(r2)



"""As we testimg with the same training data which leads to overfitting condition"""