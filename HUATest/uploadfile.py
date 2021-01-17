import  requests

def login(url):
    data = {
        "loginName": "admin",
        "password": "Qm9odWlAMTIz",
        "captcha_key": "" ,
        "rememberMe": "on"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",

    }





def upload(url):
    # url = 'http://172.17.13.172:12580/xserver/station/uploadStationPictures?stationId=1160'

    headers = {
        'Cookie' : 'xserver=E5FC9DE10586D9C76DD5F477B4154691',
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryBnDFcu8gSw6bWCOY"

    }
    files = {'file' : open('D:\\147.jpg' , 'rb')}
    # files = 1
    print(type(files))

    upload_data = {

    "Content-Disposition": "form-data; name='file' ; filename='147.jpg' ",
    "Content-Type": "image/jpeg"
    }
    res = requests.post(url , files = files , data= upload_data , headers  = headers)
    print(res.text)

def getstartionlist(url):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "xserver=E5FC9DE10586D9C76DD5F477B4154691"
    }
    data = {
        "stationIds": "",
        "needPower": "true",
        "stationType": ""
    }
    res1 = requests.request(method= "post" , url = url  , data =data , headers = headers)
    print(res1)




upload('http://172.17.13.172:12580/xserver/station/uploadStationPictures?stationId=1160')

getstartionlist('http://172.17.13.172:12580/xserver/station/getStationListByIds')