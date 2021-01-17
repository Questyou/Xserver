###for 循环
##新建一个列表
users = ['yi' , 'er' , 'san']
#学习循环、9*9 乘法表
# for i in range(1 , 10 ):
#     for j in range(1 , i+1 ):
#         print('%d * %d = %d' %(j , i , i*j) , end=' ' )
#     print(' ')

import  xlrd , openpyxl

file_path = './data/test.xlsx'
file = xlrd.open_workbook(file_path)

sh = file.sheet_by_index(0)

print(sh.nrows , sh.ncols)
print(sh.row_values(2 , 0 , 2))
