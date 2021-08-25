#3.3.3 倒着打印列表

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#注意方法reverse()是按原列表反向排列，而不是按字母顺序反向
#reverse()永久改变顺序，但是再调用一次reverse()可以变回来
