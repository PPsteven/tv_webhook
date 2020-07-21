# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     qywechet
   Description :  
   Author :       ppsteven
   date：         2020/7/21 16:22
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""
from Config.setting import *
import requests
import time
from Util import LogHandler


class WeChatWork(object):
    def __init__(self):
        self.access_token_dict = {}
        self.log = LogHandler()
        self.post_data = WECHAT_CONFIG.get('WECHET_DEFAULT_TEXT_DATA').copy()

    @classmethod
    def access_token_api(cls):
        access_token_api = WECHAT_CONFIG.get('ACCESS_TOKEN_API')
        corpid = WECHAT_CONFIG.get('CORPID')
        secret = WECHAT_CONFIG.get('CORPSECRET')
        return access_token_api.format(ID=corpid, SECRET=secret)

    @property
    def message_send_api(self):
        return WECHAT_CONFIG.get('MESSAGE_SEND_API').format(ACCESS_TOKEN=self.access_token)

    @property
    def access_token(self):
        if self.access_token_dict and \
           self.access_token_dict.get('expire_time') - time.time() <= 7200:
            self.log.debug('get access token from cookies')
            return self.access_token_dict.get('access_token')

        ret = requests.get(WeChatWork.access_token_api()).json()
        if not ret.get('errcode'):
            access_token = ret.get('access_token')
            self.access_token_dict['access_token'] = access_token
            self.access_token_dict['expire_time'] = time.time()
            self.log.debug('get access token: {0}'.format(access_token))
        else:
            self.log.error('get access token fail !!')


    def send_msg(self, subject, content):
        """
        api 格式
        {
           "touser" : "UserID1|UserID2|UserID3",
           "toparty" : "PartyID1|PartyID2",
           "totag" : "TagID1 | TagID2",
           "msgtype" : "text",
           "agentid" : 1,
           "text" : {
               "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
           },
           "safe":0,
           "enable_id_trans": 0,
           "enable_duplicate_check": 0,
           "duplicate_check_interval": 1800
        }
        :param subject:
        :param content:
        :return:
        """
        self.post_data['text']['content'] = "subject: {0} \n content: {1}".format(subject, content)
        ret = requests.post(self.message_send_api, json=self.post_data)

weChatWork = WeChatWork()


if __name__ == '__main__':
    wechat = weChatWork.send_msg('标题', '123123131')

