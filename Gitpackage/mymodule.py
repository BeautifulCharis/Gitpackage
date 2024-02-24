def top_n (items, n):
    """Return the top n items in an array, in desc order

    Arg
        items(array): list or array-like object
        n (int): num of item to return

    Return:
        array:top n items, in desc order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,3]
    
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-1):
            if items[j] > item [j +1]: # if this item is bigger than next time..
                items[j],  item [j +1] = item [j +1], items[j] # swap the two

    # get last two items
    top_n = items[-n:]
    # return in descending order
    return top_n[:: -1]
                