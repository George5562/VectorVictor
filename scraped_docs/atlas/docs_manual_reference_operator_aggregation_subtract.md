# $subtract (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $subtract (aggregation) On this page Definition Behavior Examples Definition $subtract Subtracts two numbers to return the difference, or two dates to
return the difference in milliseconds, or a date and a number in
milliseconds to return the resulting date. The $subtract expression has the following syntax: { $subtract : [ < expression1 > , < expression2 > ] } The second argument is subtracted from the first argument. The arguments can be any valid expression as long as they resolve to numbers
and/or dates. To subtract a number from a date, the date must be the
first argument. For more information on expressions, see Expression Operators . Behavior When input types are mixed, $subtract promotes the smaller input
type to the larger of the two. A type is considered larger when it
represents a wider range of values. The order of numeric types from
smallest to largest is: integer â long â double â decimal The larger of the input types also determines the result type unless
the operation overflows and is beyond the range represented by that
larger data type. In cases of overflow, $subtract promotes the
result according to the following order: If the larger input type is integer , the result type
is promoted to long . If the larger input type is long , the result type is
promoted to double . If the larger type is double or decimal , the overflow result is represented
as + or - infinity. There is no type promotion of the result. When mixing Date and non-integer operands, $subtract rounds the non-integer value to the nearest integer
before performing the operation. Examples Consider a sales collection with the following documents: db. sales . insertMany ( [ { "_id" : 1 , "item" : "abc" , "price" : 10 , "fee" : 2 , "discount" : 5 , "date" : ISODate ( "2014-03-01T08:00:00Z" ) } , { "_id" : 2 , "item" : "jkl" , "price" : 20 , "fee" : 1 , "discount" : 2 , "date" : ISODate ( "2014-03-01T09:00:00Z" ) } ]) Subtract Numbers The following aggregation uses the $subtract expression
to compute the total by subtracting the discount from the
subtotal of price and fee . db. sales . aggregate ( [ { $project : { item : 1 , total : { $subtract : [ { $add : [ "$price" , "$fee" ] } , "$discount" ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "abc" , "total" : 7 } { "_id" : 2 , "item" : "jkl" , "total" : 19 } Subtract Two Dates The following aggregation uses the $subtract expression
to subtract $date from the current date, using the system NOW and returns the difference in milliseconds: db. sales . aggregate ( [ { $project : { item : 1 , dateDifference : { $subtract : [ "$$NOW" , "$date" ] } } } ] ) Alternatively, you can use the Date() for the current date:s db. sales . aggregate ( [ { $project : { item : 1 , dateDifference : { $subtract : [ new Date ( ) , "$date" ] } } } ] ) Both operations return documents that resemble the following: { "_id" : 1 , "item" : "abc" , "dateDifference" : NumberLong ( "186136746187" ) } { "_id" : 2 , "item" : "jkl" , "dateDifference" : NumberLong ( "186133146187" ) } Subtract Milliseconds from a Date The following aggregation uses the $subtract expression
to subtract 5 * 60 * 1000 milliseconds (5 minutes) from the "$date"
field: db. sales . aggregate ( [ { $project : { item : 1 , dateDifference : { $subtract : [ "$date" , 5 * 60 * 1000 ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "abc" , "dateDifference" : ISODate ( "2014-03-01T07:55:00Z" ) } { "_id" : 2 , "item" : "jkl" , "dateDifference" : ISODate ( "2014-03-01T08:55:00Z" ) } Back $substrCP Next $sum
