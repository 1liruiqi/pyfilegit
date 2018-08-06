# -*- coding: utf-8 -*-
# @Time     : 2018/8/6 15:52
# @Author   : ScapeGoat
# @Blog      : http://cshblog.cn

import requests
import re
import base64

url = 'http://120.24.86.145:8002/web6/'
s = requests.Session()
r = s.get(url)
payload = str(r.headers)
p = re.findall("flag': '(.*?)',", payload)
post = base64.b64decode(p[0])
print(str(post))
post = re.findall(": (.*?)'", str(post))
post = base64.b64decode(post[0])
data = {'margin': post}
r = s.post(url, data=data)
print(r.text)