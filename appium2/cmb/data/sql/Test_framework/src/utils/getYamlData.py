import os
import yaml

#获取yaml文件里的database数据
def get_yaml_data(yaml_file):

    # 打开yaml文件
    print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    print(file_data)
    print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data, Loader = yaml.FullLoader)
    print(data)
    print("类型：", type(data))
    return data



# if __name__ == '__main__':
#     current_path = os.path.abspath('../../data')
#     yaml_path = os.path.join(current_path, 'loginData.yaml')
#     print(get_yaml_data(yaml_path))
















# #获取yaml文件里的database数据
# def get_yaml_data(yaml_file):
#
#     # 获取当前脚本所在目录（不包含当前文件名）
#     current_path =  os.path.split(os.path.abspath(__file__))[0]
#     # 获取当前脚本所在目录（包含当前文件名）
#     yaml_path = os.path.join(current_path, yaml_file)
#
#     # 打开yaml文件
#     print("***获取yaml文件数据***")
#     file = open(yaml_path, 'r', encoding="utf-8")
#     file_data = file.read()
#     file.close()
#
#     print(file_data)
#     print("类型：", type(file_data))
#
#     # 将字符串转化为字典或列表
#     print("***转化yaml数据为字典或列表***")
#     data = yaml.load(file_data, Loader = yaml.FullLoader)
#     print(data)
#     print("类型：", type(data))
#     return data