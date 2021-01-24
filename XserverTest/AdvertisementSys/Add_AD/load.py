import  requests  , os , time

from moviepy.editor import VideoFileClip

path = 'E:\\STE\\Xserver\\Xserver2.7\\ADSample\\jiangxi\\'
addsampleurl = 'http://172.17.13.173:12521/advertisementSample/saveOrUpdateAdvertisementSample'
token = '8a8af3a3-64cb-48b5-84f0-800370c05261'

filename123 = "E:\\STE\\Xserver\\Xserver2.7\\ADSample\\jiangxi\\奥利奥.mp4"

def get_file_times(filename):
    clip = VideoFileClip(filename)
    file_time = clip.duration
    file_time_ms = int(file_time * 1000 )
    return  file_time_ms

# def get_file_nameTest(path):
#     # names = os.fchdir(path)
#     # for name in names:
#         #获取到文件路径
#     filepath = path
#         # 打开文件
#     file = {'file': open(filepath, 'rb')}
#         #获取样本时长时间  毫秒
#     sample_time =  get_file_times(filepath)
#         #添加样本
#     add_samples(addsampleurl, "奥利奥" , file, sample_time)
#     print("完成样本" + "奥利奥" + "添加！" )

def get_file_name(fielpath):
    names = os.listdir(fielpath)
    for name in names:
        #获取到文件路径
        filepath = path + name
        #获取实际名称
        realname = name.split(".")
        # print(realname[0])
        # 打开文件
        file = {'file': open(filepath, 'rb')}
        #获取样本时长时间  毫秒
        sample_time =  get_file_times(filepath)
        #添加样本
        add_samples(addsampleurl, realname[0] , file, sample_time)
        print("完成样本" + realname[0] + "添加！" )

def add_samples(url , samplename ,files , duration_ms):

    headers = {
        'token' :  token
    }
    sample_data = {
        "id" : "" ,
        "name" : samplename ,
        "typeId" : 2004 ,
        "illegalIds" : "31" ,
        "advertisingRuleIds" : "2" ,
        "legal" : 0  ,
        "serviceIds" : "4921",
        "sourceServiceId" : 4921 ,
        "startTime" :  "2020-10-12" ,
        "endTime" : "2029-10-01" ,
        "duration": duration_ms,
        "sourceStartTime" : "2020-10-30 15:00:00" ,
        "sourceEndTime" : "2020-10-30 15:00:30" ,
        "remark"  : "样本添加",
        "onOff": 1,
        "back": 0
    }
    res = requests.post(url , data  = sample_data , files = files , headers = headers)
    time.sleep(3)
    print(res.text)

# get_file_nameTest(filename123)
get_file_name(path)



# get_file_nameT(filename123)
# import  requests , os
#
#
# namelist  = []
# path  = 'E:\\STE\\Xserver\\Xserver2.7\\ADSample\\'
#
# # def getfilenames(path):
# #     names = os.listdir(path)
# #     # for name in names:
# #     #     namelist.append(name)
# #     # print(namelist)
# #     return names
#
# def getfile(path):
# #     names = os.listdir(path)
# #     pth = path
# #     for name in names:
# #         filepath = pth + name
# #         # print(filepath)
# #     file = {'file': open(filepath, 'rb')}
#
#
#
# getfile(path)
#
# def addsample(url , file):
#     # url = 'http://172.17.13.172:12580/xserver/station/uploadStationPictures?stationId=1160'
#
#     headers = {
#         'token' : '8a8af3a3-64cb-48b5-84f0-800370c05261'
#     }
#
#     sample_data = {
#         "id" : "" ,
#         "name" : "真人秀2" ,
#         "typeId" : 2004 ,
#         "illegalIds" : "31" ,
#         "advertisingRuleIds" : "2" ,
#         "legal" : 0  ,
#         "serviceIds" : "4921",
#         "sourceServiceId" : 4921 ,
#         "startTime" :  "2020-10-12" ,
#         "endTime" : "2029-10-01" ,
#         "duration": 1196264,
#         "sourceStartTime" : "2020-10-30 15:00:00" ,
#         "sourceEndTime" : "2020-10-30 15:20:00" ,
#         "remark"  : "样本添加",
#         "onOff": 1,
#         "back": 0
#     }
#
#
#     # files = 1
#     # print(type(files))
#     res = requests.post(url , data  = sample_data , files = file , headers = headers)
#     print(res.text)
#
#
# # addsample('http://172.17.13.173:12521/advertisementSample/saveOrUpdateAdvertisementSample')
