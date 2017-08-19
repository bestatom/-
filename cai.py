# coding: utf-8
import codecs
import MySQLdb

SQL_FILEDS = []      
def read_csv():
	line_num = 0
	L1 = []  
	with codecs.open('data.csv', 'rb', 'gb2312') as csvfile:
		sql = 'insert into tbl_asset (IP, asset_name, os,manufacturer, company, group_id, user_id) values '
		for line in csvfile:
			line = line.strip()
			if line_num == 0:
				line_num += 1
				continue
			lineArr = line.split(',')
			if len(lineArr) != 7:
				return 0
			parms = '%s,'*len(lineArr)
			parms = parms[:-1] 
			SQL_FILEDS.append(' ("'+lineArr[0]+'","'+lineArr[1]+'","'+lineArr[2]+'","'+lineArr[3]+'","'+lineArr[4]+'",0,0)')
			line_num += 1

		sql_val = ','.join(SQL_FILEDS)
		sql += sql_val
		connect_db(sql)

def connect_db(sql):
	conn = MySQLdb.connect(host='localhost',user='root',passwd='root',charset='utf8')
	cursor = conn.cursor()
	conn.select_db('db_ngscanner')
	cursor.execute(sql)
	cursor.close()
	conn.close()

read_csv()
