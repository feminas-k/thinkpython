def is_power(a,b):
	c = a/b
	if ((a%b)==0) and ((c%b)==0):
		return True
	else:
		return False

print is_power(32,2)
print is_power(45,2)
 
