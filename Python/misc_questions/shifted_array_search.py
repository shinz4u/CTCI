def shifted_arr_search(shiftArr, num):

    if len(shiftArr) == 0:
        return ""

    is_left_shifted = check_shift(shiftArr)

    if not is_left_shifted:
        location = bst_search(shiftArr, num, left=0, right=len(shiftArr)-1)
        return location

    pivot_point = find_pivot_point(shiftArr)

    if num >= shiftArr[0]:
        return bst_search(shiftArr, num, left=0, right=pivot_point)
    else:
        return bst_search(shiftArr, num, left=pivot_point, right=len(shiftArr)-1)



def check_shift(shiftArr):
    if shiftArr[0] > shiftArr[-1]:
        return True
    else:
        return False


def bst_search(shiftArr, num, left, right):
    mid = int((left + right) / 2)

    while left <= right:
        if shiftArr[mid] == num:
            return mid
        elif shiftArr[mid] < num:
            left = mid + 1
            mid = int((left + right) / 2)
        else:
            right = mid - 1
            mid = int((left + right) / 2)
    return ""


def find_pivot_point(shiftArr):
    left = 0
    right = len(shiftArr)-1
    # mid = int(left + (right - left)/2)

    while left <= right:
        mid = int(left + (right - left) / 2)
        if shiftArr[mid] < shiftArr[mid-1]:
            return mid
        elif shiftArr[mid] > shiftArr[0]:
            left = mid + 1
        else:
            right = mid - 1



print(shifted_arr_search([],2)) # -1
print(shifted_arr_search([2],2)) # 0
print(shifted_arr_search([1,2],2)) #1
print(shifted_arr_search([1,2],1))  #0
print(shifted_arr_search([1,2],3)) #-1
print(shifted_arr_search([1,2,3],3)) #2
print(shifted_arr_search([1,2],0))  #-1
print(shifted_arr_search([0,1,2,3,4,5],1)) # 1
print(shifted_arr_search([1,2,3,4,5,0], 0)) # 5
print(shifted_arr_search([2,3,4,5,6,0,1], 0)) # 5
print(shifted_arr_search([2,3,4,5,6,0,1], 3)) #1
print(shifted_arr_search([2,3,4,5,6,0,1], 5)) #3
print(shifted_arr_search([2,3,4,5,6,0,1], 4)) #2
print(shifted_arr_search([9,12,17,2,4,5], 17)) # 2
print(shifted_arr_search([9,12,17,2,4,5,6], 4)) # 4
