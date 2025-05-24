def linear_search(array, element):
    for index in range(0, len(array) - 1):
        if element == array[index]:
            return index
    return -1
