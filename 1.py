import string,random

chars = string.ascii_letters + string.digits


def generate(count,length):
    for i in range(count):
        re = ""
        for i in range(length):
            re += random.choice(chars)
        print(re)
"""“Make a script both importable and executable”

意思就是说让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行。
这样既可以让“模块”文件运行，也可以被其他模块引入，而且不会执行函数2次。这才是关键。"""       
if __name__ == "__main__":
    generate(200,20)

