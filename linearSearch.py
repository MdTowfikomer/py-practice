
def linearSearch(arr, key):
    for i in range(len(arr)):
        if(arr[i] == key):
            print(f"{key} is found at index {i}..!")
            return

    print("Element not found")    
    return

arr = [2,4,6,7,9,0,1]
key = 0

linearSearch(arr, key)