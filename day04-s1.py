#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 07:55:20 2020

@author: kudevara
"""


# # List and Tuple

# lst = [0 , 1, 2 , 3, 'hello'] # list is mutable
# lst[3] = 33
# print(lst)

# s = 'hello world !!'
# print(s[0])
# #s[0] = 'H'

# # string and tuple are immutable

# #print(lst[100])

# print(lst[0] + lst[2])

# a_list = []
# for i in range(100,0,-1):
#     a_list = a_list + [i]
# print(a_list)


# print([] + [1])

# letters = []
# letters += 'python'
# print(letters)

# import random
# one = two = three = four = five = six =0
# for i in range(1,100):
#     rand = random.randrange(1,7)
#     print(rand, end=' ')
#     if rand == 1:
#         one += 1
#     if rand == 2:
#         two += 1   
#     if rand == 3:
#         three += 1
#     if rand == 4:
#         four += 1       
#     if rand == 5:
#         five += 1
#     if rand == 6:
#         six += 1  
# print('\n')
# print(f" num of 1's is {one}")   
# print(f" num of 2's is {two}")
# print(f" num of 3's is {three}")
# print(f" num of 4's is {four}")
# print(f" num of 5's is {five}")
# print(f" num of 6's is {six}")     
# from random import randrange
# from collections import Counter
# print(Counter([ random.randrange(1,7) for i in range(10)]))
# # print (rolls)
# # print(Counter(rolls))

# l1 = [10, 20]
# l2 = [30, 40]
# list_concat = l1 + l2
# print(list_concat)

# for i in range(len(list_concat)):
#     print(f'{list_concat[i]}' , end=' ')


# a = [1,2,3]
# b=[1,2,3]
# c=[1,2,3,4]
# print(a==b) 
# print(a==c) 
# print(a<c)

# lst = [1,2,3,4,5]

# def cube(lst):
#     for i in range(len(lst)):
#         lst[i] *=3
#     return(lst)    
# print(cube(lst))        


# chars = []
# chars += 'Hello world !!'
# print(chars)

# Tuple

# tup = (1,2,3,'red')
# # tup[0]=11
# # print(tup[0])
# print(tup)

# time_tupe = (9,55,30)

# print(time_tupe[0]*3600 + time_tupe[1]*60 + time_tupe[2])

# tup1 = (1,2,3)
# tup2 = tup1

# print(tup2)

# tup1 += (4,5)
# print(tup1)

# print(tup2)

# tup = (1 , 2 ,3 ,[1,2,3])

# print(tup[3][1])

# stu_tup = ('ashok', [99,100,99])

# # f_name = stu_tup[0]
# # eng = stu_tup[1][0]
# # math = stu_tup[1][1]
# # sci = stu_tup[1][2]

# # f_name, eng, math, sci = stu_tup[0], stu_tup[1][0], stu_tup[1][1], stu_tup[1][2]
# f_name, marks = stu_tup

# print(f'firstName is {f_name} and marks are {marks}')

# #print(f"{f_name}'s marks in eng is {eng} , math is {math} and sci is {sci}")


# first, second = 'h1'

# first
# Out[94]: 'h'

# second
# Out[95]: '1'

# n1,n2,n3 = [2,3,4]

# n1
# Out[97]: 2

# n3
# Out[98]: 4

# n1,n2,n3,n4,n5 = range(10,60,10)

# n3
# Out[100]: 30

# n5
# Out[101]: 50
# n1 = 99

# n2 = 100

# n1,n2 = (n1,n2)

# n1
# Out[105]: 99

# n3 =(n1,n2)

# n3
# Out[107]: (99, 100)

# colors = ['red', 'blue', 'green']

# #print(list(enumerate(colors)), end='')

# for index, value in enumerate(colors):
#     print(f'{index} : {value}')

num = [19, 3, 15, 7, 11]
print('bar chart \n')

for index, value in enumerate(num):
    print(f'{index} : {value} : {"*" * value}')









































































