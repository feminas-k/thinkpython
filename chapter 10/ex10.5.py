#to corect
def chop(t):
	while len(t)>0:
		t.pop(0)
		t.pop(-1)
		
	return t

print chop([1,2,3,4,5,6])

print chop([1,2,3])

print chop([1])


