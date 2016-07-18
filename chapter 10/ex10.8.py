#Write a function called has_duplicates that takes a list and 
#returns True if there is any element that appears more than once.
#It should not modify the original list.

def has_duplicates(l):
	new_l= sorted(l)
	for i in range(len(l)-1):
		if new_l[i] == new_l[i+1]:
			return True
	return False

print has_duplicates(['m','k','c','d','c'])


