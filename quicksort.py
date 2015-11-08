import random, string, timeit

'''
Determines the execution time of a quicksort algorithm given an array, 
length arrayLength, of random strings, length stringLength. All rights 
and original code of the quicksort algorithm belong to the OpenDSA
hypertextbook project, which is part of algoviz.org. All rights and 
original code of the wrapper and wrapped functions belong to Xiaonuo
Gantan from Python Central at 
"pythoncentral.io/time-a-python-function/".
'''

def wrapper(func, *args, **kwargs):
	'''
	Wrapper function to wrap quicksort function in to determine the
	execution time of the algorithm. 
	'''
	def wrapped():
		return func(*args, **kwargs)
	return wrapped

def quicksort(array, i, j, count):
	'''
	Quicksort algorithm for sorting an array of random strings
	Input: An array of strings, array, left bound, i, and right 
		bound, j
	Output: The sorted array of strings
	'''

	#Determine pivot index
	pivot = findpivot(array, i, j)

	#Swap pivot with rightmost element in array
	temp = array[j]
	array[j] = array[pivot]
	array[pivot] = temp

	#Partition array
	k, count = partition(array, i, j - 1, j, count)

	#Swap to put pivot in sorted position
	temp = array[k]
	array[k] = array[j]
	array[j] = temp

	#Sort left subarray
	if k - i > 1:
		quicksort(array, i, k - 1, count)

	#Sort right subarray
	if j - k > 1:
		quicksort(array, k + 1, j, count)

	return count

def findpivot(array, i, j):
	'''
	Determines pivot element in array in a quicksort algorithm
	Input: An array of strings, array, left bound, i, and right 
		   bound, j
	Output: The index of the pivot element
	'''
	return (i + j) / 2

def partition(array, left, right, pivot, count):
	'''
	Partitions an array of strings in a quicksort algorithm
	Input: An array of strings, array, left bound, left, right 
		   bound, right, and pivot index, pivot 
	Output: The index of left bound
	'''
	while left <= right:
		count += 1
		while array[left] <= array[pivot] and left < pivot:
			left += 1
		while right >= left and array[right] >= array[pivot]:
			right -= 1
		if right > left:
			temp = array[left]
			array[left] = array[right]
			array[right] = temp
	return left, count

#Assign variables
array = []
ARRAYLENGTH = 2000
STRINGLENGTH = 10
count = 0

#Generate array, length ARRAYLENGTH, of random strings, 
#length STRINGLENGTH
for i in range(ARRAYLENGTH):
	array.append(''.join(random.choice(string.lowercase) for i in range(STRINGLENGTH)))

#Wrap algorithm to determine execution time
wrapped = wrapper(quicksort, array, 0, ARRAYLENGTH - 1, count)

#Determine basic operation execution count
print quicksort(array, 0, ARRAYLENGTH - 1, count)

#Determine execution time of algorithm
print (timeit.timeit(wrapped, number = 1000)) / 1000
