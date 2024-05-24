def binary_search_recursive(ordered_list, first_element_idx, last_element_idx, term):
    if last_element_idx < first_element_idx:
        return None
    else:
        mid_point = first_element_idx + ((last_element_idx - first_element_idx)//2)
        if ordered_list[mid_point] == term:
            return mid_point
        elif ordered_list[mid_point] > term:
            return binary_search_recursive(ordered_list, first_element_idx, mid_point - 1, term)
        else:
            return binary_search_recursive(ordered_list, mid_point+1, last_element_idx, term)

def exponential_search(A, search_value):
    if (A[0] == search_value):
        return 0
    index = 1
    while index < len(A) and A[index] < search_value:
        index *= 2
    return binary_search_recursive(A, index//2, min(index, len(A)-1), search_value)

if __name__ == '__main__':
    print(exponential_search([1,2,3,4,5,6,7,8,9, 10, 11, 12, 34, 40], 34))