def has_duplicates(l):
	new_l= sorted(l)
	for i in range(len(l)-1):
		if new_l[i] == new_l[i+1]:
			return True
	return False

print has_duplicates(['m','k','c','d','c'])


