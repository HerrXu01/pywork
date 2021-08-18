#2-4调整名字的大小写
#将一个人名存储到一个变量中，再以小写、大写、首字母大写的方式显示这个人名
"""
user_name = input("Hello, what's your name?\n")
print("lower: " + user_name.lower() + "\n")
print("capital: " + user_name.upper() + "\n")
print("initial capital: " + user_name.title())
"""

user_name = input("Hello, what's your name?\n")
print("lower: " + user_name.lower() + "\n"
+ "capital: " + user_name.upper() + "\n"
+ "initial capital: " + user_name.title())
