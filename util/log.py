# coding:utf-8

import logging
from logging.handlers import TimedRotatingFileHandler

def init_log(log_file):
    if not log_file:
        return
    log_level = logging.INFO
    logFormat = '%(asctime)s [%(levelname)s] %(message)s [%(filename)s line:%(lineno)d]'
    logging.basicConfig(level=log_level, format=logFormat, datefmt='%a, %d %b %Y %H:%M:%S')

    # 每天換一個文件
    fileTimeHandler = TimedRotatingFileHandler(log_file, "D", 1, 1)
    fileTimeHandler.suffix = "%Y%m%d.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码

    formatter = logging.Formatter(logFormat)
    fileTimeHandler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(fileTimeHandler)

# init_log('log.log')
# logging.info('fdsfds')