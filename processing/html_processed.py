'''
Created on March 2 2021

author: Aaron
'''

from bs4 import BeautifulSoup
import re #only for match the names


def tag_removed(soup, cur_classes, class_counter, id_counter):
    '''
    manipulate html tag names
    '''
    for tag in soup.findAll(True):
        for attr_type, attr_values in tag.attrs.items():
            if attr_type == 'class':
                for i, class_name in enumerate(attr_values):
                    if class_name in cur_classes:
                        attr_values[i] = cur_classes[class_name]
                    else:
                        new_class_name = 'Class_' + str(class_counter)
                        attr_values[i] = new_class_name
                        cur_classes[class_name] = new_class_name
                        class_counter += 1
            elif attr_type == "id":
                new_id_name = 'Id_' + str(id_counter)
                tag.attrs[attr_type] = new_id_name
                id_counter += 1
            else:
                tag.attrs[attr_type] = ""
        # to replace data- attributes with just data-
        new_attrs = {re.sub('data-([^\s]+)', 'data-', key): tag.attrs[key] for key in tag.attrs}
        tag.attrs = new_attrs

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
    for tags in soup.find_all(string=True):
        tags.extract()

    #Do we want <br /> removed?
    for br in soup.findAll('br'):
        br.extract()


    #this method does not work with multiple string segments on same level
        # def is_the_only_string_within_a_tag(s):
        #     return (s == s.parent.string)

        # for tags in soup.find_all(string=is_the_only_string_within_a_tag):
        #     for i in range(len(tags.parent.contents)):
        #         # tags.parent.contents[i] = "Text_" + str(text_counter)
        #         # text_counter += 1
        #         print(tags.parent.contents[i]);
        
        # print(text_counter);

    return soup


