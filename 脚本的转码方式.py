# -*- coding=UTF-8 -*-
import sys
#看系统本身的编码方式
print sys.getfilesystemencoding()
s = "你就要成功了." 
s_unicode = s.decode("utf8")
print repr(s_unicode)
