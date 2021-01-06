# -*- coding:utf-8 -*-
# 使用python2运行这个文件

s = "中国"
s1 = u"你好,中国"
print(s1)
s_to_unicode = s.decode("utf-8")
print(s_to_unicode)
s_to_gbk = s_to_unicode.encode("gbk")
print(s_to_gbk)

s_to_unicode2 = s_to_gbk.decode("gbk")
print(s_to_unicode2)
gbk_to_utf8 = s_to_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)

