def check(word):
    
    #words = ['北京', '程序员', '公务员', '领导', '牛比', '牛逼', '你娘', '你妈', 'love', 'sex', 'jiangge']
    #words = open('filtered_word.txt','r').readlines()
    words = []
    for line in open('filtered_word.txt','r').readlines():
        line=line.strip('\n')
        words.append(line)
    print(words)
    for i in words:
        if word == i:
            flag = True
            break
        else:
            flag = False
    if flag :
        print ('Freedom')
    else:
        print ('humanRight')


if __name__ == "__main__":
    word =input("输入：")
    check(word) 
