class Time(object):
	'''Represents the time of day'''
t1=Time()
t1.hour=12
t1.minute=59
t1.second=30
t2=Time()
t2.hour=11
t2.minute=59
t2.second=30

def calculate(time):
	return time.hour+(time.minute/60.0)+(time.second/3600.0)

def is_after(t1,t2):
	h1,m1,s1 = t1.hour,t1.minute,t1.second
	h2,m2,s2 = t2.hour,t2.minute,t2.second
	print 'the chronological order says that,it is:',
	return calculate(t1)>calculate(t2)

print is_after(t1,t2)
