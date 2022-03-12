import os
import yaml

# 获取当前目录的绝对路径
config_dir = os.path.dirname(os.path.abspath(__file__))
# 获取yaml文件路径
config_yaml = os.path.join(config_dir, "config.yaml")


class YamlReader:
    def __init__(self):
        self.file = open(config_yaml, "r", encoding="utf-8")
        self.contents = yaml.safe_load(self.file)

    def get_url(self, url, url_path):
        return self.contents[url][url_path]

    def chrome_driver(self, chromedriver, path):
        return self.contents[chromedriver][path]

    def username(self, username, username_xpath=None, username_values=None):
        return self.contents[username][username_xpath], self.contents[username][username_values]

    def password(self, password, password_xpath=None, password_values=None):
        return self.contents[password][password_xpath], self.contents[password][password_values]

    def login(self, login_button, login_button_xpath):
        return self.contents[login_button][login_button_xpath]