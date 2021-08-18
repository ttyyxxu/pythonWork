import re

# inputstr = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
#
# print(re.split(r'[\s\;]',inputstr))
# action_list = [re.match(r'^\s*([ASDW][0-9]+)\s*$',i) for i in inputstr.split(';')]
# valid_actions = [i.groups()[0] for i in action_list if i is not None]
# loc = (0,0)
# for action in valid_actions:
#     if action.startswith('A'):
#         loc = loc[0] - int(action[1:]), loc[1]
#     elif action.startswith('W'):
#         loc = loc[0], loc[1] + int(action[1:])
#     elif action.startswith('S'):
#         loc = loc[0], loc[1] - int(action[1:])
#     elif action.startswith('D'):
#         loc = loc[0] + int(action[1:]), loc[1]

def betterCompression(s):
    dict_char = {}
    #list_char = []

    char_list = re.findall(r'([a-z][0-9]+)',s)
    for chars in char_list:
        if chars[0] in dict_char:
            dict_char[chars[0]] += int(chars[1::])
        else:
            dict_char[chars[0]] = int(chars[1::])
            # list_char.append(chars[0])
    print(dict_char)
    #print(list_char)
    print(''.join([str(k)+str(dict_char[k]) for k in sorted(dict_char.keys())]))


# betterCompression('a3c9b2c1')


import requests
import re
import time
from urllib.request import urlopen
import json
"""
website = 'https://www.vmgirls.com/13344.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}

resp = requests.get(website,headers=headers)
html = resp.text

regex = re.compile('<a href="(.*?)" alt=".*?" title=".*?">')
urls = regex.findall(html)

print(urls)

for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    resp = requests.get('https:'+url,headers = headers)
    with open(file_name, 'wb') as f:
        f.write(resp.content)
"""

def topArticles(limit):
    website = 'https://jsonmock.hackerrank.com/api/articles?page=2'
    resp = urlopen(website)
    data_json = json.loads(resp.read())

    result = {}
    limited_result = []
    for article in data_json['data']:

        if article['title'] == '' and article['story_title'] is None:
            continue
        if article['title'] != '':
            name = article['title']
        else:
            name = article['story_title']
        if article['num_comments'] is None:
            result[name] = 0
        else:
            result[name] = article['num_comments']
    print(result)

    result_sorted = sorted(zip(result.values(), result.keys()),reverse=True)
    print(result_sorted)

topArticles(4)