import  requests
from bs4 import BeautifulSoup
url = 'https://search.dangdang.com/advsearch '
h = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
}
resp = requests.get(url=url ,headers=h)
print(resp.status_code)
resp.encoding = resp.apparent_encoding
get_html=resp.text
soup = BeautifulSoup(resp.text, 'lxml')
input_tag_name= ''
conditons=soup.select('#form1 > .box.box2.clearfix > .detail_conditon > label')
print(conditons, len(conditons))
for item in conditons:
    text =item.select('span')[0].string
    if text == '出版社':
        input_tag_name = item.select('span')[0].get('name')
print('已经找到input标签，name:', input_tag_name)

url2 = ''
h2 = {
    'user-agent': ''
}
keyword = {
    'medium':'01'
}
resp2 =requests.get(url=url2,headers=h2,params=keyword)
resp2.encoding = 'gb2312'
soup2 =BeautifulSoup(resp2.text, 'lxml')