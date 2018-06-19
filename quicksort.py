from random import randint

def patition(arr, l, r):
    # pick a random index or the median of first, last and middle will lower average time complexity for edge cases
    r_index = randint(l, r) 
    arr[l], arr[r_index] = arr[r_index], arr[l]
    pivot = arr[l]    
    while l < r:
        while l < r and arr[r] >= pivot:
            r -= 1
        arr[l] = arr[r]
        while l < r and arr[l] <= pivot:
            l += 1
        arr[r] = arr[l]
    arr[l] = pivot
    return l

def quicksort(arr, l, r):
    if l < r:
        pi = patition(arr, l, r)
        quicksort(arr, l, pi-1)
        quicksort(arr, pi+1, r)

arr = [7,5,3,3,4,9,2,2,9,8]
quicksort(arr, 0, len(arr)-1)
print(arr)


