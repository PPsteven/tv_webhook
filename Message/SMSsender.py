# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     SMSsender
   Description :  
   Author :       ppsteven
   date：         2020/8/1 17:22
-------------------------------------------------
   Change Activity:
                   2020/8/1: 
-------------------------------------------------
"""
import requests
import hashlib
import time
from Config import setting
from Util import LogHandler

def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf8"))
    return m.hexdigest()


class SMSbox:
    def __init__(self):
        self.user = setting.SMSBOX_CONFIG.get('ACCOUNT')  # 短信平台账号
        self.password = setting.SMSBOX_CONFIG.get('PASSWORD')  # 短信平台密码
        self.password = md5(self.password)
        self.smsapi = "http://api.smsbao.com/sms"
        self.statusStr = {
            '0': '短信发送成功',
            '-1': '参数不全',
            '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
            '30': '密码错误',
            '40': '账号不存在',
            '41': '余额不足',
            '42': '账户已过期',
            '43': 'IP地址限制',
            '50': '内容含有敏感词'
        }
        self.log = LogHandler()

    def send_msg(self, content, receivers=[]):
        """
        :param receivers: 收信人
        :param subject: 主题
        :param content: 内容
        :return:
        """
        content = setting.SMSBOX_CONFIG.get('PATTERN').format(time=time.strftime('%Y-%m-%d %H:%M:%S'), name='ppsteven', message=content)
        content += '(ppsteven.github.com)'
        receivers = setting.SMSBOX_CONFIG.get('DEFAULT_RECEIVERS') if not receivers else receivers
        for phone in receivers:
            params = {'u': self.user, 'p': self.password, 'm': phone, 'c': content}
            ret = requests.get(self.smsapi, params=params).text
            print(ret)
            if ret == '0':
                self.log.info('短信发送成功')
            else:
                self.log.error('短信发送失败， 原因:{0}'.format(self.statusStr.get(ret)))


sms_box = SMSbox()


if __name__ == '__main__':
    sms_box = SMSbox()
    sms_box.send_msg('收到消息(ppsteven.github.com)')


