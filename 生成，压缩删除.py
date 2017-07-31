#coding:utf8
import os
import zipfile
import sys
from time import strftime
import shutil

def mkdir(path):
	path = path.strip()
	path = path.rstrip("\\")
	isExists = os.path.exists(path)
    
	if not isExists:
		os.makedirs(path)
		print path+'创建成功'
		return True
	else:
		print path + '目录已存在'
		return False

def zip_file():
	try:
		import zlib
		compression = zipfile.ZIP_DEFLATED
	except:
		compression = zipfile.ZIP_STORED
	now_time = strftime("%Y-%m-%d ")
	path = "///var/www/html/lingyun/mp/version/"+ now_time  #要进行压缩的文档目录
	start = path.rfind(os.sep) + 1
	filename = '///var/www/html/lingyun/mp/version/ '+ now_time  #压缩后的文件名
	z = zipfile.ZipFile(filename,mode = "w",compression = compression)
	try:
		for dirpath,dirs,files in os.walk(path):
			for file in files:
				if file == filename or file == "zip.py":
					continue
				print(file)
			z_path = os.path.join(dirpath,file)
			z.write(z_path,z_path[start:])
		z.close()
	except:
		if z:
			z.close()
	shutil.rmtree(path)


if __name__ == '__main__':
	
	zip_file()
