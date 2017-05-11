# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:13:08 2017

@author: john
"""

# working on this
#sources = soup.select('div #topcol1 div.clus') #  span.bls
#sources_str = [str(i).split('<span class="drhed">More:</span>')[1:] for i in sources]
#sources_str = reduce(list.__add__, sources_str)
#sources_str = [BeautifulSoup(i,'lxml') for i in sources_str]
#sources_str = [i.select('span.bls a[href]') for i in sources_str]


#%% crawling data

import requests
import datetime
from bs4 import BeautifulSoup

def getSrcHtml(urlToGet):
    return  requests.get(urlToGet).text

def getItems(date_time, suffix=''):
    # crawling from archive
    url = 'http://www.techmeme.com' + suffix
    
    src_html = getSrcHtml(url)
    soup = BeautifulSoup(src_html,'lxml')
    
    cites = soup.select('div #topcol1 div.clus table.shrtbl cite')
    cite_writers = [str(i).split('<cite>')[1].split('<a href')[0].split(' / ')[0] for i in cites]
    
    items_li = []
    items = soup.select('div #topcol1 div.clus div.ii')
    news_str_all = ''
    for i in items:
        d = {}
        i_s = i.get_text().split('\xa0 —\xa0')
        news_str_all += i.get_text() + ' '
        if i and i_s:
            d['link'] = i.select('a')[0].get('href')
            d['title'] = i_s[0].strip()
            d['intro'] = i_s[1].strip() if len(i_s) > 1 else ''
        items_li.append(d)
    return news_str_all, items_li

def getWC(str_all, suffix=''):
    
    itemsStr = str_all.lower()
    import matplotlib.pyplot as plt
    from nltk.corpus import stopwords
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    
    stopwords_addition= {'say', 'says', 'year', 'will', 'new', 'source', 'sources'}
    STOPWORDS_ = STOPWORDS.union(stopwords_addition)
    
    #add mask
    #import numpy as np
    #from PIL import Image
    #mask = np.array(Image.open("mask.jpg"))
    
    wc = WordCloud(background_color="white", 
                   #mask=mask, ##custom background     
                   width=1280, height=720,
                   margin = 10,
                   stopwords=STOPWORDS_, 
                   max_font_size=80,
                   min_font_size=20
                   )
    wc.generate(itemsStr)
    
    plt.figure()  
    plt.imshow(wc)  
    plt.axis("off")  
    plt.show() 
    
#    wc.to_image().show()
    date = suffix.replace('/','-')
    wc.to_file('./wc_img/WC'+date+'.jpg')

# date + time(hour)
#year, month, day, hour, minute = 2017, 5, 9, 18, 0
#date_time = datetime.datetime(year, month, day, hour)
def getSuffix(dt):
    s = lambda x: '%02d' % (x)
    return '/' + s(dt.year-2000) + s(dt.month) + s(dt.day) + '/h' + s(dt.hour) + s(dt.minute)

def crawling_by_datetime(date_time):
    suffix = getSuffix(date_time)
    news_all, _ = getItems(date_time, suffix)
    getWC(news_all, suffix)

#%% generate wordcloud from news of last 7 days from now at 00:00
cnt = 0
last_days = 7
tnow = datetime.datetime.now()
d0 = datetime.datetime(tnow.year, tnow.month, tnow.day)
while cnt < last_days:
    crawling_by_datetime(d0)
    d0 -= datetime.timedelta(days=1)
    cnt += 1