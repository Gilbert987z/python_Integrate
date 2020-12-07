import os
import yaml


def get_yaml_load(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data, Loader = yaml.FullLoader)

    return data

if __name__ == '__main__':
    # current_path = os.path.abspath(".")
    # yaml_path = os.path.join(current_path, "config.yml")
    data = get_yaml_load('config.yml')
    print(data)
