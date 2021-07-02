# -*- coding: utf-8 -*-
import yaml, os


def read_yaml(filename):
    filepath = os.getcwd() + os.sep + "data" + os.sep + filename
    array = list()
    with open(filepath, "r", encoding="utf-8")as f:
        for i in yaml.load(f, Loader=yaml.FullLoader)[1:]:
            array.append((i["data"], i["result"]))
    return array


# 该方法 个人调试使用
def yaml_test(filename):
    filepath = os.path.dirname(os.getcwd()) + os.sep + "data" + os.sep + filename
    print(filepath)
    array = list()
    with open(filepath, "r", encoding="utf-8")as f:
        for i in yaml.load(f, Loader=yaml.FullLoader)[1:]:
            array.append((i.get("data"), i.get("result")))
    return array


if __name__ == '__main__':
    print(yaml_test("login.yaml"))
