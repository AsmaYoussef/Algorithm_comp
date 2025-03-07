# Bubble Sort Implementation

## Description
This project contains a Python implementation of the Bubble Sort algorithm. Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process repeats until the list is sorted.

## How It Works
1. Iterate through the list multiple times.
2. Compare each pair of adjacent elements.
3. Swap them if they are in the wrong order.
4. Continue until no swaps are needed, meaning the list is sorted.

## Features
- Implements Bubble Sort in Python.
- Optimized with an early exit condition when no swaps occur in a pass.
- Sorts a list of numbers in ascending order.

## Installation
No additional installations are required. This script runs with Python 3.

## Usage
1. Clone this repository or copy the script.
2. Run the Python script:
   ```sh
   python bubble_sort.py
   ```
3. Example:
   ```python
   arr = [64, 34, 25, 12, 22, 11, 90]
   sorted_arr = bubble_sort(arr)
   print("Sorted array:", sorted_arr)
   ```

## Code
```python
def bubble_sort(arr):
    """
    Bubble Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped:  
            break  
    return arr  

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
```

## Complexity Analysis
- **Worst-case time complexity**: O(n²) (when the list is in reverse order)
- **Best-case time complexity**: O(n) (when the list is already sorted, due to the optimization)
- **Space complexity**: O(1) (sorting is done in place)

## License
This project is open-source and available for personal or educational use.

