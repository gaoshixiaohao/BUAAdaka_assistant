from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
options.add_argument('window-size=1600x900') # 指定浏览器分辨率
options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

brower = webdriver.Firefox(firefox_options=options)
brower.get("http://www.baidu.com")

brower.find_element_by_id('kw').send_keys('selenium')
brower.find_element_by_id('su').click()

time.sleep(3)
print(brower.current_url)

brower.quit()