def search_unordered(unordered_list, term):
    for i, item in enumerate(unordered_list):
        if term == item:
            return i
    return None

def search_ordered(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None
    return None

if __name__ == '__main__':

    print('------- Search Unordered -------')

    list1 = [60, 1, 88, 10, 11, 600]

    search_term = 10
    index_pos = search_unordered(list1, search_term)
    print(f"Index position of {search_term}: {index_pos}")

    list2 = ['packt', 'publish', 'data']
    search_term2 = 'data'
    index_pos2 = search_unordered(list2, search_term2)
    print(f"Index position of {search_term2}: {index_pos2}")

    print('\n------- Search Ordered -------')

    list3 = [2,3,4,6,7]

    search_term3 = 5
    index_pos3 = search_ordered(list3, search_term3)

    if index_pos3 is None:
        print(f"{search_term3} not found.")
    else:
        print(f"{search_term3} fount at position {index_pos3}")

    list4 = ['book', 'data', 'packt', 'structure']

    search_term4 = 'structure'
    index_pos4 = search_ordered(list4, search_term4)

    if index_pos4 is None:
        print(f"{search_term4} not found.")
    else:
        print(f"{search_term4} found at position {index_pos4}")