import urllib.robotparser
from lxml import  etree
import requests
from bs4 import  BeautifulSoup
import  jieba
import os
import re

http_headers = {
    'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0',
    'Accept':'text/html'
}
toppic_words = {'口号','学生','军训','队列','连队','训练','教官','军姿','嘹亮'}
website= 'https://news.fudan.edu.cn/'
get_url = 'https://news.fudan.edu.cn/zhxw/list114.html'

robot_parser = urllib.robotparser.RobotFileParser()
robot_parser.set_url(website+'/robots.txt')
robot_parser.read()


if robot_parser.can_fetch('*', get_url):
    response = requests.get(get_url, headers=http_headers)
    response.encoding = response.apparent_encoding
    content = response.text

    content = etree.HTML(content)
    href_xpath = content.xpath('//div[@id="list_pages"]/div/ul[@class="news_list clearfix"]/li')
    for i in href_xpath:
        href = i.xpath('./div[@class="news_box clearfix"]/div[2]/div[@class="news_con"]/div[@class="news_title"]/a/@href')[0]
        print(href)
        print('url相似度计算获取的结果: ', website + href)