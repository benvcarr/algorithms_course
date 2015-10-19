#!/usr/bin/python

"""
Benjamin Carr
Homework #3 - MPCS 55001
Answers:
(1) Program below.
(2) Correctness: I think this should work for every set of non-negative inputs. It basically stores the values (the num of 
    coins required) for every value up to the number we want to make change for. At each number, we basically just need to decide if there is a better way to create change than just adding 1 to the previously calculated number. Then in the ends we want to go through and step back through each value we added to the array to figure out which amounts of each
    denomination we were using to make that change.
(3) Running time: We step through the coin values array twice - once inside a loop that
    runs to the value we send it to make change for (i.e. for a submission of 10, it runs through 10 times and each of the
    10 loops has k iterations inside, where z is the number of coin values). The second usage of the array is to sum up the times we used each coin value, and it is done outside of any other loop structure. Thus, our running time looks like:
    O(nk) + O(k), dropping the lowest order terms it appears to be: O(nk)
"""
import sys

def main():
  startFindCoins()
  
def startFindCoins():
  """Begins the coin count process by reading in the stdin file.
  Args:
      None. Reads from stdin for file.

  Returns:
      No value. Prints the min number of coins required to stdout."""
  f = sys.stdin
  line1 = f.readline()
  while line1 != '':
    k = int(f.readline())
    array = form_array_from_string_line(line1)
    x,y = coin_value(array,k)
    print y
    line1 = f.readline()
    if not line1:
      break
  return

def form_array_from_string_line(line):
  """Creates an array from a (space|comma) delimited string.

    Args:
        line: A string of input line (usually from a text file) with integers
              contained within, separated by spaces.

    Returns:
        array: List object (Python's standard 'array' type) featuring each of
               the integers as a separate item in the list."""
  array = [int(n) for n in line.split()]
  return array

def coin_value(coin_vals,number):
  """Calculates the minimum number of coins needed to make change for a given value. Also
     sums up the individual counts of each coin needed.

    Args:
        coin_vals: List containing the denominations of each coin.
        number: Integer of change value to be broken into coins.

    Returns:
        minimum_coins: Integer The number of coins to make the min.
        individual_coin_count: List object containing the number of each of the respective coins needed."""
  minimum_coins = [0] * (number + 1)
  full_coin_list = [0] * (number + 1)
  individual_coin_count = [0] * len(coin_vals)
  for i in range(number + 1):
    # Per the prompt, we can always make change with a 1 cent value, so at the worst our count = the current number
    num_coins = i
    cur_coin_count = 1
    # If a coin value is bigger than our current number, we don't want to bother looking at as a possibility.
    for j in [c for c in coin_vals if c <= i]:
      if minimum_coins[i-j] + 1 < num_coins:
         num_coins = minimum_coins[i-j]+1
         cur_coin_count = j
    # Now we know the number of coins required for the i-th value, store it in an array at position i.
    minimum_coins[i] = num_coins
    full_coin_list[i] = cur_coin_count
  # For each coin value, we want to count the number of times that value was used in making our change.
  # This is pretty inefficient, since we have to make the same calculations for every value. I ran out of time
  # to be able to flesh this out to run more quickly.
  for i in range(0, len(coin_vals)):
    temp_change_val = number
    cur_count = 0
    while temp_change_val > 0:
      cur_coin = full_coin_list[temp_change_val]
      if cur_coin == coin_vals[i]:
        cur_count += 1
        # Replace the array position value with the count of the number of coins of this type
        individual_coin_count[i] = cur_count
      # Move back down the stored value list by the amount of the coin we just counted
      temp_change_val = temp_change_val - cur_coin
  return minimum_coins[number], individual_coin_count
  
if __name__ == '__main__':
  main()
