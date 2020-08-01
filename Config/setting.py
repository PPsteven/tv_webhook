# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting
   Description :  
   Author :       ppsteven
   date：         2020/7/21 15:35
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""

SERVER_API = '0.0.0.0'
SERVER_PORT = 5566

TOKEN = [
        'test123',
         ]

WECHAT_CONFIG = {
    'CORPID': 'ww357e38c68455ebd9',
    'CORPSECRET': 'oeVkBNFkeAJADZQEw0Pl2SWz8R8CZRmO8Hd3AXoCdB0',
    'ACCESS_TOKEN_API': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}',
    'MESSAGE_SEND_API': 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}',
    'WECHET_DEFAULT_TEXT_DATA': {
        "touser": "@all",
        "msgtype": "text",
        "agentid": 1000002,
        "text": {
            "content": ""
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
}

EMAIL_CONFIG = {
    'ACCOUNT': 'goldmarket123@126.com',
    'PASSWORD': 'goldmarket123',
    'SENDER': 'goldmarket123@126.com',
    'RECEIVERS': ['goldmarket123@126.com', '932163071@qq.com']
}

# 使用短信宝 http://www.smsbao.com/login
# PATTERN 模板需要自己申请
SMSBOX_CONFIG = {
    'ACCOUNT': 'ppsteven',
    'PASSWORD': '123123',
    'DEFAULT_RECEIVERS': [13816715280],
    'PATTERN': '【魔术师】当前时间: {time} ;{name} 提醒您: {message}'
}