#!/usr/bin/env python
from random import *
import binascii
def randomlist(n = 0):
	lst = []
	for i in range(0,n):
		lst.append(randint(1,1000))
	return lst

#bubble sort
def bubble(lst):
	for i in range(0, len(lst)):
		for j in range(i, len(lst)):
			if lst[i] > lst[j]:
				lst[j],lst[i] = lst[i], lst[j]
	return lst

#insertion sort
def insertion(lst):
	for i in range(1,len(lst)):
		j = i - 1
		while j >= 0 and lst[j] > lst[j+1]:
			lst[j+1],lst[j] = lst[j],lst[j+1]
			j -= 1
	return lst

#selection sort
def selection(lst):
	slst = []
	print lst
	for i in range(0,len(lst)):
		min = lst[i]
		pos = None
		for j in range(i,len(lst)):
			if min > lst[j]:
				min = lst[j]
				pos = j
		if pos:
			lst[pos] = lst[i]
			lst[i] = min
	return lst

#bucket sort
def bucket(lst):
	blst = [0] * (max(lst) + 1)
	for el in lst:
		blst[el] +=1
	lst = []
	for i, num in enumerate(blst):
		if num != 0:
			lst.extend([i]*blst[i])
	return lst

def int_to_bin_str(num):
	strr = ""
	if num == 0:
		return "0"
	while num > 0:
		strr = str(num%2) + strr
		num /=2
	return strr
def str_to_int(strr):
	if strr == "0":
		return 0

	r = 0
	for i in range(1,len(strr)+1):
		if strr[-i] == "1":
			r = r + 2**(i-1)
	return r


#radix sort
def radix(lst):
	binary_lst = [int_to_bin_str(el) for el in lst]
	mmax = len(int_to_bin_str(max(lst)))
	rest = []
	for i in range(1, mmax+1):
		buckets = [[],[]]
		
		for el in binary_lst:
			if (len(el)) > i:
				if (el[-i] == "0"):
					buckets[0].append(el)
				else:
					buckets[1].append(el)

			else: 
				rest.append(el)

		binary_lst = buckets[0] + buckets[1] 

	return [str_to_int(el) for el in rest + binary_lst]

#merge sort
def merge(lst, rst):
	r = []
	i = j = 0
	while i < len(lst) and j < len(rst):
		if lst[i] <= rst[j]:
			r.append(lst[i])
			i += 1

		else:
			r.append(rst[j])
			j += 1
	
	while i < len(lst):
		r.append(lst[i])
		i += 1

	while j < len(rst):
		r.append(rst[j])
		j += 1

	return r

def merge_sort(lst):
	
	if len(lst) <= 1:
		return lst

	return merge(merge_sort(lst[0:len(lst)/2]), \
			     merge_sort(lst[(len(lst)/2):]))
#quick sort
#	lame version
def quicksort(lst):
	
	if(len(lst) <= 1):
		return lst

	pivot = len(lst)/2
	left = [el for el in lst if el < lst[pivot]]
	right = [el for el in lst if el > lst[pivot]]
	#print left, right
	return quicksort(left) + [lst[pivot]] + quicksort(right)

#heap sort
def heap_sort(lst):
	pass
if __name__ == "__main__":

	print bubble(randomlist(10))
	print insertion(randomlist(10))
	print selection(randomlist(10))
	print bucket(randomlist(10))
	print radix(randomlist(10))
	print merge_sort(randomlist(10))
	print quicksort(randomlist(10))
	print heapsort(randomlist(10))