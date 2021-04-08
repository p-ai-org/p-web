# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:58:55 2021

@author: Alan
"""

import glob


read_files = glob.glob("./mod_htmlfiles/*.txt")

with open("result.txt", "w", encoding="utf8") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            try:
                print(f);
                outfile.write(infile.read())
                outfile.write("\n")
                outfile.write("\n")
                outfile.write("<|endoftext|>");
                outfile.write("\n")
                outfile.write("\n")
            except:
                print("error");