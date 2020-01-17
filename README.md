# KombiN
KombiN is an algorithm that gives Index # of weighted combination and back, works with combinations of two finite sets ordered by sum and then by difference of combination, without generating and enumerating through possible combinations.
## When to use KombiN?
Let's say we have two sets:
> Set X = { Apple = 1, Banana = 2, Cucumber = 3 }

> Set Y = { CEO = 1, CFO = 2, CSO = 3 }

Now get all possible unique combinations for both sets and sort first by sum of combination and after by difference of combination and in the end give Index # to all combinations. See table below:

| Index # | X | Y | X+Y | X-Y |
| -- | -- | -- | -- | -- |
|1|1|1|2|0|
|2|1|2|3|-1|
|3|2|1|3|1|
|4|1|3|4|-2|
|5|2|2|4|0|
|6|3|1|4|2|
|7|2|3|5|-1|
|8|3|2|5|1|
|9|3|3|9|0|

You can use KombiN for
1. Finding the Index # of particular combination
2. Finding the Combination of particular Index #.
