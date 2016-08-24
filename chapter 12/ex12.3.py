def most_frequent(word):
    t1=[]
    for i in word:
	t1.append((word.count(i),i))
	t1.sort(reverse=True)
    t2=[]
    for count,letter in t1:
	if letter not in t2:
	    t2.append(letter)
    return t2


print most_frequent('shesellsseashellsontheseashore')
