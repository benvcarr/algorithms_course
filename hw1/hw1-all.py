import sys

MY_LIST_TO_SORT = [4, 5, 1, 9, 7, 6, 4, 5]

LOCAL_MINIMA_LIST = [9, 7, 7, 2,1,3,7,5,4,7,3,3,4,8,6,9]

TRIPLES_LIST = [3,-4,-2,-1,4,0,1]

def main():
  x = mergeSort3(MY_LIST_TO_SORT)
  print 'The final output is: '
  print x
  splitLocalMinSearch(LOCAL_MINIMA_LIST, 0, len(LOCAL_MINIMA_LIST)-1)
  startMinSearch()
  startInversionCount()

def countInversions(array):
  if len(array) == 1:
    return array, 0
  else:
    midpoint = len(array) / 2
    a1, count_a1 = countInversions(array[0:midpoint])
    a2, count_a2 = countInversions(array[midpoint:])
    merged_array, cross_count = mergeArraysAndCountCrossInversions(a1, a2)
    total_count = count_a1 + count_a2 + cross_count
    return merged_array, total_count

def startInversionCount():
  i = 0
  for line in sys.stdin:
    array = [int(n) for n in line.split()]
    print '****Inversions Row ' + str(i) + '****'
    x,y = countInversions(array)
    print y
    i += 1
  return

def mergeArraysAndCountCrossInversions(a1,a2):
  merged_array = []
  a1_index = 0
  a2_index = 0
  count = 0
  while a1_index < len(a1) and a2_index < len(a2):
    if a1[a1_index] > a2[a2_index]:
      merged_array.append(a2[a2_index])
      a2_index += 1
      count += (len(a1)-a1_index)
    elif a1[a1_index] < a2[a2_index]:
      merged_array.append(a1[a1_index])
      a1_index += 1
  merged_array += a1[a1_index:]
  merged_array += a2[a2_index:]
  return merged_array, count

def isInversion(a1, a2, i, j):
  if (i < j) and a1[i] > a2[j]:
    return True
  else:
    return False

def splitLocalMinSearch(array, left_bound, right_bound):
  midpoint = (left_bound + right_bound) / 2
  if isLocalMinima(array, midpoint) == True:
    print 'Local minima split find is position: ' + str(midpoint+1) + ' value: ' + str(array[midpoint])
    return midpoint
  elif array[midpoint+1] > array[midpoint-1]:
    right_bound = midpoint
    left_bound = left_bound
    return splitLocalMinSearch(array, left_bound, right_bound)
  else:
    left_bound = midpoint
    right_bound = right_bound
    return splitLocalMinSearch(array, left_bound, right_bound)
  return

def splitLocalMinSearchv2(array, left_bound, right_bound):
  mid = (left_bound + right_bound) / 2
  if (mid - 2 < 0) and (mid + 1 >= len(array)):
    return -1
  elif isLocalMinima(array, mid):
    print 'Local minima split find v2 is position: ' + str(mid+1) + ' value: ' + str(array[mid])
    return array[mid]
  elif (array[mid-1] > array[mid-2]):
    return splitLocalMinSearchv2(array, left_bound, mid)
  else:
    return splitLocalMinSearchv2(array, mid, right_bound)

def straightLocalMin(array):
  i = 0
  while i < len(array):
    z = isLocalMinima(array,i)
    if z == True:
      print "Local minima straight find is position: " + str(i+1) + ' value: ' + str(array[i])
      break
    i += 1
  return

def startMinSearch():
  myfile = open('localmin_input.txt', 'r')
  i = 1
  for line in myfile:
    array = [int(n) for n in line.split()]
    print '****Row ' + str(i) + '****'
    straightLocalMin(array)
    splitLocalMinSearch(array, 0, len(array))
    splitLocalMinSearchv2(array, 0, len(array))
    i += 1

def isLocalMinima(array, value_index):
  if (array[value_index-1] >= array[value_index]) and (array[value_index] <= array[value_index+1]):
    return True
  else:
    return False

def mergeSort3(a):
  if len(a) <= 1:
    return a
  elif len(a) == 2:
    return mergeSort(a)
  else:
    point_length = len(a) / 3
    point_2_start = 2 * len(a) / 3
    point2 = point_length * 2

    a1 = mergeSort(a[0:point_length])
    a2 = mergeSort(a[point_length:point2])
    a3 = mergeSort(a[point2:])

    final = merge3(a1,a2,a3)
    return final


def merge3(a1, a2, a3):
  final_a = []
  sentinel = float('inf')
  a1_index = 0
  a2_index = 0
  a3_index = 0

  a1.append(sentinel)
  a2.append(sentinel)
  a3.append(sentinel)
  i = 0
  while a1_index < len(a1) and a2_index < len(a2) and a3_index < len(a3):
    if (a2[a2_index] <= a1[a1_index]) and (a2[a2_index] <= a3[a3_index]):
      final_a.insert(i, a2[a2_index])
      a2_index += 1
    elif (a1[a1_index] <= a2[a2_index]) and (a1[a1_index] <= a3[a3_index]):
      final_a.insert(i, a1[a1_index])
      a1_index += 1
    elif (a3[a3_index] <= a2[a2_index]) and (a3[a3_index] <= a1[a1_index]):
      final_a.insert(i, a3[a3_index])
      a3_index += 1
    i += 1

  final_a.remove(sentinel)

  return final_a

def mergeSort(a):
  if len(a) == 1:
    return a
  else:  
    midpoint = len(a) / 2
    a1 = mergeSort(a[0:midpoint])
    a2 = mergeSort(a[midpoint:])
  return merge(a1,a2)

def merge(a1, a2):
  final_a = []
  sentinel = float('inf')
  a1_index = 0
  a2_index = 0
  a1.append(sentinel)
  a2.append(sentinel)

  i = 0
  while a1_index < len(a1) and a2_index < len(a2):
    if (a1[a1_index] <= a2[a2_index]):
      final_a.insert(i, a1[a1_index])
      a1_index += 1
    else:
      final_a.insert(i, a2[a2_index])
      a2_index += 1
    i += 1
  final_a.remove(sentinel)
  return final_a

if __name__ == '__main__':
  main()
