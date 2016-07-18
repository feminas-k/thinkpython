def print_hist(h):
	k=h.keys()
	k.sort()
	for key in k:
		print key,h[key]

print_hist({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2})

