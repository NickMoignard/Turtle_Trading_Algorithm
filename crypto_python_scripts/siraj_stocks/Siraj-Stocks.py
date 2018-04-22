#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 03:30:45 2018

@author: annamoignard
"""

import csv
import numpy as np
from sklearn.svm  import SVR
import matplotlib.pyplot as plt

# plt.switch_backend('new_backend')\

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            dates.append(int(row[1]))
            prices.append(float(row[2]))
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))
    
    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel= 'rbf', C=1e3, gamma=0.1)
    
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)
    
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Polynomial')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    
    return svr_rbf.predict(x)[0], svr_poly.predict(x)[0], svr_lin.predict(x)[0]

get_data('ether.csv')
DATE = 29
predicted_price = predict_price(dates, prices, DATE)
print(predicted_price)
























