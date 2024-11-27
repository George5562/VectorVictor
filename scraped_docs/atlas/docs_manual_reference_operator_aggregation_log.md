# $log (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $log (aggregation) On this page Definition Behavior Example Definition $log Calculates the log of a number in the specified base and returns the
result as a double. $log has the following syntax: { $log : [ < number > , < base > ] } The <number> expression can be any valid expression as long as it resolves to a non-negative number. The <base> expression can be any valid expression as long as it resolves to a positive
number greater than 1 . For more information on expressions, see Expression Operators . Behavior The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. If either argument resolves to a value of null or refers to a field that is
missing, $log returns null . If either argument resolves to NaN , $log returns NaN . Example Results { $log: [ 100, 10 ] } 2 { $log: [ 100, Math.E ] } where Math.E is a JavaScript
representation for e . 4.605170185988092 Example A collection integers contains the following documents: db. integers . insertMany ( [ { _id : 1 , int : 5 } , { _id : 2 , int : 2 } , { _id : 3 , int : 23 } , { _id : 4 , int : 10 } ] ) The following example uses log 2 in its calculation to
determine the number of bits required to represent the value of int . db. integers . aggregate ( [ { $project : { bitsNeeded : { $floor : { $add : [ 1 , { $log : [ "$int" , 2 ] } ] } } } } ]) The operation returns the following results: { "_id" : 1 , "bitsNeeded" : 3 } { "_id" : 2 , "bitsNeeded" : 2 } { "_id" : 3 , "bitsNeeded" : 5 } { "_id" : 4 , "bitsNeeded" : 4 } Tip See also: $log10 $ln Back $locf Next $log10
