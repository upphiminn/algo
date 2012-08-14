#!/usr/bin/env python
import time

######## Utils
def wrap_time(functions, labels ):
	for i in xrange(len(functions)):
		start = time.time()
		print labels[i]
		result = functions[i](10,25)
		now = time.time() 
		print  "Speed " + str(( now - start )) + "\nResult " + str(result)
		print "#" * 30

def ancient_gcd(a,b):
	#O(n^3)
	while(b!=0):
		if(a>b): a-=b
		else: b-=a
	return a
def mod_gcd(a,b):
	#most efficient, halving b every time in worst case [2N - 2]
	if b==0: 
		return a
	return mod_gcd(b,a%b)

def efficient_gcd(a,b):
	# O(n^2)
	a_even = (a%2==0)
	b_even = (b%2==0)
	print a, " ", b
	if a==b:
		return a
	if 	 a_even and b_even:
		return 2*efficient_gcd(a/2,b/2)
	elif not a_even and b_even:
		return efficient_gcd(a,b/2)
	elif a_even and not b_even:
		return efficient_gcd(a/2,b)
	elif not a_even and not b_even:
		if(a>b):
			return efficient_gcd((a-b)/2,b)
		else:
			return efficient_gcd(a,(b-a)/2)

if __name__ == "__main__":
	print ancient_gcd(10,25)
	print mod_gcd(10,25)
	print efficient_gcd(10,25);
	wrap_time([ancient_gcd,mod_gcd,efficient_gcd],["ANCIENT", "MOD", "EFFICIENT"])
	#extended_euler_gcd(a,b);