#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:25:31 2020

@author: kudevara
"""


import re

# pattern = '10.1.12.124'

# strng= 'Match' if re.fullmatch(pattern,'10.1.12.114') else 'No match'

# print(strng)

# strng= 'Match' if re.fullmatch(r'\d{6}','6321267') else 'No match'

# print(strng)

# strng= 'Match' if re.fullmatch(r'\D{6}','abcdef') else 'No match'

# print(strng)

# strng= 'Match' if re.fullmatch(r'[A-Z][a-z]*','Ashok') else 'No match'

# print(strng)

# strng= 'Match' if re.fullmatch('[A-Z][a-z]*','A') else 'No match'

# print(strng)
# unless there's 'escape' no need of 'r'

# strng= 'Match' if re.fullmatch('^[a-z]+','sdjhg') else 'No match'

# print(strng)

# strng= 'Match' if re.fullmatch(r'[A-Z][a-z]*','Ashok') else 'No match'

# print(strng)

# strng= 'Match' if re.fullmatch('[*+/]','+') else 'No match'

# print(strng) [*+/] => is greedy

# strng= 'Match' if re.fullmatch('labell?ed','labellled') else 'No match'

# print(strng)

# street = r'\d{3}\s[A-Z][a-z]*\s[A-Z][a-z]*'

# string = 'Match' if re.fullmatch(street, '123 Main Street') else 'No Match'

# print(string)

# street = r'Main'

# string = 'Match' if re.fullmatch(street, '123 Main Street') else 'No Match'

# print(string)



# string = re.findall('123', '123 Main123Stree Street123 123Street 123')

# print(string)

regex = r"([a-zA-Z]+) (\d+)"
    
match = re.findall(regex, "I was born on June 24") 
print(match)


















