def sed(pattern,replace,source,destination):
	try:
		fin = open(source,'r')
		fout = open(destination,'w')
		for line in fin:
			line = line.replace(pattern,replace)
			fout.write(line)
		fin.close()
		fout.close()
	except:
		print 'Something went wrong.'

print sed('notice','look','poem1.txt','poem2.txt')
		
