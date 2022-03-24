import os
import yaml

# 获取当前目录的绝对路径
config_dir = os.path.dirname(os.path.abspath(__file__))
# 获取yaml文件路径
config_yaml = os.path.join(config_dir, "config.yaml")


class YamlReader:

    # 实例化，读取config.yaml，并加载出来
    def __init__(self):
        self.file = open(config_yaml, "r", encoding="utf-8")
        self.contents = yaml.safe_load(self.file)

    # 获取url地址
    def get_url(self, url=None):
        return self.contents['url'][url]

    # 读取谷歌浏览器驱动位置
    def chrome_driver(self, path=None):
        return self.contents['chromedriver'][path]

    # 获取元素
    def element(self, element=None):
        return self.contents['element'][element]

    # 获取元素值
    def value(self, value=None):
        return self.contents['value'][value]
