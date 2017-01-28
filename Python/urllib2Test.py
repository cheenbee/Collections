import urllib,  urllib2
url = 'https://s.taobao.com/search'
data = {
	'q':'bubao'
	}
params = urllib.urlencode(data)
full_url = url + '?' + params
print full_url
response = urllib2.urlopen(full_url)
print response.read()
