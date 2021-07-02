import requests
from configs.config import host, mscode


class MsCode():

    def mscode(self, inData, mode=False):
        url = f"{host}{mscode}"
        result = requests.post(url, json=inData)
        if mode:
            return result.json()["data"]
        else:
            return result.json()


if __name__ == '__main__':
    res = MsCode().mscode({"phone": "13439200065", "scene": "APP_LOGIN"}, True)
    print(res)
