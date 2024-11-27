# $allElementsTrue (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $allElementsTrue (aggregation) On this page Definition Behavior Example Definition $allElementsTrue Evaluates an array as a set and returns true if no element in
the array is false . Otherwise, returns false . An empty array
returns true . $allElementsTrue has the following syntax: { $allElementsTrue : [ < expression > ] } The <expression> itself must resolve to an array, separate from
the outer array that denotes the argument list. For more information
on expressions, see Expression Operators . Behavior If a set contains a nested array element, $allElementsTrue does not descend
into the nested array but evaluates the array at top-level. In addition to the false boolean value, $allElementsTrue evaluates
as false the following: null , 0 , and undefined values. The $allElementsTrue evaluates all other values as true ,
including non-zero numeric values and arrays. Example Result { $allElementsTrue: [ [ true, 1, "someString" ] ] } true { $allElementsTrue: [ [ [ false ] ] ] } true { $allElementsTrue: [ [ ] ] } true { $allElementsTrue: [ [ null, false, 0 ] ] } false Example Create an example collection named survey with the following
documents: db. survey . insertMany ( [ { "_id" : 1 , "responses" : [ true ] } , { "_id" : 2 , "responses" : [ true , false ] } , { "_id" : 3 , "responses" : [ ] } , { "_id" : 4 , "responses" : [ 1 , true , "seven" ] } , { "_id" : 5 , "responses" : [ 0 ] } , { "_id" : 6 , "responses" : [ [ ] ] } , { "_id" : 7 , "responses" : [ [ 0 ] ] } , { "_id" : 8 , "responses" : [ [ false ] ] } , { "_id" : 9 , "responses" : [ null ] } , { "_id" : 10 , "responses" : [ undefined ] } ]) The following operation uses the $allElementsTrue operator to determine if the responses array only contains values
that evaluate to true : db. survey . aggregate ( [ { $project : { responses : 1 , isAllTrue : { $allElementsTrue : [ "$responses" ] } , _id : 0 } } ] ) The operation returns the following results: { "responses" : [ true ] , "isAllTrue" : true } { "responses" : [ true , false ] , "isAllTrue" : false } { "responses" : [ ] , "isAllTrue" : true } { "responses" : [ 1 , true , "seven" ] , "isAllTrue" : true } { "responses" : [ 0 ] , "isAllTrue" : false } { "responses" : [ [ ] ] , "isAllTrue" : true } { "responses" : [ [ 0 ] ] , "isAllTrue" : true } { "responses" : [ [ false ] ] , "isAllTrue" : true } { "responses" : [ null ] , "isAllTrue" : false } { "responses" : [ undefined ] , "isAllTrue" : false } Back $addToSet Next $and
