from driver.driver import *
from src.utils.getYamlData import *
from src.utils.readExcel import *

#启动页面
current_path =  os.path.abspath('../../../config')
yaml_path = os.path.join(current_path, 'url.yaml')
driver.get(get_yaml_data(yaml_path)['gyjurl'])


# current_path =  os.path.abspath('../../../data')
# yaml_path = os.path.join(current_path, 'loginData.yaml')
# print(get_yaml_data(yaml_path))
# name = get_yaml_data(yaml_path)['admin1']['name']
# password = get_yaml_data(yaml_path)['admin1']['passoword']
# code = get_yaml_data(yaml_path)['admin1']['code']

current_path =  os.path.abspath('../../../data')
yaml_path = os.path.join(current_path, 'data.xlsx')

print(readExcel(yaml_path,'login',1,1))


#获取界面元素
driver.find_element_by_css_selector("input[placeholder='请输入用户名']").send_keys(name)
driver.find_element_by_css_selector("input[placeholder='请输入密码']").send_keys(password)
driver.find_element_by_css_selector("input[placeholder='请输入验证码']").send_keys(code)


driver.find_element_by_xpath('//*[@id="app"]/div/section/form/div[4]/div/button/span').click()


