# ----
菜菜菜
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:54:29 2017

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests
import re,json



cookie = 'PERSISTENT=XQo9um0F2M%2FyySaJr6YeGgyj9gMedZGanb0PTwjKYkw9epvY2wzcnBec2k731nACCw%3D%3D; SESS=0kF4WlB%2FG9tKM828k4pYXZcESmQmsKLVQm%2FM13h5kFMDWQbvUaBrwHaQ5zwoNwL%2FnvSMtjcNA6kY2Ls3bSAcVQ%3D%3D; Hm_lvt_407473d433e871de861cf818aa1405a1=1494663055,1494663138,1494903268,1494982984; Hm_lpvt_407473d433e871de861cf818aa1405a1=1494986173; Hm_lvt_39dcd5bd05965dcfa70b1d2457c6dcae=1494831107,1494903261,1494925456,1494982961; Hm_lpvt_39dcd5bd05965dcfa70b1d2457c6dcae=1494986206'  # get your cookie from Chrome or Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'cookie': cookie
}


def visit():
    url = 'https://apolo.zhenguanyu.com/questions?_=1495090049862'
    r = requests.post(url, headers = headers)
    r.enconding = r.apparent_encoding
    d_json = r.json()
    d = d_json['pageInfo']['list']
    v = []
    v.append(d['content'])
    print(v)
    
    #d_hot = p_json['pageInfo']['list']
    #print(d_hot)
    
    """ ID = []
    for x in range(1,29):
        ID.appen(x)
    for i in ID:
        data.append(p_json['list'][i])"""
        
    #r.text
    """ demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    soup = soup.decode('GBK')
    print(soup)
    m = re.findall(pattern,soup, re.S|re.M)
    print(m)"""
    

    
   

    
if __name__ == '__main__':
    #pattern = input('输入patten:')
    visit()
