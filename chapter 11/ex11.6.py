print "1st method"
known={0:0,1:1,2:1,3:2,4:3,5:5}
import time
start_time1=time.time()
def fib(n):
    if n in known:
	return known[n]
    res=fib(n-1)+fib(n-2)
    known[n]=res
    return res
print "fib of given number is ",fib(10)
print time.time()-start_time1, "seconds"

print "2nd method"
start_time2=time.time()
def fib2(n):
    if n==0:
	return 0
    elif n==1 or n==2:
	return 1
    else:
	return fib2(n-1)+fib2(n-2)
print "fib of given number is ",fib2(10)

print time.time()-start_time2,"seconds"
