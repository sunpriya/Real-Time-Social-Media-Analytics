#!/usr/bin/env python
import numpy as np
import pandas as pd
import subprocess
import os
import argparse


email_id = "chaosisfun00@gmail.com"
password = "Justchill@19"

#To crawl page

command_to_crawl_page = 'scrapy crawl fb -a email="chaosisfun00@gmail.com" -a password="Justchill@19" -a page="DailyGreaterKashmir" -a date="2018-01-01" -a lang="it" -a max=100 -o posts.csv'

os.system(command_to_crawl_page)
print("________________PAGE CRAWL COMPLETE.POSTS STARTED_____________")

df = pd.read_csv("/home/sunpriya/fbcrawl/posts.csv")
posts = df.url

count = 0
for post in posts:
    count = count+1
    url = "https://mbasic.facebook.com"+post
    command = 'scrapy crawl comments -a email="chaosisfun00@gmail.com" -a password="Justchill@19" -a post="'+url+'" -o comments_'+str(count)+'.csv'
    print("_____________CRAWLING POST___________\n"+url)
    os.system(command)



