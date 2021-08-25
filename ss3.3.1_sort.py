#3.3.1使用方法sort对列表进行永久排序
#按字母顺序

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

#还可以按字母顺序反向排列
#向sort()方法传递参数reverse=True
cars.sort(reverse=True)
print(cars)
