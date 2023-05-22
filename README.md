# zrlog_interface_test
这是一款基于Pytest+Requests+PyMySQL的接口自动化框架，使用Docker容器进行部署，配合Jenkins持续集成，内含各个知识点的Demo案例
## 准备工作
服务端搭建依赖docker以及docker-compose，安装指南：

https://dockerdocs.cn/get-docker/

https://dockerdocs.cn/get-started/08_using_compose/
# 效果展示
![test_result.png](tutorial_screenshot%2Ftest_result.png)
## 服务端搭建
命令行运行
```
docker -v && docker-compose -v
```
如果能正常输出版本，如下，则表示docker环境正常，可以继续
```
Docker version 20.10.8, build 3967b7d
```
```
docker-compose version 1.29.2, build 5becea4c
```
拉取镜像并启动服务（包含MySQL、Jenkins、Tomcat）：
```angular2html
docker-compose up -d  
```
## 本地环境搭建
命令行执行
```angular2html
pip install -r requirements.txt
```
## 配合Git，接入Jenkins实现持续集成
进入Jenkins容器，输入以下命令，生成ssh密钥
```angular2html
ssh-keygen
```
查看生成ssh公钥，并添加到github
```angular2html
cat ~/.ssh/id_rsa.pub
```
查看并复制ssh私钥，登录Jenkins平台，通过Manage Jenkins选项找到"添加凭据"选项，并把刚刚复制的私钥内容粘贴到Enter directly输入框中保存，如下图所示。
![image_1.png](tutorial_screenshot%2Fimage_1.png)
安装HTML Publisher,用于查看报告
![image_2.png](tutorial_screenshot%2Fimage_2.png)
添加一个Freestyle project的item，并且做如下配置，保存后就可以执行自动化测试
![image_2.png](tutorial_screenshot%2Fimage_3.png)
![image_4.png](tutorial_screenshot%2Fimage_4.png)
![image_5.png](tutorial_screenshot%2Fimage_5.png)
![image_6.png](tutorial_screenshot%2Fimage_6.png)
