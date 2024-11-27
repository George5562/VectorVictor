# $size (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $size (aggregation) On this page Definition Compatibility Syntax Behavior Example Definition $size Counts and returns the total number of items in an array. Compatibility You can use $size for deployments hosted in the following
environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Syntax $size has the following syntax: { $size : < expression > } The argument for $size can be any expression as long as it resolves to an array. For
more information on expressions, see Expression Operators . Behavior The argument for $size must resolve to an array. If the
argument for $size is missing or does not resolve to an
array, $size errors. Example Consider an inventory collection with the following documents: { "_id" : 1 , "item" : "ABC1" , "description" : "product 1" , colors : [ "blue" , "black" , "red" ] } { "_id" : 2 , "item" : "ABC2" , "description" : "product 2" , colors : [ "purple" ] } { "_id" : 3 , "item" : "XYZ1" , "description" : "product 3" , colors : [ ] } { "_id" : 4 , "item" : "ZZZ1" , "description" : "product 4 - missing colors" } { "_id" : 5 , "item" : "ZZZ2" , "description" : "product 5 - colors is string" , colors : "blue,red" } The following aggregation pipeline operation uses the $size operator to return the number of elements in the colors array: db. inventory . aggregate ( [ { $project : { item : 1 , numberOfColors : { $cond : { if : { $isArray : "$colors" } , then : { $size : "$colors" } , else : "NA" } } } } ] ) The operation returns the following: { "_id" : 1 , "item" : "ABC1" , "numberOfColors" : 3 } { "_id" : 2 , "item" : "ABC2" , "numberOfColors" : 1 } { "_id" : 3 , "item" : "XYZ1" , "numberOfColors" : 0 } { "_id" : 4 , "item" : "ZZZ1" , "numberOfColors" : "NA" } { "_id" : 5 , "item" : "ZZZ2" , "numberOfColors" : "NA" } Back $shift Next $sin
