# it won't let the program crash.

# val = int(input("Enter the value : "))
# print(val/2)

# while True:
#     try:
#         n1 = int(input("Enter the value of n1 : "))
#         n2 = int(input("Enter the value of n2 : "))
#         result = n1 /n2
#     except ValueError:
#         print('Plz enter numeric val')
#     except ZeroDivisionError:
#         print('Attempt to div by 0')

#     else:
#         result = n1/n2
#         print(f'{n1: .3f} / {n2: .3f} = {result: .3f}')
#         break
#     finally:
#         print('Always will be executed..')

# raise example hw for ashok  

try:       
    o = open('kdev.txt', 'r')
except InterruptedError:
    print('File does not exist')
else:
    print('File exist')

