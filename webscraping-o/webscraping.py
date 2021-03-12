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


for k in range(len(updatelist)): 
    w = updatelist[k]
    print(w)
    #grab the soup output for each website
    try: # need to open with try
        r = requests.get(w,timeout=3)
        soup = BeautifulSoup(r.content, features="lxml")
    except:
        #display faulty websites
        #print(w);
        continue
    
    #check where we are in program
    print(k)
    #make it more readable
    html = soup.prettify()
    
    #write html data into folder
    path = "./htmlfiles/" + title[k] + ".txt"
    
    #output html into file
    with open(path,"w") as out:
        for i in range(len(html)):
            try:
                out.write(html[i])
            except Exception:
                1+1

    # get the CSS files and put it into an array
    css_files = []

    for css in soup.find_all("link", rel = "stylesheet"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = urljoin(w, css.attrs.get("href"))
            css_files.append(css_url)

    #write css data into folder
    path = "./cssfiles/" + title[k] + ".txt"
    with open(path, "w") as out:
        #write each css link
        for i in range(len(css_files)):
            c = css_files[i]
            #output css into file
            for i in range(len(c)):
                try:
                    out.write(c[i])
                except Exception:
                    1+1
            try:
                out.write("\n")
            except Exception:
                1+1
