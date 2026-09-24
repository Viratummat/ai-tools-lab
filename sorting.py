def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == "  main__":
    sample_list = [64,34,25,78]
    print("original: ", sample_list)
    print("sorted: ", bubble_sort(sample_list) )            
