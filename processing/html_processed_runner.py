'''
Created on March 13 2021

author: Aaron
'''

from bs4 import BeautifulSoup
from html_processed import tag_removed, script_removed, content_removed

import os


# org_file_name = os.path.basename(__target_file__)

def perFile(sourceFile, destLoc, basename):


    with open(sourceFile, 'r', encoding="ISO-8859-1") as f:
        try:
            target_html = f.read() 
        except Exception as e:
            print('During file reading, this error occurred:', e)

    soup = BeautifulSoup(target_html, 'html.parser')

    cur_classes = {
        #'orgName': 'newName' 
        }
    class_counter = 1
    id_counter = 1

    soup = tag_removed(soup, cur_classes, class_counter, id_counter)
    soup = script_removed(soup)
    soup = content_removed(soup)

    with open(os.path.join(destLoc, f"./modified_{basename}"), 'wb') as f_out:
        try: 
            f_out.write(soup.prettify("utf-8"))
        except Exception as e:
            print('During file writing, this error occurred:', e)


def allFile():
    destLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), 'mod_htmlfiles'))
    sourceLoc = os.path.realpath(os.path.join(os.path.dirname(__file__), '../webscraping-o/htmlfiles'))

    for file in os.scandir(sourceLoc):
        sourceFile = os.path.join(sourceLoc, file.name);
        # perFile(sourceFile, destLoc, file.name)
    os.scandir().close()


# allFile();

perFile('/Users/aaronxie/Documents/CodingProjects/p-web/webscraping-o/htmlfiles/2ch.txt', os.path.realpath(os.path.join(os.path.dirname(__file__), 'mod_htmlfiles')), '2ch.txt')




















