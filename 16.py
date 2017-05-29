from collections import OrderedDict
import xlwt,json

with open('D://pics//student.txt','r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('student', cell_overwrite_ok=True)
    """enumerate的顺序嵌套性质"""
    for row, i in enumerate(data):
        for col, j in enumerate(i):
            sheet1.write(row, col, j)
    
    workbook.save('D://pics//student.xls')
