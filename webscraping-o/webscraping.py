# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:44:50 2021

@author: Alan
"""
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

a_file = open("./websitelist.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

updatelist = []
title = []
for w in contents_split:
    # updatelist.append("https://www." + w + ".com") 
    updatelist.append("https://www." + w)
    # updatelist.append(w);
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

     
    #GRABBING CSS FILES
           
    #array for css_files stylesheet url array
    css_files = []
        
    # get the CSS files and put it into an array
    for css in soup.find_all("link", rel = "stylesheet"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = urljoin(w, css.attrs.get("href"))
            css_files.append(css_url)
    
    #running css path variable
    csspathiter = 0
    #grab the raw css from each url stored in css_files
    for cssurl in css_files:
        csspath = "./cssfiles/" + title[k] + "-" + str(csspathiter) + ".txt"
        csspathiter = csspathiter + 1
        
        # try to open the cssurl from css_files
        try: # need to open with try
            css_r = requests.get(cssurl,timeout=3)
            soup = BeautifulSoup(css_r.content, features="lxml")
        except:
            continue
        
        #get the text data from the css file (stored in p tag)
        css_data = ""
        for para_tag in soup.find_all('p'):
            css_data = para_tag.decode_contents()
        
        #save the css data into a text file
        with open(csspath,"w") as out:
            for i in range(len(css_data)):
                try:
                    out.write(css_data[i])
                except Exception:
                    1+1
                    
        print(csspath)
    
        
        


