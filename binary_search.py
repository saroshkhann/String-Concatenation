def binary_search(arr, target):
    n = len(arr)
    start = 0
    end = n-1
    while start <= end:
        mid= (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1


sorted_list = [10,22,35,46,57,68,78,99]
sorted1_list = [100,212,385,446,567,68,78,999]
target = 99

result = binary_search(sorted_list,target)
print(result)
