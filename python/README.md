# KombiN - Python 3 Library

This is the python implementation of KombiN, which is an algorithm to get index for combination pair and to get combination pair from index, where all possible combination pairs from two finite sets are sorted by their weight in ascending order.

## Installation

Available on [pypi](https://pypi.org/project/kombin/)

```diff
pip install kombin
```

## Usage

where set 'A' has 100 elements and set 'B' has 80 elements and both sets has zerobased indexing.

```py
from kombin import Table

# Initialize object of Table class
myObj = Table(100, 80, true)

# Get Index value for combination pair(ai: 46, bi: 72)
index = myObj.GetIndexOfElements(46, 72)

# Get combination pair from index value
ai, bi = myObj.GetElementsAtIndex(index);

```
