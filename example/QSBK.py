# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

from util.HttpRequst import catchHelper


# 糗事百科爬虫类
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        # self.loadPageIndex()

        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 笑話是按照最新的放最前面，所以沒有必要記住觀看位置
    # def loadPageIndex(self):
    #     try:
    #         with open('record.txt', 'rb') as f:
    #             record = json.load(f)
    #             self.pageIndex = record.get('pageIndex')
    #     except Exception as e:
    #         logging.error('loadPageIndex error:%s',e)
    #
    # def recordPageIndex(self):
    #     with open('record.txt', 'wb') as f:
    #         record = json.load(f)
    #         record['pageIndex'] = self.pageIndex
    #         json.dump(record)
    #         f.write(record)

    def matchContent(self, html):
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("div", class_="content"):
            for child in i.children:
                if child and child.string and child.string.strip():
                    self.stories.append(child.string)

    # 传入某一页代码，返回本页不带图片的段子列表
    def loadPage(self):
        url = 'http://www.qiushibaike.com/hot/page/%d' % self.pageIndex
        pageCode = catchHelper.getHtml(url)
        if not pageCode:
            print "页面加载失败...."
            return None
        self.pageIndex += 1
        self.matchContent(pageCode)

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self):
        # 遍历一页的段子

        for story in self.stories:
            # 等待用户输入
            input = raw_input()
            # 每当输入回车一次，判断一下是否要加载新页面
            print story

            # 将全局list中第一个元素删除，因为已经取出
            del self.stories[0]

            # 如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return

        self.loadPage()

    # 开始方法
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 输出该页的段子
                self.getOneStory()


spider = QSBK()
