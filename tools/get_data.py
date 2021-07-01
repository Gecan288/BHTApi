import yaml


def read_yaml(filename):
    filepath = "../data/"+filename
    with open(filepath, "r", encoding="utf-8")as f:
        return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':
    print(read_yaml("loginPwd.yaml"))