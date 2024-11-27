# $reverseArray (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $reverseArray (aggregation) On this page Definition Behavior Example Definition $reverseArray Accepts an array expression as an argument and returns an array with the
elements in reverse order. $reverseArray has the following operator
expression syntax : { $reverseArray : < array expression > } The argument can be any valid expression as long as it resolves to an array. Behavior If  the argument resolves to a value of null or refers to a
missing field, $reverseArray returns null . If the argument does not resolve to an array or null nor refers
to a missing field, $reverseArray returns an error. $reverseArray returns an empty array when the argument is an empty array. If the argument contains subarrays, $reverseArray only operates on the top level array elements and will not reverse the contents of subarrays. Example [ 1 ] Results { $reverseArray : { $literal : [ 1 , 2 , 3 ] } } [ 3, 2, 1 ] { $reverseArray : { $slice : [ [ "foo" , "bar" , "baz" , "qux" ] , 1 , 2 ] } } } [ "baz", "bar" ] { $reverseArray : null } null { $reverseArray : { $literal : [ ] } } [ ] { $reverseArray : { $literal : [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ] } } [ [ 4, 5, 6 ], [ 1, 2, 3 ] ] [ 1 ] The examples in the table take a literal argument. To avoid parsing
ambiguity if the literal argument is an array, you must wrap the
literal array in a $literal expression or keep the
outer array that designates the argument list (e.g. [ [ 1, 2, 3 ]
] ) to pass in the literal array [1, 2, 3] . Example A collection named users contains the following documents: { "_id" : 1 , "name" : "dave123" , "favorites" : [ "chocolate" , "cake" , "butter" , "apples" ] } { "_id" : 2 , "name" : "li" , "favorites" : [ "apples" , "pudding" , "pie" ] } { "_id" : 3 , "name" : "ahn" , "favorites" : [ ] } { "_id" : 4 , "name" : "ty" } The following example returns an array containing the elements of
the favorites array in reverse order: db. users . aggregate ( [ { $project : { name : 1 , reverseFavorites : { $reverseArray : "$favorites" } } } ]) The operation returns the following results: { "_id" : 1 , "name" : "dave123" , "reverseFavorites" : [ "apples" , "butter" , "cake" , "chocolate" ] } { "_id" : 2 , "name" : "li" , "reverseFavorites" : [ "pie" , "pudding" , "apples" ] } { "_id" : 3 , "name" : "ahn" , "reverseFavorites" : [ ] } { "_id" : 4 , "name" : "ty" , "reverseFavorites" : null } Back $replaceAll Next $round
