# -*- coding: utf-8 -*-
# @Time     : 2018/8/8 9:52
# @Author   : ScapeGoat
# @Blog      : http://cshblog.cn
import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex02/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
}


def get_csrf(s, u):
    response = s.get(u, headers=headers)
    response = str(response.headers)
    csrf = re.findall('csrftoken=(.*?);', response)
    return csrf[0]


def attack(csrf, password, s):
    data = {
        "csrfmiddlewaretoken": csrf,
        "username": "aaa",
        "password": password,
    }
    response = s.post(url, headers=headers, data=data).text
    # print(response)
    info = re.findall('<h3>(.*?)</h3>', response)
    print(info[0])


def main():
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
    s = requests.Session()
    csrf = get_csrf(s, login_url)
    data = {
        "csrfmiddlewaretoken": csrf,
        "username": "sgcsh",
        "password": 'csh525800',
    }
    s.post(login_url, headers=headers, data=data)
    # print(login.text)
    for password in range(31):
        csrf = get_csrf(s, url)
        print(password)
        attack(csrf, password, s)


main()