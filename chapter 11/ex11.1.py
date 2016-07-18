def make_keys():
	d={}
	f=open('words.txt')
	t=[]
	for line in f:
		t=t+line.split()
	for element in t:
		d[element]=''
	return d
print make_keys()

		
