# Create an Index on an Array Field - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Multikey Create an Index on an Array Field On this page About this Task Procedure Results Learn More You can create an index on a field containing an array value to improve
performance for queries on that field. When you create an index on a
field containing an array value, MongoDB stores that index as a multikey
index. To create an index, use the db.collection.createIndex() method. Your operation should resemble this prototype: db. < collection > . createIndex ( { < field > : < sortOrder > } ) About this Task The example on this page uses a students collection that contains
these documents: db. students . insertMany ( [ { "name" : "Andre Robinson" , "test_scores" : [ 88 , 97 ] } , { "name" : "Wei Zhang" , "test_scores" : [ 62 , 73 ] } , { "name" : "Jacob Meyer" , "test_scores" : [ 92 , 89 ] } ] ) You regularly run a query that returns students with at least one test_score greater than 90 . You can create an index on the test_scores field to improve performance for this query. Procedure The following operation creates an ascending multikey index on the test_scores field of the students collection: db. students . createIndex ( { test_scores : 1 } ) Because test_scores contains an array value, MongoDB stores this
index as a multikey index. Results The index contains a key for each individual value that appears in the test_scores field. The index is ascending, meaning the keys are
stored in this order: [ 62, 73, 88, 89, 92, 97 ] . The index supports queries that select on the test_scores field. For
example, the following query returns documents where at least one
element in the test_scores array is greater than 90: db. students . find ( { test_scores : { $elemMatch : { $gt : 90 } } } ) Output: [ { _id : ObjectId ( "632240a20646eaee87a56a80" ) , name : 'Andre Robinson' , test_scores : [ 88 , 97 ] } , { _id : ObjectId ( "632240a20646eaee87a56a82" ) , name : 'Jacob Meyer' , test_scores : [ 92 , 89 ] } ] Learn More To learn how to create a multikey index on embedded document fields,
see Create an Index on an Embedded Field in an Array . To learn about multikey index bounds, see Multikey Index Bounds . Back Multikey Next Embedded Array Field
