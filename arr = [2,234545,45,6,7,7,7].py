def find_smallest(arr):
    bigger = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > bigger:
            bigger = arr[i]
    return bigger

print(find_smallest([6,234545,45,6,7,7,7]))
