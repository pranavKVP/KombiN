# Copyright (c) 2020 Pranavkumar Patel. All rights reserved. Licensed under the MIT license.

import math


class Table:
    """
    Provides a methods to get index of combination pair
    and to get combination pair from index value.
    """
    def __init__(self, lengthOfA: int, lengthOfB: int, zeroBasedIndex: bool):
        """
        Args:
            lengthOfA: Number of elements in first set.
            lengthOfB: Number of elements in second set.
            zeroBasedIndex: True if sets index starts with zero otherwise False.

        Returns:
            Table object.

        Raises:
            ValueError: if lengthOfA or lengthOfB is 0 or less.
        """
        if (lengthOfA < 1 or lengthOfB < 1):
            raise ValueError("Length of both sets must be grater than 0.")

        self._LengthOfA = lengthOfA
        self._LengthOfB = lengthOfB
        self._ZeroBasedIndex = zeroBasedIndex
        self._LowerLength = 0
        self._MaxSumRange1 = self._MaxSumRange2 = self._MaxSumRange3 = 0
        self._MaxIndexRange1 = self._MaxIndexRange2 = self._MaxIndexRange3 = 0
        self._Abstract()

    def _Abstract(self) -> None:
        """
        Sets an abstract values useful to get index and combination pair.
        """
        self._LowerLength = self._LengthOfA if (self._LengthOfA < self._LengthOfB) else self._LengthOfB
        higherLength = self._LengthOfA if (self._LengthOfA > self._LengthOfB) else self._LengthOfB
        difference = higherLength - self._LowerLength
        product = higherLength * self._LowerLength
        sum = higherLength + self._LowerLength
        self._MaxSumRange1 = self._LowerLength + 1
        if(difference == 0):
            self._MaxIndexRange1 = (product * self._MaxSumRange1) // sum
        elif(difference == 1):
            self._MaxIndexRange1 = product // 2
        elif(difference >= 2):
            self._MaxSumRange2 = higherLength
            self._MaxIndexRange1 = (product - self._LowerLength * (sum - 1 - 2 * self._LowerLength)) // 2
            self._MaxIndexRange2 = (product + self._LowerLength * (sum - 1 - 2 * self._LowerLength)) // 2

        if(product >= 2):
            self._MaxSumRange3 = sum
            self._MaxIndexRange3 = product

    def GetIndexOfElements(self, ai: int, bi: int) -> int:
        """Get index value for the combination pair.

        Args:
            ai: Element index of set A.
            ai: Element index of set B.

        Returns:
            Index value for the given combination pair.

        Raises:
            ValueError: if ai or bi has invalid value.
        """
        if(self._ZeroBasedIndex):
            if(ai < 0 or bi < 0):
                raise ValueError("Both element index values must be 0 or more.")
            ai += 1
            bi += 1
        elif(ai < 1 or bi < 1):
            raise ValueError("Both element index values must be 1 or more.")

        index = 0
        previousIndex = 0
        sum = ai + bi

        if(sum <= self._MaxSumRange1):
            previousIndex = sum - 2
            index = ((previousIndex // 2) * (previousIndex + 1) if (previousIndex % 2 == 0) else \
                     (((previousIndex - 1) // 2) * previousIndex) + previousIndex) \
                + ai
        elif(sum <= self._MaxSumRange2):
            index = self._MaxIndexRange1 \
                + ((sum - (self._MaxSumRange1 + 1)) * self._LowerLength) \
                + (ai if (self._LengthOfA < self._LengthOfB) else (self._LengthOfB + 1) - bi)
        elif(sum <= self._MaxSumRange3):
            previousIndex = self._MaxSumRange3 - sum + 1
            index = self._MaxIndexRange3 \
                - ((previousIndex // 2) * (previousIndex + 1) if (previousIndex % 2 == 0) else \
                   (((previousIndex - 1) // 2) * previousIndex) + previousIndex) \
                + (ai if (self._MaxIndexRange3 < 2) else (self._LengthOfB + 1) - bi)
        else:
            raise ValueError(f"Sum of both the element index values must not be greater than {self._MaxSumRange3}")

        if (self._ZeroBasedIndex):
            index -= 1

        return index

    def GetElementsAtIndex(self, index: int):
        """Get the combination pair for given index value.

        Args:
            index: Index value of combination pair.

        Returns:
            combination pair

        Raises:
            ValueError: if index has invalid value.
        """
        if (self._ZeroBasedIndex):
            if (index < 0):
                raise ValueError("Index value must be 0 or more.")
            index += 1
        elif (index < 1):
            raise ValueError("Index value must be 1 or more.")

        ai: int = 0
        bi: int = 0
        previousIndex: int
        sum: int

        if (index <= self._MaxIndexRange1):
            sum = math.ceil((math.sqrt(index * 8 + 1) + 1) / 2)
            ai = index - ((sum - 1) * (sum - 2) // 2)
            bi = sum - ai
        elif (index <= self._MaxIndexRange2):
            sum = self._MaxSumRange1 \
                + ((index - self._MaxIndexRange1) // self._LowerLength) \
                - (1 if ((index - self._MaxIndexRange1) % self._LowerLength == 0) else 0) \
                + 1
            previousIndex = self._MaxIndexRange1 + ((sum - 1 - self._MaxSumRange1) * self._LowerLength)
            if (self._LengthOfA >= self._LengthOfB):
                bi = (self._LengthOfB + 1) - (index - previousIndex)
                ai = sum - bi
            else:
                ai = index - previousIndex
                bi = sum - ai
        elif (index <= self._MaxIndexRange3):
            generic_MaxSumRange3 = self._MaxSumRange3 \
                - (self._MaxSumRange1 if self._MaxSumRange2 == 0 else self._MaxSumRange2)
            generic_Index = index \
                - (self._MaxIndexRange1 if self._MaxIndexRange2 == 0 else self._MaxIndexRange2)
            b = (2 * generic_MaxSumRange3) + 1
            generic_Sum = math.ceil((b - math.sqrt(b * b - 8 * generic_Index)) / 2)
            sum = (self._MaxSumRange1 if self._MaxSumRange2 == 0 else self._MaxSumRange2) \
                + generic_Sum
            previousIndex = (self._MaxIndexRange1 if self._MaxIndexRange2 == 0 else self._MaxIndexRange2) \
                + (0 if generic_Sum == 1 else (((generic_Sum - 1) * (b - generic_Sum + 1)) // 2))
            if (self._MaxIndexRange3 >= 2):
                bi = (self._LengthOfB + 1) - (index - previousIndex)
                ai = sum - bi
            else:
                ai = index - previousIndex
                bi = sum - ai
        else:
            raise ValueError(f"Index value must not be greater than {self._MaxIndexRange3}")

        if (self._ZeroBasedIndex):
            ai -= 1
            bi -= 1

        return ai, bi
