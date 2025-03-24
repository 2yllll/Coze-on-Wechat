FROM python:3.12
LABEL authors="zengyilun"


WORKDIR /app
COPY . /app


# 安装基本依赖项
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 暴露服务端口
EXPOSE 9919
COPY ./config-template.json ./config.json
CMD ["python", "app.py"]