def firstRepeatedInt(firstList, secondList):
    """This function returns the first integer repeated on these lists.

    Parameters:
    firstList (list): First compared list (vector).
    secondList (list):Second compared list (vector).

    Returns:
    int:The first repeated value.

   """
    indexSum = -1
    currentIndexSum = -1
    secondListIndex = 0
    firstRepeatedNumber = -1
    currentFirstListValue = 0

    if not all(map(lambda listItem: (isinstance(listItem, int) and not isinstance(listItem, bool)), firstList)):
        raise Exception("The first input list contains a non-integer value.")
    elif not all(map(lambda listItem: (isinstance(listItem, int) and not isinstance(listItem, bool)), secondList)):
        raise Exception("The second input list contains a non-integer value.")

    for firstListIndex in range(len(firstList)):
        currentFirstListValue = firstList[firstListIndex]
        try:
            secondListIndex = secondList.index(currentFirstListValue)
            currentIndexSum = firstListIndex + secondListIndex
        except ValueError:
            continue
        if ((secondListIndex != -1) and ((indexSum > currentIndexSum) or (indexSum == -1))):
            indexSum = currentIndexSum
            firstRepeatedNumber = currentFirstListValue

    if (indexSum != -1):
        print("The first repeated element of these lists is %d." % firstRepeatedNumber)
    else:
        raise Exception("There is not any repeted element between these lists.")
    return firstRepeatedNumber