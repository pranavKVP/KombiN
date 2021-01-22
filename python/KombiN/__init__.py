"""KombiN is an algorithm to get index for pair of combination or
to get pair of combination from index, where all possible pairs
of combination from two finite sets are sorted by their weight
in ascending order.

Usage:

"""


import math


class KombiN:

    def __init__(self, lengthOfA: int, lengthOfB: int, zeroBasedIndex: bool):
        """Initializes KombiN object.

        Args:
            lengthOfA: Number of elements in first set.
            lengthOfB: Number of elements in second set.
            zeroBasedIndex: True if sets index starts with zero otherwise False.
        """
        if (lengthOfA < 1 or lengthOfB < 1):
            raise ValueError("Length of both sets must be grater than 0.")

        self._lengthOfA = lengthOfA
        self._lengthOfB = lengthOfB
        self._zeroBasedIndex = zeroBasedIndex

        self._lowerLength, self._maxSumRange1, self._maxSumRange2, self._maxSumRange3, \
            self._maxIndexRange1, self._maxIndexRange2, self._maxIndexRange3 = self._Abstract(lengthOfA, lengthOfB)

    def _Abstract(self, lengthOfA: int, lengthOfB: int):
        """Get an abstract values useful to get index and pair of combination.

        Args:
            lengthOfA: Number of elements in first set.
            lengthOfB: Number of elements in second set.

        Returns:
            lowerLength: Lower value from lengthOfA and lengthOfB.
            maxSumRange1: Maximum value of Sum in range 1.
            maxSumRange2: Maximum value of Sum in range 2.
            maxSumRange3: Maximum value of Sum in range 3.
            maxIndexRange1: Maximum value of Index in range 1.
            maxIndexRange2: Maximum value of Index in range 2.
            maxIndexRange3: Maximum value of Index in range 3.
        """
        lowerLength = lengthOfA if (lengthOfA < lengthOfB) else lengthOfB
        higherLength = lengthOfA if (lengthOfA > lengthOfB) else lengthOfB
        difference = higherLength - lowerLength
        product = higherLength * lowerLength
        sum = higherLength + lowerLength

        maxSumRange1 = lowerLength + 1
        maxSumRange2 = maxSumRange3 = maxIndexRange1 = maxIndexRange2 \
            = maxIndexRange3 = 0

        if(difference == 0):
            maxIndexRange1 = (product * maxSumRange1) // sum
        elif(difference == 1):
            maxIndexRange1 = product // 2
        elif(difference >= 2):
            maxSumRange2 = higherLength
            maxIndexRange1 = (product - lowerLength * (sum - 1 - 2 * lowerLength)) // 2
            maxIndexRange2 = (product + lowerLength * (sum - 1 - 2 * lowerLength)) // 2

        if(product >= 2):
            maxSumRange3 = sum
            maxIndexRange3 = product

        return lowerLength, maxSumRange1, maxSumRange2, maxSumRange3, \
            maxIndexRange1, maxIndexRange2, maxIndexRange3

    def GetIndex(self, Ai: int, Bi: int) -> int:
        """Get index value for the pair of combination.

        Args:
            Ai: Element index of set A.
            Bi: Element index of set B.

        Returns:
            Index: Index value for the given pair of combination.
        """
        if(self._zeroBasedIndex):
            if(Ai < 0 or Bi < 0):
                raise ValueError("Both element index values must be 0 or more.")
            Ai += 1
            Bi += 1
        else:
            if(Ai < 1 or Bi < 1):
                raise ValueError("Both element index values must be 1 or more.")

        Index = 0
        previousIndex = 0
        Sum = Ai + Bi

        if(Sum <= self._maxSumRange1):
            previousIndex = Sum - 2
            Index = ((previousIndex // 2) * (previousIndex + 1) if (previousIndex % 2 == 0) else \
                     (((previousIndex - 1) // 2) * previousIndex) + previousIndex) \
                + Ai
        elif(Sum <= self._maxSumRange2):
            Index = self._maxIndexRange1 \
                + ((Sum - (self._maxSumRange1 + 1)) * self._lowerLength) \
                + (Ai if (self._lengthOfA < self._lengthOfB) else (self._lengthOfB + 1) - Bi)
        elif(Sum <= self._maxSumRange3):
            previousIndex = self._maxSumRange3 - Sum + 1
            Index = self._maxIndexRange3 \
                - ((previousIndex // 2) * (previousIndex + 1) if (previousIndex % 2 == 0) else \
                   (((previousIndex - 1) // 2) * previousIndex) + previousIndex) \
                + (Ai if (self._maxIndexRange3 < 2) else (self._lengthOfB + 1) - Bi)
        else:
            raise ValueError(f"Sum of both the element index values must not be greater than {self._maxSumRange3}")

        if (self._zeroBasedIndex):
            Index -= 1

        return Index

    def GetCombination(self, index: int):
        """Get the pair of combination for given index value

        Args:
            index: Index value of pair of combination.

        Returns:
            Ai: Element index of set A.
            Bi: Element index of set B.
        """
        if (self._zeroBasedIndex):
            if (index < 0):
                raise ValueError("Index value must be 0 or more.")
            index += 1
        else:
            if (index < 1):
                raise ValueError("Index value must be 1 or more.")

        Ai: int = 0
        Bi: int = 0
        previousIndex: int
        Sum: int

        if (index <= self._maxIndexRange1):
            Sum = math.ceil((math.sqrt(index * 8 + 1) + 1) / 2)
            Ai = index - ((Sum - 1) * (Sum - 2) // 2)
            Bi = Sum - Ai
        elif (index <= self._maxIndexRange2):
            Sum = self._maxSumRange1 \
                + ((index - self._maxIndexRange1) // self._lowerLength) \
                - (1 if ((index - self._maxIndexRange1) % self._lowerLength == 0) else 0) \
                + 1
            previousIndex = self._maxIndexRange1 + ((Sum - 1 - self._maxSumRange1) * self._lowerLength)
            if (self._lengthOfA >= self._lengthOfB):
                Bi = (self._lengthOfB + 1) - (index - previousIndex)
                Ai = Sum - Bi
            else:
                Ai = index - previousIndex
                Bi = Sum - Ai
        elif (index <= self._maxIndexRange3):
            generic_maxSumRange3 = self._maxSumRange3 \
                - (self._maxSumRange1 if self._maxSumRange2 == 0 else self._maxSumRange2)
            generic_index = index \
                - (self._maxIndexRange1 if self._maxIndexRange2 == 0 else self._maxIndexRange2)
            b = (2 * generic_maxSumRange3) + 1
            generic_Sum = math.ceil((b - math.sqrt(b * b - 8 * generic_index)) / 2)
            Sum = (self._maxSumRange1 if self._maxSumRange2 == 0 else self._maxSumRange2) \
                + generic_Sum
            previousIndex = (self._maxIndexRange1 if self._maxIndexRange2 == 0 else self._maxIndexRange2) \
                + (0 if generic_Sum == 1 else (((generic_Sum - 1) * (b - generic_Sum + 1)) // 2))
            if (self._maxIndexRange3 >= 2):
                Bi = (self._lengthOfB + 1) - (index - previousIndex)
                Ai = Sum - Bi
            else:
                Ai = index - previousIndex
                Bi = Sum - Ai
        else:
            raise ValueError(f"Index value must not be greater than {self._maxIndexRange3}")

        if (self._zeroBasedIndex):
            Ai -= 1
            Bi -= 1

        return Ai, Bi
