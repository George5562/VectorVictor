# $slice (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $slice (aggregation) On this page Definition Behavior Example Definition $slice Returns a subset of an array. $slice has one of two syntax forms: The following syntax returns elements from either the start or end
of the array: { $slice : [ < array > , < n > ] } The following syntax returns elements from the specified position in
the array: { $slice : [ < array > , < position > , < n > ] } Operand Description <array> Any valid expression as long as
it resolves to an array. <position> Optional. Any valid expression as long
as it resolves to an integer. If positive, $slice determines the starting position from
the start of the array. If <position> is greater than the number of
elements, the $slice returns an empty array. If negative, $slice determines the starting position from
the end of the array. If the absolute value of the <position> is
greater than the number of elements, the starting position is the start
of the array. <n> Any valid expression as long as it
resolves to an integer. If <position> is specified, <n> must
resolve to a positive integer. If positive, $slice returns up to the first n elements in the array. If the <position> is specified, $slice returns the first n elements starting from the
position. If negative, $slice returns up to the last n elements
in the array. n cannot resolve to a negative number if <position> is specified. For more information on expressions, see Expression Operators . Behavior Example Results { $slice : [ [ 1 , 2 , 3 ] , 1 , 1 ] } [ 2 ] { $slice : [ [ 1 , 2 , 3 ] , - 2 ] } [ 2 , 3 ] { $slice : [ [ 1 , 2 , 3 ] , 15 , 2 ] } [ ] { $slice : [ [ 1 , 2 , 3 ] , - 15 , 2 ] } [ 1 , 2 ] Example A collection named users contains the following documents: { "_id" : 1 , "name" : "dave123" , favorites : [ "chocolate" , "cake" , "butter" , "apples" ] } { "_id" : 2 , "name" : "li" , favorites : [ "apples" , "pudding" , "pie" ] } { "_id" : 3 , "name" : "ahn" , favorites : [ "pears" , "pecans" , "chocolate" , "cherries" ] } { "_id" : 4 , "name" : "ty" , favorites : [ "ice cream" ] } The following example returns at most the first three elements in the favorites array for each user: db. users . aggregate ( [ { $project : { name : 1 , threeFavorites : { $slice : [ "$favorites" , 3 ] } } } ]) The operation returns the following results: { "_id" : 1 , "name" : "dave123" , "threeFavorites" : [ "chocolate" , "cake" , "butter" ] } { "_id" : 2 , "name" : "li" , "threeFavorites" : [ "apples" , "pudding" , "pie" ] } { "_id" : 3 , "name" : "ahn" , "threeFavorites" : [ "pears" , "pecans" , "chocolate" ] } { "_id" : 4 , "name" : "ty" , "threeFavorites" : [ "ice cream" ] } Back $sinh Next $sortArray
