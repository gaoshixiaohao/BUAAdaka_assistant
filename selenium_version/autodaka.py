from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from userinfo import UserInfo


if __name__ == '__main__':
    userinfo = UserInfo()
    #在userinfo.py中改成你的统一认证用户名和密码
    user_name = userinfo.username
    pwd = userinfo.password

    # 加上这两句话不打开浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('headless') # 设置option
    # 用浏览器打开打卡的网址
    driver = webdriver.Chrome(options=option)
    driver.get("https://app.buaa.edu.cn/site/ncov/xisudailyup")

    # 输用户名和密码
    locator = (By.CSS_SELECTOR, '#app > div.content > div:nth-child(1) > input[type=text]')
    user_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    user_name_input.send_keys(user_name)
    user_pwd_input = driver.find_element_by_css_selector('#app > div.content > div:nth-child(2) > input[type=password]')
    user_pwd_input.send_keys(pwd)

    # 然后点击登录按钮
    login_button = driver.find_element_by_css_selector('#app > div.btn')
    ActionChains(driver).move_to_element(login_button).click(login_button).perform()
    print('点击登陆')

    locator = (By.XPATH, '/html/body/div[1]/div[1]/div/section/div[5]/div/a')
    done_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    if 'you have been submitted' in done_check.text:
        print('今天已提交过')
        time.sleep(1)
        driver.quit()

    locator = (By.CSS_SELECTOR, 'body > div.item-buydate.form-detail2.ncov-page > div:nth-child(1) > div > section > div.form > ul > li:nth-child(4) > div > input[type=text]')
    location_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].click();",location_button)
    # ActionChains(driver).move_to_element(location_button).click(location_button).perform()
    print('获取位置')

    time.sleep(2)
    # 选择温度
    temperature_button = driver.find_element_by_css_selector('body > div.item-buydate.form-detail2.ncov-page > div:nth-child(1) > div > section > div.form > ul > li:nth-child(5) > div > div > div:nth-child(2) > span:nth-child(1) > i')
    # ActionChains(driver).move_to_element(temperature_button).click(temperature_button).perform()
    driver.execute_script("arguments[0].click();",temperature_button)

    time.sleep(2)
    # 点击提交
    submit_button = driver.find_element_by_css_selector('body > div.item-buydate.form-detail2 > div > div > section > div.list-box > div > a')
    driver.execute_script("arguments[0].click();",submit_button)
    # ActionChains(driver).move_to_element(submit_button).click(submit_button).perform()
    print('点击提交')
    

    time.sleep(1)
    # 确定
    
    try:
        locator = (By.CSS_SELECTOR,'#wapcf > div > div.wapcf-btn-box > div.wapcf-btn.wapcf-btn-ok')
        confirm_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        ActionChains(driver).move_to_element(confirm_button).click(confirm_button).perform()
        print('提交成功')
    except:
        print('提交失败')

    time.sleep(1)
    driver.quit()
