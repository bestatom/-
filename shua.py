# -*- coding: utf-8 -*-
import threading
from time import ctime
import requests

def loop():
	url ='http://count.2881.com/count/count.asp?id=32022&sx=1&ys=20'

	r = requests.get(url)
	print(r.text)
def main():
	threads = []
	nloops = range(1000)
	for i in nloops:
		t = threading.Thread(target = loop,args = ())
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print('all DONE at:', ctime())

if __name__ == '__main__':
	while True:
		main()
