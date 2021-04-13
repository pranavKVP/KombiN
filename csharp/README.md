# KombiN - DotNet Library

This is the C# implementation of KombiN, which is an algorithm to get index for combination pair and to get combination pair from index, where all possible combination pairs from two finite sets are sorted by their weight in ascending order.

## Installation

Available on [NuGet](https://www.nuget.org/packages/Ninja.Pranav.Algorithms.Kombin)

## Usage

where set 'A' has 100 elements and set 'B' has 80 elements and both sets has zerobased indexing.

```cs

using Ninja.Pranav.Algorithms.Kombin;

// Initialize object of Table class
Table myObj = new Table(100, 80, true);

// Get Index value for combination pair(ai: 46, bi: 72)
long index = myObj.GetIndexOfElements(46, 72);

// Get combination pair from index value
long ai, bi;
(ai, bi) = myObj.GetElementsAtIndex(index);

```
