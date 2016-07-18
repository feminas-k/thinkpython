def count_new(word,letter,index):
	new_word=word[index:]
	count=0
	for char in new_word:
		if char == letter:
			count += 1
	return count

print count_new('helloooo','o',6) 
