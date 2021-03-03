'''
Created on March 2 2021

First Commit Progress:
So far, this just removes all the tags (class, style, src etc.); Still in progress
'''

from bs4 import BeautifulSoup
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

__target_file__ = '../webscraping-o/htmlfiles/2ch.txt' #relative to the tag_anon.py 
org_file_name = os.path.basename(__target_file__)


with open(os.path.join(__location__,__target_file__), 'r', encoding="ISO-8859-1") as f:
    try:
        target_html = f.read() 
    except:
        print("Error in reading file")

soup = BeautifulSoup(target_html, 'html.parser')

def tag_removed(soup):
    '''
    remove inline html tags
    '''
    for tag in soup.findAll(True):
        tag.attrs = None
    return soup

def script_removed(soup):
    '''
    function to remove embedded javascript
    '''



soup = tag_removed(soup)

with open(os.path.join(__location__, f"./modified_{org_file_name}"), 'wb') as f_out:
    try: 
        f_out.write(soup.prettify("utf-8"))
    except:
        print("Error in writing file")


