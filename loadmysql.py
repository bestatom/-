# -*- coding: utf-8 -*-
#import MySQLdb as mdb
import sys
import csv
import os  
import MySQLdb


'''def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.txt':  
                L.append(os.path.join(root, file))
    l = str(L[0])
    return l[-3:]'''

def readcsv(path):
    l = path[-3:]
    if l == 'csv':
        list1 = []
        reader = csv.reader(file(path,'rb'))
        #print(len(reader[0]))
        for line in reader:
           #print(len(line))
            #line[0] = line.decode('GB2312').encode('utf8')
            list1.append(line)
        #print list1
        return list1
    elif l == 'txt':
        list2 = []
        f = open(path,'r')
        lines = f.readlines()
        for line in lines:
            list2.append(line)
        #print list2
        return list2

def judge(list3):
    list4 =[]
    for i in list3:
        list4.append(str(i))

def insert(list1):
    import MySQLdb
    n = len(list1[0])
    conn = MySQLdb.connect(host='localhost',user='root',passwd='111111',charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("""create database python """)
    conn.select_db('python')
    tablename = ''
    for i in range(0,n):
        tablename =tablename + str(list1[0][i]) + ' char(20),'
    tablename = tablename[:-1]    
    print(tablename)
    #tablename = str(list1[0][0])+' char(20),'+ str(list1[0][1])+' char(20),'+ str(list1[0][2])+' char(20),'+ str(list1[0][3])+' char(20)'
    cursor.execute("create table hahaha1("+tablename+") character set utf8 collate utf8_unicode_ci")
    #cursor.execute('create table tea111111111111(name char(20),info char(20),age char(20),hah char(10)) character set utf8 collate utf8_unicode_ci')
    values=[]
    for i in range(20):
        values.append((i,'Hello Mysqldb'+str(i)))
    values.insert(5,'@')
    count1,count = 0,0
    print n
#   cursor.executemany("""insert into test2 values(%s,%s)""",values)
    for value in list1[1:]:
        try:
            list_x = []
            for i in value:
                x = i.decode('GB2312').encode('utf8')
                #print x
                list_x.append(x)
            insert = '%s,'*n
            insert1 = insert[:-1]            
            cursor.execute("insert into hahaha1 values("+insert1+")",list_x)
            count1 += 1
        except Exception,e:
        #except:
            print e
            #print list_x
            count += 1   
    cursor.close()
    print count1,count


if __name__ == '__main__':
    path = '/var/host1.csv'
    list1 = readcsv(path)
    insert(list1)
    
