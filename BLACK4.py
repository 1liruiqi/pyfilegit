# -*- coding: utf-8 -*-
# @Time     : 2018/8/8 11:03
# @Author   : ScapeGoat
# @Blog      : http://cshblog.cn
import requests
import re


url = 'http://www.heibanke.com/lesson/crawler_ex02/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
}
password = [None]*100


def get_csrf(s, u):
    response = s.get(u, headers=headers, timeout=30)
    response = str(response.headers)
    csrf = re.findall('csrftoken=(.*?);', response)
    return csrf[0]


def attack(csrf, password1, s):
    data = {
        "csrfmiddlewaretoken": csrf,
        "username": "aaa",
        "password": password1,
    }
    response = s.post(url, headers=headers, data=data, timeout=30).text
    # print(response)
    info = re.findall('<h3>(.*?)</h3>', response)
    print(info[0])


def get_password(u, s):
    html = s.get(u, headers=headers, timeout=30).text
    password_pos = re.findall('title="password_pos">(\d+)</td>', html)
    print(password_pos)
    password_val = re.findall('title="password_val">(\d+)</td>', html)
    print(password_val)
    if len(password_pos)==8:
        for i in range(8):
            password[int(password_pos[i])-1] =password_val[i]
    else:
        for i in range(4):
            password[int(password_pos[i])-1] = password_val[i]


def main():
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
    s = requests.Session()
    csrf = get_csrf(s, login_url)
    data = {
        "csrfmiddlewaretoken": csrf,
        "username": "sgcsh",
        "password": 'csh525800',
    }
    s.post(login_url, headers=headers, data=data, timeout=30)
    flag = 1
    while flag:
        if None in password:
            for i in range(1, 14):
                print(i)
                pass_url = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page={}'.format(str(i))
                get_password(pass_url, s)
                print(password)
        else:
            print(password)
            flag = 0
    answer = ''
    for word in password:
        answer += word
    print(answer)


main()