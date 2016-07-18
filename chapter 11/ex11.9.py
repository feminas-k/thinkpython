#create function named has_duplicates
#that takes a list as a parameter and 
#returns True if there is any object that appears more than once in the list.

def has_duplicates(t):
	d = {}
	for x in t:
		if x in d:
            		return True
        	d[x] = True
	return False

print has_duplicates([1,2,3,2,4])

