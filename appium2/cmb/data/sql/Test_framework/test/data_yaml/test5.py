import os
import yaml

# yaml文件中含有多个文档时，分别获取文档中数据
def get_yaml_load_all(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    all_data = yaml.load_all(file_data, Loader = yaml.FullLoader)
    for data in all_data:
        print(data)
current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "config5.yaml")
get_yaml_load_all(yaml_path)
"""结果
{'animal1': 'dog', 'age': 2}
{'animal2': 'cat', 'age': 3}
"""