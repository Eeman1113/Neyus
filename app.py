import streamlit as st 
import os

import requests#used fror getting websites in the code 
from bs4 import BeautifulSoup#used for web scraping 
import json#importing java in python
import requests
from bs4 import BeautifulSoup
import json
import random

clicked = st.button('Configure',help='If the AI dosent work pleases click here')
if clicked==True:
    os.system('pip3 install openai')
    import openai
    os.system('pip install lxml')
st.markdown('---')
st.title('Random NLP App')
run=st.button('Run',help='run the AI')
if run==True:
    url = 'https://inshorts.com/en/read'
    response = requests.get(url)
    def print_headlines(response_text): #fuction to get headlines from any channel 
        soup = BeautifulSoup(response_text, 'lxml')
        headlines = soup.find_all(attrs={"itemprop": "headline"})
        a=[]
        for headline in headlines:
          a.append(headline.text)
          return a
          print(headline.text)
    
    
    import requests
    from bs4 import BeautifulSoup
    import json
    
    sexy_lst = []
    def print_headlines(response_text):
    
        soup = BeautifulSoup(response_text, 'lxml')
        headlines = soup.find_all(attrs={"itemprop": "headline"})
        for headline in headlines:
            a = headline.text
            print(a)
            sexy_lst.append(a)
    
        # sexy_lst = headlines
        # print(headlines)
    
    
    def get_headers():
        return {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "_ga=GA1.2.474379061.1548476083; _gid=GA1.2.251903072.1548476083; __gads=ID=17fd29a6d34048fc:T=1548476085:S=ALNI_MaRiLYBFlMfKNMAtiW0J3b_o0XGxw",
            "origin": "https://inshorts.com",
            "referer": "https://inshorts.com/en/read/",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
    
    a=[]
    url = 'https://inshorts.com/en/read'
    response = requests.get(url)
    a.append(print_headlines(response.text))
    
    # get more news
    url = 'https://inshorts.com/en/ajax/more_news'
    news_offset = "apwuhnrm-1"
    
    while True:
        response = requests.post(url, data={"category": "", "news_offset": news_offset}, headers=get_headers())
        if response.status_code != 200:
            # print(response.status_code)
            break
    
        response_json = json.loads(response.text)
        print_headlines(response_json["html"])
        j=print_headlines(response_json["html"])
        a.append(print_headlines(response_json["html"]))
        news_offset = response_json["min_news_id"]
    # print(a)
    
    print(sexy_lst)
    
    

    print(sexy_lst)
    len(sexy_lst)
    
    for i in sexy_lst:
        st.info(print(i, end='\n'))
        print(i, end='\n')