import urllib.request
import re
 
def open_url(url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
 
def get_img(url):
        html = open_url(url).decode('utf-8')
        p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
        imglist = re.findall(p, html)
        
        
       # for each in imglist:
        #        print(each)
        
        for each in imglist:
                filename = each.split('/')[-1]
                urllib.request.urlretrieve(each, filename, None)
 
if __name__ == '__main__':
        url = "http://tieba.baidu.com/p/6243853070?red_tag=c2244459606"
        get_img(url)
