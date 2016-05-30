def f1():
	print 'I am f1'

def call_fun(f,n):
	if n <= 0:
		return
	f()
	call_fun(f,n-1)

call_fun(f1,4)

