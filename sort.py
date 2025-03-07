import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def test_sorting_performance():
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    
    print("\nSmall Dataset (50 elements):")  # Replaced 🔹 with plain text
    
    bubble_test = small_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"Bubble Sort took {end_time - start_time:.6f} seconds.")  # Replaced ✅
    
    selection_test = small_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"Selection Sort took {end_time - start_time:.6f} seconds.")  # Replaced ✅
    
    print("\nLarge Dataset (1000 elements):")  # Replaced 🔹
    
    bubble_test = large_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"Bubble Sort took {end_time - start_time:.6f} seconds.")  # Replaced ⚠️
    
    selection_test = large_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"Selection Sort took {end_time - start_time:.6f} seconds.")  # Replaced ✅
    
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"Python Built-in Sort took {end_time - start_time:.6f} seconds.")  # Replaced 🚀

test_sorting_performance()