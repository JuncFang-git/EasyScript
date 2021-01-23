'''
Author: your name
Date: 2021-01-23 17:20:04
LastEditTime: 2021-01-23 20:16:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \EasyScript\script\ihdu_internet.py
'''

import urllib.parse
import urllib.request
import argparse

# get user name and password 
def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type=str, required=True, help='The username for login')
    parser.add_argument('--pwd', type=str, required=True, help='The password for the user')
    args = parser.parse_args()
    return args

# login in hdu network
def authenticate_ihdu(username, pwd):
    
    url = "http://2.2.2.2/ac_portal/login.php"
    
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

    data = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url, data, headers)

    with urllib.request.urlopen(req) as f:
        resp = f.read()
        print(resp)
        
if __name__ == "__main__":
    args = get_parser()
    authenticate_ihdu(args.user, args.pwd)