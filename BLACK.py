# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 16:29
# @Author   : ScapeGoat
# @Blog      : http://cshblog.cn

import requests
import re


def get_num(s, url):
    r = s.get(url)
    # print(r.text)
    a = re.findall('数字是(\d+)\.', r.text)
    # print(a)
    return a[0]


def main():
    url = 'http://www.heibanke.com/lesson/crawler_ex00/36133'
    s = requests.Session()
    flag = True
    while flag:
        try:
            num = get_num(s, url)
            url = 'http://www.heibanke.com/lesson/crawler_ex00/' + str(num)
            print(url)
        except IndexError:
            print(num)
            flag = False


main()