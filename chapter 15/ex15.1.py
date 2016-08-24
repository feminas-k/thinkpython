import math
def distance_between_points((x1,y1),(x2,y2)):
	dx=x2-x1
	dy=y2-y1
	return math.sqrt(dx**2+dy**2)

print distance_between_points((0,0),(3,4))

