from selenium import webdriver
import time
import xlwt

OpenURL = 'http://172.17.13.76:11780/ums/login'
Driver = webdriver.Chrome(r'd:\chromedriver.exe')

usernameList  =  ['kuangjunyu','fuyunxia','yechujin','liuhui','matianxin','wangqiang','fanghuanliang',
                  'fengxuemei','tanboping']
realnameList  =  ['邝俊瑜','付云霞','叶楚津','刘辉','马天欣',
                  '王强','方焕良','冯雪梅','谭柏平']
# realnameList  =  []
# usernameList  =  []
print(len(usernameList))
print(len(realnameList))
#直接进入了UMS
Driver.get(OpenURL)
time.sleep(2)
def Login():
    Driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form[1]/div/p[1]/input').send_keys('admin')
    Driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form[1]/div/p[2]/input').send_keys('Bohui@123')
    Driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form[1]/div/div/input').click()
    time.sleep(3)
    Driver.find_element_by_xpath('/html/body/div/ul/li[1]/a').click()
    time.sleep(2)
    Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[1]/div/a').click()
    time.sleep(2)

def adduser():
    for i in range(300):
        Driver.find_element_by_class_name('add').click()
        time.sleep(1)
        # Driver.find_element_by_name('userNumber').send_keys('12')
        # username = str(usernameList[0]) + str(i)
        # realname = str(realnameList[0]) + str(i)
        username =  str(usernameList[i])
        realname = str(realnameList[i])
        Driver.find_element_by_name('username').send_keys(username)
        Driver.find_element_by_name('realname').send_keys(realname)
        Driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/form/div[2]/ul/li[1]/div/div').click()
        time.sleep(5)

Login()
adduser()






