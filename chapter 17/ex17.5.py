class Point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return '(%g,%g)'%(self.x,self.y)
	def __add__(self,other):
		if isinstance(other,Point):
			return self.add_point(other)
		if isinstance(other,tuple):
			return self.add_tup(other)
	def add_point(self,other):
		xsum=self.x+other.x
		ysum=self.y+other.y
		return xsum,ysum
	def add_tup(self,tup1):
		xtup=tup1[0]
		ytup=tup1[1]
		xsum=self.x+xtup
		ysum=self.y+ytup
		return xsum,ysum

point1=Point(1,2)
point2=Point(3,4)
print 'the result of addition of the given points:',
print point1+point2
print 'the result of addition of the first point with given tuple is:',
print point1+(5,6)
