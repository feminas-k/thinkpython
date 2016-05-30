def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res
print capitalize_all(['as','w','ath','i'])

def capitalize_nested(t):
	res = []
	for s in t:
		res.append(capitalize_all(s))
	return res

print capitalize_nested([['ab','c','def'],['g','hi','lmn'],['o']])



