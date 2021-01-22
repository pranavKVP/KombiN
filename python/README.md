# KombiN
This is the python implementation of KombiN, which is an algorithm to get index for pair of combination or to get pair of combination from index, where all possible pairs of combination from two finite sets are sorted by their weight in ascending order.

## Installation:
````
pip install KombiN
````

## Usage:
##### *where set 'A' has 100 elements and set 'B' has 80 elements and both sets has zerobased indexing*.
````
from KombiN.KombiN import KombiN


myObj = KombiN(100, 80, True)

# Get Index value for pair of combination(Ai: 46, Bi: 72)
index = myObj.GetIndex(46, 72)

# Get pair of combination from index value
Ai, Bi = myObj.GetCombination(index)

````
