# -*- coding: utf-8 -*- 
from re import template
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import datetime
import random
import csv
import sys
import pandas as pd
import numpy as np
import json
import requests
import time

def Get_Now():
    Today_Time = datetime.datetime.today().strftime("%Y%m%d")
    # Today_Time_Stamp = time.strptime(Today_Time, "%Y%m%d")

    return Today_Time

def Get_Now_Plus():
    day = datetime.datetime.today().isoweekday()
    Today_Time = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    Today_Time_Array = time.strptime(Today_Time, "%Y-%m-%d-%H-%M-%S")
    Today_Time_Stamp = int(time.mktime(Today_Time_Array)) * 1000
    
    return Today_Time_Stamp

def crawler(url):
    time.sleep(3)
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    # ua = UserAgent()
    # uadata = ua.random
    headers = {'User-Agent': 'Mozilla/5.0',
    #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #    'Accept-Encoding': 'none',
    #    'Accept-Language': 'en-US,en;q=0.8',
    #    'Connection': 'keep-alive'
    }
    while 1:
        try:
            session = requests.Session()
            res =  session.get(url, headers=headers, timeout=5)
            if res.status_code != 200:
                time.sleep(random.randint(3,5))
                print(res.status_code)
                print(url)
                return 
            else:
                res.encoding = 'utf-8'
                print(res.status_code)
                print(url)
                return res.text
        except Exception as e:
            print(e)
            time.sleep(random.randint(3,5))
            continue
        except KeyboardInterrupt as e:
            sys.exit(1)