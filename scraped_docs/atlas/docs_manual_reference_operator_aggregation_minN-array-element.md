# $minN (array operator) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $minN (array operator) On this page Definition Syntax Behavior Example Definition $minN New in version 5.2 . Returns the n smallest values in an array. Tip See also: $maxN Syntax $minN has the following syntax: { $minN : { n : < expression > , input : < expression > } } Field Description n An expression that resolves to a
positive integer. The integer specifies the number of array elements
that $minN returns. input An expression that resolves to the
array from which to return the minimal n elements. Behavior You cannot specify a value of n less than 1 . $minN filters out null values found in the input array. If the specified n is greater than or equal to the number of elements
in the input array, $minN returns all elements in the input array. If input resolves to a non-array value, the aggregation
operation errors. If input contains both numeric and string elements, the numeric elements
are sorted before string elements according to the BSON comparison order . Example Create a scores collection with the following documents: db. scores . insertMany ( [ { "playerId" : 1 , "score" : [ 1 , 2 , 3 ] } , { "playerId" : 2 , "score" : [ 12 , 90 , 7 , 89 , 8 ] } , { "playerId" : 3 , "score" : [ null ] } , { "playerId" : 4 , "score" : [ ] } , { "playerId" : 5 , "score" : [ 1293 , "2" , 3489 , 9 ]} ]) The following example uses the $minN operator to retrieve the two
lowest scores for each player. The lowest scores are returned in the new field minScores created by $addFields . db. scores . aggregate ( [ { $addFields : { minScores : { $minN : { n : 2 , input : "$score" } } } } ]) The operation returns the following results: [ { "playerId" : 1 , "score" : [ 1 , 2 , 3 ] , "minScores" : [ 1 , 2 ] } , { "playerId" : 2 , "score" : [ 12 , 90 , 7 , 89 , 8 ] , "minScores" : [ 7 , 8 ] } , { "playerId" : 3 , "score" : [ null ] , "minScores" : [ ] } , { "playerId" : 4 , "score" : [ ] , "minScores" : [ ] } , { "playerId" : 5 , "score" : [ 1293 , "2" , 3489 , 9 ] , "minScores" : [ 9 , 1293 ] }] Back $minN Next $millisecond
