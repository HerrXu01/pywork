#3.2.2 在列表中添加元素

#(1) 在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#这种方法很常用，比如新建一个空列表，再用方法append向其中不断添加元素

#(2) 在列表中插入元素
#方法insert可以在列表的任意位置添加新元素，需要指定新元素的索引和值
motorcycles_1 = ['honda', 'yamaha', 'suzuki']
motorcycles_1.insert(0,'ducati')
print(motorcycles_1)

