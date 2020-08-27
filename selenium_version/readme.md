# 树莓派版本打卡程序介绍

## 介绍

这个程序使用python编写，使用selenium库实现对人点击的模拟，并且提交，进而代替打卡。
这个branch介绍了在树莓派上配置自动打卡

## 环境配置

### 系统安装与连接

在官网下载系统并烧录到SD卡中，SD卡在刚打开的目录下，新建一个文件ssh。（新系统默认ssh服务没有打开）

用网线连接笔记本和树莓派，在cmd中arp -a找到树莓派的地址，用ssh工具连接树莓派。默认用户名pi，密码raspberry

### 必要的软件和配置

#### 换源

sudo nano /etc/apt/sources.list
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
sudo apt-get update

#### 安装selenium、firefox、webdriver

![](https://img-blog.csdnimg.cn/20190423012831542.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpYW5fbGVsZQ==,size_16,color_FFFFFF,t_70)

pip install selenium==3.5

sudo apt-get install firefox-esr -y

firefox -version

可通过[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)下载相关版本的 geckodriver

我的是52版本，树莓派系统下载[geckodriver-v0.17.0-arm7hf.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-arm7hf.tar.gz)

将下载后的包通过解压缩命令解压：

tar -zxvf geckodriver-v0.17.0-arm7hf.tar.gz 

将解压后的文件 geckodriver 复制至 /usr/bin/ 目录下，并添加执行权限(+x)

chmod +x geckodriver
sudo cp ~/install_package/geckodriver /usr/bin

接下来还要安装一个图形界面，否则会报Error: GDK_BACKEND does not match available displays

sudo apt-get install xvfb

Xvfb -ac :7  -screen  0  1280x1024x8 -extension RANDR -nolisten inet6 &
export DISPLAY=:7

接下来就可以执行代码了

python autodaka.py

**别忘了修改userinfo里面的账号密码**

### 定时任务

nano crontab -e

添加

```
00 08 * * * python3 ~/code/BUAAdaka_assistant/selenium_version/autodaka.py
00 12 * * * python3 ~/code/BUAAdaka_assistant/selenium_version/autodaka.py
00 19 * * * python3 ~/code/BUAAdaka_assistant/selenium_version/autodaka.py
```

sudo /etc/init.d/cron restart
