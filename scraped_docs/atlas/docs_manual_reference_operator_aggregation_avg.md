# $avg (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $avg (aggregation) On this page Definition Syntax Behavior Examples Definition Changed in version 5.0 . $avg Returns the average value of the numeric values. $avg ignores non-numeric values. $avg is available in these stages: $addFields $bucket $bucketAuto $group $match stage that includes an $expr expression $project $replaceRoot $replaceWith $set $setWindowFields (Available starting in MongoDB 5.0) Syntax When used in the $bucket , $bucketAuto , $group , and $setWindowFields stages, $avg has this syntax: { $avg: <expression> } When used in other supported stages, $avg has one of two
syntaxes: $avg has one specified expression as its operand: { $avg: <expression> } $avg has a list of specified expressions as its
operand: { $avg: [ <expression1>, <expression2> ... ]  } For more information on expressions, see Expression Operators . Behavior Result Type The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. Non-numeric or Missing Values $avg ignores non-numeric values, including missing values. If all of the
operands for the average are non-numeric, $avg returns null since the average of zero values is undefined. Array Operand In the $group stage, if the expression resolves to an
array, $avg treats the operand as a non-numerical value. In the other supported stages: With a single expression as its operand, if the expression resolves
to an array, $avg traverses into the array to operate on the
numeric elements of the array to return a single value. With a list of expressions as its operand, if any of the expressions
resolves to an array, $avg does not traverse into the
array but instead treats the array as a non-numeric value. Examples Use in $group Stage Consider a sales collection with the following documents: { "_id" : 1 , "item" : "abc" , "price" : 10 , "quantity" : 2 , "date" : ISODate ( "2014-01-01T08:00:00Z" ) } { "_id" : 2 , "item" : "jkl" , "price" : 20 , "quantity" : 1 , "date" : ISODate ( "2014-02-03T09:00:00Z" ) } { "_id" : 3 , "item" : "xyz" , "price" : 5 , "quantity" : 5 , "date" : ISODate ( "2014-02-03T09:05:00Z" ) } { "_id" : 4 , "item" : "abc" , "price" : 10 , "quantity" : 10 , "date" : ISODate ( "2014-02-15T08:00:00Z" ) } { "_id" : 5 , "item" : "xyz" , "price" : 5 , "quantity" : 10 , "date" : ISODate ( "2014-02-15T09:12:00Z" ) } Grouping the documents by the item field, the following operation
uses the $avg accumulator to compute the average amount and
average quantity for each grouping. db. sales . aggregate ( [ { $group : { _id : "$item" , avgAmount : { $avg : { $multiply : [ "$price" , "$quantity" ] } } , avgQuantity : { $avg : "$quantity" } } } ] ) The operation returns the following results: { "_id" : "xyz" , "avgAmount" : 37.5 , "avgQuantity" : 7.5 } { "_id" : "jkl" , "avgAmount" : 20 , "avgQuantity" : 1 } { "_id" : "abc" , "avgAmount" : 60 , "avgQuantity" : 6 } Use in $project Stage A collection students contains the following documents: { "_id" : 1 , "quizzes" : [ 10 , 6 , 7 ] , "labs" : [ 5 , 8 ] , "final" : 80 , "midterm" : 75 } { "_id" : 2 , "quizzes" : [ 9 , 10 ] , "labs" : [ 8 , 8 ] , "final" : 95 , "midterm" : 80 } { "_id" : 3 , "quizzes" : [ 4 , 5 , 5 ] , "labs" : [ 6 , 5 ] , "final" : 78 , "midterm" : 70 } The following example uses the $avg in the $project stage to calculate the average quiz scores, the
average lab scores, and the average of the final and the midterm: db. students . aggregate ( [ { $project : { quizAvg : { $avg : "$quizzes" } , labAvg : { $avg : "$labs" } , examAvg : { $avg : [ "$final" , "$midterm" ] } } } ]) The operation results in the following documents: { "_id" : 1 , "quizAvg" : 7.666666666666667 , "labAvg" : 6.5 , "examAvg" : 77.5 } { "_id" : 2 , "quizAvg" : 9.5 , "labAvg" : 8 , "examAvg" : 87.5 } { "_id" : 3 , "quizAvg" : 4.666666666666667 , "labAvg" : 5.5 , "examAvg" : 74 } Use in $setWindowFields Stage New in version 5.0 . Create a cakeSales collection that contains cake sales in the states
of California ( CA ) and Washington ( WA ): db. cakeSales . insertMany ( [ { _id : 0 , type : "chocolate" , orderDate : new Date ( "2020-05-18T14:10:30Z" ) , state : "CA" , price : 13 , quantity : 120 } , { _id : 1 , type : "chocolate" , orderDate : new Date ( "2021-03-20T11:30:05Z" ) , state : "WA" , price : 14 , quantity : 140 } , { _id : 2 , type : "vanilla" , orderDate : new Date ( "2021-01-11T06:31:15Z" ) , state : "CA" , price : 12 , quantity : 145 } , { _id : 3 , type : "vanilla" , orderDate : new Date ( "2020-02-08T13:13:23Z" ) , state : "WA" , price : 13 , quantity : 104 } , { _id : 4 , type : "strawberry" , orderDate : new Date ( "2019-05-18T16:09:01Z" ) , state : "CA" , price : 41 , quantity : 162 } , { _id : 5 , type : "strawberry" , orderDate : new Date ( "2019-01-08T06:12:03Z" ) , state : "WA" , price : 43 , quantity : 134 } ] ) This example uses $avg in the $setWindowFields stage to output the moving average for the cake sales quantity for
each state : db. cakeSales . aggregate ( [ { $setWindowFields : { partitionBy : "$state" , sortBy : { orderDate : 1 } , output : { averageQuantityForState : { $avg : "$quantity" , window : { documents : [ "unbounded" , "current" ] } } } } } ] ) In the example: partitionBy: "$state" partitions the documents in the collection by state . There are partitions for CA and WA . sortBy: { orderDate: 1 } sorts the documents in each partition by orderDate in ascending order ( 1 ), so the earliest orderDate is first. output sets the averageQuantityForState field to the moving
average quantity using $avg for the documents in a documents window. The window contains documents between
an unbounded lower limit and the current document in the
output. This means $avg returns the moving average quantity for the documents between the beginning of the partition
and the current document. In this output, the moving average quantity for CA and WA is shown in the averageQuantityForState field: { "_id" : 4 , "type" : "strawberry" , "orderDate" : ISODate ( "2019-05-18T16:09:01Z" ) , "state" : "CA" , "price" : 41 , "quantity" : 162 , "averageQuantityForState" : 162 } { "_id" : 0 , "type" : "chocolate" , "orderDate" : ISODate ( "2020-05-18T14:10:30Z" ) , "state" : "CA" , "price" : 13 , "quantity" : 120 , "averageQuantityForState" : 141 } { "_id" : 2 , "type" : "vanilla" , "orderDate" : ISODate ( "2021-01-11T06:31:15Z" ) , "state" : "CA" , "price" : 12 , "quantity" : 145 , "averageQuantityForState" : 142.33333333333334 } { "_id" : 5 , "type" : "strawberry" , "orderDate" : ISODate ( "2019-01-08T06:12:03Z" ) , "state" : "WA" , "price" : 43 , "quantity" : 134 , "averageQuantityForState" : 134 } { "_id" : 3 , "type" : "vanilla" , "orderDate" : ISODate ( "2020-02-08T13:13:23Z" ) , "state" : "WA" , "price" : 13 , "quantity" : 104 , "averageQuantityForState" : 119 } { "_id" : 1 , "type" : "chocolate" , "orderDate" : ISODate ( "2021-03-20T11:30:05Z" ) , "state" : "WA" , "price" : 14 , "quantity" : 140 , "averageQuantityForState" : 126 } Back $atanh Next $binarySize