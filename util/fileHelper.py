# coding:utf-8
import os

def autoBuildDir_by_file(file_path):
    '''檢測文件所在目錄是否存在，不存在則創建'''
    file_path = os.path.abspath(file_path)
    dir = os.path.split(file_path)[0]
    autoBuildDir_by_dir(dir)

def autoBuildDir_by_dir(dir):
    '''檢測文件所在目錄是否存在，不存在則創建'''
    if not os.path.exists(dir):
        os.makedirs(dir)