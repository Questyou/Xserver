from selenium import webdriver
import time
import xlwt
from selenium.webdriver import  ActionChains
from XserverTest import  Readxslx
import xlrd
import re

firstRow = Readxslx.table.row_values(0)


print(firstRow[0])