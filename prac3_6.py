#practice 3-6
#找到了一个更大的餐桌，可容纳更多人，再邀请三个人
#以3-5为基础，末尾加一句print，说找到一个更大的餐桌
#使用insert将一个新嘉宾加到名单开头
#使用insert将另一个新嘉宾加到名单中间
#使用append将最后一位新嘉宾加到名单末尾
#打印邀请信息

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

