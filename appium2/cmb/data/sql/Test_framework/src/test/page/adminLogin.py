

from driver.driver import *



def getLoginPage(name,password,code):
    #获取界面元素
    print('获取元素')
    driver.find_element_by_css_selector("input[placeholder='请输入用户名']").send_keys(name)
    driver.find_element_by_css_selector("input[placeholder='请输入密码']").send_keys(password)
    driver.find_element_by_css_selector("input[placeholder='请输入验证码']").send_keys(code)

    driver.find_element_by_xpath('//*[@id="app"]/div/section/form/div[4]/div/button/span').click()


