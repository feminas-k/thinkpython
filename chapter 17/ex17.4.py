class Point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return'(%g,%g)'%(self.x,self.y)
	def __add__(self,other):
		xsum=self.x+other.x
		ysum=self.y+other.y
		print 'the new point after the summation is:',
		return xsum,ysum

point1=Point(1,2)
point2=Point(3,4)
print 'the first point is:',
print point1
print 'the second point is:',
print point2

print point1+point2
