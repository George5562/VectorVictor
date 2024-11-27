# $log10 (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $log10 (aggregation) On this page Definition Behavior Example Definition $log10 Calculates the log base 10 of a number and returns the result as a
double. $log10 has the following syntax: { $log10 : < number > } The <number> expression can be any valid expression as long as it resolves to a non-negative
number. For more information on expressions, see Expression Operators . $log10 is equivalent to $log: [ <number>, 10 ] expression. Behavior The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. If the argument resolves to a value of null or refers to a field that is
missing, $log10 returns null . If the argument resolves to NaN , $log10 returns NaN . Example Results { $log10: 1 } 0 { $log10: 10 } 1 { $log10: 100 } 2 { $log10: 1000 } 3 Example Create a collection named samples with the following documents: db. samples . insertMany ( [ { _id : 1 , H3O : 0.0025 } , { _id : 2 , H3O : 0.001 } , { _id : 3 , H3O : 0.02 } ] ) The following example calculates the pH value of the samples: db. samples . aggregate ( [ { $project : { pH : { $multiply : [ - 1 , { $log10 : "$H3O" } ] } } } ] ) The operation returns the following results: { "_id" : 1 , "pH" : 2.6020599913279625 } { "_id" : 2 , "pH" : 3 } { "_id" : 3 , "pH" : 1.6989700043360187 } Tip See also: $log Back $log Next $lt
