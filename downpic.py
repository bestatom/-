# -# -*- coding: utf-8 -*-
import sys
import re
import urllib
import requests
reload(sys)   
sys.setdefaultencoding('utf8') 

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html




def getImg(html):
      #r = requests.get("http://tieba.baidu.com/p/1253655105")
      reg = r'src="(.+?\.png)"'
      imgre = re.compile(reg)
      imglist = re.findall(reg,html)
      x = 0
      for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.png' % x)
        x += 1


if __name__ == '__main__':
  html = getHtml("http://tieba.baidu.com/p/1253655105")
  print getImg(html)

