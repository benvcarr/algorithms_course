import sys

x = [7,10,9,6,5,2,4,1,8,3]

def main():
  printList(x)
  z = raw_input('Give me input')
  print z
  sys.stdout.write("hi")
  
def printList(list):
  for item in list:
    print item
	
def mergeSort(array, left_index, right_index):
  if left_index < right_index:
	midpoint = (left_index + right_index) / 2
	mergeSort(array, left_index, midpoint)
	mergeSort(array, midpoint+1, right_index)
	mergeArrays(array, left_index, midpoint, right_index)

def mergeArrays(array, left_index, midpoint, right_index):
	left_half_length = midpoint - left_index + 1
	right_half_length = right_index - midpoint
	left_array = []
	right_array = []
	
	for i in range(left_half_length):
	  left_array.append(array[left_index + i - 1])
	for j in range(right_half_length):
	  right_array.append(array[midpoint+ j + 1])
	  
if __name__ == '__main__':
	  main()
	