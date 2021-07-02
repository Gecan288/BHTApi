import requests, hashlib
from configs.config import host, login


def get_md5(pwd):
    md5 = hashlib.md5()
    # 调用加密方法直接加密
    md5.update(pwd.encode("utf-8"))
    return md5.hexdigest()

class Login():

    def login(self, inData, mode=False):
        url = f"{host}{login}"
        result = requests.post(url, json=inData)
        if mode:
            return result.json()["data"]["accessToken"]
        else:
            return result.json()


if __name__ == '__main__':
    res = Login().login({"phone":"13439200065","password":"FCSTu9b2i9v5WuxnlGSfS6bivIEuaWc9FCPB3EKgmLBBmq1aURA9NCMsD5mfOVXDHwJxZxk9U7etGQBlm+KoK/tnylbzwfTmjGgbyx/5gPG4DqOQTlQDfHYhZVFOGg5GCYs4qBrKU+7ilPx//5nRWRFYuJcdGnqhCO8c89arYYU=","type":"0"})
    print(res)
