def zero_sum(num):
	count = 0
	for i in str(num):
		if i == '0':
			count += 1
		else:
			count = 0

	return count

print(zero_sum(100))