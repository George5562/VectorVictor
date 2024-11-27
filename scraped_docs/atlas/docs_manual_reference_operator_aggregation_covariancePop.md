# $covariancePop (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $covariancePop (aggregation) On this page Definition Behavior Example Definition New in version 5.0 . $covariancePop Returns the population covariance of two numeric expressions that are evaluated using documents in the $setWindowFields stage window . $covariancePop is only available in the $setWindowFields stage. $covariancePop syntax: { $covariancePop: [ <numeric expression 1>, <numeric expression 2> ] } Behavior $covariancePop behavior: Ignores non-numeric values, null values, and missing fields in a
window. If the window contains one document, returns null .
(Compare to $covarianceSamp , which returns null if
the window contains one document.) If the window is empty, returns null . If the window contains a NaN value, returns NaN . If the window contains one or more Infinity value(s) that are
all positive or all negative, returns Infinity . The returned Infinity value has the same sign as the Infinity values in the
window. If the window contains Infinity values with different signs,
returns NaN . If the window contains a decimal value, returns a decimal value. If none of the previous points apply, returns a double value. The returned values in order of precedence are as follows: NaN Infinity decimal double Example Create a cakeSales collection that contains cake sales in the states
of California ( CA ) and Washington ( WA ): db. cakeSales . insertMany ( [ { _id : 0 , type : "chocolate" , orderDate : new Date ( "2020-05-18T14:10:30Z" ) , state : "CA" , price : 13 , quantity : 120 } , { _id : 1 , type : "chocolate" , orderDate : new Date ( "2021-03-20T11:30:05Z" ) , state : "WA" , price : 14 , quantity : 140 } , { _id : 2 , type : "vanilla" , orderDate : new Date ( "2021-01-11T06:31:15Z" ) , state : "CA" , price : 12 , quantity : 145 } , { _id : 3 , type : "vanilla" , orderDate : new Date ( "2020-02-08T13:13:23Z" ) , state : "WA" , price : 13 , quantity : 104 } , { _id : 4 , type : "strawberry" , orderDate : new Date ( "2019-05-18T16:09:01Z" ) , state : "CA" , price : 41 , quantity : 162 } , { _id : 5 , type : "strawberry" , orderDate : new Date ( "2019-01-08T06:12:03Z" ) , state : "WA" , price : 43 , quantity : 134 } ] ) This example uses $covariancePop in the $setWindowFields stage to output the population covariance
values for the cake sales orderDate year and quantity values: db. cakeSales . aggregate ( [ { $setWindowFields : { partitionBy : "$state" , sortBy : { orderDate : 1 } , output : { covariancePopForState : { $covariancePop : [ { $year : "$orderDate" } , "$quantity" ] , window : { documents : [ "unbounded" , "current" ] } } } } } ] ) In the example: partitionBy: "$state" partitions the documents in the collection by state . There are partitions for CA and WA . sortBy: { orderDate: 1 } sorts the documents in each partition by orderDate in ascending order ( 1 ), so the earliest orderDate is first. output sets the population covariance values for the orderDate year and quantity values using $covariancePop run in a documents window. The window contains documents between
an unbounded lower limit and the current document in the
output. This means $covariancePop sets the covariancePopForState field to the population covariance values
for the documents between the beginning of the partition and the
current document. In this output, the population covariance is shown in the covariancePopForState field: { "_id" : 4 , "type" : "strawberry" , "orderDate" : ISODate ( "2019-05-18T16:09:01Z" ) , "state" : "CA" , "price" : 41 , "quantity" : 162 , "covariancePopForState" : 0 } { "_id" : 0 , "type" : "chocolate" , "orderDate" : ISODate ( "2020-05-18T14:10:30Z" ) , "state" : "CA" , "price" : 13 , "quantity" : 120 , "covariancePopForState" : - 10.5 } { "_id" : 2 , "type" : "vanilla" , "orderDate" : ISODate ( "2021-01-11T06:31:15Z" ) , "state" : "CA" , "price" : 12 , "quantity" : 145 , "covariancePopForState" : - 5.666666666666671 } { "_id" : 5 , "type" : "strawberry" , "orderDate" : ISODate ( "2019-01-08T06:12:03Z" ) , "state" : "WA" , "price" : 43 , "quantity" : 134 , "covariancePopForState" : 0 } { "_id" : 3 , "type" : "vanilla" , "orderDate" : ISODate ( "2020-02-08T13:13:23Z" ) , "state" : "WA" , "price" : 13 , "quantity" : 104 , "covariancePopForState" : - 7.5 } { "_id" : 1 , "type" : "chocolate" , "orderDate" : ISODate ( "2021-03-20T11:30:05Z" ) , "state" : "WA" , "price" : 14 , "quantity" : 140 , "covariancePopForState" : 2 } Back $count-accumulator Next $covarianceSamp