# $concat (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $concat (aggregation) On this page Definition Example Definition $concat Concatenates strings and returns the concatenated string. $concat has this syntax: { $concat : [ < expression1 > , < expression2 > , ... ] } The arguments can be any valid expression as long as they resolve to
strings. For more information on expressions, see Expression Operators . If the argument resolves to a value of null or refers to a field
that is missing, $concat returns null . Example Create an inventory collection with these documents: db. inventory . insertMany ( [ { _id : 1 , item : "ABC1" , quarter : "13Q1" , description : "product 1" } , { _id : 2 , item : "ABC2" , quarter : "13Q4" , description : "product 2" } , { _id : 3 , item : "XYZ1" , quarter : "14Q2" , description : null } ] ) Use the $concat operator to concatenate the item field and the description field with a " - " delimiter: db. inventory . aggregate ( [ { $project : { itemDescription : { $concat : [ "$item" , " - " , "$description" ] } } } ] ) Output: { _id : 1 , itemDescription : "ABC1 - product 1" } { _id : 2 , itemDescription : "ABC2 - product 2" } { _id : 3 , itemDescription : null } Back $cmp Next $concatArrays