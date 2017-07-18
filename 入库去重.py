#coding:utf8
import pymongo
import csv

def readcsv():
    list2 = []
    reader = csv.reader(file('lol.csv','rb'))
    for line in reader:
        list2.append(line)
    return list2

def remongo(list2):
    list1 = []
    client = pymongo.MongoClient('localhost',27017)
    db = client.db_lingyun
    collection = db.sys_det_rule
    for i in list2:
        dic = {}
        dic['desc'] = i[1]
        dic['rule'] = i[0]
        if collection.find(dic).count() == 0:
            collection.insert(dic)

if __name__ == '__main__':
	readcsv()
	remongo(readcsv())
