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
