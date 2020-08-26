# selenium版本打卡程序介绍

## 介绍

这个程序使用python编写，使用selenium库实现对人点击的模拟，并且提交，进而代替打卡。

## 环境配置

首先要有python

安装selenium库

```
pip install selenium
```

安装浏览器对应版本的webdriver，比如使用chrome，就装一个chromedriver(对应版本在设置->关于chrome，查看，下载完成放在python\Scripts目录下)，在这个网页可以快速下载[http://npm.taobao.org/mirrors/chromedriver/85.0.4183.83/](http://npm.taobao.org/mirrors/chromedriver/85.0.4183.83/)

在userinfo.py中把用户名和密码改成你自己的

## 运行

命令行:python autodaka.py

