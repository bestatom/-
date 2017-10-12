from openpyxl import load_workbook
from openpyxl import Workbook
list1 = []
list2 = []
list3 = []
local = 0
local1 = 0 
def read():
    wb = load_workbook('text1.xlsx')
    ws3 = wb['Sheet1']
    with open('vul.txt','r') as infp:
        str1 = infp.read()
    list1 = str1.split('\n')
    for i in range(len(list1)):
        list2 = list1[i].split('\t')
        if len(list2)>2:
            local = 'A'+str(i+1)
            local1 = 'B'+str(i+1)
            list3 = list2[1:3]
            item = list3[0]
            print(list3[0])
            print(local)
            ws3[str(local)] = list3[0]
            ws3[str(local1)] = list3[1]
    wb.save('text1.xlsx')
        
read()

