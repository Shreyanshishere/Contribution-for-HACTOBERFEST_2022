# -*- coding: utf-8 -*-
"""hand digit recognition using logistic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vccGI9dAKAj_id2zCXdyxczlXpVsJT5m
"""

from sklearn.datasets import fetch_openml

mnist=fetch_openml('mnist_784')

x=mnist.data.values
y=mnist.target

temp=x[95]
temp.shape

import matplotlib.pyplot as plt

plt.imshow(temp.reshape(28,28)) # 28 ka squre 784   imshow used for image showing   reshape for 2d array temp meh 1 d array value toh 2d for sklearn beacduse sklearn uses 2d

y[95]

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=10)

from sklearn.linear_model import LogisticRegression

from matplotlib.scale import LogisticTransform
model=LogisticRegression(multi_class='multinomial',solver='saga')

model.fit(xtrain,ytrain)

model.score(xtrain,ytrain)

model.score(xtest,ytest)

