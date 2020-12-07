from selenium import webdriver

def chromeDriver():

    chrome_path = "./driver/chromedriver"  # 修改默认的chrome位置
    # print(now(), '启动谷歌浏览器')

    # 无界面
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options) #启动谷歌

    driver = webdriver.Chrome(executable_path=chrome_path)

    return driver

