import urllib, urllib2, json
import requests

url = "http://pipecenter.dingdingbao.com/cgi/user/api/userinfo/get?curDist=UNICOM_BJ&chnlId=appstore&uid=2102025803&vid=2.3.4&devId=65bbc18ff8b856a30889b0ba2841136df4f43ea2&devType=ios&token=ea948cdc3fe1ed858373d3e9984bcab5&sign=28885e5def351f6c631a5af58da46f4f&osver=10.1.1"

data  ={'hasLanInfo': '1', 'number': '2102025803', 'queryType': 'uid'}



method = 'POST'

headers = {'Content-Type': 'application/json'}

res = urllib2.Request(url,data=json.dumps(data),headers = headers) 
response = urllib2.urlopen(res)
print response.read()
