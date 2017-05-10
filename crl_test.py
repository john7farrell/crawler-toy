# -*- coding: utf-8 -*-
"""
@author: john

"""
#%% crawling data

import requests
import datetime
from bs4 import BeautifulSoup

def getSrcHtml(urlToGet):
    return  requests.get(urlToGet).text


url = 'https://www.techmeme.com/river'
src_html = getSrcHtml(url)

soup = BeautifulSoup(src_html,'lxml')
river_items_raw = soup.select('tr.ritem > td > a')

def getTitleLink(items_all):
    data_li = []
    for item in items_all:
        title = item.get_text()
        link = item.get('href')
        data = {
                'title': title,
                'link': link,
                }
        print(data)
        data_li.append(data)
    return data_li

river_items_li = getTitleLink(river_items_raw)

#%% generate wordcloud

items_all = [d['title'] for d in river_items_li]
itemsStr = ' '.join(items_all).lower()

import matplotlib.pyplot as plt
import wordcloud
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

stopwords_addition= {'say', 'says', 'year', 'will', 'new', 'source', 'sources'}
STOPWORDS_ = STOPWORDS.union(stopwords_addition)
wc = WordCloud(background_color="white", 
               width=1280, height=720,
               stopwords=STOPWORDS_, 
               max_font_size=80,
               min_font_size=10
               )
wc.generate(itemsStr)

wc.to_image()
date = str(datetime.datetime.today())[:10]
wc.to_file('./wc_img/WC-'+date+'.jpg')
