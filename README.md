# zrlog_interface_test
这是一款基于Pytest+Requests+PyMySQL的接口自动化框架，使用Docker容器进行部署，配合Jenkins持续集成，内含各个知识点的Demo案例
## 准备工作
服务端搭建依赖docker以及docker-compose，安装指南：

https://dockerdocs.cn/get-docker/

https://dockerdocs.cn/get-started/08_using_compose/
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