# $divide (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $divide (aggregation) On this page Definition Behavior Examples Definition $divide Divides one number by another and returns the result. Pass the
arguments to $divide in an array. The $divide expression has the following syntax: { $divide : [ < expression1 > , < expression2 > ] } The first argument is the dividend, and the second argument is the
divisor; i.e. the first argument is divided by the second argument. The arguments can be any valid expression as long as they resolve to numbers. For
more information on expressions, see Expression Operators . Behavior The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. Examples Consider a conferencePlanning collection with the following documents: db. conferencePlanning . insertMany ( [ { "_id" : 1 , "city" : "New York" , "hours" : 80 , "tasks" : 7 } , { "_id" : 2 , "city" : "Singapore" , "hours" : 40 , "tasks" : 4 } ] ) The following aggregation uses the $divide expression to
divide the hours field by a literal 8 to compute the number of
work days: db. planning . aggregate ( [ { $project : { city : 1 , workdays : { $divide : [ "$hours" , 8 ] } } } ] ) The operation returns the following results: { "_id" : 1 , "city" : "New York" , "workdays" : 10 } { "_id" : 2 , "city" : "Singapore" , "workdays" : 5 } Back $derivative Next $documentNumber
