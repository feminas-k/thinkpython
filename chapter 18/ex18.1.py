class Time(object):
	def __init__(self,hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	def time_to_int(self):
		minute=self.hour*60+self.minute
		second=minute*60+self.second
		return second
	def __cmp__(self,other):
		t1=self.time_to_int()
		t2=other.time_to_int()
		return cmp(t1,t2)

t1=Time(9,30,59)
t2=Time(2,30,59)

print t1.__cmp__(t2)

t3=Time(4,0,1)
t4=Time(5,9,4)
print t3.__cmp__(t4)

