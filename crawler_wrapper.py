#!/usr/bin/env python
import numpy as np
import pandas as pd
import subprocess
import os
import argparse



#To crawl page
pages = ['DailyGreaterKashmir','TimesNow','cnnnews18','jandknow','bbcindia','indiatvnews','KashmirReader','KashmirMonitor','IndiaToday','JammuKashmirTV','kashmirnewzservice']

count = 0

for page in pages:
    count = count+1
    command_to_crawl_page = 'scrapy crawl fb -a email="geekinception17@gmail.com" -a password="rajeevpaji98#" -a page="'+page+'" -a date="2018-01-01" -a lang="it" -o posts_'+str(count)+'.csv'
    os.system(command_to_crawl_page)
print("________________PAGE CRAWL COMPLETE.POSTS STARTED_____________")


for i in range(len(pages)):
    df = pd.read_csv("posts_"+str(i+1)+".csv")
    posts = df.url

    count = 0
    for post in posts:
        count = count+1
        url = "https://mbasic.facebook.com"+post
        command = 'scrapy crawl comments -a email="geekinception17@gmail.com" -a password="rajeevpaji98#" -a post="'+url+'" -o comments'+'.csv'
        print("_____________CRAWLING POST___________\n"+url)
        os.system(command)



