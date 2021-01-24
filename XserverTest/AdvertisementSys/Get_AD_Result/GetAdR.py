from  XserverTest.AdvertisementSys.Get_AD_Result.mysql_db import MysqlDB
import _json
import os
idlist = []
db =  MysqlDB()

def sample_result_count(sql):
    data = db.select_data(sql)
    i = 0
    for i in range(len(data)):
        data1 = data[i]
        sample_id = data1[0]
        count = db.select_count(
            "SELECT COUNT(*) FROM `t_advertisement_search_result` WHERE sample_id =  %s" % sample_id)
        i += 1
        if count != 0:
            print(data1[0], data1[1], data1[11], data1[12])
            print(str(sample_id) +"广告出现的次数" + count)

sample_result_count("SELECT * FROM `t_advertisement_sample`")