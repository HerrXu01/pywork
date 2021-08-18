#2.3.4 删除空白

#介绍几个删除字符串中空白的方法

#去除末尾空白  .rstrip()
#去除开头空白  .lstrip()
#同时去除字符串两端空白  .strip()

message = "   Hello, Python world! "
#在打印字符串的时候末尾加个1，更清楚看到空白的删除
print(message + "1")
print(message.rstrip() + "1")
print(message.lstrip() + "1")
print(message.strip() + "1")

print("\n")
#这些方法不会改变变量的值，如果要改变这些变量的值，可以用这些方法给变量重新赋值
print(message)
message = message.strip()
print(message + "1")
