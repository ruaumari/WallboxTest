def minNecessaryPermutations(flipsSequence):
    """This function returns the minimum number of permutations on a list of flip results
       that makes possible the creation of a list with an interspersed pattern.

    Parameters:
    flipsSequence (list): List with flips results (possible values: 1-tail 0-head).

    Returns:
    int:The minimum number of permutations.

   """
    tailAsFirstValueSequence = 0
    headAsFirstValueSequence = 1
    sequenceTailsHeadPerm = 0
    sequenceHeadTailsPerm = 0
    totalTails = flipsSequence.count(tailAsFirstValueSequence)
    totalHeads = flipsSequence.count(headAsFirstValueSequence)
    flipResultsDiff = totalTails - totalHeads

    if ((flipResultsDiff > 1) or (flipResultsDiff < -1)):
        raise Exception("It is impossible to generate an interspersed sequence.")
    if ((totalTails + totalHeads) < len(flipsSequence)):
        raise Exception("List contain an invalid flip value.")
    for flip in flipsSequence:
        if (flip == tailAsFirstValueSequence):
            sequenceHeadTailsPerm += 1
            tailAsFirstValueSequence = headAsFirstValueSequence
            headAsFirstValueSequence = flip
        elif (flip == headAsFirstValueSequence):
            sequenceTailsHeadPerm += 1
            headAsFirstValueSequence = tailAsFirstValueSequence
            tailAsFirstValueSequence = flip

    if((sequenceHeadTailsPerm % 2) != 0):
        return (sequenceTailsHeadPerm / 2)
    elif((sequenceTailsHeadPerm % 2) != 0):
        return (sequenceHeadTailsPerm / 2)
    else:
        sequenceHeadTailsPerm /= 2
        sequenceTailsHeadPerm /= 2
        return min(sequenceHeadTailsPerm, sequenceHeadTailsPerm)