
def get_txt_list(txt_path):
    with open(txt_path, "r", encoding='UTF-8') as f:    #打开文件
        data = f.read()   #读取文件

    list = data.split('\n')

    return list