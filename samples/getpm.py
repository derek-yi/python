# -*- coding: utf-8 -*-
# get pm2.5
# python 3.5

import urllib.request
import threading
from time import ctime
from bs4 import BeautifulSoup

def get_pm25(city_name):
    site = 'http://www.pm25.com/' + city_name + '.html'
    html = urllib.request.urlopen(site)
    soup = BeautifulSoup(html, 'lxml')
    #print(soup.prettify().encode('utf-8'))
    
    city = soup.find(class_ = 'bi_loaction_city')
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})
    quality = soup.select(".bi_aqiarea_right span")
    result = soup.find("div", class_='bi_aqiarea_bottom')
    
    print(city.text + ' AQI:' + aqi.text + ' quality: ' + quality[0].text + result.text)

def one_thread():
    get_pm25('wuhan')

def two_thread():
    threads = []
    t1 = threading.Thread(target=get_pm25, args=('wuhan',))
    threads.append(t1)
    t2 = threading.Thread(target=get_pm25, args=('shenzhen',))
    threads.append(t2)
    
    for t in threads:
        t.start()
    
if __name__ == '__main__':
    #one_thread()
    two_thread()
    
    
    