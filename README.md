# KombiN

[![Maven Central](https://img.shields.io/maven-central/v/ninja.pranav.algorithms/kombin.svg?label=Maven%20Central)](https://search.maven.org/search?q=g:%22ninja.pranav.algorithms%22%20AND%20a:%22kombin%22)
![Nuget](https://img.shields.io/nuget/v/Ninja.Pranav.Algorithms.Kombin)

KombiN is an algorithm that gives Index # of weighted combination and back, works with combinations of two finite sets ordered by sum and then by difference of combination, without generating and enumerating through possible combinations.
## When to use KombiN?
Let's say we have two sets:
> Set X = { Apple = 0, Banana = 1, Cucumber = 2 }

> Set Y = { CEO = 0, CFO = 1, CSO = 2 }

Now get all possible unique combinations for both sets and sort first by sum of combination and after by difference of combination and in the end give Index # to all combinations.

In above example, both sets have zero-based index so KombiN will have output as shown in left side Table below. For example, both sets are in DataTable with Non-zero index, In that case KombiN will have output as shown in right side Table below.

In short, It provides zero and non-zero index based on type of index used in both sets.

| Index # | X | Y |  | | Index # | X | Y |
| -- | -- | -- | -- | -- | -- | -- | -- |
|0|0|0|                      | |1|1|1|
|1|0|1|                     | |2|1|2|
|2|1|0|                      | |3|2|1|
|3|0|2|                     | |4|1|3|
|4|1|1|                      | |5|2|2|
|5|2|0|                      | |6|3|1|
|6|1|2|                     | |7|2|3|
|7|2|1|                      | |8|3|2|
|8|2|2|                      | |9|3|3|

You can use KombiN for
1. Finding the Index # of particular combination
2. Finding the Combination of particular Index #.
