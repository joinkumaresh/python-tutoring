# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  8 09:36:46 2020

# @author: kudevara
# """

# #operators

# import numpy as np

# # n = np.arange(1,6)
# # # print(n)

# # # print(n * 2)
# # # n += 10
# # # print(n)

# # n2 = np.linspace(1.1,5.5,5)
# # print(n2)

# # print(f'{n*n2}')

# # gd = np.array([[1,2,3,4], [5,6,7,8], [10,11,12,13]])

# # print(gd.sum())
# # gd.max()
# # gd.min()
# # print(gd.mean(axis=1))
# # gd.std()
# # gd.var()

# # 12 random grades 60 to 100
# # reshape 3 X 4
# # find avg of grades  / avg of row / avg of col

# grades = np.random.randint(60,101,12).reshape(3,4)
# # print(grades.mean())
# # print(grades.mean(axis=0))
# # print(grades.mean(axis=1))


# # print(np.power(3,3))

# grades[0,1] = 96



# # shallow copy

# g2 = grades.view()












# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# [1 2 3 4 5]

# [ i * 2 for in in rane(6)]
#   File "<ipython-input-11-a86a2a03b14c>", line 1
#     [ i * 2 for in in rane(6)]
#                  ^
# SyntaxError: invalid syntax


# [ i * 2 for i in rane(6)]
# Traceback (most recent call last):

#   File "<ipython-input-12-8f1e353471b4>", line 1, in <module>
#     [ i * 2 for i in rane(6)]

# NameError: name 'rane' is not defined


# [ i * 2 for i in range(6)]
# Out[13]: [0, 2, 4, 6, 8, 10]

# n
# Out[14]: array([1, 2, 3, 4, 5])

# n * 2
# Out[15]: array([ 2,  4,  6,  8, 10])

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# [1 2 3 4 5]
# [ 2  4  6  8 10]

# n ** 3
# Out[17]: array([  1,   8,  27,  64, 125])

# [1,2,3] * 2
# Out[18]: [1, 2, 3, 1, 2, 3]

# [ i * 2 for i in range(6)]
# Out[19]: [0, 2, 4, 6, 8, 10]

# n += 10

# n
# Out[21]: array([11, 12, 13, 14, 15])

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
#   File "<fstring>", line 1
#     (n += 10)
#         ^
# SyntaxError: invalid syntax


# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# [1 2 3 4 5]
# [ 2  4  6  8 10]
# [11 12 13 14 15]

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# [1.1 2.2 3.3 4.4 5.5]

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# [1.1 2.2 3.3 4.4 5.5]
# [ 1.1  4.4  9.9 17.6 27.5]

# n > 10
# Out[26]: array([False, False, False, False, False])

# n < 10
# Out[27]: array([ True,  True,  True,  True,  True])

# n2 > 10
# Out[28]: array([False, False, False, False, False])

# n == n2
# Out[29]: array([False, False, False, False, False])

# n != n2
# Out[30]: array([ True,  True,  True,  True,  True])

# np.arange(1,6) ** 2
# Out[31]: array([ 1,  4,  9, 16, 25])

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')

# gd
# Out[33]: 
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [10, 11, 12, 13]])

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# 82

# gd.mean?
# Docstring:
# a.mean(axis=None, dtype=None, out=None, keepdims=False)

# Returns the average of the array elements along given axis.

# Refer to `numpy.mean` for full documentation.

# See Also
# --------
# numpy.mean : equivalent function
# Type:      builtin_function_or_method

# gd.mean??
# Docstring:
# a.mean(axis=None, dtype=None, out=None, keepdims=False)

# Returns the average of the array elements along given axis.

# Refer to `numpy.mean` for full documentation.

# See Also
# --------
# numpy.mean : equivalent function
# Type:      builtin_function_or_method

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# 82
# Traceback (most recent call last):

#   File "/Users/kudevara/untitled0.py", line 30, in <module>
#     print(gd.mean(axes=0))

# TypeError: _mean() got an unexpected keyword argument 'axes'


# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# 82
# [5.33333333 6.33333333 7.33333333 8.33333333]

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# 82
# [ 2.5  6.5 11.5]

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')

