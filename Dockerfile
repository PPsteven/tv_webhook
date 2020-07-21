FROM python:3.6-slim

LABEL author=ppsteven

LABEL email=ppsteven@outlook.com

ENV TZ Asia/Shanghai

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . .

EXPOSE 5566

WORKDIR /usr/src/app/cli

ENTRYPOINT [ "sh", "start.sh" ]