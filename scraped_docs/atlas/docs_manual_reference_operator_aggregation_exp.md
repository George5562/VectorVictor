# $exp (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $exp (aggregation) On this page Definition Behavior Example Definition $exp Raises Euler's number (i.e. e ) to the specified exponent and
returns the result. $exp has the following syntax: { $exp : < exponent > } The <exponent> expression can be any valid expression as long as it resolves to a number. For
more information on expressions, see Expression Operators . Behavior The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. If the argument resolves to a value of null or refers to a field that is
missing, $exp returns null . If the argument resolves to NaN , $exp returns NaN . Example Results { $exp: 0 } 1 { $exp: 2 } 7.38905609893065 { $exp: -2 } 0.1353352832366127 Example A collection named accounts contains the following documents: db. accounts . insertMany ( [ { _id : 1 , interestRate : .08 , presentValue : 10000 } , { _id : 2 , interestRate : .0825 , presentValue : 250000 } , { _id : 3 , interestRate : .0425 , presentValue : 1000 } ] ) The following example calculates the effective interest rate for
continuous compounding: db. accounts . aggregate ( [ { $project : { effectiveRate : { $subtract : [ { $exp : "$interestRate" } , 1 ] } } } ] ) The operation returns the following results: { "_id" : 1 , "effectiveRate" : 0.08328706767495864 } { "_id" : 2 , "effectiveRate" : 0.08599867343905654 } { "_id" : 3 , "effectiveRate" : 0.04341605637367807 } Back $eq Next $expMovingAvg
