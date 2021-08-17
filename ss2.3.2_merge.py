#2.3.2合并（拼接）字符串

#可以使用+号来合并字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

#还可以通过拼接来创建一个完整的消息，再将其存储在一个变量中

message = "Hello, " + full_name.title() + "!"
print(message)
