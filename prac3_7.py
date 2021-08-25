#practice 3-7 缩减名单
#新购买的餐桌无法及时送达，只能邀请两个人
#以3-6为基础，末尾加一句只能邀请两个人
#使用pop()不断删除，直到还剩两人，每次删除一人时，都打印一条信息说抱歉
#剩下的两人指出他们仍在受邀人之列
#使用del将最后两人删除，让名单变成空的，打印该名单，证实是空的

guests = ['Boliang', 'Mingzhe', 'Qianyue']
message = 'I want to invite ' + guests[0] + ', '\
			+ guests[1] + ', ' + guests[2] + ' for dinner.'
print(message)

print("Qianyue cannot come.")

guests[2] = 'Fengge'
message = 'I want to invite ' + guests[0] + ', '\
			+ guests[1] + ', ' + guests[2] + ' for dinner.'
print(message)

print("I have found a bigger room for dinner.")

guests.insert(0, 'Tianshi')
guests.insert(2, 'Qianyue')
guests.append('Dake')

for guest in guests:
	print('I want to invite ' + guest + ' for dinner.')

print('The table I bought cannot be delivered in time, '\
			'so I have to only invite two of you.')

#print(len(guests))

while len(guests) > 2:
	guest_p = guests.pop()
	print('I cannot invite you for dinner, ' + guest_p + '. My apology.')

for guest in guests:
	print('You are still invited, ' + guest + '.')
	
del guests[0]
del guests[0]
print(guests)
print(len(guests))
