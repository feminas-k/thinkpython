def gcd(a,b):
	if b ==0:
		return a
	else:
		return gcd(b,a%b)

print gcd(4,8)
print gcd(3,4)
print gcd(8,12)

 
