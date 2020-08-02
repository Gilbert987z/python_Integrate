# coding=utf-8
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:40005",
#     "platformVersion": "6.0",
#     "appPackage": "com.fanwe.p2p",
#     "appActivity": "com.fanwe.p2p.InitActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True}  # 隐藏键盘
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# time.sleep(5)
# driver.find_elements_by_android_uiautomator("new UiSelector().text(\"登录/注册\")")[0].click()
# # driver.find_elements_by_android_uiautomator('new UiSelector().text("登录/注册")')[0].click()
# driver.find_element_by_id('act_login_et_username').send_keys('zhangz')
# driver.find_element_by_id('act_login_et_password').send_keys('123456')
# driver.find_element_by_class_name('android.widget.Button').click()

desired_caps = {
    "platformName": "Android",
    "deviceName": "f7c5caec",
    "platformVersion": "6.0",
    "appPackage": "com.idougong.jyj",
    "appActivity": "com.idougong.jyj.module.ui.FlickerScreenActivity",   #com.idougong.jyj.module.ui.FlickerScreenActivity
    "unicodeKeyboard": True,
    "resetKeyboard": True}  # 隐藏键盘
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#time.sleep(5)
driver.implicitly_wait(10)
print ("智能等待时间结束")
# driver.find_elements_by_android_uiautomator("new UiSelector().text(\"登录/注册\")")[0].click()
# # driver.find_elements_by_android_uiautomator('new UiSelector().text("登录/注册")')[0].click()
# driver.find_element_by_id('act_login_et_username').send_keys('zhangz')
# driver.find_element_by_id('act_login_et_password').send_keys('123456')
# driver.find_element_by_class_name('android.widget.Button').click()


#取消弹框
#driver.switch_to.alert.dismiss()
#driver.switch_to_alert().dismiss()
#TouchAction(driver).press(x=50,y=308).release().perform()
#TouchAction(driver).tap(385,1550).perform().release()
#el=driver.find_element_by_id('com.idougong.jyj:id/lin_banner2')
#print("定位成功")

#TouchAction(driver).tap()
#TouchAction(driver).press(el,540,0,1).release().perform()
#print("点击")
# butten = driver.find_elements_by_class_name('android.widget.Button')
# print (butten)
# butten[0].click()

#driver.find_element_by_id('com.idougong.jyj:id/lin_banner2').click()
#driver.switch_to_alert()
contexts = driver.contexts
print(contexts)

#切换到webview
driver.switch_to.context(contexts[1])
#获取当前得环境，看是否切换成功
now = driver.current_context
print(now)


