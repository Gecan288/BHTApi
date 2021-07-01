import pytest, sys, os, allure
sys.path.append(os.getcwd())
from tools.get_data import read_yaml
from libs.login import Login


class TestLogin():

    @pytest.mark.parametrize("body, result", read_yaml("login.yaml"))
    def test_login(self, body, result):
        res = Login().login(body)
        assert result in res["msg"]
