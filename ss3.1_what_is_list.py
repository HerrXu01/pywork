#ss3.1 列表是什么

#列表由一系列按特定顺序排列的元素组成。
#可以创建包含字母表中所有字母、数字0-9或一些姓名的列表
#列表的元素之间也可以没有任何关系。
#通常会给列表指定一个表示复数的名称，如names, letters等
#用[]来表示列表，并用,来分隔其中的元素

#以下是一个所有元素为字符串的列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("\n")


#可以通过以下方法访问列表元素
#要注意是从0开始计数的
print(bicycles[0])
print(bicycles[1].title())

#在python中，可以用负数来访问倒数第几个元素
#比如用-1，就是访问倒数第一个元素，-2就是倒数第二个
#在不知道列表长度的情况下，可以这样方便地访问列表最后一个元素
print(bicycles[-2])
print("\n")

#可以像使用其他变量一样使用列表中的各个值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
