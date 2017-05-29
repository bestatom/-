import os
import requests
from bs4 import BeautifulSoup

  
def get_html(url): 
    r = requests.get(url)
    r.text
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    img_urls=soup.findAll('img',bdwater='杉本有美吧,1280,860')
    root = "D://pics//"
    for img_url in img_urls:
        img_src=img_url['src']
        os.path.split(img_src)[1]
        with open(root+os.path.split(img_src)[1],'wb') as f:
            f.write(requests.get(img_src).content)
    
       
url = 'http://tieba.baidu.com/p/2166231880'  
get_html(url)
