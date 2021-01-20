import  requests


def addsample(url):
    # url = 'http://172.17.13.172:12580/xserver/station/uploadStationPictures?stationId=1160'

    headers = {
        'token' : '8a8af3a3-64cb-48b5-84f0-800370c05261'
    }
    filename  = 'baohujiayuan.mp4'
    path = 'E:\\STE\\Xserver\\Xserver2.7\\ADSample\\' + filename
    file = {'file': open(path, 'rb')}

    sample_data = {
        "id" : "" ,
        "name" : "广告名称" ,
        "typeId" : 2004 ,
        "illegalIds" : "31" ,
        "advertisingRuleIds" : "2" ,
        "legal" : 0  ,
        "serviceIds" : "4921",
        "sourceServiceId" : 4921 ,
        "startTime" :  "2020-10-12" ,
        "endTime" : "2029-10-01" ,
        "duration": 30000,
        "sourceStartTime" : "2020-10-30 15:00:00" ,
        "sourceEndTime" : "2020-10-30 15:00:30" ,
        "remark"  : "样本添加",
        "onOff": 1,
        "back": 0
    }


    # files = 1
    # print(type(files))
    res = requests.post(url , data  = sample_data , files = file , headers = headers)
    print(res.text)


addsample('http://172.17.13.173:12521/advertisementSample/saveOrUpdateAdvertisementSample')
