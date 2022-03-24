from config.config import YamlReader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginPage:

    # 实例化，使用谷歌驱动浏览器输入地址，且窗口放大
    def __init__(self):
        self.path = Service(YamlReader().chrome_driver(path="path"))
        self.driver = webdriver.Chrome(service=self.path)

        self.driver.get(YamlReader().get_url(url='iums'))
        self.driver.maximize_window()

    # 浏览器定位用户名元素
    def username_element(self):
        username_element = self.driver.find_element(By.XPATH, YamlReader().element(element='username_element'))
        return username_element

    # 浏览器定位密码元素
    def password_element(self):
        password_element = self.driver.find_element(By.XPATH, YamlReader().element(element='password_element'))
        return password_element

    # 浏览器定位登录元素
    def login_button_element(self):
        login_button_element = self.driver.find_element(By.XPATH, YamlReader().element(element='login_button_element'))
        return login_button_element
