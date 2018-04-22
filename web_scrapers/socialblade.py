# import libraries
import requests
import csv
from bs4 import BeautifulSoup
import urllib, urllib2, cookielib
""

def test_login():
    username = 'nicklmoignard@gmail.com' # Gmail Address
    password = 'hsp109MTG' # Gmail Password
    cookie_jar = cookielib.CookieJar() 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar)) 
    login_dict = urllib.urlencode({'username' : username, 'password' :password}) 
    opener.open('https://accounts.google.com/ServiceLogin', login_dict) 
    response = opener.open('https://music.google.com/')
    soup = BeautifulSoup(response, 'html.parser')

    print soup

if __name__ == '__main__':
    test_login()