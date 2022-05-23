import pytest
from FirstRepeated import firstRepeatedInt

def test_TC_BadCase_NoIntegerRepeated():
    firstList = [1, 2, 3, 4, 5]
    secondList = [6, 7, 8]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_BadCase_NonIntegerValue():
    firstList = [1, 2, 3.3, 4, 5]
    secondList = [1, 2, 3, 4, 5]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    firstList = [1, 2, 3, 4, 5]
    secondList = [1, 2, 3.3, 4, 5]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    firstList = [1, 2, 3, 4, 5]
    secondList = [1, 2, True, 4, 5]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    firstList = [1, 2, True, 4, 5]
    secondList = [1, 2, 3, 4, 5]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    firstList = [1, 2, 3, 4, 5]
    secondList = [1, 2, "1", 4, 5]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    firstList = [1, 2, "1", 4, 5]
    secondList = [1, 2, 3, 4, 5]
    exceptionCatch = False
    try:
         firstRepeatedInt(firstList, secondList)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_GoodCase_Minimum_Index_Bound():
    firstList = [1]
    secondList = [1, 2, 3, 1, 5]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 1

    secondList = [6, 1, 18]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 1

    firstList = [7, 6, 3, 4, 5]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 6

    firstList = [6, 2]
    secondList = [7, 2, 3, 4, 2]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 2

def test_TC_GoodCase_Nominal_Index_Bound():
    firstList = [1, 2, 3, 4, 5, 11, 22, 33, 44]
    secondList = [6, 7, 1, 8, 9]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 1

    firstList = [6, 7, 2, 8, 9, 10, 11]
    secondList = [2, 1, 3, 4, 5]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 2

    firstList = [1, 2, 3, 4, 5, 11, 22, 33, 44]
    secondList = [6, 7, 44, 8, 9]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 44

    firstList = [9, 7, 6, 8, 5]
    secondList = [2, 1, 3, 4, 10, 11, 6]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 6
 
    firstList = [0, 3, 2, 1, 4, 18]
    secondList = [5, 6, 3, 7, 8, 10, 9]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 3

    firstList = [0, 9, 2, 1, 4, 44]
    secondList = [5, 6, 9, 7, 8]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 9

    firstList = [0, 1, 3, 4, 2, 72, 9, 4]
    secondList = [5, 6, 3, 7, 8, 32]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 3

def test_TC_GoodCase_Maximum_Index_Bound():
    firstList = [1, 2, 3, 4, 5]
    secondList = [6, 7, 5]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 5

    firstList = [6, 7, 2, 8, 9, 10, 14]
    secondList = [22, 1, 3, 4, 10]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 10

    firstList = [0, 13, 4, -1]
    secondList = [5, 6, 3, -1, 8]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == -1

    firstList = [0, 1, 2, 9, 4]
    secondList = [5, 6, 7, 9, 8]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 9

def test_TC_GoodCase_Priority():
    firstList = [1, 2, 3, 4, 5]
    secondList = [2, 1, 5]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 1

    firstList = [3, 1, 3, 4, 5]
    secondList = [6, 5, 4]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 4

    firstList = [3, 6, 5, 7, 8]
    secondList = [6, 5, 6, 4]
    firstRepeatedNumber = firstRepeatedInt(firstList, secondList)
    assert firstRepeatedNumber == 6