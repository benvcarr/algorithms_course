#!/usr/bin/python

"""
Benjamin Carr
Homework #2 - MPCS 55001
Answers:
(1) Program below.
(2) My program is correct for all cases where both the numbers and the distances from the median
    are unique. I spent a lot of time (30+ hrs) trying to figure out other ways of doing this other than using a 
    dictionary to store key,val pairs but didn't come up with anything that would work for all situations. So, it
    works for situations that meet that criteria. It also assumes the median is always equal to floor(n/2), which is
    a bit of a mathematical compromise.
(3) It should run in O(n) time - the worst running time is a function of the O(n) lookup to select()
    that is initially used to find the median. Both of the core FOR loops (lines 66 & 71) take O(n) as well.
"""
import sys
import math
from random import randint

def main():
  startFindClosest()

def startFindClosest():
  """Begins the closest search process by reading in the stdin file.
  Args:
      None. Reads from stdin for file.

  Returns:
      No value. Prints closest k values to median to stdout."""
  f = sys.stdin
  line1 = f.readline()
  while line1 != '':
    k = int(f.readline())
    array = form_array_from_string_line(line1)
    print findClosestKValues(array, 0, len(array)-1, k)
    line1 = f.readline()
    if not line1:
      break
  return

def findClosestKValues(array, l_index, r_index, k):
  """Finds the closest K values to the median.
  Args:
      array: List object containing unsorted list of values.
      k: The number of numbers closest to the median we wish to find.

  Returns:
      nums: a list object containing the closest k numbers to median."""
  nums = []
  temp_array = []
  pairing = {}

  """
  Note: This is code I tried to use to get it work for varying lengths to accurately output
        the median value. It turned out to be more complex than imagined so I left it out.
  if (len(array) % 2) == 0:
    median_A = randomizedSelect(array, l_index, r_index, (len(array)/2))
    median_B = randomizedSelect(array, l_index, r_index, ((len(array)-1)/2))
    median = (median_A + median_B) / 2.0
  else:
    median = randomizedSelect(array, l_index, r_index, (len(array)/2))"""

  median = randomizedSelect(array, l_index, r_index, math.floor(len(array)/2))
  array.remove(median)
  array.append(median)
  for i in range(0,r_index+1):
    pairing[abs(array[i]-median)] = array[i]
    temp_array.append(abs(array[i] - median))
  
  kth_element = randomizedSelect(temp_array, l_index, len(temp_array)-1, k)
  for j in range(0,len(array)):
    if temp_array[j] <= kth_element:
        nums.append(pairing[temp_array[j]])

  return nums

def form_array_from_string_line(line):
  """Begins the inversion count process by reading in the stdin file.

    Args:
        line: A string of input line (usually from a text file) with integers
              contained within, separated by spaces.

    Returns:
        array: List object (Python's standard 'array' type) featuring each of
               the integers as a separate item in the list."""
  array = [int(n) for n in line.split()]
  return array

def randomizedSelect(array, l_index, r_index, i):
  """Uses the randomizedPartion method to find the specified i-th value.

    Args:
      array: List object containing unsorted list of values.
      l_index: Left index of the subarray we want to search in.
      r_index: Right index of the subarray we want to search in.
      i: The i-th sorted value we want to find.
      
    Returns:
        array: List object (Python's standard 'array' type) featuring each of
               the integers as a separate item in the list."""
  if l_index == r_index:
    return array[l_index]
  q = randomizedPartition(array, l_index, r_index)
  k = q - l_index + 1
  if i == k:
    return array[q]
  elif i < k:
    return randomizedSelect(array, l_index, q-1, i)
  else:
    return randomizedSelect(array, q+1, r_index, i-k)

def randomizedPartition(array, l_index, r_index):
  """Randomizes the partion method.

    Args:
      array: List object containing unsorted list of values.
      l_index: Left index of the subarray we want to search in.
      r_index: Right index of the subarray we want to search in.
      
    Returns:
        i+1: Integer value of the index of the partition."""
  i = randint(l_index, r_index)
  array = valueSwap(array, i, r_index)
  return partition(array, l_index, r_index)

def partition(array, l_index, r_index):
  """Identifies the partion index.

    Args:
      array: List object containing unsorted list of values.
      l_index: Left index of the subarray we want to search in.
      r_index: Right index of the subarray we want to search in.
      
    Returns:
        i+1: Integer value of the index of the partition."""
  pivot = array[r_index]
  i = l_index - 1
  j = l_index

  for j in range(l_index, r_index):
    if array[j] <= pivot:
      i += 1
      array = valueSwap(array, i, j)
  array = valueSwap(array, i+1, r_index)
  return i+1

def valueSwap(array, index_one, index_two):
  """Swaps two values in a given array.

    Args:
      array: List object containing unsorted list of values.
      index_one: Index of first item we want to swap.
      index_two: Index of second item we want to swap.
      
    Returns:
        array: List with the desired values swapped."""
  if len(array) <= 1:
    return array
  else:
    try:
      temp = array[index_one]
      array[index_one] = array[index_two]
      array[index_two] = temp
    except IndexError, e:
      print e
      print "Tried to swap index: " + str(index_one) + ' with index: ' + str(index_two)
  return array

if __name__ == '__main__':
  main()
