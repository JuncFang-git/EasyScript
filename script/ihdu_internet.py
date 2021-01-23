'''
Author: your name
Date: 2021-01-23 17:20:04
LastEditTime: 2021-01-23 17:21:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \EasyScript\script\ihdu_internet.py
'''

import urllib.parse
import urllib.request

url = "http://2.2.2.2"

username = "191050020"  # add ihdu student id
pwd = "fcjt86fn70215yRM"  # add ihdu passwd

headers = {"Host": "2.2.2.2", "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",\
 "Accept-Language": "en-US,en;q=0.5",\
 "Accept-Encoding": "gzip, deflate",\
 "Content-type":"application/x-www-form-urlencoded; charset=UTF-8",\
 "Accept":"*/*",\
 "Referer":"http://2.2.2.2/ac_portal/default/pc.html?tabs=pwd",\
 "X-Requested-With":"XMLHttpRequest",\
 "connection":"keep-alive"}
data = {
    "opr": "pwdLogin",
    "userName": username,
    "pwd": pwd,
    "rememberPwd": "1"
}

url = "http://2.2.2.2/ac_portal/login.php"

data = urllib.parse.urlencode(data).encode("utf-8")

req = urllib.request.Request(url, data, headers)

with urllib.request.urlopen(req) as f:
    resp = f.read()
    print(resp)