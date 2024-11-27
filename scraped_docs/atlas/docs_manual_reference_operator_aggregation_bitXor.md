# $bitXor (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $bitXor (aggregation) On this page Definition Syntax Behavior Example Learn More Definition New in version 6.3 . $bitXor Returns the result of a bitwise xor (exclusive or) operation on an
array of int and long values. Syntax The $bitXor operator has the following syntax: { $bitXor : [ < expression1 > , < expression2 > , ... ] } Behavior If the operands include both integers and long values, MongoDB sign-extends the
calculated integer result and returns a long value. Otherwise, if the operands
include only integers or only longs, MongoDB returns results with the
corresponding value type. Note All numbers in mongosh are doubles, not integers. To
specify integers in mongosh , use the NumberInt() or the NumberLong() constructor. To learn more, see Int32 or Long . To learn how your MongoDB driver handles numeric values, refer to your driver's documentation . If any arguments in the array are of a different data type such as a string,
double, or decimal, MongoDB returns an error. If the argument is an empty array, the operation returns NumberInt(0) . If any of the arguments in the array equate to null , the operation returns null . Example The example on this page uses the switches collection: db. switches . insertMany ( [ { _id : 0 , a : NumberInt ( 0 ) , b : NumberInt ( 127 ) } , { _id : 1 , a : NumberInt ( 2 ) , b : NumberInt ( 3 ) } , { _id : 2 , a : NumberInt ( 3 ) , b : NumberInt ( 5 ) } ] ) The following aggregation uses the $bitXor operator in the $project stage: db. switches . aggregate ( [ { $project : { result : { $bitXor : [ "$a" , "$b" ] } } } ]) The operation returns the following results: [ { _id : 0 , result : 127 } , { _id : 1 , result : 1 } , { _id : 2 , result : 6 } ] Learn More Aggregation Operators $bit Back $bitOr Next $bottom
