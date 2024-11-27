# $substr (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $substr (aggregation) On this page Definition Behavior Example Definition $substr Deprecated since version 3.4 : $substr is now an alias for $substrBytes . Returns a substring of a string, starting at a specified index
position and including the specified number of characters. The index
is zero-based. $substr has the following syntax: { $substr : [ < string > , < start > , < length > ] } The arguments can be any valid expression as long as the first argument
resolves to a string, and the second and third arguments resolve to
integers. For more information on expressions, see Expression Operators . Behavior If <start> is a negative number, $substr returns an
empty string "" . If <length> is a negative number, $substr returns a
substring that starts at the specified index and includes the rest of
the string. $substr only has a well-defined behavior for strings of ASCII characters. Example Consider an inventory collection with the following documents: { "_id" : 1 , "item" : "ABC1" , quarter : "13Q1" , "description" : "product 1" } { "_id" : 2 , "item" : "ABC2" , quarter : "13Q4" , "description" : "product 2" } { "_id" : 3 , "item" : "XYZ1" , quarter : "14Q2" , "description" : null } The following operation uses the $substr operator
to separate the quarter value into a yearSubstring and a quarterSubstring : db. inventory . aggregate ( [ { $project : { item : 1 , yearSubstring : { $substr : [ "$quarter" , 0 , 2 ] } , quarterSubtring : { $substr : [ "$quarter" , 2 , - 1 ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "ABC1" , "yearSubstring" : "13" , "quarterSubtring" : "Q1" } { "_id" : 2 , "item" : "ABC2" , "yearSubstring" : "13" , "quarterSubtring" : "Q4" } { "_id" : 3 , "item" : "XYZ1" , "yearSubstring" : "14" , "quarterSubtring" : "Q2" } Back $strLenCP Next $substrBytes
