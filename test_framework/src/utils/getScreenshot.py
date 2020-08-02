# coding=utf-8
from selenium import webdriver
import time
import os

def getScreenshot(casePicDir):
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    time.sleep(2)
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(picture_time)


    current_path =  os.path.abspath('../../report')
    print(current_path)
    pic_path = os.path.join(current_path, 'screenshot\\')
    print(pic_path)


    # 创建的目录--‘分类图片可用’
    picDetail_path = os.path.join(pic_path, casePicDir+'\\')
    if not os.path.exists(picDetail_path):
        os.mkdir(picDetail_path)


    try:
        picture_url=driver.get_screenshot_as_file(picDetail_path + picture_time +'.png')
        print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
    driver.quit()



if __name__ == '__main__':
    getScreenshot('zTest')