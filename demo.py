from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests

# url = 'https://loudi.newhouse.fang.com/house/s/'
# # 发送http请求
# response = requests.get(url)
# response.encoding = "gb2312"
# # html源码
# html = response.text
# # 分析找出信息
# content = re.findall(r'id="newhouse_loupai_list">(.*?)</ul></div>',html,re.S)[0]
# print(content)

# html = urlopen("https://morvanzhou.github.io/").read().decode('utf-8')
# #res = re.findall('<link href=(.*?)>',html,re.S)
# soup = BeautifulSoup(html, features='lxml')
# all_href = soup.find_all('a',{'href':re.compile('https://morvanzhou\.*?')})
# for l in all_href:
#     print(l['href'])

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')

    soup = BeautifulSoup(html,features='lxml')
    title = soup.find('h1').get_text()
    print(title,'   url:',his[-1])

    sub_urls = soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        his.pop()