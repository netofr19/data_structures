def binary_search_iterative(ordered_list, term):
    size_of_list = len(ordered_list)-1
    index_of_first_element = 0
    index_of_last_element = size_of_list
    while index_of_first_element <= index_of_last_element:
        mid_point = int((index_of_first_element + index_of_last_element)/2)
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
    if index_of_first_element > index_of_last_element:
        return None


def binary_search_recursive(ordered_list, first_element, last_element, term):
    if last_element < first_element:
        return None
    else:
        mid_point = first_element + ((last_element - first_element)//2)
        if ordered_list[mid_point] > term:
            return binary_search_recursive(ordered_list, first_element, (mid_point-1), term)
        elif ordered_list[mid_point] < term:
            return binary_search_recursive(ordered_list, (mid_point+1), last_element, term)
        else:
            return mid_point


if __name__ == '__main__':

    import time

    print("-------- Binary Search Iterative --------")

    start_time_iter = time.time()

    list1 = list(range(0, 100000000, 10))

    search_term = 10
    index_pos = binary_search_iterative(list1, search_term)
    if index_pos is None:
        print(f"The data item {search_term} was not found.")
    else:
        print(f"The data item {search_term} was found at position {index_pos}.")

    list2 = ['book', 'data', 'packt', 'structure']

    search_term2 = 'structure'
    index_pos2 = binary_search_iterative(list2, search_term2)
    if index_pos2 is None:
        print(f"The data item '{search_term2}' was not found.")
    else:
        print(f"The data item '{search_term2}' was found at position {index_pos2}.")

    finish_time_iter = time.time() - start_time_iter

    print(f"Total time...: {round(finish_time_iter, 6)} seconds")

    print("\n-------- Binary Search Recursive --------")

    start_time_rec = time.time()

    list1 = list(range(0, 100000000, 10))

    search_term = 10
    index_pos = binary_search_recursive(list1, 0, len(list1)-1, search_term)
    if index_pos is None:
        print(f"The data item {search_term} was not found.")
    else:
        print(f"The data item {search_term} was found at position {index_pos}.")

    list2 = ['book', 'data', 'packt', 'structure']

    search_term2 = 'structure'
    index_pos2 = binary_search_recursive(list2, 0, len(list2)-1, search_term2)
    if index_pos2 is None:
        print(f"The data item '{search_term2}' was not found.")
    else:
        print(f"The data item '{search_term2}' was found at position {index_pos2}.")

    finish_time_rec = time.time() - start_time_rec

    print(f"Total time...: {round(finish_time_rec, 6)} seconds")


