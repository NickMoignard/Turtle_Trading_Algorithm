# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:09:29 2018

@author: Admin1
"""

# uClassifier Test Script
url_string = "https://api.uclassify.com/v1/"
user_name = "Dingo"
api_key = "Token 8rHa3F7jwp0o"

import json
import requests
import csv

#url = url_string + user_name + '/Sentiment' + '/classify' 
url = 'https://api.uclassify.com/v1/uClassify/Sentiment/classify'
headers = {'Content-Type': 'application/json', 'Authorization': api_key}

google_dates = []


# get text snippets to analyse
with open('plfer_csvs/buy_bitcoin_11_4_18.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # skip headers
    headers = next(reader)
    
    # fill payload
    payload_texts = []
    for row in reader:
        google_dates.append(row[7])
        payload_texts.append(row[5])
        
payload = {'texts': payload_texts}


# create file & write to it
with open('sentiment_results.csv', 'w', newline='') as csvfile2:
    writer = csv.writer(csvfile2)
    # table headers
    writer.writerow(['datetime', 'negativity'])
    
    # create request
    req = requests.post(url, data=json.dumps(payload), headers=headers)
            
    # parse json
    response_data = json.loads(req.content)
        
    # write rows
    counter = 0
    for result in response_data:
        
        writer.writerow([result['classification'][1]['p']])   
        counter += 1
    
    

