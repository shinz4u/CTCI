# a[i] == i

def magic_Index(arr):
    """
    Non recursive method
    """
    left = 0
    right = len(arr) - 1
    mid = left + int((right-left)/2)
    while left <= right:
        if arr[mid] == mid:
            while arr[mid-1] == mid - 1:
                mid  = mid - 1
            return arr[mid]
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
        mid = left + int((right-left)/2)
    return None


def magic_index_recursive(arr, left, right):
    mid = left + int((right-left)/2)
    if arr[mid] == mid:
        while arr[mid-1] == mid - 1:
            mid = mid - 1
        return arr[mid]
    elif arr[mid] > mid:
        return magic_index_recursive(left, mid-1, arr)
    else:
        return magic_index_recursive(mid + 1, right, arr)
    



arr = [-40,-30, 2 , 3, 4 ,5 ,7,10,12,24]

print(magic_index_recursive(arr, 0, (len(arr)-1)))
