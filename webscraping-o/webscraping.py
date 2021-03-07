# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:44:50 2021

@author: Alan
"""
from bs4 import BeautifulSoup
import requests

#change this path to where the website list is saved
a_file = open("./websitelist.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

updatelist = []
title = []
for w in contents_split:
    updatelist.append("https://www." + w)
    title.append(w.split('.')[0])
print(updatelist)
print(title)

k = 0

for w in updatelist:   
    print(w)
    #grab the soup output for each website
    try: # need to open with try
        r = requests.get(w)
        soup = BeautifulSoup(r.content, features="lxml")
    except:
        #display faulty websites
        #print(w)
        k = k + 1
        continue
    
    #check where we are in program
    print(k)
    #make it more readable
    html = soup.prettify()
    
    #write html data into folder
    path = "./htmlfiles/" + title[k] + ".txt"
    
    #iterate name variable
    k = k + 1
    
    #output into file
    with open(path,"w") as out:
        for i in range(0, len(html)):
            try:
                out.write(html[i])
            except Exception:
                1+1
    
    
