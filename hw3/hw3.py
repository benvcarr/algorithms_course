#!/usr/bin/python

TEST_ARRAY = [-6, 12, -7, 0, 14, -7, 5]

def main():
  print largestSum(TEST_ARRAY)
  print getMinSteps(10)
  return

def largestSum(array):
  # Initialize our two vars
  current_largest_sum = 0
  sum_of_cur_subarray = 0
  
  # Inspect each value of the array.
  for i in range(0, len(array)):
    # Each subarray's value will be added to the current subarray value.
    sum_of_cur_subarray = sum_of_cur_subarray + array[i]

    # If our addition made this value go negative, reset the value to zero.
    # This will help us find points where we are no longer adding benefit to the subarray.
    if sum_of_cur_subarray < 0:
      sum_of_cur_subarray = 0
    # Return the larger of the two values - store the larger as our current max sum.
    elif (current_largest_sum < sum_of_cur_subarray):
      current_largest_sum = sum_of_cur_subarray
  return current_largest_sum
  
def reconstructString(string):
  n = len(string)
  # Init an array to hold our bool values for if we can 
  valid_string = []
  for i in range(0, n):
    # By default, we want to set the current value to False unless we know it is a word
    valid_string[i] = False
    for j in range(0,n):
      # if our substring is a valid word, set the value to true
      if dict(string[i:j]) == True:
        valid_string[i] = True
  return valid_string[n]

def isCompatible(city_blocks, desired_placement_n_s, desired_placement_w_e):
  # If any of the N, S, W, E blocks have an ad, then this block cannot.
  # A given city_block coordinate is 'True' if there is currently an ad there.
  if city_blocks[desired_placement_n_s-1][desired_placement_w_e] == True:
    is_compatible = False
  elif city_blocks[desired_placement_n_s+1][desired_placement_w_e] == True:
    is_compatible = False
  elif city_blocks[desired_placement_n_s][desired_placement_w_e-1] == True:
    is_compatible = False
  elif city_blocks[desired_placement_n_s][desired_placement_w_e+1] == True:
    is_compatible = False
  else:
    is_compatible = True
  return is_compatible


def maxAdValue(west_east_blocks,block_values):
  # Args: west_east_blocks: the integer value of the num of columns
  #       block_values: an array containing the value of a given x,y coordinate block
  city_blocks = createArray([4][west_east_blocks]) # always a total of 4 N/S rows
  cur_max_value = 0
  #initialize all values in city_blocks = False
  previous_pattern = []
  for i in range(0,west_east_blocks):
    for j in range(0, 3): # each row N/S
      if isCompatible(city_blocks,j,i) == True:
        cur_max_value += block_values[i,j]
      else: # we know this value can't be added in
        # Try other values, with the follow patterns:
        # If k = [1,3], k+1 = [2,4]
        # elif k = [1,4]: k+1 = [] or single
        # elif k = [2,4]: k+1 = [1,3]
        # elif k = []: k+1 = try: [1,3], [1,4], [2,4]
  return cur_max_value


      
  
def getMinSteps(value):
  values = [-1] * value
  values[0] = 0

  for i in range(2, value):
    values[i] = 1 + values[i]
    if i % 2 == 0:
      values[i] = min(values[i],1+values[i/2])
    if i % 3 == 0:
      values[i] = min(values[i],1+values[i/3])
  print values
  return values[value-1]
"""
The following pseudocode finds the composition of an optimal subset using
the table m output by the DP 0/1 knapsack algorithm presented in class
(and repeated in code below).

OptSubset(n, w[1..n], W, m[0..n, 0..W])//m[0..n, 0..W] is output of DP alg
01 create array S[1..n]
02 for l = 1 to n
03     S[l] = 0
04 k = 0 // number of items in an optimal subset
05 j = W
06 for i = n downto 1
07     if m[i,j] > m[i-1,j]
08          k = k+1
09          S[k] = i // include item i in S
10          j = j-w[i]
11 return S

Subarray S[1..k] will contain the items in an optimal subset.

DP 0/1 Knapsack(n, w[1..n], v[1..n], W) //w[i], 1 =< i =< n, W integers
01 create array m[0..n, 0..W]
02 for i = 0 to n
03     m[i,0] = 0
04 for j = 1 to W
05     m[0,j] = 0
06 for i = 1 to n
07     for j = 1 to W
08         if j < w[i] then m[i,j] = m[i-1,j] // item i cannot be selected
09         else m[i,j] = max{m[i-1,j], v[i] + m[i-1, j-w[i]]}
10 return m  // required optimum is the value m[n,W]

The input of the knapsack problem is an array of weights w[1..n], an array of values v[1..n], and a weight limit W.  All these are positive real numbers.

The problem is to find a subset S of {1,..,n} such that the following constraint is observed: the sum of the weights w[k] for each k in S is less than or equal to W.  The *objective* is to maximize the total value, i.e., sum of the values v[k] for each k in S, under this constraint.

"""
  
if __name__ == '__main__':
  main()
  
