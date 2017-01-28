# 

def add(x, y):
	print "x is %s and y is %s" % (x, y)
	return x + y

print add(y=6, x=5)

def varargs(*args):
	return args
print varargs(1, 2, 3)

def keyword_args(**kwargs):
	return kwargs
	
print keyword_args(big="foot",loch="ness")


def all_the_args(*args, **kwargs):
	print args
	print kwargs

all_the_args(1, 2, c=2)
