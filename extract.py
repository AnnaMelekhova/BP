# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:02:37 2020

@author: Anna
"""

import json

f=open('train_features_0.jsonl')
my_lines = f.readlines()

label=[]
inputs=[]

for i in range(0,len(my_lines)):
    lines_dict=json.loads(my_lines[i]) #returns a dictionary
    
    if lines_dict['label'] == 0 or lines_dict[label] == 1:
        label.append(lines_dict['label'])
    
    new_input=[]
    new_input.append(lines_dict["general"]["has_debug"])
    new_input.append(lines_dict["general"]["has_tls"])
    new_input.append(lines_dict["general"]["has_relocations"])
    new_input.append(lines_dict["general"]["has_signature"])
    new_input.append(lines_dict['general']['has_resources'])
    
    if lines_dict['general']['imports']>0:#if has imports is 1 if not is 0
        new_input.append(1)
    else:
        new_input.append(0)
        
    if lines_dict['general']['exports']>0:#if has exports is 1 if not is 0
        new_input.append(1)
    else:
        new_input.append(0)

    
    for section in lines_dict['section']['sections']:
        new_input.append(section['entropy'])
        break #extract entropy from first section 
                    
    inputs.append(new_input)


