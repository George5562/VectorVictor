# Sparse Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Properties Sparse Indexes On this page Create a Sparse Index Behavior Examples Sparse indexes only contain entries for documents that have the indexed
field, even if the index field contains a null value. The index skips
over any document that is missing the indexed field. The index is
"sparse" because it does not include all documents of a collection. By
contrast, non-sparse indexes contain all documents in a collection,
storing null values for those documents that do not contain the indexed
field. Important MongoDB provides the option to create partial indexes . Partial indexes
offer a superset of the functionality of sparse indexes.
Partial Indexes should be preferred over sparse indexes. Create a Sparse Index To create a sparse index, use the db.collection.createIndex() method with the sparse option set to true . For example, the following operation in mongosh creates a
sparse index on the xmpp_id field of the addresses collection: db. addresses . createIndex ( { "xmpp_id" : 1 } , { sparse : true } ) The index does not index documents that do not include the xmpp_id field. Note Do not confuse sparse indexes in MongoDB with block-level indexes in other databases. Think of them as dense indexes with a
specific filter. Behavior Sparse Index and Incomplete Results If a sparse index would result in an incomplete result set for queries
and sort operations, MongoDB will not use that index unless a hint() explicitly specifies the index. For example, the query { x: { $exists: false } } will not use a
sparse index on the x field unless explicitly hinted. See Sparse Index On A Collection Cannot Return Complete Results for an example that details the
behavior. If you include a hint() that specifies a sparse index when you perform a count() of all documents in a collection (i.e. with
an empty query predicate), the sparse index is used even if the sparse
index results in an incorrect count. db. collection . insertOne ( { _id : 1 , y : 1 } ) ; db. collection . createIndex ( { x : 1 } , { sparse : true } ) ; db. collection . find ( ). hint ( { x : 1 } ). count ( ) ; To obtain the correct count, do not hint() with a sparse index when performing a count of all
documents in a collection. db. collection . find ( ). count ( ) ; db. collection . createIndex ( { y : 1 } ) ; db. collection . find ( ). hint ( { y : 1 } ). count ( ) ; Indexes that are Sparse by Default The following index types are always sparse: 2d 2dsphere (version 2) Text Wildcard Sparse Compound Indexes Compound indexes can contain different types of sparse indexes. The
combination of index types determines how the compound index matches
documents. This table summarizes the behavior of a compound index that contains
different types of sparse indexes: Compound Index Components Compound Index Behavior Ascending indexes Descending indexes Only indexes documents that contain a value for at least one of
the keys. Ascending indexes Descending indexes Geospatial indexes Only indexes a document when it contains a value for one of
the geospatial fields. Does not index documents in the
ascending or descending indexes. Ascending indexes Descending indexes Text indexes Only indexes a document when it matches one of the text fields. Does not index documents in the ascending or descending
indexes. Sparse and Unique Properties An index that is both sparse and unique prevents a collection from having documents with duplicate values for a
field but allows multiple documents that omit the key. Examples Create a Sparse Index On A Collection Consider a collection scores that contains the following documents: { "_id" : ObjectId ( "523b6e32fb408eea0eec2647" ) , "userid" : "newbie" } { "_id" : ObjectId ( "523b6e61fb408eea0eec2648" ) , "userid" : "abby" , "score" : 82 } { "_id" : ObjectId ( "523b6e6ffb408eea0eec2649" ) , "userid" : "nina" , "score" : 90 } The collection has a sparse index on the field score : db. scores . createIndex ( { score : 1 } , { sparse : true } ) Then, the following query on the scores collection uses the sparse
index to return the documents that have the score field less than
( $lt ) 90 : db. scores . find ( { score : { $lt : 90 } } ) Because the document for the userid "newbie" does not contain the score field and thus does not meet the query criteria, the query
can use the sparse index to return the results: { "_id" : ObjectId ( "523b6e61fb408eea0eec2648" ) , "userid" : "abby" , "score" : 82 } Sparse Index On A Collection Cannot Return Complete Results Consider a collection scores that contains the following documents: { "_id" : ObjectId ( "523b6e32fb408eea0eec2647" ) , "userid" : "newbie" } { "_id" : ObjectId ( "523b6e61fb408eea0eec2648" ) , "userid" : "abby" , "score" : 82 } { "_id" : ObjectId ( "523b6e6ffb408eea0eec2649" ) , "userid" : "nina" , "score" : 90 } The collection has a sparse index on the field score : db. scores . createIndex ( { score : 1 } , { sparse : true } ) Because the document for the userid "newbie" does not contain the score field, the sparse index does not contain an entry for that
document. Consider the following query to return all documents in the scores collection, sorted by the score field: db. scores . find ( ). sort ( { score : - 1 } ) Even though the sort is by the indexed field, MongoDB will not select the sparse index to fulfill the query in order to return
complete results: { "_id" : ObjectId ( "523b6e6ffb408eea0eec2649" ) , "userid" : "nina" , "score" : 90 } { "_id" : ObjectId ( "523b6e61fb408eea0eec2648" ) , "userid" : "abby" , "score" : 82 } { "_id" : ObjectId ( "523b6e32fb408eea0eec2647" ) , "userid" : "newbie" } To use the sparse index, explicitly specify the index with hint() : db. scores . find ( ). sort ( { score : - 1 } ). hint ( { score : 1 } ) The use of the index results in the return of only those documents with
the score field: { "_id" : ObjectId ( "523b6e6ffb408eea0eec2649" ) , "userid" : "nina" , "score" : 90 } { "_id" : ObjectId ( "523b6e61fb408eea0eec2648" ) , "userid" : "abby" , "score" : 82 } Tip See also: explain() Interpret Explain Plan Results Sparse Index with Unique Constraint Consider a collection scores that contains the following documents: { "_id" : ObjectId ( "523b6e32fb408eea0eec2647" ) , "userid" : "newbie" } { "_id" : ObjectId ( "523b6e61fb408eea0eec2648" ) , "userid" : "abby" , "score" : 82 } { "_id" : ObjectId ( "523b6e6ffb408eea0eec2649" ) , "userid" : "nina" , "score" : 90 } You could create an index with a unique constraint and sparse filter on the score field using
the following operation: db. scores . createIndex ( { score : 1 } , { sparse : true , unique : true } ) This index would permit the insertion of documents that had unique
values for the score field or did not include a score field.
As such, given the existing documents in the scores collection, the
index permits the following insert operations : db. scores . insertMany ( [ { "userid" : "newbie" , "score" : 43 } , { "userid" : "abby" , "score" : 34 } , { "userid" : "nina" } ] ) However, the index would not permit the addition of the following
documents since documents already exists with score value of 82 and 90 : db. scores . insertMany ( [ { "userid" : "newbie" , "score" : 82 } , { "userid" : "abby" , "score" : 90 } ] ) Sparse and Non-Sparse Unique Indexes Starting in MongoDB 5.0, unique sparse and unique non-sparse indexes with the same key pattern can exist on a single collection. Unique and Sparse Index Creation This example creates multiple indexes with the same key pattern and
different sparse options: db. scoreHistory . createIndex ( { score : 1 } , { name : "unique_index" , unique : true } ) db. scoreHistory . createIndex ( { score : 1 } , { name : "unique_sparse_index" , unique : true , sparse : true } ) Basic and Sparse Index Creation You can also create basic indexes with the same key pattern with and
without the sparse option: db. scoreHistory . createIndex ( { score : 1 } , { name : "sparse_index" , sparse : true } ) db. scoreHistory . createIndex ( { score : 1 } , { name : "basic_index" } ) Back Partial Next TTL
