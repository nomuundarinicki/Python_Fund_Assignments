check = [1,2,3,4]
red = '* * * *'
black = '* * *'

for num1 in check:
	if num1 % 2 != 0:
		print red
	elif num1 % 2 ==0:
		print black

for num1 in check:
	if num1 % 2 != 0:
		print black
	elif num1 % 2 ==0:
		print red
