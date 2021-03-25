'''
Created on March 2 2021

author: Aaron
'''

from bs4 import BeautifulSoup
import re #only for match the names


def tag_removed(soup, cur_classes, class_counter, id_counter, cur_ids):
    '''
    manipulate html tag names

    tags to keep:
    align
    type
    rel
    role
    width
    height
    allowtransparency
    allowfullscreen
    aria-* !!!! Except aria-labeledby and aria-describedby which need to replace with ID and aria-label which is custom text (so replace with "" )
    '''
    for tag in soup.findAll(True):
        for attr_type, attr_values in tag.attrs.items():
            # class subbed with placeholder
            if attr_type == 'class':
                for i, class_name in enumerate(attr_values):
                    if class_name in cur_classes:
                        attr_values[i] = cur_classes[class_name]
                    else:
                        new_class_name = 'class_' + str(class_counter)
                        attr_values[i] = new_class_name
                        cur_classes[class_name] = new_class_name
                        class_counter += 1
            # id subbed with placeholder
            elif attr_type == "id":
                if attr_values in cur_ids:
                    tag.attrs[attr_type] = cur_ids[attr_values] 
                else:
                    new_id_name = 'id_' + str(id_counter)
                    cur_ids[attr_values] = new_id_name
                    tag.attrs[attr_type] = new_id_name
                    id_counter += 1
            # aria tags to replace 
                #aria-labeledby is reference to ID so replace with ID
            elif re.search("aria-labelledby", attr_type) is not None or re.search("aria-describedby", attr_type) is not None:
                if attr_values in cur_ids:
                    tag.attrs[attr_type] = cur_ids[attr_values]
                else:
                    new_id_name = 'id_' + str(id_counter)
                    cur_ids[attr_values] = new_id_name
                    tag.attrs[attr_type] = new_id_name
                    id_counter += 1
            elif re.search("aria-label", attr_type) is not None:
                tag.attrs[attr_type] = ""
            # other Aria-* tags and their value should be kept
            elif re.search("aria", attr_type) is not None:
                continue
            # exclude tags that has reoccuring values, all else replace with empty string
            elif attr_type not in ['align','type','rel','role','width','height','allowtransparency']:
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

    return soup


