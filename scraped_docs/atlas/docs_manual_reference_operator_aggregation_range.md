# $range (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $range (aggregation) On this page Definition Behavior Example Definition $range Returns an array whose elements are a generated sequence of numbers. $range generates the sequence from the specified
starting number by successively incrementing the starting number by
the specified step value up to but not including the end point. $range has the following operator
expression syntax : { $range : [ < start > , < end > , < non-zero step > ] } Operand Description <start> An integer that specifies the start of the sequence. Can be
any valid expression that resolves to an integer. <end> An integer that specifies the exclusive upper limit of the
sequence. Can be any valid expression that resolves to an integer. <non-zero step> Optional. An integer that specifies the increment value.
Can be any valid expression that resolves to a non-zero integer. Defaults to 1. Behavior The <start> and <end> arguments are required and must be
integers. The <non-zero step> argument is optional, and defaults
to 1 if omitted. Example Results { $range: [ 0, 10, 2 ] } [ 0, 2, 4, 6, 8 ] { $range: [ 10, 0, -2 ] } [ 10, 8, 6, 4, 2 ] { $range: [ 0, 10, -2 ] } [ ] { $range: [ 0, 5 ] } [ 0, 1, 2, 3, 4 ] Example The following example uses a collection called distances that lists cities along with their distance in miles from San
Francisco. Documents in the distances collection: db. distances . insertMany ( [ { _id : 0 , city : "San Jose" , distance : 42 } , { _id : 1 , city : "Sacramento" , distance : 88 } , { _id : 2 , city : "Reno" , distance : 218 } , { _id : 3 , city : "Los Angeles" , distance : 383 } ]) ; A bicyclist is planning to ride from San
Francisco to each city listed in the
collection and wants to stop and rest every 25 miles.
The following aggregation pipeline
operation uses the $range operator to determine
the stopping points for each trip. db. distances . aggregate ( [ { $project : { _id : 0 , city : 1 , "Rest stops" : { $range : [ 0 , "$distance" , 25 ] } } }]) The operation returns the following: { "city" : "San Jose" , "Rest stops" : [ 0 , 25 ] } { "city" : "Sacramento" , "Rest stops" : [ 0 , 25 , 50 , 75 ] } { "city" : "Reno" , "Rest stops" : [ 0 , 25 , 50 , 75 , 100 , 125 , 150 , 175 , 200 ] } { "city" : "Los Angeles" , "Rest stops" : [ 0 , 25 , 50 , 75 , 100 , 125 , 150 , 175 , 200 , 225 , 250 , 275 , 300 , 325 , 350 , 375 ] } Back $rand Next $rank
