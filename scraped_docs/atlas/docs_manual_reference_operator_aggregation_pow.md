# $pow (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $pow (aggregation) On this page Definition Behavior Example Definition $pow Raises a number to the specified exponent and returns the result. $pow has the following syntax: { $pow : [ < number > , < exponent > ] } The <number> expression can be any valid expression as long as it resolves to a number. The <exponent> expression can be any valid expression as long as it resolves to a number. You cannot raise 0 to a negative exponent. Behavior When input types are mixed, $pow promotes the smaller input
type to the larger of the two. A type is considered larger when it
represents a wider range of values. The order of numeric types from
smallest to largest is: integer â long â double â decimal The larger of the input types also determines the result type unless
the operation overflows and is beyond the range represented by that
larger data type. In cases of overflow, $pow promotes the
result according to the following order: If the larger input type is integer , the result type
is promoted to long . If the larger input type is long , the result type is
promoted to double . If the larger type is double or decimal , the overflow result is represented
as + or - infinity. There is no type promotion of the result. If either argument resolves to a value of null or refers to a field that is
missing, $pow returns null . If either argument resolves to NaN , $pow returns NaN . Example Results { $pow: [ 5, 0 ] } 1 { $pow: [ 5, 2 ] } 25 { $pow: [ 5, -2 ] } 0.04 { $pow: [ -5, 0.5 ] } NaN Example Create a collection called quizzes with the following documents: db. quizzes . insertMany ( [ { _id : 1 , scores : [ { name : "dave123" , score : 85 } , { name : "dave2" , score : 90 } , { name : "ahn" , score : 71 } ] } , { _id : 2 , scores : [ { name : "li" , quiz : 2 , score : 96 } , { name : "annT" , score : 77 } , { name : "ty" , score : 82 } ] } ] ) The following example calculates the variance for each quiz: db. quizzes . aggregate ( [ { $project : { variance : { $pow : [ { $stdDevPop : "$scores.score" } , 2 ] } } } ] ) The operation returns the following results: { _id : 1 , variance : 64.66666666666667 } { _id : 2 , variance : 64.66666666666667 } Back $percentile Next $push
