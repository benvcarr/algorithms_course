#!/usr/bin/python

"""
Benjamin Carr
Homework #1 - MPCS 55001
Answers:
(1) Divide and conquer program (See below).
(2) This is a heavy modification of merge sort. We take the principles of merge
    sort and apply them - we split the job into smaller batches (divide and
    conquer-esque). In those smaller batches, we want to sort the subarrays we
    created to count the inversions within them. We can count these inversions 
    as part of the sort process.
(3) T(n) = 7*1 (line 29, 30, 44, 57, 60, 67, 88) + n/2 (line 62) + n/2 (line 63) + n (line 66) + n (line 87)
T(n) =  2 T(n/2) + 2 T(n) + 7
a = 2, b = 2, d = 1; log_b_a = log_2_2 = (2^x = 2) = 1 = d
Thus, by master theorem - O(n^d log_2_n) = O(n log_2_n)
"""

import sys

def main():
  start_inversion_count()

def start_inversion_count():
  """Begins the inversion count process by reading in the stdin file.
    Args:
        None. Reads from stdin for file.

    Returns:
        No value. Prints inversion count to stdout."""
  for line in sys.stdin:
    array = form_array_from_string_line(line)
    final_array, total_count = count_inversions(array)
    print total_count
  return

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

def count_inversions(array):
  """Counts the inversions present in a given array.

  Args:
      array: A list of integer values.

  Returns:
      merged_array: List of the final array merged back together from the 
                    created subarrays.
      total_count: Integer value of the total number of inversions."""
  if len(array) == 1:
    return array, 0
  else:
    midpoint = len(array) / 2
    # Recursively call this function for smaller and smaller arrays
    a1, count_a1 = count_inversions(array[0:midpoint])
    a2, count_a2 = count_inversions(array[midpoint:])
    # Each time we get a pair of arrays back, we want to know the count of 
    # inversions within and between them
    merged_array, cross_count = merge_and_count(a1, a2)
    total_count = count_a1 + count_a2 + cross_count
    return merged_array, total_count
  return

def merge_and_count(a1, a2):
  """Merges two arrays and counts the inversions present amongst them.

  Args:
      a1: A list of integer values.
      a2: Another list of integer values.

  Returns:
      merged_array: List of the final array merged back together from the 
                    created subarrays.
      count: Integer value of the number of inversions in the two arrays."""
  merged_array = []
  a1_index = 0
  a2_index = 0
  count = 0

  while a1_index < len(a1) and a2_index < len(a2):
    if a1[a1_index] > a2[a2_index]:
      # Append the smaller number to the next spot in our new sorted array
      merged_array.append(a2[a2_index])
      a2_index += 1
      # We know that every other item in a1 is also bigger, so our count goes up
      # for each one.
      count += (len(a1)-a1_index)
    elif a1[a1_index] < a2[a2_index]:
      # Again appending the smaller number to the next spot in the merged array
      merged_array.append(a1[a1_index])
      a1_index += 1
  # Since we've maxed out at last one of our lists, need to add the remainder
  # from both lists, as we know these numbers are even bigger than current ones
  merged_array += a1[a1_index:]
  merged_array += a2[a2_index:]
  return merged_array, count

if __name__ == '__main__':
  main()
