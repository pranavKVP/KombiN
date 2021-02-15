# KombiN - JavaScript Library with built-in TypeScript declarations

This is the TypeScript implementation of KombiN, which is an algorithm to get index for combination pair and to get combination pair from index, where all possible combination pairs from two finite sets are sorted by their weight in ascending order.

## Installation

Available on [npm](https://www.npmjs.com/package/@pranav.ninja/algorithms-kombin)

```diff
npm i @pranav.ninja/algorithms-kombin
```

## Usage

where set 'A' has 100 elements and set 'B' has 80 elements and both sets has zerobased indexing.

```js
// Initialize object of Table class
let myObj = new Table(100, 80, true);

// Get Index value for combination pair(ai: 46, bi: 72)
let index = myObj.GetIndexOfElements(46, 72);

// Get combination pair from index value
let [ai, bi] = myObj.GetElementsAtIndex(index);

```
