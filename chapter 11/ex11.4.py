# a function reverse_lookup 
#so that it builds and returns a list of all keys that map to v, 
#or an empty list if there are none.
def reverse_lookup(d,v):
    t=[]
    for k in d:
	if d[k]==v:
	    t.append(k)
    return t
print reverse_lookup({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2},2)
print reverse_lookup({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2},3)


