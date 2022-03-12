"""
    访问谷歌浏览器，实现登录
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import YamlReader
from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self):
        self.s = Service(YamlReader().chrome_driver(chromedriver="chromedriver", path="path"))
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get(YamlReader().get_url(url='url', url_path='iums'))
        self.driver.maximize_window()
        time.sleep(10)

    def user_name(self):
        xpath = self.driver.find_element(By.XPATH, YamlReader().username(username="username", username_xpath="username_xpath"))
        xpath.send_keys(YamlReader().username(username="username", username_values="username_values"))
        time.sleep(3)

    def password(self):
        xpath = self.driver.find_element(By.XPATH, YamlReader().password(password="password", password_xpath="password_xpath"))
        xpath.send_keys(YamlReader().password(password="password", password_values="password_values"))
        time.sleep(3)

    def login(self):
        xpath = self.driver.find_element(By.XPATH, YamlReader().login(login_button="login_button", login_button_xpath="login_button_xpath"))
        xpath.click()
        time.sleep(3)


"""
下一步：
1、iums登录封装，在当前文件
2、selenium方法二次封装，另起文件
"""


if __name__ == '__main__':

    LoginPage().user_name()
    LoginPage().password()
    LoginPage().login()
