# $add (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $add (aggregation) On this page Definition Behavior Examples Definition $add Adds numbers together or adds numbers and a date. If one of the
arguments is a date, $add treats the other arguments
as milliseconds to add to the date. The $add expression has the following syntax: { $add : [ < expression1 > , < expression2 > , ... ] } The arguments can be any valid expression as long as they resolve to
either all numbers or to numbers and a date. For more information on
expressions, see Expression Operators . Starting in MongoDB 6.1 you can optimize the $add operation. To
improve performance, group references at the end of the argument
list. For example, $add : [ 1 , 2 , 3 , '$a' , '$b' , '$c' ] Behavior When input types are mixed, $add promotes the smaller input
type to the larger of the two. A type is considered larger when it
represents a wider range of values. The order of numeric types from
smallest to largest is: integer â long â double â decimal The larger of the input types also determines the result type unless
the operation overflows and is beyond the range represented by that
larger data type. In cases of overflow, $add promotes the
result according to the following order: If the larger input type is integer , the result type
is promoted to long . If the larger input type is long , the result type is
promoted to double . If the larger type is double or decimal , the overflow result is represented
as + or - infinity. There is no type promotion of the result. When mixing Date and non-integer operands, $add rounds the non-integer value to the nearest integer
before performing the operation. Examples The following examples use a sales collection with the following
documents: { "_id" : 1 , "item" : "abc" , "price" : 10 , "fee" : 2 , date : ISODate ( "2014-03-01T08:00:00Z" ) } { "_id" : 2 , "item" : "jkl" , "price" : 20 , "fee" : 1 , date : ISODate ( "2014-03-01T09:00:00Z" ) } { "_id" : 3 , "item" : "xyz" , "price" : 5 , "fee" : 0 , date : ISODate ( "2014-03-15T09:00:00Z" ) } Add Numbers The following aggregation uses the $add expression in the $project pipeline to calculate the total cost: db. sales . aggregate ( [ { $project : { item : 1 , total : { $add : [ "$price" , "$fee" ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "abc" , "total" : 12 } { "_id" : 2 , "item" : "jkl" , "total" : 21 } { "_id" : 3 , "item" : "xyz" , "total" : 5 } Perform Addition on a Date The following aggregation uses the $add expression to
compute the billing_date by adding 3*24*60*60000 milliseconds
(i.e. 3 days) to the date field : db. sales . aggregate ( [ { $project : { item : 1 , billing_date : { $add : [ "$date" , 3 * 24 * 60 * 60000 ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "abc" , "billing_date" : ISODate ( "2014-03-04T08:00:00Z" ) } { "_id" : 2 , "item" : "jkl" , "billing_date" : ISODate ( "2014-03-04T09:00:00Z" ) } { "_id" : 3 , "item" : "xyz" , "billing_date" : ISODate ( "2014-03-18T09:00:00Z" ) } Back $acosh Next $addToSet
