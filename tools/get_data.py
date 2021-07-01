import yaml, os


def read_yaml(filename):
    filepath = os.getcwd() + os.sep + "data" + os.sep + filename
    arrs = []
    with open(filepath, "r", encoding="utf-8")as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
    del res[0]
    for i in res:
        arrs.append((i["data"], i["result"]))
    return arrs


if __name__ == '__main__':
    print(read_yaml("login.yaml"))
