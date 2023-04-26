Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@XingsYu 
XingsYu
/
52pojie_Sign
Public
forked from RoadIsLong/52pojie_Sign
Cannot fork because you own this repository and are not a member of any organizations.
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Beta Try the new code view
52pojie_Sign/main.py /
@RoadIsLong
RoadIsLong Update main.py
Latest commit e264230 on Aug 9, 2022
 History
 1 contributor
40 lines (35 sloc)  1.1 KB
 

# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

def sign(cookie):
    result = ""
    url1 = "https://www.52pojie.cn/CSPDREL2hvbWUucGhwP21vZD10YXNrJmRvPWRyYXcmaWQ9Mg==?wzwscspd=MC4wLjAuMA=="
    url2 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2F'
    url3 = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
    headers = {
        "Cookie": cookie,
        "ContentType": "text/html;charset=gbk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    r = requests.get(url1, headers=headers, allow_redirects=False)
    s_cookie = r.headers['Set-Cookie']
    cookie = cookie + s_cookie
    headers['Cookie'] = cookie
    r = requests.get(url2, headers=headers, allow_redirects=False)
    s_cookie = r.headers['Set-Cookie']
    cookie = cookie + s_cookie
    headers['Cookie'] = cookie
    r = requests.get(url3, headers=headers)
    r_data = BeautifulSoup(r.text, "html.parser")
    jx_data = r_data.find("div", id="messagetext").find("p").text
    if "您需要先登录才能继续本操作" in jx_data:
        result += "Cookie 失效"
    elif "恭喜" in jx_data:
        result += "签到成功"
    elif "不是进行中的任务" in jx_data:
        result += "今日已签到"
    else:
        result += "签到失败"
    return result 

def main():
    b = os.environ['POJIE']
    cookie = b
    sign_msg = sign(cookie=cookie)
    print(sign_msg)


if __name__ == "__main__":
    main()
52pojie_Sign/main.py at master · XingsYu/52pojie_Sign
