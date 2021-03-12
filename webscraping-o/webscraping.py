# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:44:50 2021

@author: Alan
"""
from bs4 import BeautifulSoup
import requests
import time
import datetime
from urllib.parse import urljoin

a_file = open("./websitelist.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

updatelist = []
title = []
for w in contents_split:
    # updatelist.append("https://www." + w + ".com") 
    updatelist.append("https://www." + w)
    title.append(w.split('.')[0])
print(updatelist)
print(title)

k = 0
for w in updatelist: 
    print(w)
    #grab the soup output for each website
    try: # need to open with try
        r = requests.get(w,timeout=3)
        soup = BeautifulSoup(r.content, features="lxml")
    except:
        #display faulty websites
        #print(w);
        k = k + 1
        continue
    
    #check where we are in program
    print(k)
    #make it more readable
    html = soup.prettify()
    
    #iterate name variable
    k = k + 1
    
    #write html data into folder
    path = "./htmlfiles/" + title[k] + ".txt"
    
    #output html into file
    with open(path,"w") as out:
        for i in range(0, len(html)):
            try:
                out.write(html[i])
            except Exception:
                1+1

    # get the CSS files
    css_files = []

    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = urljoin(w, css.attrs.get("href"))
            css_files.append(css_url)   

    #write css data into folder
    for i in range(len(css_files)):
        c = css_files[i]
        path = "./cssfiles/" + title[k] + str(i) + ".txt"
        #output css into file
        with open(path,"w") as out:
            for i in range(0, len(c)):
                try:
                    out.write(c[i])
                except Exception:
                    1+1
    