# grades
# Out[41]: 
# array([[71, 61, 72, 93],
#        [69, 85, 72, 66],
#        [99, 98, 82, 76]])

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# 81.75
# [90.66666667 75.33333333 80.         81.        ]
# [73.5  87.25 84.5 ]

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')
# 27

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')

# grades
# Out[46]: 
# array([[85, 96, 94, 83],
#        [91, 90, 93, 74],
#        [64, 72, 96, 72]])

# grades[1]
# Out[47]: array([91, 90, 93, 74])

# grades[0:2]
# Out[48]: 
# array([[85, 96, 94, 83],
#        [91, 90, 93, 74]])

# grdaes[1]
# Traceback (most recent call last):

#   File "<ipython-input-49-74b907e38416>", line 1, in <module>
#     grdaes[1]

# NameError: name 'grdaes' is not defined


# grades[1]
# Out[50]: array([91, 90, 93, 74])

# grades[3]
# Traceback (most recent call last):

#   File "<ipython-input-51-5041764402b7>", line 1, in <module>
#     grades[3]

# IndexError: index 3 is out of bounds for axis 0 with size 3


# grades[2]
# Out[52]: array([64, 72, 96, 72])

# grades[[0,2]]
# Out[53]: 
# array([[85, 96, 94, 83],
#        [64, 72, 96, 72]])

# grades[:,0]
# Out[54]: array([85, 91, 64])

# grades[:,1:3]
# Out[55]: 
# array([[96, 94],
#        [90, 93],
#        [72, 96]])

# grades[2,1:3]
# Out[56]: array([72, 96])

# runfile('/Users/kudevara/untitled0.py', wdir='/Users/kudevara')

# grades
# Out[58]: 
# array([[73, 96, 78, 94],
#        [82, 91, 62, 82],
#        [72, 98, 83, 99]])

# g2
# Out[59]: 
# array([[73, 96, 78, 94],
#        [82, 91, 62, 82],
#        [72, 98, 83, 99]])

# id(grades)
# Out[60]: 4803031328

# id(g2)
# Out[61]: 4710123760

# n[1] *= 10

# grdaes[1] *= 10
# Traceback (most recent call last):

#   File "<ipython-input-63-cfeabb07c0f8>", line 1, in <module>
#     grdaes[1] *= 10

# NameError: name 'grdaes' is not defined


# grades[1] *= 10

# grdaes
# Traceback (most recent call last):

#   File "<ipython-input-65-0a0947591299>", line 1, in <module>
#     grdaes

# NameError: name 'grdaes' is not defined


# grades
# Out[66]: 
# array([[ 73,  96,  78,  94],
#        [820, 910, 620, 820],
#        [ 72,  98,  83,  99]])

# g2
# Out[67]: 
# array([[ 73,  96,  78,  94],
#        [820, 910, 620, 820],
#        [ 72,  98,  83,  99]])

# g2[1] /=10
# Traceback (most recent call last):

#   File "<ipython-input-68-f4204ab041fc>", line 1, in <module>
#     g2[1] /=10

# TypeError: No loop matching the specified signature and casting was found for ufunc true_divide


# g2[1] /= 10
# Traceback (most recent call last):

#   File "<ipython-input-69-75aaac4300d8>", line 1, in <module>
#     g2[1] /= 10

# TypeError: No loop matching the specified signature and casting was found for ufunc true_divide


# g2[1] 
# Out[70]: array([820, 910, 620, 820])

# g2[1] /= 10
# Traceback (most recent call last):

#   File "<ipython-input-71-75aaac4300d8>", line 1, in <module>
#     g2[1] /= 10

# TypeError: No loop matching the specified signature and casting was found for ufunc true_divide


# g2[1] *= 10

# g2[1] 
# Out[73]: array([8200, 9100, 6200, 8200])

# g2[1] /= 10
# Traceback (most recent call last):

#   File "<ipython-input-74-75aaac4300d8>", line 1, in <module>
#     g2[1] /= 10

# TypeError: No loop matching the specified signature and casting was found for ufunc true_divide


