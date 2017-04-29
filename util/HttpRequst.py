# coding:utf-8
import logging
import urllib,urllib2
import cookielib
import json

from util import log
class CatchHelper():
    def __init__(self):
        with open('config.json', 'rb') as f:
            config = json.load(f)
            log_file = config.get('log').get('file')
            log.init_log(log_file)

    def openHttpLog(self):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)
        urllib2.install_opener(opener)

    def openProxy(self):
        enable_proxy = True
        proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
        null_proxy_handler = urllib2.ProxyHandler({})
        if enable_proxy:
            opener = urllib2.build_opener(proxy_handler)
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)

    def saveCookie(self, fileName, url):
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = fileName
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        handler = urllib2.HTTPCookieProcessor(cookie)
        # 通过handler来构建opener
        opener = urllib2.build_opener(handler)
        # 创建一个请求，原理同urllib2的urlopen
        response = opener.open(url)
        # 保存cookie到文件
        # ignore_discard:即使cookies将被丢弃也将它保存下来
        # ignore_expires:如果在该文件中cookies已经存在，则覆盖原文件写入
        cookie.save(ignore_discard=True, ignore_expires=True)

    def getCookie(self, fileName, url):
        # 创建MozillaCookieJar实例对象
        cookie = cookielib.MozillaCookieJar()
        # 从文件中读取cookie内容到变量
        cookie.load(fileName, ignore_discard=True, ignore_expires=True)
        # 创建请求的request
        req = urllib2.Request(url)
        # 利用urllib2的build_opener方法创建一个opener
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        response = opener.open(req)
        print response.read()

    def getHtml(self, url):
        # request = urllib2.Request(url, data, headers)
        # 用户浏览器信息
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        # 用于应付防盗链
        referer = 'http://www.zhihu.com/articles'
        headers = {'User-Agent': user_agent, 'Referer': referer}
        request = urllib2.Request(url, headers=headers)

        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            # BadStatusLine 应该是headers验证的问题
            logging.error(e.reason)

        html = response.read().decode('utf-8')
        return  html




catchHelper = CatchHelper()
values = {'username' : 'cqc',  'password' : 'XXXX' }
data = urllib.urlencode(values)




