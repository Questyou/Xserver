import xlrd
import re
# 读取文件的内容

import os.path

fileurl = 'D:\Xserver\XserverTest\TrinityAres-StreamCenter\Work.xlsx'
data = xlrd.open_workbook(fileurl)
sheetName = data.sheet_names()
table = data.sheet_by_name(sheetName[0])

def getnrow():
    # print(table.nrows)
    return table.nrows



def lineone():
    # table.col_values(0)
    print(table.row_values(0))


def getLineOneData(num):
    for i in range(table.nrows):
        cel = table.cell( i+num  , 0 ).value
        # celB = re.findall(r"[\w']+" , cel)
        # print(celB)
        # celB = cel.replace("、","/")
        # break
        print(cel)
