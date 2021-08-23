#practice 3-5
#有一个人无法赴约，另邀请一位
#以3-4为基础，末尾加一句print，指出哪一个人不能来
#修改嘉宾名单，将不能来的人替换为新邀请的人
#再次打印邀请消息

guest = ['Boliang', 'Mingzhe', 'Qianyue']
message = 'I want to invite ' + guest[0] + ', '\
			+ guest[1] + ', ' + guest[2] + ' for dinner.'
print(message)

print("Qianyue cannot come.")

guest[2] = 'Fengge'
message = 'I want to invite ' + guest[0] + ', '\
			+ guest[1] + ', ' + guest[2] + ' for dinner.'
print(message)
