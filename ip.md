# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:57:02 2017

@author: admin
"""
import os,time

def pingIp(IPbegin,IPend):
    start_Time=int(time.time())
    ip_RE = open(IPbegin+'.txt','w+')
    IP1 =  IPbegin.split('.')[0]
    IP2 =  IPbegin.split('.')[1]
    IP3 =  IPbegin.split('.')[2]
    IP4 = IPbegin.split('.')[-1]
    IPend_last = IPend.split('.')[-1]
    count_False = 0
    for i in range(int(IP4)-1,int(IPend_last)):
        ip = str(IP1+'.'+IP2+'.'+IP3+'.'+IP4)
        print(ip)
        int_IP4 = int(IP4)
        int_IP4 += 1
        IP4 = str(int_IP4)
        cmd = 'ping -n 2 %s'%ip
        #p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #(stdoutput,erroutput) = p.communicate()
        output = os.popen(cmd)
                 
        out = str(output.read())
        if u'请求超时。\n请求超时。' in out:
            count_False += 1
            print(count_False)
        ip_RE.write(out)
        
    ip_RE.close()
    end_Time = int(time.time())
    print(count_False)
    print("time(秒)：",end_Time - start_Time,"s")
    
if __name__ == '__main__':
    IPbegin = '211.138.52.0'
    IPend = '211.138.52.255'
    pingIp(IPbegin,IPend)
     
