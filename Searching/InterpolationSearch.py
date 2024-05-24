def nearest_mid(input_list, low_index, upper_index, search_value):
    mid = low_index + ((upper_index - low_index)/(input_list[upper_index] - input_list[
        low_index])) * (search_value - input_list[low_index])
    return int(mid)

def interpolation_search(ordered_list, search_value):
    low_index = 0
    upper_index = len(ordered_list) - 1
    while low_index <= upper_index:
        mid_point = nearest_mid(ordered_list, low_index, upper_index, search_value)
        if mid_point > upper_index or mid_point < low_index:
            return None
        if ordered_list[mid_point] == search_value:
            return mid_point
        elif ordered_list[mid_point] < search_value:
            low_index = mid_point + 1
        else:
            upper_index = mid_point - 1
    if low_index > upper_index:
        return None


if __name__ == '__main__':
    list1 = [44, 60, 75, 100, 120, 230, 250]
    a = interpolation_search(list1, 120)
    print(f"Index position of value 120 is...: {a}")