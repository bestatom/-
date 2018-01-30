import os,sys
from win32com import client as wc


def findname(filename):
	with open(filename,'r') as file_to_read:
	    lines = file_to_read.readlines()
	    file_to_read.close()
	    return lines[48:49][0]



doc = os.listdir('D:\\3')
for temp in doc:
	temp2 = temp 
	word = wc.Dispatch('Word.Application')
	temp = u'D:\\3\\'+temp
	doc = word.Documents.Open(temp)
	print(temp[5:-3])
	temp1 = temp[0:-3]+'txt'
	doc.SaveAs(temp1, 4)
	doc.Close()
	new = findname(temp1)
	os.remove(temp1)
	print(new)
	if len(new) > 1:
		new = new.replace('\n','')
		new_name = str(new)+'-'+temp2
		print(new_name)
		try:
			os.rename(temp,'D:\\3\\'+new_name)
		except:
			pass
