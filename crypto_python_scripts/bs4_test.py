# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:02:06 2018

@author: Admin1
"""
from bs4 import BeautifulSoup
import requests

url_string = "https://www.google.com.au/search?q=bitcoin&rlz=1C1AVSX_enAU699AU700&tbm=nws&source=lnms&tbs=qdr:d&sa=X&ved=0ahUKEwjv1aG-uK_aAhWKiLwKHfp-CcYQ_AUICigB&biw=1921&bih=954&dpr=1"

google_page = requests.get(url_string)

soup = BeautifulSoup(google_page.content, 'html.parser')

articles = soup.find_all('div', class_='st')
text_snippets = []
for article in articles:        
    text_snippets.append(article.get_text())
    
# write data to csv
import csv

time = '2018-04-10 20:26:00'

with open('text_snippets.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', 
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['time', 'text'])
    for snippet in text_snippets:
        writer.writerow([time , snippet])
        
    # write each result as a new row
    
    
#.find_all('div', class_='tile'