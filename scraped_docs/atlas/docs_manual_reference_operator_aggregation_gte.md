# $gte (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $gte (aggregation) On this page Definition Example Definition $gte Compares two values and returns: true when the first value is greater than or equal to the
second value. false when the first value is less than the second value. The $gte compares both value and type, using the specified BSON comparison order for values of different types. $gte has the following syntax: { $gte : [ < expression1 > , < expression2 > ] } For more information on expressions, see Expression Operators . Example Create an inventory collection with these documents: db. inventory . insertMany ( [ { _id : 1 , item : "abc1" , description : "product 1" , qty : 300 } , { _id : 2 , item : "abc2" , description : "product 2" , qty : 200 } , { _id : 3 , item : "xyz1" , description : "product 3" , qty : 250 } , { _id : 4 , item : "VWZ1" , description : "product 4" , qty : 300 } , { _id : 5 , item : "VWZ2" , description : "product 5" , qty : 180 } ] ) Use the $gte operator to determine if qty is greater than or
equal to 250 : db. inventory . aggregate ( [ { $project : { item : 1 , qty : 1 , qtyGte250 : { $gte : [ "$qty" , 250 ] } , _id : 0 } } ] ) Output: { item : "abc1" , qty : 300 , qtyGte250 : true } { item : "abc2" , qty : 200 , qtyGte250 : false } { item : "xyz1" , qty : 250 , qtyGte250 : true } { item : "VWZ1" , qty : 300 , qtyGte250 : true } { item : "VWZ2" , qty : 180 , qtyGte250 : false } Back $gt Next $hour