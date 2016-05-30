def cumulative_sum(t):
	res = []
	for i in range(len(t)):
		res.append(sum(t[:i+1]))
	return res
print cumulative_sum([1,2,3,4,5,6,7,8,9])



