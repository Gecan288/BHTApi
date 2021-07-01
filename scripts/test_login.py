from tools.get_data import read_yaml
from libs.login import Login


res = read_yaml("loginPwd.yaml")[1]
print(res)
respdata = Login().login(res['data'])
print(respdata)

if res["result"]["msg"] in respdata["msg"]:
    print("----通过----")
