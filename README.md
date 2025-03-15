<div align="center">
<img src="https://lf-coze-web-cdn.coze.cn/obj/coze-web-cn/obric/coze/favicon.1970.png" alt="Coze" width="100">
<h1>Coze on WeChat</h1>

本项目基于 chatgpt-on-wechat 和 dify-on-wechat 二次开发，主要是对接 Coze 平台

如果我的项目对您有帮助，请点一个 star 吧~
</div>

---

## 📋 功能概览

### 功能展示
![微信截图_20250213101950](https://github.com/user-attachments/assets/aadf95b7-0291-4ff3-9f3d-1905e02eb93d)

### 文本聊天功能
继承自 chatgpt-on-wechat 和 dify-on-wechat  
![image](https://github.com/user-attachments/assets/96551277-dde1-4ccd-8cc6-418643cd9f83)

### 语音功能
- 支持语音识别，但是只支持发送 20s 以内语音，接收没有限制  
![image](https://github.com/user-attachments/assets/e72329ed-dc35-47d4-bf18-8d4d672bec77)

- 语音回复  
![image](https://github.com/user-attachments/assets/93625656-e77f-43d4-9cfb-dcdc7bc4abc4)

https://github.com/user-attachments/assets/e221d35b-e6bb-479c-9850-3c5d404511e5

### 插件功能
支持 Coze 插件，支持插件卡片转微信链接

![image](https://github.com/user-attachments/assets/738fd3b9-6be4-407f-a60c-aa995268535b)

![image](https://github.com/user-attachments/assets/56934c06-64fd-43bf-8522-535edd5edfb0)

### Web 管理界面
![image](https://github.com/user-attachments/assets/71638577-4a26-4138-ae03-e21e4c5435eb)
![image](https://github.com/user-attachments/assets/225c699f-569b-40cf-865f-c98c5ab790c7)

---

## 🚀 快速使用

### 1. 准备工作
本项目主要对接 Coze 平台，所以需要在 [Coze 平台注册账号](https://www.coze.cn/)，并且创建机器人，创建完成后需要前往 [个人访问令牌页面](https://www.coze.cn/open/oauth/pats) 添加令牌

### 2. 运行环境
基于 [Gewechat](https://github.com/Devo919/Gewechat) 项目实现的微信个人号通道，使用 iPad 协议登录，相比 itchat 协议更稳定。

#### 部署 Gewechat 服务

```bash
# 从阿里云镜像仓库拉取(国内)
docker pull registry.cn-chengdu.aliyuncs.com/tu1h/wechotd:alpine
docker tag registry.cn-chengdu.aliyuncs.com/tu1h/wechotd:alpine gewe

# 创建数据目录并启动服务
mkdir -p gewechat/data  
docker run -itd -v ./gewechat/data:/root/temp -p 2531:2531 -p 2532:2532 --restart=always --name=gewe gewe
```

#### 安装项目
**(1) 克隆项目代码：**

```bash
git clone https://github.com/JC0v0/Coze-on-Wechat
cd Coze-on-Wechat/
```
**(2) 创建虚拟环境：**

使用 venv 创建虚拟环境
```bash
python3 -m venv Coze-on-Wechat
source Coze-on-Wechat/bin/activate
```
使用 conda 创建虚拟环境

```bash
conda create -n Coze-on-Wechat python=3.12
conda activate Coze-on-Wechat
```

**(3) 安装核心依赖 (必选)：**

```bash
pip3 install -r requirements.txt
```
**(4) 配置 config.json：**

```bash
cp config.json.example config.json          # 如果你使用web启动，则不需要配置
```

### 3. 运行项目

#### 本地运行
```bash
python3 app.py  # 需要先配置 config.json 中的参数
```

#### 服务器运行
```bash
nohup python3 app.py & tail -f nohup.out          # 需要先配置 config.json 中的参数
```

#### Web 界面
```bash
cd web/
streamlit run Home.py  # 可以在网页配置 config.json
```

---

## 📊 项目统计

[![Star History Chart](https://api.star-history.com/svg?repos=JC0v0/Coze-on-Wechat&type=Date)](https://star-history.com/#JC0v0/Coze-on-Wechat&Date)
## 📬 联系方式
![image](https://github.com/user-attachments/assets/d61764ec-c975-4b34-96c3-96bef668d67a)
