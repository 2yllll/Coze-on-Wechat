FROM python:3.12
LABEL authors="zengyilun"
# 设置环境变量，确保激活虚拟环境时可以直接访问
ENV PATH=/app/env/bin:$PATH
ENV TZ=Asia/Shanghai

# 对时
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime


WORKDIR /app
COPY . /app


# 安装基本依赖项，包括 Git
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 暴露服务端口
EXPOSE 9919
COPY ./config-template.json ./config.json
CMD ["python", "app.py"]