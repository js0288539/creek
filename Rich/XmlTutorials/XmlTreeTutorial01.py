# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:25:39 2020

https://docs.python.org/2/library/xml.etree.elementtree.html

@author: owner
"""

import xml.etree.ElementTree as ET

# full_input_file = 'F:/Public/Creek/Rich/XmlTutorials/XmlTreeTutorial01.py'
full_input_file = r'XmlTutorials/TestFile01.xml'
full_input_file = 'TestFile01.xml'

tree = ET.parse(full_input_file)
root = tree.getroot()

# print(root.attrib)
for child in root:
    print(f"Child:{child.tag}\tAttribute: {child.attrib['name']}")

print('\n')

for neighbor in root.iter('neighbor'):
    print(f"Name: {neighbor.attrib['name']}\tDirection: {neighbor.attrib['direction']}")

