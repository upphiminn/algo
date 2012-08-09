#!usr/bin/env pythonb

import time
from math import sqrt
from pylab import *

######## Utils
def wrap_time(functions, labels ):
	for i in xrange(len(functions)):
		start = time.time()
		print labels[i]
		result = functions[i](30)
		now = time.time() 
		print  "Speed " + str(( now - start )) + "\nResult " + str(result)
		print "#" * 30


def fibo_plot(func, n):
	data = []		
	for i in xrange(1,n):
		start = time.time()
		func(i)
		now = time.time() 
		data.append(now-start)
		
	plot(xrange(1,n), data)
	draw()
	show()

####### Fibo Garden

def fibo2(n):
	#Iterative fibo N complexity, N extra space
	f = [None]*(n+1)
	f[0] = 0
	f[1] = 1
	for i in range(2,n+1):
		f[i] = f[i-1] + f[i-2]
	return f[n]

def fibo1(n):
	#Naive fibo with exponenetial complexity 2^N-1 * 3
	if n==0: return 0
	if n==1: return 1
	return fibo1(n-1) + fibo1(n-2)


thefibocache = {0:0, 1:1}
def fibo3(n):
	#Cached recursive fibo with N complexity, and N space complexity
	global thefibocache
	if n in thefibocache:
		return thefibocache[n]
		print "yes"
	else:
		thefibocache[n] = fibo3(n-1) + fibo3(n-2)
		return thefibocache[n]

def fibo4(n):
	#Constant N time fibo with 2 space complexity
	r = 0 
	prev1 = 0
	prev2 = 1
	for i in range(2,n+1):
		r = prev1+ prev2
		prev1 = prev2
		prev2 = r
	return r

def fibo5(n):
	#Fibo linear algebra
	if n <= 2:
		return (1,1)
	fn1 = fibo5(n-1)
	return (1*fn1[1] + 0*fn1[0], 1*fn1[0] + 1*fn1[1])

def fibo6(n):
	#Fibo Magic Formula
	return 1/sqrt(5)*((1+sqrt(5))/2)**n - 1/sqrt(5)*((1-sqrt(5))/2)**n	
	
#fibo_plot(fibo6, 105)

wrap_time([fibo1, fibo2,fibo3, fibo4,fibo5, fibo6], \
 ["Fibo Naive","Fibo Iterative","Fibo Cache", "Fibo Light","Fibo Matrix Mul","Fibo Formula"])

