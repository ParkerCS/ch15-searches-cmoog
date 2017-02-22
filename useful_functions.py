def binary_search(search_term, input_list):
    key = search_term.upper()
    lower_bound = 0
    upper_bound = len(input_list) - 1
    found = False
    # loop until we find item or the bounds meet
    while lower_bound <= upper_bound and not found:
        # find the middle
        middle_position = (lower_bound + upper_bound) // 2
        # figure out if we need to move up or down
        if input_list[middle_position] < key:
            lower_bound = middle_position + 1
        elif input_list[middle_position] > key:
            upper_bound = middle_position - 1
        else:
            found = True
    return found, 