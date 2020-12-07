
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.refresh_bro()
        self.timeout = 10
        self.t = 0.5


    #定义获取元素
    def find_element(self,*loc,index=0):
        wait = WebDriverWait(self.driver, self.timeout, self.t)
        if isinstance(index,int):
            return wait.until(EC.visibility_of_any_elements_located(*loc))[index]
        else:
            return wait.until(EC.visibility_of_any_elements_located(*loc))

    def find_element(self, *locator):
        try:
            print("定位元素:%s" % (locator,))
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except Exception as msg:
            print(u"%s 页面中未能找到 %s 元素" % (self, locator))
            print("错误信息%s" % msg)