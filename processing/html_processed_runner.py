'''
Created on March 13 2021

author: Aaron
'''

from bs4 import BeautifulSoup
from html_processed import tag_removed, script_removed, content_removed, style_extract

import os


def perFile(sourceFile, destLoc, basename, styleDestLoc):


    with open(sourceFile, 'r', encoding="ISO-8859-1") as f:
        try:
            target_html = f.read() 
        except Exception as e:
            print('During file reading, this error occurred:', e)

    soup = BeautifulSoup(target_html, 'html.parser')

    cur_classes = {
        #'orgName': 'newName' 
        }
    cur_ids = {
        # 'orgName' : 'newName
    }
    class_counter = 1
    id_counter = 1

    soup = style_extract(soup, styleDestLoc, basename)
    soup = script_removed(soup)
    soup = tag_removed(soup, cur_classes, class_counter, id_counter, cur_ids)
    soup = content_removed(soup) # must be last, or else contents of style won't be kept 

    with open(os.path.join(destLoc, f"./modified_{basename}"), 'wb') as f_out:
        try: 
            f_out.write(soup.prettify("utf-8"))
        except Exception as e:
            print('During file writing, this error occurred:', e)


def allFile():
    destLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), 'mod_htmlfiles'))
    sourceLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), '../webscraping-o/htmlfiles'))
    styleDestLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), 'extract_css'))

    for file in os.scandir(sourceLoc):
        sourceFile = os.path.join(sourceLoc, file.name);
        perFile(sourceFile, destLoc, file.name, styleDestLoc)
    os.scandir().close()


allFile();

# Single File Testing
# oneDestLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), 'mod_htmlfiles'))
# oneSourceLoc = os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), '../webscraping-o/htmlfiles')), 'cnn.txt')
# styleDestLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), 'extract_css'))
# perFile(oneSourceLoc, oneDestLoc, 'cnn.txt', styleDestLoc)
