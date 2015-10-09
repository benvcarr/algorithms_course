from random import randint

MAIN_ARRAY = [5, 7, 8, 9, 2, 4]
EQUAL_ARRAY = [1, 1, 1, 1, 1, 1]
TEST_ARRAY = [1, 4, 7, 2, 3, 6, 6]

def main():
  output = quicksort(MAIN_ARRAY, 0, len(MAIN_ARRAY)-1)
  print output
  a,x,y = newPartition(TEST_ARRAY, 0, len(TEST_ARRAY)-1)
  print 'left bound: ' + str(x)
  print 'right bound: ' + str(y)
  output2 = newQuickSort(MAIN_ARRAY, 0, len(MAIN_ARRAY)-1)
  print output2
  output3 = randomizedSelect(TEST_ARRAY, 0, len(TEST_ARRAY)-1, 3)
  print 'The 3rd value is: ' + str(output3)
  print calculateQuantiles(MAIN_ARRAY,3)
  print retreiveQuantiles(MAIN_ARRAY, 0, len(MAIN_ARRAY)-1, 1, 3, 4)


def calculateQuantiles(array, quantile_value):
  # Calculate the value of each quantile
  value = len(array) / quantile_value
  # Store the indices where each value will live, relative to the size of our input
  quantile_indices = [value]
  i = 1
  # Maintain a running var to keep track of the next index
  running_value = value
  for i in range(1, quantile_value):
    running_value += value
    # Adds in each index value to our list
    quantile_indices.append(running_value)
  j = 0
  quantiles = []
  # For each index value we have, we want to return the value of the item in that sorted position
  for index in quantile_indices:
    # Utilize the randomized select function to find the i-th (index) value
    quantiles.append(randomizedSelect(array, 0, len(array)-1, index))
  return quantiles

def retreiveQuantiles(array, l_index, r_index, i, j, quantiles):
  n = len(array)
  m = (i+j)/2
  q = m*(n/quantiles)
  q = q-l_index+1
  q = randomizedSelect(array, l_index, r_index, q)
  q = partition(array, l_index, r_index)
  if i < m:
      L=retreiveQuantiles(array, l_index, q-1, i, m-1, quantiles)
  if m < j:
      R=retreiveQuantiles(array, q+1, r_index, m+1, j, quantiles)
  return L, U, A[q], U, R

def randomizedSelect(array, l_index, r_index, i):
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

def randomizedQuicksort(array, l_index, r_index):
  if l_index < r_index:
    q = randomizedPartition(array, l_index, r_index)
    array = randomizedQuicksort(array, l_index, q-1)
    array = randomizedQuicksort(array, q+1, r_index)
  return array

def randomizedPartition(array, l_index, r_index):
  i = randint(l_index, r_index)
  array = valueSwap(array, i, r_index)
  return partition(array, l_index, r_index)

def valueSwap(array, index_one, index_two):
  temp = array[index_one]
  array[index_one] = array[index_two]
  array[index_two] = temp
  return array

def quicksort(array, l_index, r_index):
  if l_index < r_index:
    pivot = partition(array, l_index, r_index)
    array = quicksort(array, l_index, pivot - 1)
    array = quicksort(array, pivot + 1, r_index)
  return array

def partition(array, l_index, r_index):
  pivot = array[r_index]
  i = l_index - 1
  j = l_index

  for j in range(l_index, r_index):
    if array[j] <= pivot:
      i += 1
      array = valueSwap(array, i, j)
  array = valueSwap(array, i+1, r_index)
  return i+1

def newPartition(A, p, r):
  pivot = A[r]
  i = p - 1
  j = p
  same_val_count = 0
  for j in range(p, r):
    if A[j] <= pivot:
      if A[j] == pivot:
        same_val_count += 1
      i += 1
      A = valueSwap(A, i, j)

  A = valueSwap(A, i+1, r)
  q = (i+1) - same_val_count 
  t = i+1
  return A, q, t

def randomizedNewPartition(array, l_index, r_index):
  i = randint(l_index, r_index)
  array = valueSwap(array, i, r_index)
  return newPartition(array, l_index, r_index)

def newQuickSort(array, l_index, r_index):
  if l_index < r_index:
    array, q, t = randomizedNewPartition(array, l_index, r_index)
    array = newQuickSort(array, l_index, q-1)
    array = newQuickSort(array, t+1, r_index)
  return array

if __name__ == '__main__':
  main()
