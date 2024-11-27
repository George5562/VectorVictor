# $toHashedIndexKey (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $toHashedIndexKey (aggregation) On this page Definition Syntax Example Learn More Definition $toHashedIndexKey Computes and returns the hash value of the input expression using
the same hash function that MongoDB uses to create a hashed index.
A hash function maps a key or string to a fixed-size numeric
value. Note Unlike hashed indexes, the $toHashedIndexKey aggregation operator does not account for collation.
This means the operator can produce a hash that does not
match that of a hashed index based on the same data. Syntax $toHashedIndexKey has the following syntax: { $toHashedIndexKey : < key or string to hash > } Example You can use $toHashedIndexKey to compute the hashed value of a
string in an aggregation pipeline. This example computes the hashed
value of the string "string to hash" : db. aggregate ( [ { $documents : [ { val : "string to hash" } ] } , { $addFields : { hashedVal : { $toHashedIndexKey : "$val" } } } ] ) Example output: [ { val : 'string to hash' , hashedVal : Long ( "763543691661428748" ) } ] Learn More convertShardKeyToHashed() Back $toDouble Next $toInt
