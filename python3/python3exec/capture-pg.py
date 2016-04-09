#encoding:UTF-8
import urllib.request

## 抓取www.baidu.com
##url = "http://www.baidu.com"
##data = urllib.request.urlopen(url).read()
##data = data.decode('UTF-8')
##print(data)



## 抓取百度上面搜索关键词为Jecvay Notes的网页
import urllib
import urllib.request
 
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)




