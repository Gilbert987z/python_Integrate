import requests


r = requests.get('http://www.baidu.com')
print(r.elapsed.total_seconds())