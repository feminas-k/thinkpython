class Time(object):
	def time_to_int(self):
		minutes=self.hour*60+self.minute
		seconds=minutes*60+self.second
		print 'the total seconds is :',
		return seconds

start=Time()
start.hour=9
start.minute=30
start.second=40

print start.time_to_int()

