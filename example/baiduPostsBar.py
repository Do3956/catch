# -*- coding:utf-8 -*-
import logging
import time
import os
from bs4 import BeautifulSoup

from util.HttpRequst import catchHelper
from util.fileHelper import autoBuildDir_by_dir


# 糗事百科爬虫类
class BaiduPostsBar:
    # 初始化方法，定义一些变量
    def __init__(self, config):
        baidutieba_config =config.get('baidutieba')
        self.urlList = baidutieba_config.get('urlList')
        self.onlyAuthor = baidutieba_config.get('onlyAuthor')
        self.dataDir = config.get('dataDir')

        self.pageIndex = 1
        self.title = ''
        self.barName = ''


    def getUrl(self, url):
        url = '%s?pn=%s' % (url, self.pageIndex)
        if self.onlyAuthor:
            url = '%s&see_lz=1' % url
        return url

    def matchContent(self, html):
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("div", class_="d_badge_title"):
        for i in soup.find_all("div", class_="d_post_content j_d_post_content "):
            for child in i.children:
                if child and child.string and child.string.strip():
                    self.stories.append(child.string)

    def matchTitle(self, html):
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("title"):
            return i.string.split('_')[:2]

    # 传入某一页代码，返回本页不带图片的段子列表
    def loadPage(self):
        stime = time.time()
        for url in self.urlList:
            url = self.getUrl(url)
            logging.info('11111111111 %s', time.time() - stime)
            pageCode = catchHelper.getHtml(url)
            if not pageCode:
                print "页面加载失败...."
                continue
            logging.info('9999999 %s', time.time() - stime)
            if self.pageIndex == 1:
                self.title, self.barName = self.matchTitle(pageCode)
            logging.info('22222222222 %s', time.time() - stime)
            content = self.matchContent(pageCode)
            logging.info('3333333 %s', time.time() - stime)
            self.writeData(content)
            self.pageIndex += 1
        self.pageIndex = 0

        logging.info('-------------%s',time.time()-stime)

    def writeData(self, content):
        ''
        dir_path = '%s/百度贴吧/%s/%s' % (self.dataDir(), self.barName)
        file_path = '%s/%s' % (dir_path, self.title)

        if not os.path.exists(file_path):
            autoBuildDir_by_dir(dir_path)

            with open(file_path, 'wb') as f:
                f.write(self.title)
                f.write(content)
        else:
            with open(file_path, 'ab') as f:
                f.write(content)




    def writeData(self, barName, content):


    # 开始方法
    def start(self):
        print "開始記錄···"

        # 先加载一页内容
        self.loadPage()
        # # 局部变量，控制当前读到了第几页
        # nowPage = 0
        # while self.enable:
        #     if len(self.stories) > 0:
        #         # 输出该页的段子
        #         self.getOneStory()

