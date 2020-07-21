# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     Mail126
   Description :  
   Author :       ppsteven
   date：         2020/7/21 23:16
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""
from Message.BaseEmail import BaseMail


class Mail126(BaseMail):
    def __init__(self, *args, **kwargs):
        BaseMail.__init__(self, *args, **kwargs)

    def login(self):
        self.smtpObj.connect("smtp.126.com", 25)
        self.smtpObj.login(self.name, self.pwd)


mail126 = Mail126()


if __name__ == "__main__":
    mail126.send_mail('标题', '内容')
    mail126.send_mail('标题', '内容')
