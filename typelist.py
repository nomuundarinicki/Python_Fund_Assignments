our_list = ['magical unicorns', 19, 'hello', 98.98, 'world']
our_sum = 0
our_string = ""

for idx in range(0,len(our_list)):
	print idx, our_list[idx], type(our_list[idx])
	type_of_element = type(our_list[idx])

	if type_of_element is int:
		our_sum += our_list[idx]


	elif type_of_element is float:

		our_sum += our_list[idx]
		print our_sum, 'our sum'

	elif type_of_element is str:
		our_string += our_list[idx]
