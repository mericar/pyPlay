def binary_search_recursive(input_array, value):
    #base case
    if len(input_array) == 0:
        return -1
    #recursive case
    else:
        mid = len(input_array) // 2
        if input_array[mid] == value:
            return input_array[mid]
        else:
            if value < input_array[mid]:
                return binary_search_recursive(input_array[:mid], value)
            else:
                return binary_search_recursive(input_array[mid+1:], value)


        
def binary_search_iterative(input_array, value):
    lo = 0
    hi= len(input_array)-1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if input_array[mid] == value:
            return mid
        else:
            if value > input_array[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False
