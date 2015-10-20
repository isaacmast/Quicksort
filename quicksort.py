import random, string, timeit

'''
Determines the execution time of a quicksort algorithm given an array, 
length arrayLength, of random strings, length stringLength. I do not 
own this code. All rights and original code of the quicksort algorithm 
belong to the OpenDSA hypertextbook project, which is part of 
algoviz.org. All rights and original code of the wrapper and wrapped 
functions belong to Xiaonuo Gantan from Python Central. 
'''

def wrapper(func, *args, **kwargs):
    '''
    Wrapper function to wrap quicksort function in to determine the
    execution time of the algorithm. 
    '''
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def quicksort(array, i, j):
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
    k = partition(array, i, j - 1, j)

    #Swap to put pivot in sorted position
    temp = array[k]
    array[k] = array[j]
    array[j] = temp

    #Sort left subarray
    if k - i > 1:
        quicksort(array, i, k - 1)

    #Sort right subarray
    if j - k > 1:
        quicksort(array, k + 1, j)
    
def findpivot(array, i, j):
    '''
    Determines pivot element in array in a quicksort algorithm
    Input: An array of strings, array, left bound, i, and right 
           bound, j
    Output: The index of the pivot element
    '''
    return (i + j) / 2

def partition(array, left, right, pivot):
    '''
    Partitions an array of strings in a quicksort algorithm
    Input: An array of strings, array, left bound, left, right 
           bound, right, and pivot index, pivot 
    Output: The index of left bound
    '''
    while left <= right:
        while array[left] <= array[pivot] and left < pivot:
            left += 1
        while right >= left and array[right] >= array[pivot]:
            right -= 1
        if right > left:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
    return left

array = []
arrayLength = 10
stringLength = 10
for i in range(arrayLength):
	array.append(''.join(random.choice(string.lowercase) for i in range(stringLength)))
wrapped = wrapper(quicksort, array, 0, arrayLength - 1)
print timeit.timeit(wrapped, number = 1000)
