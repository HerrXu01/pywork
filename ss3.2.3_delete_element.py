#3.2.3 从列表中删除元素

#(1) 根据位置删除元素，使用del语句
print('(1) 根据位置删除元素，使用del语句')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
print('\n')

#使用del语句删除元素后，就无法再访问它了

#(2) 使用方法pop删除元素，删除列表末尾的元素，但还能继续使用它的值
print('(2) 使用方法pop删除元素，删除列表末尾的元素，但还能继续使用它的值')
motorcycles_1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_1)

popped_motorcycle = motorcycles_1.pop()
print(motorcycles_1)
print(popped_motorcycle)
print('\n')

#(3) 使用pop方法弹出列表中任意位置的元素
print('(3) 使用pop方法弹出列表中任意位置的元素')
motorcycles_2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_2)

first_owned = motorcycles_2.pop(0)
print(motorcycles_2)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print('\n')

#(4) 根据值删除元素
print('(4) 根据值删除元素')
motorcycles_3 = ['honda', 'yamaha', 'ducati', 'suzuki', 'ducati']
print(motorcycles_3)

motorcycles_3.remove('ducati')
print(motorcycles_3)
#方法remove只会删除第一个指定的值

