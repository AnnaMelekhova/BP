# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:02:37 2020

@author: Anna
"""

import json
import pandas as pd

f=open('train_features_0.jsonl')
my_lines = f.readlines()

label=[]
entropy=[]
has_debug=[]
has_relocations=[]
has_signature=[]
has_resources=[]
has_tls=[]
exports=[]
imports=[]
imports_l=[]

for i in range(0,len(my_lines)):
    lines_dict=json.loads(my_lines[i]) #returns a dictionary
    label.append(lines_dict['label']) #label list
    has_debug.append(lines_dict['general']['has_debug']) #has_debug list
    has_signature.append(lines_dict['general']['has_signature'])
    has_relocations.append(lines_dict['general']['has_relocations'])
    has_resources.append(lines_dict['general']['has_resources'])
    has_tls.append(lines_dict['general']['has_tls'])
    exports.append(lines_dict['general']['exports'])
    imports.append(lines_dict['general']['imports'])
    imports_l.append(lines_dict['imports'])
    
    for section in lines_dict['section']['sections']:
        entropy.append(section['entropy']/8) #entropy list in section
        

