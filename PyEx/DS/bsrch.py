
def newbinary_search(a_list, item):
    if len(a_list) == 0:
       return False
    else:
        midpoint = len(a_list) // 2

    print "mid: ", midpoint, a_list
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return newbinary_search(a_list[:midpoint], item)
        else:
            return newbinary_search(a_list[midpoint + 1:], item)

def binary_search(arr, item):
    if len(arr) == 0:
        return False
    mid = len(arr)  // 2

    print "mid: ", mid, arr
    if arr[mid] == item:
        return True
    elif arr[mid] < item:
        return binary_search(arr[mid+1:], item)
    else: #arr[mid] > item:
        return binary_search(arr[0:mid], item)

def bub_sort(arr):
    for i in xrange(len(arr)):
        for j in xrange(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def ins_sort(arr):
    for i in xrange(len(arr)):
        cur_pos = i 
        cur_val = arr[i]

        while cur_pos > 0 and arr[cur_pos - 1] > cur_val:
            arr[cur_pos] = arr[cur_pos - 1] 
            cur_pos = cur_pos - 1

        arr[cur_pos] = cur_val

    return arr

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            elif left[i] > right[j]:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i <  len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j <  len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
    return arr

print binary_search([2, 3, 5, 6, 9, 10, 22], 7)
#print newbinary_search([2, 3, 5, 6, 9, 10, 22], 9)
#print bub_sort([100, 2, 3, 5, 6, 9, 10, 22])
print ins_sort([100, 2, 3, 5, 6, 9, 10, 22])
print 'merge:', merge_sort([100, 2, 3, 5, 6, 9, 10, 22])
