# $ceil (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $ceil (aggregation) On this page Definition Behavior Example Definition $ceil Returns the smallest integer greater than or equal to the specified
number. $ceil has the following syntax: { $ceil : < number > } The <number> expression can be any valid expression as long as it resolves to a number. For
more information on expressions, see Expression Operators . Behavior If the argument resolves to a value of null or refers to a field that is
missing, $ceil returns null . If the argument resolves to NaN , $ceil returns NaN . Example Results { $ceil: 1 } 1 { $ceil: 7.80 } 8 { $ceil: -2.8 } -2 Example Create a collection named samples with the following documents: db. samples . insertMany ( [ { _id : 1 , value : 9.25 } , { _id : 2 , value : 8.73 } , { _id : 3 , value : 4.32 } , { _id : 4 , value : - 5.34 } ] ) The following example returns both the original value and the ceiling
value: db. samples . aggregate ( [ { $project : { value : 1 , ceilingValue : { $ceil : "$value" } } } ]) The operation returns the following results: { "_id" : 1 , "value" : 9.25 , "ceilingValue" : 10 } { "_id" : 2 , "value" : 8.73 , "ceilingValue" : 9 } { "_id" : 3 , "value" : 4.32 , "ceilingValue" : 5 } { "_id" : 4 , "value" : - 5.34 , "ceilingValue" : - 5 } Back $bsonSize Next $cmp
