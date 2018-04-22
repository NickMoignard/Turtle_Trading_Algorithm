# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:01:54 2018

@author: Admin1
"""

import statistics
import requests
from datetime import datetime
import json
import math
#time = datetime.fromtimestamp(1491782400)
#late_time = datetime.fromtimestamp(1522108800)
#print(time)

res = requests.get('https://api.blockchain.info/charts/market-price?format=json')
prices = []
json_data = json.loads(res.content)
for item in json_data['values']:
    prices.append(item['y'])
    # print("date: {}, price: {}".format(datetime.fromtimestamp(item['x']), item['y']))
    # print("")
differences = []

for i in range(1, len(prices)):
    _delta = abs(prices[i - 1] - prices[i])
    differences.append(_delta)

mean_difference = statistics.mean(differences)
median_difference = statistics.median(differences)
standard_deviation = statistics.stdev(differences)
                                      
mean_std_dev = 0
median_std_dev = 0

for dif in differences:
    mean_std_dev += (dif - mean_difference)**2/364
    median_std_dev += (dif - median_difference)**2/364 

print(math.sqrt(mean_std_dev))
print(math.sqrt(median_std_dev))

print(standard_deviation)                                     

