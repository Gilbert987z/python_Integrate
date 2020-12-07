# coding = utf-8

from ..page.cheryJetourPage import CheryJetourPage as JETOUR
from ..page.logPage import LogPage as LOG


#todo
# 抓不到包

def downloadLog(cookies, VIN):
    JETOUR.remote_setting_search_vin(cookies, VIN)
    log_cookies = LOG.login_log('username', 'password')
    LOG.log_download(log_cookies, VIN)