# g2 = grades[0:3]

# g2
# Out[76]: 
# array([[  73,   96,   78,   94],
#        [8200, 9100, 6200, 8200],
#        [  72,   98,   83,   99]])

# id(grades)
# Out[77]: 4803031328

# id(g2)
# Out[78]: 4722786096

# g2[3]
# Traceback (most recent call last):

#   File "<ipython-input-79-dc644a6c474a>", line 1, in <module>
#     g2[3]

# IndexError: index 3 is out of bounds for axis 0 with size 3


# grades
# Out[80]: 
# array([[  73,   96,   78,   94],
#        [8200, 9100, 6200, 8200],
#        [  72,   98,   83,   99]])

# g2
# Out[81]: 
# array([[  73,   96,   78,   94],
#        [8200, 9100, 6200, 8200],
#        [  72,   98,   83,   99]])

# grades[3]
# Traceback (most recent call last):

#   File "<ipython-input-82-5041764402b7>", line 1, in <module>
#     grades[3]

# IndexError: index 3 is out of bounds for axis 0 with size 3


# g3 = grades[:,1:3]

# g3
# Out[84]: 
# array([[  96,   78],
#        [9100, 6200],
#        [  98,   83]])

# g3[:,0]
# Out[85]: array([  96, 9100,   98])

# g3[:,4]
# Traceback (most recent call last):

#   File "<ipython-input-86-c4e8fb413ad1>", line 1, in <module>
#     g3[:,4]

# IndexError: index 4 is out of bounds for axis 1 with size 2


# g3[:,3]
# Traceback (most recent call last):

#   File "<ipython-input-87-ee9b0ef86792>", line 1, in <module>
#     g3[:,3]

# IndexError: index 3 is out of bounds for axis 1 with size 2


# g3[:,2]
# Traceback (most recent call last):

#   File "<ipython-input-88-dbfd4291689e>", line 1, in <module>
#     g3[:,2]

# IndexError: index 2 is out of bounds for axis 1 with size 2








# n = np.arange(1,6)

# n
# Out[90]: array([1, 2, 3, 4, 5])

# n2 = n.copy()

# n2
# Out[92]: array([1, 2, 3, 4, 5])

# n[1]
# Out[93]: 2

# n[1] *= 10

# n[1]
# Out[95]: 20

# n2[1]
# Out[96]: 2

# n
# Out[97]: array([ 1, 20,  3,  4,  5])

# n2
# Out[98]: array([1, 2, 3, 4, 5])

# n2 = n

# n
# Out[100]: array([ 1, 20,  3,  4,  5])

# n2
# Out[101]: array([ 1, 20,  3,  4,  5])

# n
# Out[102]: array([ 1, 20,  3,  4,  5])

# grades
# Out[103]: 
# array([[  73,   96,   78,   94],
#        [8200, 9100, 6200, 8200],
#        [  72,   98,   83,   99]])

# gd
# Out[104]: 
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [10, 11, 12, 13]])

# gd.reshape(1,6)
# Traceback (most recent call last):

#   File "<ipython-input-105-b4e5fbf89ee6>", line 1, in <module>
#     gd.reshape(1,6)

# ValueError: cannot reshape array of size 12 into shape (1,6)


# gd.reshape(1,12)
# Out[106]: array([[ 1,  2,  3,  4,  5,  6,  7,  8, 10, 11, 12, 13]])

# gd
# Out[107]: 
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [10, 11, 12, 13]])

# gd
# Out[108]: 
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [10, 11, 12, 13]])

# gd.resize(1,12)

# gd
# Out[110]: array([[ 1,  2,  3,  4,  5,  6,  7,  8, 10, 11, 12, 13]])

# gd
# Out[111]: array([[ 1,  2,  3,  4,  5,  6,  7,  8, 10, 11, 12, 13]])

# gd.resize(3,4)

# gd
# Out[113]: 
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [10, 11, 12, 13]])

# gd.T
# Out[114]: 
# array([[ 1,  5, 10],
#        [ 2,  6, 11],
#        [ 3,  7, 12],
#        [ 4,  8, 13]])

















