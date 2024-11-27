# $cond (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $cond (aggregation) On this page Definition Compatibility Syntax Example Definition $cond Evaluates a boolean expression to return one of the two specified
return expressions. Compatibility You can use $cond for deployments hosted in the following
environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Syntax The $cond expression has one of two syntaxes: { $cond : { if : < boolean - expression > , then : < true - case > , else : < false - case > } } Or: { $cond : [ < boolean - expression > , < true - case > , < false - case > ] } $cond requires all three arguments ( if-then-else )
for either syntax. If the <boolean-expression> evaluates to true , then $cond evaluates and returns the value of the <true-case> expression. Otherwise, $cond evaluates
and returns the value of the <false-case> expression. The arguments can be any valid expression . For more information on expressions, see Expression Operators . Tip See also: $switch Example The following example use a inventory collection with the following
documents: { "_id" : 1 , "item" : "abc1" , qty : 300 } { "_id" : 2 , "item" : "abc2" , qty : 200 } { "_id" : 3 , "item" : "xyz1" , qty : 250 } The following aggregation operation uses the $cond expression to set the discount value to 30 if qty value is
greater than or equal to 250 and to 20 if qty value is less
than 250 : db. inventory . aggregate ( [ { $project : { item : 1 , discount : { $cond : { if : { $gte : [ "$qty" , 250 ] } , then : 30 , else : 20 } } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "abc1" , "discount" : 30 } { "_id" : 2 , "item" : "abc2" , "discount" : 20 } { "_id" : 3 , "item" : "xyz1" , "discount" : 30 } The following operation uses the array syntax of the $cond expression and returns the same results: db. inventory . aggregate ( [ { $project : { item : 1 , discount : { $cond : [ { $gte : [ "$qty" , 250 ] } , 30 , 20 ] } } } ] ) Back $concatArrays Next $convert
