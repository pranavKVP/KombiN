# Uses python3

# Get Abstract Values using length of two sets
def GetAbstract(lengthOfA: int, lengthOfB: int):
    lowerLength = lengthOfA if (lengthOfA < lengthOfB) else lengthOfB
    higherLength = lengthOfA if (lengthOfA > lengthOfB) else lengthOfB
    difference = higherLength - lowerLength
    product = higherLength * lowerLength
    sum = higherLength + lowerLength

    maxSumRange1 = lowerLength + 1
    maxSumRange2 = maxSumRange3 = maxIndexRange1 = maxIndexRange2 \
        = maxIndexRange3 = zeroLengthRange2 = zeroLengthRange3 = 0

    if(difference == 0):
        maxIndexRange1 = (product * maxSumRange1) // sum
    elif(difference == 1):
        maxIndexRange1 = product // 2
    elif(difference >= 2):
        maxSumRange2 = higherLength
        zeroLengthRange2 = 0 if (lengthOfA < lengthOfB) else lengthOfB
        maxIndexRange1 = (product - lowerLength * (sum - 1 - 2 * lowerLength)) // 2
        maxIndexRange2 = (product + lowerLength * (sum - 1 - 2 * lowerLength)) // 2

    if(product >= 2):
        maxSumRange3 = sum
        zeroLengthRange3 = lengthOfB
        maxIndexRange3 = product

    return maxSumRange1, maxSumRange2, maxSumRange3, \
        maxIndexRange1, maxIndexRange2, maxIndexRange3, \
        lowerLength, zeroLengthRange2, zeroLengthRange3
    

# Get Index value for given Combination pair
def GetIndex (Ai: int, Bi: int, lengthOfA: int, lengthOfB: int, zeroBasedIndex: bool) -> int:
    if(zeroBasedIndex):
        Ai += 1
        Bi += 1
    
    maxSumRange1, maxSumRange2, maxSumRange3, maxIndexRange1, \
        maxIndexRange2, maxIndexRange3, lowerLength, zeroLengthRange2, \
        zeroLengthRange3 = GetAbstract(lengthOfA, lengthOfB)

    Index = 0, previousIndex
    Sum = Ai + Bi
    
    if(Sum <= maxSumRange1):
        previousIndex = Sum - 2
        Index = (previousIndex // 2) * (previousIndex + 1) if (previousIndex % 2 == 0) else (((previousIndex - 1) // 2) * previousIndex) + previousIndex
        Index += Ai
    elif(Sum <= maxSumRange2):
        Index = maxIndexRange1 \
            + ((Sum - (maxSumRange1 + 1)) * lowerLength) \
            + Ai if (zeroLengthRange2 == 0) else (zeroLengthRange2 + 1) - Bi
    elif(Sum <= maxSumRange3):
        Index = maxIndexRange1 if (maxIndexRange2 == 0) else maxIndexRange2
        previousIndex = maxSumRange3 - Sum + 1
        Index += maxIndexRange3 \
            - maxIndexRange1 if (maxIndexRange2 == 0) else maxIndexRange2 \
            - (previousIndex // 2) * (previousIndex + 1) if (previousIndex % 2 == 0) \
           else (((previousIndex - 1) // 2) * previousIndex) + previousIndex
        Index += Ai if (zeroLengthRange3 == 0) else (zeroLengthRange3 + 1) - Bi
    
    if (zeroBasedIndex):
        Index -= 1
    return Index

# 