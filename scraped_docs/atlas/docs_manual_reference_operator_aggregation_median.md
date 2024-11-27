# $median (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $median (aggregation) On this page Definition Syntax Command Fields Behavior Examples Learn More Definition $median New in version 7.0 . Returns an approximation of the median , the 50th percentile , as a scalar value. You can use $median as an accumulator in the $group stage or as
an aggegation expression . Syntax The syntax for $median is: { $median : { input : < number > , method : < string > } } Command Fields $median takes the following fields: Field Type Necessity Description input Expression Required $median calculates the 50th percentile value of this data. input must be a field name or an expression that evaluates to
a numeric type. If the expression cannot be converted to a
numeric type, the $median calculation ignores it. method String Required The method that mongod uses to calculate the 50th percentile
value. The method must be 'approximate' . Behavior You can use $median in: $group stages as an accumulator $setWindowFields stages as an accumulator $project stages as an aggregation expression $median has the following characteristics as an accumulator, it: Calculates a single result for all the documents in the stage. Uses the t-digest algorithm to
calculate approximate, percentile based metrics. Uses approximate methods to scale to large volumes of data. $median has the following characteristics as an aggregation
expression, it: Accepts an array as input Calculates a separate result for each input document Type of Operation In a $group stage, $median is an accumulator and calculates
a value for all documents in the window. In a $project stage, $median is an aggregation expression and
calculates values for each document. In $setWindowFields stages, $median returns a result
for each document like an aggregation expression, but the results are
computed over groups of documents like an accumulator. Calculation Considerations In $group stages, $median always uses an approximate
calculation method. In $project stages, $median might use the discrete
calculation method even when the approximate method is specified. In $setWindowFields stages, the workload determines the calculation
method that $median uses. The computed percentiles $median returns might vary, even on the
same datasets. This is because the algorithm calculates approximate
values. Duplicate samples can cause ambiguity. If there are a large number of
duplicates, the percentile values may not represent the actual sample
distribution. Consider a data set where all the samples are the same.
All of the values in the data set fall at or below any percentile. A
"50th percentile" value would actually represent either 0 or 100 percent
of the samples. Array Input If you use $median as an aggregation expression in a $project stage, you can use an array as input. $median ignores non-numeric array values. The syntax is: { $median : { input : [ < expression1 , < expression2 > , ... , < expressionN > ] , method : < string > } } Window Functions A window function lets you calculate results over a moving "window" of
neighboring documents. As each document passes though the pipeline, the $setWindowFields stage: Recomputes the set of documents in the current window calculates a value for all documents in the set returns a single value for that document You can use $median in a $setWindowFields stage to calculate
rolling statistics for time series or
other related data. When you use $median in a $setWindowField stage, the input value must be a field name. If you enter an array instead of a
field name, the operation fails. Examples The following examples use the testScores collection. Create the
collection: db. testScores . insertMany ( [ { studentId : "2345" , test01 : 62 , test02 : 81 , test03 : 80 } , { studentId : "2356" , test01 : 60 , test02 : 83 , test03 : 79 } , { studentId : "2358" , test01 : 67 , test02 : 82 , test03 : 78 } , { studentId : "2367" , test01 : 64 , test02 : 72 , test03 : 77 } , { studentId : "2369" , test01 : 60 , test02 : 53 , test03 : 72 } ] ) Use $median as an Accumulator Create an accumulator that calculates the median value: db. testScores . aggregate ( [ { $group : { _id : null , test01_median : { $median : { input : "$test01" , method : 'approximate' } } } } ] ) Output: { _id : null , test01_median : 62 } The _id field value is null so $group selects all the
documents in the collection. The $median accumulator takes its input from the test01 field. $median calculates the median value for the field, 62 in this example. Use $median in a $project Stage In a $group stage, $median is an accumulator and calculates
a single value for all documents. In a $project stage, $median is an aggregation expression and calculates values for
each document. You can use a field name or an array as input in a $project stage. db. testScores . aggregate ( [ { $project : { _id : 0 , studentId : 1 , testMedians : { $median : { input : [ "$test01" , "$test02" , "$test03" ] , method : 'approximate' } } } } ] ) Output: { studentId : '2345' , testMedians : 80 } , { studentId : '2356' , testMedians : 79 } , { studentId : '2358' , testMedians : 78 } , { studentId : '2367' , testMedians : 72 } , { studentId : '2369' , testMedians : 60 } When $median is an aggregation expression there is a result for
each studentId . Use $median in a $setWindowField Stage To base your percentile values on local data trends, use $median in a $setWindowField aggregation pipeline stage. This example creates a window to filter scores: db. testScores . aggregate ( [ { $setWindowFields : { sortBy : { test01 : 1 } , output : { test01_median : { $median : { input : "$test01" , method : 'approximate' } , window : { range : [ - 3 , 3 ] } } } } } , { $project : { _id : 0 , studentId : 1 , test01_median : 1 } } ] ) Output: { studentId : '2356' , test01_median : 60 } , { studentId : '2369' , test01_median : 60 } , { studentId : '2345' , test01_median : 60 } , { studentId : '2367' , test01_median : 64 } , { studentId : '2358' , test01_median : 64 } In this example, the median calculation for each document also
incorporates data from the three documents before and after it. Learn More The $percentile operator is a more general
version of the $median operator that allows you to set one or
more percentile values. For more information on window functions, see: $setWindowFields . Back $maxN-array-element Next $mergeObjects
