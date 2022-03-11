"""
    访问谷歌浏览器，实现登录
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import YamlReader
import time


class LoginPage:

    def __init__(self):
        self.s = Service(YamlReader().chrome_driver(chromedriver="chromedriver", path="path"))
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get(YamlReader().get_url(url='url', url_path='iums'))
        self.driver.maximize_window()
        time.sleep(10)


"""
下一步：
1、iums登录封装，在当前文件
2、selenium方法二次封装，另起文件
"""


if __name__ == '__main__':

    LoginPage()

