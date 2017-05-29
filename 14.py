# ----
菜菜菜
from collections import OrderedDict
import xlwt,json

with open('D://pics//student.txt','r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    """如果对一个单元格重复操作，会引发returns error:
    Exception: Attempt to overwrite cell:
    sheetname=u'sheet 1' rowx=0 colx=0
    所以在打开时加cell_overwrite_ok=True解决"""
    sheet1 = workbook.add_sheet('student', cell_overwrite_ok=True)
    for index, (key, values) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        for i, value in enumerate(values):
            sheet1.write(index, i+1, value)
    workbook.save('D://pics//student.xls')
