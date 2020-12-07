

with open(r"C:\Users\天籁纸鸢\Desktop\test.txt", "r", encoding='UTF-8') as f:    #打开文件
    data = f.read()   #读取文件

list = data.split(',')
print(list)

for l in list:
    l=l.strip('\n')
    print(l)
# x = list[4].replace('\n','')
# print(list[4].replace('\n',''))
# print(x)