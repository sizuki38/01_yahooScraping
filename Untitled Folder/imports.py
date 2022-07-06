import os, pickle, time, requests, schedule
from datetime import datetime
from glob import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

yahoo     = 'https://news.yahoo.co.jp/ranking/access/news/'
comment = '/comments'
page    = '?page='
order   = '&order=newer'

category = {'総合':'total','国内':'domestic','国際':'world',
'経済':'business','エンタメ':'entertainment','スポーツ':'sports',
'IT・科学':'it-science','ライフ':'life','地域':'local'}


key = 'AIzaSyCzbQZosbQFVCmZmggfsFbf03PAqssAo-g'
url = f'https://language.googleapis.com/v1/documents:analyzeSentiment?key={key}'
header = {'Content-Type': 'application/json'}