def find(search_list, value):
    if len(search_list) > 0:
        search_list.sort()
        min_index = 0
        max_index = search_list.index(search_list[-1])
        while max_index >= min_index:
            mid_point = max_index - min_index // 2
            if value > search_list[mid_point]:
                min_index = mid_point + 1
            if value < search_list[mid_point]:
                max_index = mid_point - 1
            if value == search_list[mid_point]:
                return search_list.index(search_list[mid_point])
    raise ValueError("value not in array")
        
