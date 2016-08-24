class Point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		print 'the point is:',
		return '(%g,%g)'%(self.x,self.y)

start=Point(4,5)
print start
