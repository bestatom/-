a = '======================================================'

infp = open('1.txt', "r")
str1 = infp.read()
txt1 = '======================================================\n\n\n\n======================================================\n'
list1 = str1.split(txt1)
for i in list1:
    txt2 = '\n======================================================'
    str2 = ''.join(list(i))
    list2 = str2.split(txt2)
    
    str3 = ''.join(list2)
    list3 = str3.split('\n')
    for index,item in enumerate(list3):
        if item == a:
            del list3[index]
    
    if (list3[-1] == '' and list3[-2] == '' and list3[-3] == ''):
        pass
    else:
        for index,item in enumerate(list3):
            if item == '':
                print(list3[index:])
      
