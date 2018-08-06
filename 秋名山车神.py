import requests
import re

url = 'http://120.24.86.145:8002/qiumingshan/'

s = requests.Session()
response = s.get(url)
response.encoding = response.apparent_encoding
# print(response.text)
a = re.findall('<div>(.*?)=\?;</div>', response.text)
print a
payload = eval(a[0])
data = {'value': payload}
print data
r = s.post(url, data=data)
r.encoding = r.apparent_encoding
print r.text


