## TradingView webhook
webhook 接口支持两种报警方式

### 报警方式：
- email：126邮箱
- wechat：企业微信

### 支持dockerfile
容器构建
```
docker build -t tvwebhook:v1.0 .
```
容器运行
```
docker run -it --name tv -p 5566:5566 tvwebhook:v.1.0
```
