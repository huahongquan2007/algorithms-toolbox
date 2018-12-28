
def binary_search(query, array):
    """
    Determine whether the query is in an sorted array.
    Return the index of the query if it is present in the array.
    If the query is not in the array, return -1
    >>> binary_search(4, [1, 2, 3, 4, 5, 6, 7, 8])
    3
    >>> binary_search(8, [1, 2, 3, 4, 5, 6, 7, 8])
    7
    >>> binary_search(10, [1, 2, 3, 4, 5, 6, 7, 8])
    -1
    """
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if query < array[mid]:
            hi = mid - 1
        elif query > array[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
