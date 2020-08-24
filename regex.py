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



# string = re.findall('192.168.1.62', '192.168.1.62 Main192.168.1.62Stree Stree192.168.1.62 123Street 192.168.1.62')

# print(len(string))

# regex = r"([a-zA-Z]+) (\d+)"
    
# match = re.findall(regex, "I was born on June 24") 
# print(match)

# text = 'Kumaresh Devarajan, email: kdev123@gmail.com'
# pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), email: (\w+@\w+\.\w{3})'
# result = re.search(pattern, text)

# print(result.groups(1))


import pandas as pd

# zips = pd.Series({'Udt' : '642126', 'blr-sjp' : '56003'})

# print(zips.str.match(r'\d{6}'))

# cities = pd.Series({'A':'123A', 'B':'234B'})
# print(cities.str.contains(r'[A-Z]'))                    
                    
# match => looks for a match for the entire string
# contains => looks for a match for the patternb in the string


contacts = [['K Dev', 'kdev123@gmail.com', '1234567890'],
            ['A Jaya', 'ash@gmail.com', '0987654321']]
contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Mobile'])
print(contactsdf)

def get_formattable_mobile(value):
    result = re.fullmatch(r'(\d{3}\d{3}\d{4})', value)
    return '-'.join(result.groups()) if result else value

formatted_phone = contactsdf['Mobile'].map(get_formattable_mobile)
contactsdf['Mobile'] = formatted_phone

print(contactsdf)







































