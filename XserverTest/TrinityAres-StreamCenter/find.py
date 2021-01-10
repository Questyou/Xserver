from selenium import webdriver
import time
from selenium.webdriver import  ActionChains
from XserverTest import  Readxslx
import xlrd
import re

Driver = webdriver.Chrome(r'd:\chromedriver.exe')
url = 'http://172.17.13.98:10009/'

Driver.get(url)
time.sleep(2)
#获取菜单列表
menus = Driver.find_elements_by_class_name("menuItem")

menus[1].click()
time.sleep(1)

#读取SC待添加的流
def readdata( rownum):

    firstRow = Readxslx.table.row_values(rownum)
    # addwork( firstRow[0],  firstRow[1],  firstRow[2])
    print( firstRow[0],  firstRow[1],  firstRow[2])
    addwork(firstRow[0], firstRow[1], firstRow[2])
    # print('等待读取SC待添加的文件')

#添加SC任务
def addwork( progcode, progname, progurl):
    #点击添加按钮
    Driver.find_element_by_css_selector('[class="blue_button add"]').click()
    time.sleep(2)

    Driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/span[2]/input').send_keys(progcode)
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[2]/div[2]/span[2]/input').send_keys(progname)
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div[4]/span[2]/input').send_keys(progurl)
    #选择录像
    Driver.find_element_by_css_selector('[class="el-switch el-switch--wide"]').click()
    #点击确认添加
    Driver.find_element_by_css_selector('[class="blue_button sure"]').click()
    time.sleep(3)
# print()
for i in range(Readxslx.getnrow()):
    readdata(i+1)
