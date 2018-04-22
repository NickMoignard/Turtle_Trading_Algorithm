# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

with open('text.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['DADSHOUSE', 'OH', 'GOD', 'NOW'])
    


with open('text.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ',
                        quotechar='|')
    
    for row in reader:
        print(', '.join(row))