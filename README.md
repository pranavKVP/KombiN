# KombiN
KombiN is an algorithm that gives Index # of weighted combination and back, works with combinations of two finite sets ordered by sum and then by difference of combination, without generating and enumerating through possible combinations.
## When to use KombiN?
Let's say we have two sets:
> Set X = { Apple = 0, Banana = 1, Cucumber = 2 }

> Set Y = { CEO = 0, CFO = 1, CSO = 2 }

Now get all possible unique combinations for both sets and sort first by sum of combination and after by difference of combination and in the end give Index # to all combinations.

In above example, both sets have zero-based index so KombiN will have output as shown in left side Table below. For example, both sets are in DataTable with Non-zero index, In that case KombiN will have output as shown in right side Table below.

In short, It provides zero and non-zero index based on type of index used in both sets.

| Index # | X | Y | X+Y | X-Y |  | | Index # | X | Y | X+Y | X-Y |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|0|0|0|0|0|                      | |1|1|1|2|0|
|1|0|1|1|-1|                     | |2|1|2|3|-1|
|2|1|0|1|1|                      | |3|2|1|3|1|
|3|0|2|2|-2|                     | |4|1|3|4|-2|
|4|1|1|2|0|                      | |5|2|2|4|0|
|5|2|0|2|2|                      | |6|3|1|4|2|
|6|1|2|3|-1|                     | |7|2|3|5|-1|
|7|2|1|3|1|                      | |8|3|2|5|1|
|8|2|2|4|0|                      | |9|3|3|9|0|

You can use KombiN for
1. Finding the Index # of particular combination
2. Finding the Combination of particular Index #.
