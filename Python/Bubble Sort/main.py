
def bubble_sort(list_to_sort):
    """ Sort list in input using bubble sorting.

    :param list_to_sort: the list to sort
    :type list_to_sort: list
    :return: the list sorted
    :rtype: list
    """
    list_size = len(list_to_sort)
    for i in range(list_size):
        for j in range(0, list_size-i-1):
            if list_to_sort[j] > list_to_sort[j+1] :
                # Swap current and next element
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


# Test sorting method
n = int(input('Enter size of the list'))
unsorted_list = [int(input(i) for i in range(n)]
sorted_list = bubble_sort(unsorted_list)
print (f"Sorted list is: {', '.join([str(n) for n in sorted_list])}")
