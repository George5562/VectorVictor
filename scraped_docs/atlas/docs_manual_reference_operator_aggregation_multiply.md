# $multiply (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $multiply (aggregation) On this page Definition Behavior Example Definition $multiply Multiplies numbers together and returns the result. Pass the
arguments to $multiply in an array. The $multiply expression has the following syntax: { $multiply : [ < expression1 > , < expression2 > , ... ] } The arguments can be any valid expression as long as they resolve to numbers. For
more information on expressions, see Expression Operators . Starting in MongoDB 6.1 you can optimize the $multiply operation.
To improve performance, group references at the end of the argument
list. For example, $multiply : [ 1 , 2 , 3 , '$a' , '$b' , '$c' ] Behavior When input types are mixed, $multiply promotes the smaller input
type to the larger of the two. A type is considered larger when it
represents a wider range of values. The order of numeric types from
smallest to largest is: integer â long â double â decimal The larger of the input types also determines the result type unless
the operation overflows and is beyond the range represented by that
larger data type. In cases of overflow, $multiply promotes the
result according to the following order: If the larger input type is integer , the result type
is promoted to long . If the larger input type is long , the result type is
promoted to double . If the larger type is double or decimal , the overflow result is represented
as + or - infinity. There is no type promotion of the result. Example Consider a sales collection with the following documents: { "_id" : 1 , "item" : "abc" , "price" : 10 , "quantity" : 2 , date : ISODate ( "2014-03-01T08:00:00Z" ) } { "_id" : 2 , "item" : "jkl" , "price" : 20 , "quantity" : 1 , date : ISODate ( "2014-03-01T09:00:00Z" ) } { "_id" : 3 , "item" : "xyz" , "price" : 5 , "quantity" : 10 , date : ISODate ( "2014-03-15T09:00:00Z" ) } The following aggregation uses the $multiply expression
in the $project pipeline to multiply the price and the quantity fields: db. sales . aggregate ( [ { $project : { date : 1 , item : 1 , total : { $multiply : [ "$price" , "$quantity" ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "abc" , "date" : ISODate ( "2014-03-01T08:00:00Z" ) , "total" : 20 } { "_id" : 2 , "item" : "jkl" , "date" : ISODate ( "2014-03-01T09:00:00Z" ) , "total" : 20 } { "_id" : 3 , "item" : "xyz" , "date" : ISODate ( "2014-03-15T09:00:00Z" ) , "total" : 50 } Back $month Next $ne
