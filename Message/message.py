# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     message
   Description :  
   Author :       ppsteven
   date：         2020/7/21 16:54
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""
from Message.QyWechet import weChatWork
from Message.Mail126 import mail126
from Message.SMSsender import sms_box

class MessageManger(object):
    def __init__(self,wechat=True, sms=True, email=True):
        self.wechat, self.sms, self.email = wechat, sms, email

    def seng_msg(self, subject, content):
        if self.wechat:
            weChatWork.send_msg(subject, content)
        if self.email:
            mail126.send_mail(subject, content)
        if self.sms:
            sms_box.send_msg(content)


if __name__ == '__main__':
     MessageManger().seng_msg('title', 'xxxxxxx')
     MessageManger().seng_msg('title2', 'xxxxxxx2')


