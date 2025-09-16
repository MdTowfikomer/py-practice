def binarySearch(arr, key):
    n = len(arr)
    st = 0
    end = n-1
    
    while st <= end:
        mid = (st + end)//2
    
        if(arr[mid] == key):
            print(f"Key found at index {mid}")
            return
        elif(arr[mid] > key):
            end = mid-1
        else:
            st = mid+1

    print("Element not found")
    return        


arr = [2,4,5,10,12,20]
key = 10
binarySearch(arr, key)
    