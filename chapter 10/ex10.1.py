def nested_sum(t):
	for i in range(len(t)):
		t[i] = sum(t[i])
	return t

print nested_sum([[1,2],[3,4,5],[6,7],[8],[9,10]])


