def  binary_search(arr, e):
    # assume array is sorted
    arr_len = len(arr)
    half = arr_len//2 # half needed to split array

    # Array is empty
    if arr_len == 0:
        print("Array is empty.")
        return -1 # -1 represents null value
    
    # check halfway element x
    if arr[half] == e: 
        return half
    # element not found after several iterations
    elif arr_len <= 1 and arr[0] != e: 
        print("Element " + str(e) + " was not found.")
        return -1
    # split array case
    elif arr_len > 1:
        bottom_half = arr[0:half]
        top_half = arr[half:arr_len]
        if e < arr[half]:
            return binary_search(bottom_half, e)
        else:
            result = binary_search(top_half, e)
            if result != -1: # needed to return proper null value
                return binary_search(top_half, e) + half
            else:
                return result

def  binary_search_count(arr, e):
    # same as binary_search except instead of returning the index, we return the # of times it is called
    # assume array is sorted
    arr_len = len(arr)
    if arr_len == 0:
        raise Exception("Array is empty.")
    half = arr_len//2
    if arr[half] == e:
        return 1
    elif arr_len == 1 and arr[0] != e:
        raise Exception("Element " + str(e) + " was not found.")
    elif arr_len > 1:
        bottom_half = arr[0:half]
        top_half = arr[half:arr_len]
        if e < arr[half]:
            return binary_search_count(bottom_half, e) + 1
        else:
            return binary_search_count(top_half, e) + 1


def test_array(a):
    array_length = len(a)
    
    count_sum = 0
    max_count = 0
    for i in range(array_length):
        count = binary_search_count(a, a[i])
        count_sum += count
        if count > max_count:
            max_count = count
    avg = count_sum/array_length
    
    print("# of elements in array: " + str(array_length))
    print("highest # of calls: " + str(max_count))
    print("avg # of calls: " + str(avg))


def main():
    # to prove it works
    
    print("Binary search for 1 on empty array: ")
    result = binary_search([], 1)
    print("Element: 1 " + "Result: " + str(result))
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Binary search for #s 1-10, on an array of #s 1-8:")
    for i in range(len(arr) + 2):
        result = binary_search(arr, i)
        print("Element: " + str(i) + " " + "Result: " + str(result))
    
    
    
    for i in range(20):
        arr_test = []
        for j in range(8*(i+1)):
            arr_test.append(j)
        
        print("Array#" + str(i + 1) + ":")
        test_array(arr_test)

main()

    