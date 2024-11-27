# $trunc (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $trunc (aggregation) On this page Definition Syntax Behavior Example Definition $trunc $trunc truncates a number to a whole integer or to a
specified decimal place. Syntax The $trunc operator has the following syntax: { $trunc : [ < number > , < place > ] } Field Type Description <number> number Can be any valid expression that resolves to a number. Specifically, the expression must
resolve to an integer, double, decimal ,
or long . $trunc returns an error if the expression
resolves to a non-numeric data type. <place> integer Optional Can be any valid expression that resolves to an integer between -20 and 100, exclusive. For example, -20 < place < 100 . Defaults to 0 if unspecified. If <place> resolves to a positive integer, $trunc truncates to <place> decimal places. For example, $trunc : [1234.5678, 2] truncates to two
decimal  places and returns 1234.56 . If <place> resolves to a negative integer, $trunc replaces <place> digits left of the decimal with 0 . For example, $trunc : [1234.5678, -2] replaces to two
digits left of the decimal with 0 and returns 1200 . If the absolute value of <place> exceeds the number of
digits to the left of the decimal, $trunc returns 0 . For example, $trunc : [ 1234.5678, -5] specifies the
fifth digit left of the decimal. This exceeds the
number of digits left of the decimal and returns 0 . If <place> resolves to 0 , $trunc truncates all digits to the right of the decimal and returns
the whole integer value. For example, $trunc : [1234.5678, 0] returns 1234 The <number> expression can be any valid expression as long as it resolves to a number. For
more information on expressions, see Expression Operators . Behavior $trunc does not round the truncated data. To round
input values to a specified place, use the $round expression. Returned Data Type The returned data type matches the data type of the input expression
or value. null , NaN , and +/- Infinity If the argument resolves to a value of null or refers to a field
that is  missing, $trunc returns null . If the argument resolves to NaN , $trunc returns NaN . If the argument resolves to negative or positive infinity, $trunc returns negative or positive infinity
respectively. Example Results { $trunc: [ NaN, 1] } NaN { $trunc: [ null, 1] } null { $trunc : [ Infinity, 1 ] } Infinity { $trunc : [ -Infinity, 1 ] } -Infinity Example Create a collection named samples with the following documents: db. samples . insertMany ( [ { _id : 1 , value : 19.25 } , { _id : 2 , value : 28.73 } , { _id : 3 , value : 34.32 } , { _id : 4 , value : - 45.34 } ] ) The following aggregation returns value truncated to the first
decimal place: db. samples . aggregate ( [ { $project : { truncatedValue : { $trunc : [ "$value" , 1 ] } } } ]) The operation returns the following results: { "_id" : 1 , "truncatedValue" : 19.2 } { "_id" : 2 , "truncatedValue" : 28.7 } { "_id" : 3 , "truncatedValue" : 34.3 } { "_id" : 4 , "truncatedValue" : - 45.3 } The following aggregation returns value truncated to the first
place: db. samples . aggregate ( [ { $project : { truncatedValue : { $trunc : [ "$value" , - 1 ] } } } ]) The operation returns the following results: { "_id" : 1 , "truncatedValue" : 10 } { "_id" : 2 , "truncatedValue" : 20 } { "_id" : 3 , "truncatedValue" : 30 } { "_id" : 4 , "truncatedValue" : - 40 } The following aggregation returns``value`` truncated to the whole
integer: db. samples . aggregate ( [ { $project : { truncatedValue : { $trunc : [ "$value" , 0 ] } } } ]) The operation returns the following results: { "_id" : 1 , "truncatedValue" : 19 } { "_id" : 2 , "truncatedValue" : 28 } { "_id" : 3 , "truncatedValue" : 34 } { "_id" : 4 , "truncatedValue" : - 45 } Back $trim Next $type
