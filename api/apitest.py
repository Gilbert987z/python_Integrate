import requests

from api.test import HttpRequests

url1 = "http://gyj-dev-api.idougong.com/v2/groups/batch/insert/personnel"
url = "http://gyj-dev-api.idougong.com/biz/login"
params = {"mobile": "17376597890", "smsCode": "idougong"}
res = HttpRequests(url, params).http_requests("post").json()