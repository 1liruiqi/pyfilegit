# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 20:54
# @Author   : ScapeGoat
# @Blog      : http://cshblog.cn
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
}


def get_csrf():
    url = 'http://www.heibanke.com/lesson/crawler_ex01/'
    response = requests.get(url, headers=headers)
    response = str(response.headers)
    csrf = re.findall('csrftoken=(.*?);', response)
    return csrf[0]


def attack(csrf, password):
    data = {
        "csrfmiddlewaretoken": csrf,
        "username": "aaa",
        "password": password,
    }
    url = 'http://www.heibanke.com/lesson/crawler_ex01/'
    response = requests.post(url, headers=headers, data=data).text
    info = re.findall('<h3>(.*?)</h3>', response)
    print(info[0])


def main():
    csrf = get_csrf()
    for password in range(31):
        print(password)
        attack(csrf,password)


main()