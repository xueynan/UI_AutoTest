import unittest
from login.business import Business
from ddt import ddt, data, unpack
import data.login_data as dt


@ddt
class TestLoginCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @data(*dt.login_case())
    @unpack
    # 登录用例
    def test_login_case(self, u, p):
        self.login = Business()
        self.login.login(u, p)


if __name__ == '__main__':
    unittest.main()
    pass
