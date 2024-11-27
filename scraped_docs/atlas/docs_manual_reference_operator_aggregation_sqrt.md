# $sqrt (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $sqrt (aggregation) On this page Definition Behavior Example Definition $sqrt Calculates the square root of a positive number and returns the
result as a double. $sqrt has the following syntax: { $sqrt : < number > } The argument can be any valid expression as long as it resolves to a non-negative number. For more information
on expressions, see Expression Operators . Behavior The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. If the argument resolves to a value of null or refers to a field that is
missing, $sqrt returns null . If the argument resolves to NaN , $sqrt returns NaN . $sqrt errors on negative numbers. Example Results { $sqrt: 25 } 5 { $sqrt: 30 } 5.477225575051661 { $sqrt: null } null Example A collection points contains the following documents: { _id : 1 , p1 : { x : 5 , y : 8 } , p2 : { x : 0 , y : 5 } } { _id : 2 , p1 : { x : - 2 , y : 1 } , p2 : { x : 1 , y : 5 } } { _id : 3 , p1 : { x : 4 , y : 4 } , p2 : { x : 4 , y : 0 } } The following example uses $sqrt to calculate the
distance between p1 and p2 : db. points . aggregate ( [ { $project : { distance : { $sqrt : { $add : [ { $pow : [ { $subtract : [ "$p2.y" , "$p1.y" ] } , 2 ] } , { $pow : [ { $subtract : [ "$p2.x" , "$p1.x" ] } , 2 ] } ] } } } } ]) The operation returns the following results: { "_id" : 1 , "distance" : 5.830951894845301 } { "_id" : 2 , "distance" : 5 } { "_id" : 3 , "distance" : 4 } Back $split Next $stdDevPop
