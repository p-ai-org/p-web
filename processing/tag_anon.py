'''
Created on March 2 2021

Still working on content_removed; others are done
'''

from bs4 import BeautifulSoup
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

__target_file__ = '../webscraping-o/htmlfiles/2ch.txt' #relative to the tag_anon.py 
org_file_name = os.path.basename(__target_file__)


with open(os.path.join(__location__,__target_file__), 'r', encoding="ISO-8859-1") as f:
    try:
        target_html = f.read() 
    except Exception as e:
        print('During file reading, this error occurred:', e)

soup = BeautifulSoup(target_html, 'html.parser')

def tag_removed(soup):
    '''
    change inline html text content so that it says 'ANON_TEXT' (incl. class names, type, style attributes etc.)
    '''
    for tag in soup.findAll(True):
        tag.attrs = tag.attrs.fromkeys(tag.attrs,'ANON_TEXT')
    return soup

def script_removed(soup):
    '''
    empties script tags; ie. remove embedded javascript while still keeping the <script> 
    '''
    for tag in soup.findAll('script'):
        tag.clear()
    return soup

def content_removed(soup):
    '''
    anonymize text content
    '''
    for tag in soup.findAll('True'):
        tag.string = "None"
    return soup


soup = tag_removed(soup)
soup = script_removed(soup)

with open(os.path.join(__location__, f"./modified_{org_file_name}"), 'wb') as f_out:
    try: 
        f_out.write(soup.prettify("utf-8"))
    except Exception as e:
        print('During file writing, this error occurred:', e)


