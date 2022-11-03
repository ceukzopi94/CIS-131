"""
Christian Urbanski
CIS 131
09/06/2022

"""

#put constants here
import random
from timeit import timeit


def main(): 
    #put code here

    data1 = [0] * 100
    build_random_num_list(data1, 1, 1000)

    data2 = data1.copy()
    data3 = data1.copy()

    print(f'Unsorted list: {data1}')

    selection_sort(data1)
    insertion_sort(data2)
    merge_sort(data3)

    print(f'Selection Sorted list: {data1}')
    print(f'Insertion Sorted list: {data2}')
    print(f'Merge Sorted list: {data3}')


def build_random_num_list(data, min_num, max_num):
    """Function to build random number list."""
    for index in range(0, len(data) - 1):
        data[index] = random.randint(min_num, max_num)


def selection_sort(data):
    """Sort array using selection sort. O(n^2)"""
    #loop oer len(data) -  1 elements
    for index1 in range(len(data) - 1):
        smallest = index1#first index of remaining array

        #loop to find index of smallest element
        for index2 in range(index1 + 1, len(data)):
            if data[index2] < data[smallest]:
                smallest = index2

        #swap smallest element into position
        data[smallest], data[index1] = data[index1], data[smallest]


def insertion_sort(data):
    """Sort iterable variable using insertion sort. O(n^2)"""
    #loop over len(data) - 1 elements
    for next in range(1, len(data)):
        insert = data[next] #value to insert
        move_item = next #location to place element

        #search for place to put current element
        while move_item > 0 and data[move_item - 1] > insert:
            #shift element right one slot
            data[move_item] = data[move_item - 1]
            move_item -= 1

        data[move_item] = insert #place inserted element


def merge_sort(data):
    """Recursive fucntion to begin merge sorting. O(n log n)"""
    sort_array(data, 0, len(data) - 1)


def sort_array(data, low, high):
    """Split data, sort subarrays and merge them into sorted array."""
    #test base case size of array equals 1
    if(high - low) >= 1: #if not base case
        middle1 = (low + high) // 2 #calc middle of array
        middle2 = middle1 + 1 #calc next element over

        #split arrat in half then sort each half (recursive calls)
        sort_array(data, low, middle1)  # first half of array
        sort_array(data, middle2, high)  # second half of array

        #merge two sorted arrays after split calls return
        merge(data, low, middle1, middle2, high)


def merge(data, left, middle1, middle2, right):
    """Merge two sorted subarrays int one sorted array"""
    left_index = left #index into left subarray
    right_index = middle2 #index into right subarray
    combined_index = left #index into temporary working array
    merged = [0] * len(data) #working array

    #merge arrays until reaching end of either
    while left_index <= middle1 and right_index <= right:
        #place smaller of two currentelements into result
        #and move to next space in arrays
        if data[left_index] <= data[right_index]:
            merged[combined_index] = data[left_index]
            combined_index += 1
            left_index += 1
        else:
            merged[combined_index] = data[right_index]
            combined_index += 1
            right_index += 1

    #if left array is empty
    if left_index == middle2: #if True, copy in rest of right array
        merged[combined_index:right + 1] = data[right_index:right + 1]
    else: #right array is empty, copy in rest of left array
        merged[combined_index:right + 1] = data[left_index:middle1 + 1]

    data[left:right + 1] = merged[left:right + 1] #cope back to data


#---------------------------------------------------------------------------------


def get_integer(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        try:            
            newValue = int(input())
            return newValue
        except ValueError:
            print('Error: non-numeric value entered')

def get_float(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        try:
            newValue = float(input())
            return newValue
        except ValueError:
            print('Error: non-numeric value entered')
    
def get_string(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        newValue = input()
        if newValue and newValue.strip():
            return newValue
        else:
            print('Error: no data entered')
            
def get_yes_or_no(message, prompt="none"):
    while True:
        new_value = get_string(message, prompt)
        new_value = new_value.lower()
        if new_value == "y" or new_value == "yes":
            return True
        if new_value == "n" or new_value == "no":
            return False
        print('Error: invalid value entered') 

def display_prompt(message, prompt):
        print(message, end="")
        if prompt != "none":
            print ("\n" + prompt + " ", end="")

"""
loop that creates a grid of rows and columns for things to be placed in. 
    for row in range(1, MAX_ROWS + 1):
        for col in range(1, MAX_COLS + 1):
"""

#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
