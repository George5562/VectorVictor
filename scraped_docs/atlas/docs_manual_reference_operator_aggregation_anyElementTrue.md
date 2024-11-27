# $anyElementTrue (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $anyElementTrue (aggregation) On this page Definition Behavior Example Definition $anyElementTrue Evaluates an array as a set and returns true if any of the
elements are true and false otherwise. An empty array
returns false . $anyElementTrue has the following syntax: { $anyElementTrue : [ < expression > ] } The <expression> itself must resolve to an array, separate from
the outer array that denotes the argument list. For more information
on expressions, see Expression Operators . Behavior If a set contains a nested array element, $anyElementTrue does not descend
into the nested array but evaluates the array at top-level. In addition to the false boolean value, $anyElementTrue evaluates
as false the following: null , 0 , and undefined values. The $anyElementTrue evaluates all other values as true ,
including non-zero numeric values and arrays. Example Result { $anyElementTrue: [ [ true, false ] ] } true { $anyElementTrue: [ [ [ false ] ] ] } true { $anyElementTrue: [ [ null, false, 0 ] ] } false { $anyElementTrue: [ [ ] ] } false Example Create an example collection named survey with the following
documents: db. survey . insertMany ( [ { "_id" : 1 , "responses" : [ true ] } , { "_id" : 2 , "responses" : [ true , false ] } , { "_id" : 3 , "responses" : [ ] } , { "_id" : 4 , "responses" : [ 1 , true , "seven" ] } , { "_id" : 5 , "responses" : [ 0 ] } , { "_id" : 6 , "responses" : [ [ ] ] } , { "_id" : 7 , "responses" : [ [ 0 ] ] } , { "_id" : 8 , "responses" : [ [ false ] ] } , { "_id" : 9 , "responses" : [ null ] } , { "_id" : 10 , "responses" : [ undefined ] } ]) The following operation uses the $anyElementTrue operator
to determine if the responses array contains any value that
evaluates to true : db. survey . aggregate ( [ { $project : { responses : 1 , isAnyTrue : { $anyElementTrue : [ "$responses" ] } , _id : 1 } } ] ) HIDE OUTPUT [ { _id : 1 , responses : [ true ] , isAnyTrue : true } , { _id : 2 , responses : [ true , false ] , isAnyTrue : true } , { _id : 3 , responses : [ ] , isAnyTrue : false } , { _id : 4 , responses : [ 1 , true , 'seven' ] , isAnyTrue : true } , { _id : 5 , responses : [ 0 ] , isAnyTrue : false } , { _id : 6 , responses : [ [ ] ] , isAnyTrue : true } , { _id : 7 , responses : [ [ 0 ] ] , isAnyTrue : true } , { _id : 8 , responses : [ [ false ] ] , isAnyTrue : true } , { _id : 9 , responses : [ null ] , isAnyTrue : false } , { _id : 10 , responses : [ null ] , isAnyTrue : false } ] In the results: Document with _id: 1 is true because the element inside the responses array evaluates as true . Documents with _id: 2 and _id: 4 are true because at least
one element inside the responses array evaluates as true . Documents with _id: 6 , _id: 7 , and _id: 8 are true because the responses array, which is the array that $anyElementTrue evaluated for the operation, contains a nested
array, which $anyElementTrue always evaluates as true . Back $and Next $arrayElemAt
