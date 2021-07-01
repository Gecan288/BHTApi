import requests
from configs.config import host, mscode


class MsCode():

    def mscode(self, inData):
        url = f"{host}{mscode}"
        resp = requests.post(url, json=inData)
        return resp.json()


if __name__ == '__main__':
    res = MsCode().mscode({"phone":"13439200065","scene":"APP_LOGIN"})
    print(res)