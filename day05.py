#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 08:47:14 2020

@author: kudevara
"""

#subset of seq

# num = [2,3,4,5,6,7,8]

# print(num[2:4])

# num_1 = num[:]

# print(num[::3])

# print(num[9:0:-1])

# print(num[-1:-8:-1])

# num_2 = ['a','b','c']

# num[0:3] = []

# print(num)

# num[0:3] = num_2

# print(num)

# num[:] = []

# print(num)

# num = list(range(1,61))

# print(num)

# print(num[0:len(num):2])


# num[5:10] = [0] * len(num[5:10])
# print(num)

# num[5:]= [0] * len(num[5:])
# print(num)

# num = list(range(1,10))

# # del num[-1]

# # print(num)

# # del num[0:2]

# # print(num)

# del num[:]

# print(num)

# del num

# print(num)

# Pass list to function

# def modify_ele(items):
#     for i in range(len(items)):
#         items[i] *= 2
#     return items
# items = (1,2,3,4)
# print(modify_ele(items))

num = [10,1,9,3,2]
num=sorted(num)
print(num)