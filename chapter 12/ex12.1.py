#Write a function called sumall that takes any number of arguments 
#and returns their sum.
def sumall(*args):
	t=[]
	for i in args:
		t.append(i)
	return sum(t)

print sumall(1,2,3,4,5,6)



