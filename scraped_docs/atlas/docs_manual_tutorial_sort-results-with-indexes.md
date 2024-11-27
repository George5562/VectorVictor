# Use Indexes to Sort Query Results - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Strategies Use Indexes to Sort Query Results On this page Sort with a Single Field Index Sort on Multiple Fields Index Sort Order Index Use and Collation Examples Since indexes contain ordered records, MongoDB can obtain the results of
a sort from an index that includes the sort fields. MongoDB may use multiple indexes to support a sort operation if the sort uses the
same indexes as the query predicate. If MongoDB cannot use an index or indexes to obtain the sort
order, MongoDB must perform a blocking sort operation on the data.
A blocking sort indicates that MongoDB must consume and process all
input documents to the sort before returning results. Blocking sorts do
not block concurrent operations on the collection or database. Starting in MongoDB 6.0, if the server requires more than 100 megabytes
of memory for a pipeline execution stage, MongoDB automatically writes
temporary files to disk unless that query specifies { allowDiskUse: false } . If the server needs more than 100 megabytes of
system memory for the blocking sort operation, MongoDB returns an error unless
that query specifies cursor.allowDiskUse() . For details, see allowDiskUseByDefault . Sort operations that use an index often have better performance than
blocking sorts. Note When you sort based on an array field that is indexed with a multikey index , the query plan includes a blocking sort stage unless both of the following are true: The index boundaries for
all sort fields are [MinKey, MaxKey] . No boundaries for any multikey-indexed field have the same path prefix
as the sort pattern. Sort with a Single Field Index If an ascending or a descending index is on a single field, the sort
operation on the field can be in either direction. For example, create an ascending index on the field a for a
collection records : db. records . createIndex ( { a : 1 } ) This index can support an ascending sort on a : db. records . find ( ). sort ( { a : 1 } ) The index can also support the following descending sort on a by
traversing the index in reverse order: db. records . find ( ). sort ( { a : - 1 } ) Sort on Multiple Fields Create a compound index to support sorting
on multiple fields. You can specify a sort on all the keys of the index or on a subset;
however, the sort keys must be listed in the same order as they
appear in the index. For example, an index key pattern { a: 1, b: 1
} can support a sort on { a: 1, b: 1 } but not on { b: 1, a:
1 } . For a query to use a compound index for a sort, the specified sort direction
for all keys in the cursor.sort() document must match the index
key pattern or match the inverse of the index key pattern.
For example, an index key pattern { a: 1, b: -1 } can
support a sort on { a: 1, b: -1 } and { a: -1, b: 1 } but not on { a: -1, b: -1 } or {a: 1, b: 1} . Sort and Index Prefix If the sort keys correspond to the index keys or an index prefix ,
MongoDB can use the index to sort the query results. A prefix of a
compound index is a subset that consists of one or more keys at the
start of the index key pattern. For example, create a compound index on the data collection: db. data . createIndex ( { a : 1 , b : 1 , c : 1 , d : 1 } ) Then, the following are prefixes for that index: { a : 1 } { a : 1 , b : 1 } { a : 1 , b : 1 , c : 1 } The following query and sort operations use the index prefixes to sort
the results. These operations do not need to sort the result set in
memory. Example Index Prefix db.data.find().sort( { a: 1 } ) { a: 1 } db.data.find().sort( { a: -1 } ) { a: 1 } db.data.find().sort( { a: 1, b: 1 } ) { a: 1, b: 1 } db.data.find().sort( { a: -1, b: -1 } ) { a: 1, b: 1 } db.data.find().sort( { a: 1, b: 1, c: 1 } ) { a: 1, b: 1, c: 1 } db.data.find( { a: { $gt: 4 } } ).sort( { a: 1, b: 1 } ) { a: 1, b: 1 } Consider the following example in which the prefix keys of the index
appear in both the query predicate and the sort: db. data . find ( { a : { $gt : 4 } } ). sort ( { a : 1 , b : 1 } ) In such cases, MongoDB can use the index to retrieve the documents in
order specified by the sort. As the example shows, the index prefix in
the query predicate can be different from the prefix in the sort. Sort and Non-prefix Subset of an Index An index can support sort operations on a non-prefix subset of the
index key pattern. To do so, the query must include equality conditions on all the prefix keys that precede the sort keys. For example, the collection data has the following index: { a : 1 , b : 1 , c : 1 , d : 1 } The following operations can use the index to get the sort order: Example Index Prefix db.data.find( { a: 5 } ).sort( { b: 1, c: 1 } ) { a: 1 , b: 1, c: 1 } db.data.find( { b: 3, a: 4 } ).sort( { c: 1 } ) { a: 1, b: 1, c: 1 } db.data.find( { a: 5, b: { $lt: 3} } ).sort( { b: 1 } ) { a: 1, b: 1 } As the last operation shows, only the index fields preceding the sort
subset must have the equality conditions in the query document; the
other index fields may specify other conditions. If the query does not specify an equality condition on an index
prefix that precedes or overlaps with the sort specification, the
operation will not efficiently use the index. For example, the
following operations specify a sort document of { c: 1 } , but the
query documents do not contain equality matches on the preceding index
fields a and b : db. data . find ( { a : { $gt : 2 } } ). sort ( { c : 1 } ) db. data . find ( { c : 5 } ). sort ( { c : 1 } ) These operations will not efficiently use the index { a: 1, b: 1,
c: 1, d: 1 } and may not even use the index to retrieve the documents. Index Sort Order A collection of indexed documents may have multiple data types in the
key field. When an index has a key with multiple data types, the index is
sorted according to the BSON type sort order . In array comparisons: An ascending sort compares the smallest
elements of the array according to the BSON type sort order. A descending sort compares the largest elements of the array according
to the reverse BSON type sort order. Comparison Query Operators , such as $lt and $gt ,
perform comparisons on arrays lexicographically. When comparing a field whose value is a one element array (for example, [ 1 ] ) with non-array fields (for example, 2 ), the comparison is
for 1 and 2 . A comparison of an empty array (for example, [ ] ) considers the empty
array as less than a null value or a missing field value. A comparison of a nested array (for example, [[1, 2], [3, 4]] ) compares
any array after the outmost array lexicographically. See the index sorting example . Index Use and Collation To use an index for string comparisons, an operation must also
specify the same collation. That is, an index with a collation
cannot support an operation that performs string comparisons on the
indexed fields if the operation specifies a different collation. Warning Because indexes that are configured with collation use ICU
collation keys to achieve sort order, collation-aware index keys
may be larger than index keys for indexes without collation. For example, the collection myColl has an index on a string
field category with the collation locale "fr" . db. myColl . createIndex ( { category : 1 } , { collation : { locale : "fr" } } ) The following query operation, which specifies the same collation as
the index, can use the index: db. myColl . find ( { category : "cafe" } ). collation ( { locale : "fr" } ) However, the following query operation, which by default uses the
"simple" binary collator, cannot use the index: db. myColl . find ( { category : "cafe" } ) For a compound index where the index prefix keys are not strings,
arrays, and embedded documents, an operation that specifies a
different collation can still use the index to support comparisons
on the index prefix keys. For example, the collection myColl has a compound index on the
numeric fields score and price and the string field category ; the index is created with the  collation locale "fr" for string comparisons: db. myColl . createIndex ( { score : 1 , price : 1 , category : 1 } , { collation : { locale : "fr" } } ) The following operations, which use "simple" binary collation
for string comparisons, can use the index: db. myColl . find ( { score : 5 } ). sort ( { price : 1 } ) db. myColl . find ( { score : 5 , price : { $gt : NumberDecimal ( "10" ) } } ). sort ( { price : 1 } ) The following operation, which uses "simple" binary collation
for string comparisons on the indexed category field, can use
the index to fulfill only the score: 5 portion of the query: db. myColl . find ( { score : 5 , category : "cafe" } ) Important Matches against document keys, including embedded document keys,
use simple binary comparison. This means that a query for a key
like "foo.bÃ¡r" will not match the key "foo.bar", regardless of the value you
set for the strength parameter. Examples The following example demonstrates sorting when index keys have the
same or different types. Create the keyTypes collection: db. keyTypes . insertMany ( [ { seqNum : 1 , seqType : null , type : "null" } , { seqNum : 29 , seqType : null , type : "null" } , { seqNum : 2 , seqType : Int32 ( "10" ) , type : "Int32" } , { seqNum : 28 , seqType : Int32 ( "10" ) , type : "Int32" } , { seqNum : 3 , seqType : Long ( "10" ) , type : "Long" } , { seqNum : 27 , seqType : Long ( "10" ) , type : "Long" } , { seqNum : 4 , seqType : Decimal128 ( "10" ) , type : "Decimal128" } , { seqNum : 26 , seqType : Decimal128 ( "10" ) , type : "Decimal128" } , { seqNum : 5 , seqType : Double ( "10" ) , type : "Double" } , { seqNum : 25 , seqType : Double ( "10" ) , type : "Double" } , { seqNum : 6 , seqType : String ( "10" ) , type : "String" } , { seqNum : 24 , seqType : String ( "10" ) , type : "String" } , { seqNum : 7 , seqType : [ "1" , "2" , "3" ] , type : "Array" } , { seqNum : 23 , seqType : [ "1" , "2" , "3" ] , type : "Array" } , { seqNum : 8 , seqType : [ [ 1 ] , [ 2 ] , [ 3 ] ] , type : "Array" } , { seqNum : 22 , seqType : [ [ 1 ] , [ 2 ] , [ 3 ] ] , type : "Array " } , { seqNum : 9 , seqType : [ 1 , 2 , 3 ] , type : "Array" } , { seqNum : 21 , seqType : [ 1 , 2 , 3 ] , type : "Array" } , { seqNum : 10 , seqType : true , type : "Boolean" } , { seqNum : 11 , seqType : new Timestamp ( ) , type : "Timestamp" } , { seqNum : 12 , seqType : new Date ( ) , type : "Date" } , { seqNum : 13 , seqType : new ObjectId ( ) , type : "ObjectId" } , ] ) Create indexes on the sequence number ( seqNum ) and sequence type
( seqType ) fields: db. keyTypes . createIndex ( { seqNum : 1 } ) db. keyTypes . createIndex ( { seqType : 1 } ) Query the collection using find() .
The projection document, { _id: 0 } , suppresses the _id field
in the output display. db. keyTypes . find ( { } , { _id : 0 } ) The documents are returned in insertion order: { seqNum: 1, seqType: null, type: 'null' }, { seqNum: 29, seqType: null, type: 'null' }, { seqNum: 2, seqType: 10, type: 'Int32' }, { seqNum: 28, seqType: 10, type: 'Int32' }, { seqNum: 3, seqType: Long("10"), type: 'Long' }, { seqNum: 27, seqType: Long("10"), type: 'Long' }, { seqNum: 4, seqType: Decimal128("10"), type: 'Decimal128' }, // Output truncated The sequence number ( seqNum ) index has values of the same type.
Use the seqNum index to query the keyTypes collection: db. keyTypes . find ( { } , { _id : 0 } ). sort ( { seqNum : 1 } ) The seqNum keys are integers. The documents are returned in
numerical order: { seqNum: 1, seqType: null, type: 'null' }, { seqNum: 2, seqType: 10, type: 'Int32' }, { seqNum: 3, seqType: Long("10"), type: 'Long' }, { seqNum: 4, seqType: Decimal128("10"), type: 'Decimal128' }, { seqNum: 5, seqType: 10, type: 'Double' }, { seqNum: 6, seqType: '10', type: 'String' }, { seqNum: 7, seqType: [ '1', '2', '3' ], type: 'Array' }, // Output truncated The sequence type ( seqType ) index has values of the different
types. Use the seqType index to query the keyTypes collection: db. keyTypes . find ( { } , { _id : 0 } ). sort ( { seqType : 1 } ) The documents are returned in BSON type sort order : { seqNum: 1, seqType: null, type: 'null' }, { seqNum: 29, seqType: null, type: 'null' }, { seqNum: 9, seqType: [ 1, 2, 3 ], type: 'Array' }, { seqNum: 21, seqType: [ 1, 2, 3 ], type: 'Array' }, { seqNum: 2, seqType: 10, type: 'Int32' }, { seqNum: 28, seqType: 10, type: 'Int32' }, { seqNum: 3, seqType: Long("10"), type: 'Long' }, { seqNum: 27, seqType: Long("10"), type: 'Long' }, { seqNum: 4, seqType: Decimal128("10"), type: 'Decimal128' }, { seqNum: 26, seqType: Decimal128("10"), type: 'Decimal128' }, { seqNum: 5, seqType: 10, type: 'Double' }, { seqNum: 25, seqType: 10, type: 'Double' }, { seqNum: 7, seqType: [ '1', '2', '3' ], type: 'Array' }, { seqNum: 23, seqType: [ '1', '2', '3' ], type: 'Array' }, { seqNum: 6, seqType: '10', type: 'String' }, { seqNum: 24, seqType: '10', type: 'String' }, { seqNum: 8, seqType: [ [ 1 ], [ 2 ], [ 3 ] ], type: 'Array' }, { seqNum: 22, seqType: [ [ 1 ], [ 2 ], [ 3 ] ], type: 'Array ' }, { seqNum: 13, seqType: ObjectId("6239e3922604d5a7478df071"), type: 'ObjectId' }, { seqNum: 10, seqType: true, type: 'Boolean' }, { seqNum: 12, seqType: ISODate("2022-03-22T14:56:18.100Z"), type: 'Date' }, { seqNum: 11, seqType: Timestamp({ t: 1647960978, i: 1 }), type: 'Timestamp' } In array comparisons: An ascending sort compares the smallest
elements of the array according to the BSON type sort order. A descending sort compares the largest elements of the array according
to the reverse BSON type sort order. Comparison Query Operators , such as $lt and $gt ,
perform comparisons on arrays lexicographically. When comparing a field whose value is a one element array (for example, [ 1 ] ) with non-array fields (for example, 2 ), the comparison is
for 1 and 2 . A comparison of an empty array (for example, [ ] ) considers the empty
array as less than a null value or a missing field value. A comparison of a nested array (for example, [[1, 2], [3, 4]] ) compares
any array after the outmost array lexicographically. Numerical types (Int32, Long, Decimal128, Double) are equivalent when
compared with other types. Within the Numbers BSON type, numerical types are sorted: Int32 Long Decimal128 Double Back Equality, Sort, Range Rule Next Ensure Query Selectivity
