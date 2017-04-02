def great(list_range):

    l = [x for x in range(list_range)]
    # initializing an empty list
    y = []
    # iterate the list
    for item in l:
        # divide by 5
        if item == 0:
            continue
        if item%5 == 0:
            # if remainder equals 0, then add to the list
            y.append(item)
            continue
        if item%3 == 0:
            y.append(item)
            continue
        if item%2 == 0:
            y.append(item)
    return y


print great(51)


    # divide by 2
    # if remainder equals 0, then add to the list
    # divide by 3
    # if remainder equals 0, then add to the list