import requests
import http.cookiejar as cookielib
import urllib
import re
import time


import requests

# resp = requests.get('http://www.baidu.com/index.html')
# print(resp.status_code)
# print(resp.headers)
# print(resp.cookies)
# print(resp.content.decode('utf-8'))
#
# resp = requests.post('http://httpbin.org/post', data={'name': 'Hao', 'age': 40})
# print(resp.text)
# data = resp.json()
# print(type(data))

URL = "https://confluence.cec.lab.emc.com/display/ISILON/Filesystems+LP"
# URL = 'https://movie.douban.com/top250'

resp = requests.get(
    url=URL,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    },
    verify=False
)
print(resp.status_code)
[print(i) for i in resp.content.decode('utf-8').split('\n')]