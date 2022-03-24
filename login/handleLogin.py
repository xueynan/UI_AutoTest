from login.loginpage import LoginPage


class HandleLogin(LoginPage):

    # 继承父类LoginPage
    def __init__(self):
        LoginPage.__init__(self)

    def user_send_kends(self, username):
        self.username_element().send_keys(username)

    def pwd_send_kends(self, password):
        self.password_element().send_keys(password)

    def login_btn_click(self):
        self.login_button_element().click()