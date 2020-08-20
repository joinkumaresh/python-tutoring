#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:11:19 2020

@author: kudevara
"""

# grade = 60 

# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')    
# elif grade >= 70:
#     print('C')
# else:
#     print('D')    
    
# *********************    

# for / while

# when u know the limit => use for
# when you don't know the limit => use while

# prod = 3
# while prod <= 50:
#     prod = prod * 3
# print(prod)    

# for char in 'Programming':
#     print(char, end = ' ')

# total = 0
# for num in [-2,-3,0,7,8]:
#     total+=num
# print(total)    

# for counter in range(11):
#     print(counter, end = ' ')

# ex1: sum of values from 0 to 1m
# ex2: given an i/p what is the sq of that value   

# n = 10
# print(f'square of {n} is {n*n}')

# keep getting i/p from the user until he/she press -1
# find total and avg

# initialize
# get marks as i/p
# total = 0
# marks_counter = 0


# # process

# mark = int(input('Please enter you marks, also enter -1 if you want to terminate '))
# while mark != -1:
#     total += mark
#     marks_counter += 1
#     mark = int(input('Please enter you marks, also enter -1 if you want to terminate '))

# #print(total / marks_counter)
    


# # display

# if total != 0:
#     avg = total / marks_counter
#     print(f'class avg is {avg:.2f}')
# else:
#     print('no grade was entered')    



# for num in range(102, 0, -3):
#     print(num, end = ' ')

from decimal import Decimal
print(f"{Decimal('37.45') * Decimal('1.062') :.2f}")



    

    