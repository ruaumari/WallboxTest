import pytest
from CoinFlipsPermutations import minNecessaryPermutations

def test_TC_BadCase_ImpossibleSequence():
    exceptionCatch = False
    flipsSequence = [1, 1, 1, 1]
    try:
         minNecessaryPermutations(flipsSequence)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    exceptionCatch = False
    flipsSequence = [1, 0, 1, 1]
    try:
         minNecessaryPermutations(flipsSequence)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_BadCase_InvalidSequenceValue():
    exceptionCatch = False
    flipsSequence = [1, 0, 1, 0, 3]
    try:
         minNecessaryPermutations(flipsSequence)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    exceptionCatch = False
    flipsSequence = [1, 0, "1", 0]
    try:
         minNecessaryPermutations(flipsSequence)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

    exceptionCatch = False
    flipsSequence = [1, 0, 1, 0, 10]
    try:
         minNecessaryPermutations(flipsSequence)
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_GoodCases():
    flipsSequence = [1, 1, 0, 0]
    minPerm = minNecessaryPermutations(flipsSequence)
    assert (minPerm == 1)

    flipsSequence = [1, 1, 0, 0, 1]
    minPerm = minNecessaryPermutations(flipsSequence)
    assert (minPerm == 1)

    flipsSequence = [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    minPerm = minNecessaryPermutations(flipsSequence)
    assert (minPerm == 3)
