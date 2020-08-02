from appium import webdriver


desired_caps = {
    "platformName": "Android",
    "deviceName": "f7c5caec",
    "platformVersion": "6.0",
    "appPackage": "com.idougong.caipifa",
    "appActivity": "com.idougong.caipifa.module.ui.FlickerScreenActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True}  # 隐藏键盘
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)