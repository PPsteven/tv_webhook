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
        'test123434',
         ]

WECHAT_CONFIG = {
    'CORPID': 'ww357e38c6111455ebe9',
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
    'ACCOUNT': 'your_mail@xx.com',
    'PASSWORD': 'xxx',
    'SENDER': 'your_mail@xx.com',
    'RECEIVERS': ['your_mail@xx.com', 'your_mail2@xx.com']
}

# 使用短信宝 http://www.smsbao.com/login
# PATTERN 模板需要自己申请
SMSBOX_CONFIG = {
    'ACCOUNT': 'xxxx',
    'PASSWORD': 'xxxx',
    'DEFAULT_RECEIVERS': [138111111111],
    'PATTERN': '【魔术师】当前时间: {time} ;{name} 提醒您: {message}'
}
