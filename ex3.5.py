def print_twice(f):
	f()
	f()
def print_four(f):
	print_twice(f)
	print_twice(f)
def beam():
	print '+----',
def post():
	print '|    ',
def get_beam():
	print_twice(beam)
	print '+'
def get_post():
	print_twice(post)
	print '|'
def one_row():
	get_beam()
	print_four(get_post)
def grid():
	print_twice(one_row)
	get_beam()
grid()

