def great(list_range):

    l = [x for x in range(list_range)]
    # initializing an empty list
    y = []
    # iterate the list
    for item in l:
        # divide by 5
        if item%5 == 0:
            # if remainder equals 0, then add to the list
            y.append(item)
    return y


print great(10000)


    # divide by 2
    # if remainder equals 0, then add to the list
    # divide by 3
    # if remainder equals 0, then add to the list