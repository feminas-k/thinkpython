def find_new(word,letter,num):
	index=num
	while index<len(word):
		if word[index]==letter:
	    		return index
		index=index+1
	return -1

print find_new('helloooo','l',3)

