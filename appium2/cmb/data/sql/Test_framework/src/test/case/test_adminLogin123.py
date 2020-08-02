#coding=utf-8
from src.utils.getYamlData import *
from driver.driver import *
from src.utils.readExcel import readExcel
from src.test.page.adminLogin import getLoginPage
import pytest

current_path = os.path.abspath('./config')
yaml_path = os.path.join(current_path, 'url.yaml')
print(yaml_path)
driver.get(get_yaml_data(yaml_path)['gyjurl'])

class TestCase():

    def setup_module(self):
        print("setup_module：所有用例执行之前")
        # 启动页面


    def setup_class(self):
        print("setup_class：所有用例执行之前")
        self.n = 1

    def teardown_class(self):
        print("teardown方法执行")


    def setup(self):
        print("setup: 每个用例开始前执行")
        getLoginPage(readExcel('login', self.n, 0), readExcel('login', self.n, 1),readExcel('login', self.n, 1))
        self.n = self.n + 1

    def teardown(self):
        print("teardown方法执行")

    def test_two(self):
        print("test_two方法执行")
        assert "o" in "love"

if __name__ == "__main__":
    pytest.main(['-s', 'test_adminLogin123.py'])

    # current_path =  os.path.abspath('../../../config')
    # yaml_path = os.path.join(current_path, 'url.yaml')
    # #启动页面
    # driver.get(get_yaml_data(yaml_path)['gyjurl'])
    #
    #
    # current_path =  os.path.abspath('../../../data')
    # yaml_path = os.path.join(current_path, 'loginData.yaml')
    # print(get_yaml_data(yaml_path))
    #
    #
    #
    # name = get_yaml_data(yaml_path)['admin1']['name']
    # password = get_yaml_data(yaml_path)['admin1']['passoword']
    # code = get_yaml_data(yaml_path)['admin1']['code']
    #
    #
    # #获取界面元素
    # driver.find_element_by_css_selector("input[placeholder='请输入用户名']").send_keys(name)
    # driver.find_element_by_css_selector("input[placeholder='请输入密码']").send_keys(password)
    # driver.find_element_by_css_selector("input[placeholder='请输入验证码']").send_keys(code)
    #
    #
    # driver.find_element_by_xpath('//*[@id="app"]/div/section/form/div[4]/div/button/span').click()


