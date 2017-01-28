some_var = 10
if some_var > 10:
	print "some_var is bigger than 10"
elif some_var < 10:
	print "some_var is smaller than 10"
else:
	print "some_var is indeed 10"


for animal in ["dog", "cat", "sheep"]:
	print "%s is a aniaml" % animal

for i in range(4):
	print i

x = 0
while x < 4:
	print x
	x += 1

try:
	raise IndexError("This is an index error")
except IndexError as e:
	print "NO error"
	pass
