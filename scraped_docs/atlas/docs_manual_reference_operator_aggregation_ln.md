# $ln (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $ln (aggregation) On this page Definition Behavior Example Definition $ln Calculates the natural logarithm ln (i.e log e ) of a number and
returns the result as a double. $ln has the following syntax: { $ln : < number > } The <number> expression can be any valid expression as long as it resolves to a non-negative
number. For more information on expressions, see Expression Operators . $ln is equivalent to $log: [ <number>, Math.E ] expression, where Math.E is a JavaScript representation for
Euler's number e . Behavior The default return type is a double . If at least
one operand is a decimal , then the return
type is a decimal. If the argument resolves to a value of null or refers to a field that is
missing, $ln returns null . If the argument resolves to NaN , $ln returns NaN . Example Results { $ln: 1 } 0 { $ln: Math.E } where Math.E is a JavaScript representation for e . 1 { $ln: 10  } 2.302585092994046 Example A collection sales contains the following documents: { _id : 1 , year : "2000" , sales : 8700000 } { _id : 2 , year : "2005" , sales : 5000000 } { _id : 3 , year : "2010" , sales : 6250000 } The following example transforms the sales data: db. sales . aggregate ( [ { $project : { x : "$year" , y : { $ln : "$sales" } } } ] ) The operation returns the following results: { "_id" : 1 , "x" : "2000" , "y" : 15.978833583624812 } { "_id" : 2 , "x" : "2005" , "y" : 15.424948470398375 } { "_id" : 3 , "x" : "2010" , "y" : 15.648092021712584 } Tip See also: $log Back $literal Next $locf
