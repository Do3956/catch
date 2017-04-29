# coding:utf-8
import json
# from example.QSBK import spider
# spider.start()

# from example.baiduPostsBar import BaiduPostsBar
# with open('config.json', 'rb') as f:
#     config = json.load(f)
#     spider = BaiduPostsBar(config)
#     spider.start()

from bs4 import BeautifulSoup

from util.HttpRequst import catchHelper
def matchContent(self, html):
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.find_all("div", class_="d_badge_title"):
        for i in soup.find_all("div", class_="d_post_content j_d_post_content "):
            for child in i.children:
                if child and child.string and child.string.strip():
                    self.stories.append(child.string)


pageCode = catchHelper.getHtml('https://tieba.baidu.com/p/4935228097')