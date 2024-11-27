# $abs (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $abs (aggregation) On this page Definition Behavior Example Definition $abs Returns the absolute value of a number. $abs has the following syntax: { $abs : < number > } The <number> expression can be any valid expression as long as it resolves to a number. For
more information on expressions, see Expression Operators . Behavior If the argument resolves to a value of null or refers to a field that is
missing, $abs returns null . If the argument resolves to NaN , $abs returns NaN . Example Results { $abs: -1 } 1 { $abs: 1 } 1 { $abs: null } null Example A collection temperatureChange contains the following documents: db. temperatureChange . insertMany ( [ { _id : 1 , startTemp : 50 , endTemp : 80 } , { _id : 2 , startTemp : 40 , endTemp : 40 } , { _id : 3 , startTemp : 90 , endTemp : 70 } , { _id : 4 , startTemp : 60 , endTemp : 70 } ] ) The following example calculates the magnitude of difference between
the startTemp and endTemp ratings: db. temperatureChange . aggregate ( [ { $project : { delta : { $abs : { $subtract : [ "$startTemp" , "$endTemp" ] } } } } ]) The operation returns the following results: { "_id" : 1 , "delta" : 30 } { "_id" : 2 , "delta" : 0 } { "_id" : 3 , "delta" : 20 } { "_id" : 4 , "delta" : 10 } Back Operators Next $accumulator
