def binary_search(lst, left, right, key):
    while left <= right:
        mid = (left + right) // 2
        print(f"mid = {mid}")
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


lst = list(map(int, input("Enter list : ").strip().split()))
key = int(input("Enter the key : "))

print(f"index : {binary_search(lst, 0, len(lst)-1, key)}")