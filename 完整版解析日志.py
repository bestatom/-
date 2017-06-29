
import xlwt



list5 = []
list6 = []
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet',cell_overwrite_ok = True)
a = '======================================================'
with open('2.txt','r') as infp:
    #读取，按字符串特点切割
    str1 = infp.read()
    txt1 = '======================================================\n\n\n\n======================================================\n'
    list1 = str1.split(txt1)
    for i in list1:
        txt2 = '\n======================================================'
        str2 = ''.join(list(i))
        list2 = str2.split(txt2)
   
        str3 = ''.join(list2)
        list3 = str3.split('\n')
   #删除残留的a
        for index,item in enumerate(list3):
            if item == a:
                del list3[index]
   #判断post数据是否为空
        if (list3[-1] == '' and list3[-2] == '') or list3[-2] == ' ':
            pass
    
        else:
        #确定位置，开始将url和post写入列表中
            for index,item in enumerate(list3):
                try:
                    
                    if list3[index] == '' and list3[index+1] != '' and list3[-1] == '' :
                        str4 = ''.join(list3[1])
                        list4 = str4.split('T ')
                        list5.append(list4[1])
                        list6.append(list3[index:])
                        
                except:
                    pass
#将url和post分别写入xls中             
for i in range(len(list5)):
    sheet1.write(i,1,list5[i])
for i in range(len(list6)):
    sheet1.write(i,2,list6[i])

f.save('text6.xls')   
