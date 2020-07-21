# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     Logger
   Description :  
   Author :       ppsteven
   date：         2020/7/21 20:39
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""
__author__ = 'ppsteven'

import logging
from logging.handlers import TimedRotatingFileHandler
import os

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(DIR_PATH, os.path.pardir)
LOG_PATH = os.path.join(ROOT_PATH, "Log")

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

class LogHandler(logging.Logger):
    def __init__(self, name="message", level=logging.DEBUG, stream=True, file=True):
        self.name = name
        self.level = level
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        logging.Logger.__init__(self, name, level)
        if stream:
            self.__setStreamHandler()
        if file:
            self.__setFileHandler()

    def __setStreamHandler(self, level=None):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def __setFileHandler(self, level=None):
        file_name = os.path.join(LOG_PATH, '{0}.log'.format(self.name))
        file_handler = TimedRotatingFileHandler(file_name, when='D', interval=1, backupCount=15)
        file_handler.setFormatter(self.formatter)
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def reSetHandler(self, name):
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler()

if __name__ == '__main__':
    log = LogHandler('abc')
    log.info('this is a test ')
    log.reSetHandler('abc2')
    log.info('this is test 2')


