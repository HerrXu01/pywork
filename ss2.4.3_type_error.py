#2.4.3 使用函数str()避免类型错误

'''
age = 23
message = "Happy " + age + "rd Birthday"
print(message)
'''
#以上错误在于age是一个整型变量，不能直接赋值给字符串message
#需要用函数str()进行类型装换

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
