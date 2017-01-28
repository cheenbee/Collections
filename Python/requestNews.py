#import requests
#url = "http//news.163.com/rank/"
#response = requests.get(url)
#content = requests.get(url).content

#import urllib2
#url = "http://news.163.com/rank/"
#response = urllib2.urlopen(url)
#content = urllib2.urlopen(url).read() 
#print content.decode("gbk")
#response = response.read()
#print response

#import requests

#cs_url = 'http://www.so.com/s'
#param = {'ie':'utf-8', 'q':'query'}
#r = requests.get (cs_url, params = param)
#print r.url, r.status_code

#cs_url = "http://www.haosou.com/s"
#r = requests.get (cs_url, params = param)
#print r.url, r.status_code, r.history

import requests

url = 'http://www.zhihu.com'
response = requests.get(url)
if response.status_code == requests.codes.ok:
	print response.encoding
else:
	print 'Error'
