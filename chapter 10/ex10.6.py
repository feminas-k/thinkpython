def is_sorted(l):
	for i in range(len(l)-1):
		if l[i+1] < l[i]:
			return False
	return True

print is_sorted([1,2,2])
print is_sorted(['b','a'])

	
