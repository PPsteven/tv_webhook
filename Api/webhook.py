# -*- encoding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     webhook
   Description :  
   Author :       ppsteven
   date：         2020/7/21 15:31
-------------------------------------------------
   Change Activity:
                   2020/7/21: 
-------------------------------------------------
"""
import sys
from flask import Flask
from flask import request

sys.path.append('../')

from Config.setting import *
from Message import MessageManger
app = Flask(__name__)


@app.route('/api/v1.0/tradingview', methods=['POST'])
def tv_post_data():
    token = request.values.get('token', None)
    text = request.values.get('text')
    subject = request.values.get('subject')
    if token != TOKEN:
        return "wrong token!"
    MessageManger().seng_msg(subject, text)
    return text, 200


def runFlask():
    app.run(SERVER_API, SERVER_PORT, debug=False)


if __name__ == '__main__':
    runFlask()
