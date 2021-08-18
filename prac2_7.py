#剔除人名中的空白
#存储一个人名，并在其开头和末尾都包含一些空白字符，
#务必至少使用字符组合\t和\n一次
#打印这个人名，以显示空白，然后分别用剔除函数处理并打印

name = "\tSheldon Cooper  \n"
print(name)

print(name.rstrip())
print(name.lstrip())
print(name.strip())
