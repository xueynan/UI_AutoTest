from login.handleLogin import HandleLogin
import time


class Business(HandleLogin):

    def __init__(self):
        HandleLogin.__init__(self)

    # 登录用例
    def login(self, username, password):
        self.user_send_kends(username)
        self.pwd_send_kends(password)
        self.login_btn_click()
        time.sleep(3)
        self.driver.quit()
