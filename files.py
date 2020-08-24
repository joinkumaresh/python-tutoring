# text: seq of chars
# 1st pos '0'
# bin files => seq of bytes (img/video)

# with open('acc.txt', mode='w') as ac:
#     ac.write('123 a 123.32\n')
#     ac.write('234 b 234.32\n')
#     ac.write('345 c 345.32\n')
#     ac.write('456 d 456.32\n')
#     ac.write('567 e 567.32\n')
    
# with open('acc.txt', 'r') as ac_r:
#     print(f'{"Acc_no": <10} {"Acc_name": <10} {"Acc_bal": >10}')
#     for rec in ac_r:
#         acc,name,bal = rec.split()
#         print(f'{acc : <10} {name : <10} {bal : >10}')

# update 345 => 300 Ashok J 333.33\n
# read 
# write 

# acc_r = open('acc.txt', 'r')
# temp_f = open('temp.txt', 'w')

# with acc_r, temp_f:
#     for rec in acc_r:
#         account,name,balance = rec.split()
#         if account != '345':
#             temp_f.write(rec)
#         else:
#             account= '300'
#             name= 'Ashok J'
#             balance= '333.33\n'
#             new_rec = ' '.join([account,name,balance])
#             temp_f.write(new_rec)    

# import os
# os.rename('temp.txt', 'acc.txt')

# JSON
# more or like py dict obj
# "Kumaresh" / 100 or 100.50 / true - false / Py: None Json: null 
# Py dict obj => JSON obj xml/json / yaml

# acc_dict = {
#     'accounts' : [
#         { 'acc' : 100, 'name' : 'Kdev', 'bal' : 234.23 },
#         { 'acc' : 200, 'name' : 'AshokJ', 'bal' : 456.23 },
#         { 'acc' : 300, 'name' : 'Jay', 'bal' : 567.23 }]
# }
import json
# with open('accounts.json', 'w') as acc_j:
#     json.dump(acc_dict, acc_j)

with open('accounts.json', 'r') as acj_r:
    #acc_json = json.load(acj_r)
    #print(acc_json['accounts'][1])
    print(json.dumps(json.load(acj_r), indent=4))