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
from Util import LogHandler

app = Flask(__name__)


@app.route('/api/v1.0/tradingview', methods=['POST'])
def tv_post_data():
    """
    request 获取参数参考：
    https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request/16664376#16664376?newreg=11b034b8c3ed488eb4fe0b6eba4097db

    1. 通过 application/json 提交数据
    >>> url = 'http://127.0.0.1:5566/api/v1.0/tradingview?token=XXXX'
    >>> data = {'text': 'xxx', 'subject': 'xxx', 'token': 'xxx'}
    >>> request.post(url, data=data)

    2. 通过 plain/text 方式提交数据
    >>> url = 'http://127.0.0.1:5566/api/v1.0/tradingview?token=XXX'
    >>> data = '12345'
    >>> headers = {'Content-Type': 'plain/text'}
    >>> request.post(url, headers=headers, data=data)
    http://127.0.0.1:5566/api/v1.0/tradingview

    返回结果:{'code': 0, 'msg': '成功'}, {'code': 1, 'msg': 'token err'}
    :return:
    """
    #
    log = LogHandler()
    token, text, subject = None, None, ''
    json_data = request.get_json()
    if json_data:
        token = json_data.get('token')
        text = json_data.get('text')
        subject = json_data.get('subject')
    token = request.values.get('token') if not token else token
    if not text or 'plain/text' in request.headers.keys().get('Content-Type'):
        text = request.data.decode('utf-8')
    if not subject:  # 没有输入主题
        subject = text[:10] + '...' if len(text) > 10 else text
    log.debug('token:{0}, text:{1}, subject:{2}'.format(token, text, subject))
    if token not in TOKEN:
        return {'code': 1, 'msg': 'token err'}, 200

    MessageManger(email=False).seng_msg(subject, text)
    return {'code': 0, 'msg': 'success'}, 200


@app.route('/')
def index():
    ip = request.remote_addr
    print(ip)
    return ip, 200


def runFlask():
    app.run(SERVER_API, SERVER_PORT, debug=False)


if __name__ == '__main__':
    runFlask()
