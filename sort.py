import time
import random
import matplotlib.pyplot as plt

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

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_sorting_performance():
    sizes = [50, 100, 500, 1000]
    times = {"Bubble Sort": [], "Selection Sort": [], "Insertion Sort": [], "Python Sort": []}
    
    for size in sizes:
        dataset = [random.uniform(1, 100) for _ in range(size)]
        
        for sort_name, sort_function in zip(["Bubble Sort", "Selection Sort", "Insertion Sort", "Python Sort"], 
                                            [bubble_sort, selection_sort, insertion_sort, sorted]):
            test_data = dataset.copy()
            start_time = time.time()
            sort_function(test_data)
            end_time = time.time()
            times[sort_name].append(end_time - start_time)
    
    # Plotting the results
    plt.figure(figsize=(10, 5))
    for sort_name, time_values in times.items():
        plt.plot(sizes, time_values, marker='o', label=sort_name)
    
    plt.xlabel("Dataset Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.grid()
    plt.show()

test_sorting_performance()