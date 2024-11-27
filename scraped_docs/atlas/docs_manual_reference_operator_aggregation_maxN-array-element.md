# $maxN (array operator) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $maxN (array operator) On this page Definition Syntax Behavior Example Definition $maxN New in version 5.2 . Returns the n largest values in an array. Tip See also: $minN Syntax $maxN has the following syntax: { $maxN : { n : < expression > , input : < expression > } } Field Description n An expression that resolves to a
positive integer. The integer specifies the number of array elements
that $maxN returns. input An expression that resolves to the
array from which to return the maximal n elements. Behavior You cannot specify a value of n less than 1 . $maxN filters out null values found in the input array. If the specified n is greater than or equal to the number of elements
in the input array, $maxN returns all elements in the input array. If input resolves to a non-array value, the aggregation
operation errors. If input contains both numeric and string elements, the string elements
are sorted before numeric elements according to the BSON comparison order . Example Create a scores collection with the following documents: db. scores . insertMany ( [ { "playerId" : 1 , "score" : [ 1 , 2 , 3 ] } , { "playerId" : 2 , "score" : [ 12 , 90 , 7 , 89 , 8 ] } , { "playerId" : 3 , "score" : [ null ] } , { "playerId" : 4 , "score" : [ ] } { "playerId" : 5 , "score" : [ 1293 , "2" , 3489 , 9 ]} ]) The following example uses the $maxN operator to retrieve the two
highest scores for each player. The highest scores are returned in the new field maxScores created by $addFields . db. scores . aggregate ( [ { $addFields : { maxScores : { $maxN : { n : 2 , input : "$score" } } } } ]) The operation returns the following results: [ { "playerId" : 1 , "score" : [ 1 , 2 , 3 ] , "maxScores" : [ 3 , 2 ] } , { "playerId" : 2 , "score" : [ 12 , 90 , 7 , 89 , 8 ] , "maxScores" : [ 90 , 89 ] } , { "playerId" : 3 , "score" : [ null ] , "maxScores" : [ ] } , { "playerId" : 4 , "score" : [ ] , "maxScores" : [ ] } , { "playerId" : 5 , "score" : [ 1293 , "2" , 3489 , 9 ] , "maxScores" : [ "2" , 3489 ] }] Back $maxN Next $median
