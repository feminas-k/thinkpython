#Two words are anagrams if you can rearrange
#the letters from one to spell the other.
#Write a function called is_anagram that takes two strings 
#and returns True if they are anagrams.

def is_anagram(x,y):
	return sorted(x)==sorted(y)
print is_anagram("no","on")
print is_anagram('yes','no')
print is_anagram('now','own')

