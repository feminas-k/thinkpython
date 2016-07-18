# Two words 'interlock' if taking alternating letters from each 
# and forms a new word.

def inter_lock(word1,word2):
	res = []
	if len(word1)==len(word2):
		for i in range(len(word1)):
			res.append(word1[i])
			res.append(word2[i])
		return ''.join(res)
	else:
		return 
print inter_lock('sor','try')
print inter_lock('yes','no')
print inter_lock('shoe','cold')
