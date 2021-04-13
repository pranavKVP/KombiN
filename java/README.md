# KombiN - Java Library

This is the java implementation of KombiN, which is an algorithm to get index for combination pair and to get combination pair from index, where all possible combination pairs from two finite sets are sorted by their weight in ascending order.

## Installation

Available on [Maven Central](https://search.maven.org/search?q=g:ninja.pranav.algorithms%20AND%20a:kombin)

## Usage

where set 'A' has 100 elements and set 'B' has 80 elements and both sets has zerobased indexing.

```java

import ninja.pranav.algorithms.kombin;

// Initialize object of Table class
Table myObj = new Table(100, 80, true);

// Get Index value for combination pair(ai: 46, bi: 72)
long index = myObj.GetIndexOfElements(46, 72);

// Get combination pair from index value
Pair myPair = myObj.GetElementsAtIndex(index);

```
