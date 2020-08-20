# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

text = ('This is a sample text '
         'This is another sample text')

word_count ={}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, frequency in word_count.items():        
      print(f' {word:<12} {frequency}')
      
print('Total number of unique words' , len(word_count))      

# num = [1,2,3,4,5,6,7]

# # def is_odd(x):
# #     return x%2 !=0

# # print(list(filter(is_odd, num)))

# # a = [item for item in num if is_odd(item)]
# # print(a)

# print(list(filter(lambda x: x%2 !=0,num)))

# a=list(map(lambda x: x**2,num))
# print(a)

# import functools

# print(functools.reduce( lambda x,y: x+y,[1,2,3,4,5]))

# print(((((1+2)+3)+4)+5))