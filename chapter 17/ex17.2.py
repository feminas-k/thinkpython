class Point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def print_points(self):
		print 'the point is :',
		return '(%g,%g)'%(self.x,self.y)

start=Point()
print start.print_points()

end=Point(3.0,4.0)
print end.print_points()
