#2.3字符串
#字符串就是一系列字符，用引号括起来，可以是单引号也可以双引号

#2.3.1字符串的大小写
name = "ada lovelace"
print(name.title())
#name后面的title()是方法。
#方法是python可对数据执行的操作
#name后面的.让python对变量name执行方法title()指定的操作。
#title()是以首字母大写的方式显示每个单词

#还有其他几个大小写处理方法

name = name.title()
print(name)
print(name.upper())
print(name.lower())

#upper()将字符串改为全大写
#lower()将字符串改为全小写

