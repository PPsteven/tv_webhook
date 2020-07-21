# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     Email
   Description :  
   Author :       ppsteven
   date：         2020/7/21 22:53
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""
from Config.setting import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import requests
import time
from Util import LogHandler


class BaseMail(object):
        def __init__(self, debug=False):
            self.name = EMAIL_CONFIG.get('ACCOUNT')
            self.pwd = EMAIL_CONFIG.get('PASSWORD')
            self.sender = EMAIL_CONFIG.get('SENDER')
            self.receivers = EMAIL_CONFIG.get('RECEIVERS')
            self.debug = debug
            self.smtpObj = smtplib.SMTP()
            # 打印出交互的所有内容
            if self.debug:
                self.smtpObj.set_debuglevel(1)
            self.log = LogHandler()

        def login(self):
            self.smtpObj.connect("smtp.126.com", 25)
            self.smtpObj.login(self.name, self.pwd)
            self.log.info('log in email account')

        def send_mail(self, subject, content):
            self.login()
            self.message = MIMEMultipart()
            self.message.attach(MIMEText(content, 'plain', 'utf-8')) # 内容，文本，编码
            self.message['From'] = self.sender
            self.message['To'] = ';'.join(self.receivers)
            self.message['Subject'] = Header(subject, 'utf-8')

            try:
                self.smtpObj.sendmail(
                    self.sender, self.receivers, self.message.as_string())
                self.log.info('sender: {0}, receivers, {1}, send email success'.format(self.sender, self.receivers))
            except Exception as e:
                self.log.error('send mail fail!, error msg:{0}'.format(e))

            # 发送完毕，关闭连接
            self.smtpObj.quit()
