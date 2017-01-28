def power(x, n):
	while n > 0:
		x *= x
		n -= 1
	return x

print power(2,1)