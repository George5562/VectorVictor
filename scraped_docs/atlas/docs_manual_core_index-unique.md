# Unique Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Properties Unique Indexes On this page Create a Unique Index Behavior A unique index ensures that the indexed fields do not store duplicate
values. A unique index on a single field ensures that a value appears
at most once for a given field. A unique compound index ensures that
any given combination of the index key values only appears at most
once. By default, MongoDB creates a unique index on the _id field during the creation of a collection. You can create and manage unique indexes in the UI for deployments hosted in MongoDB Atlas . Create a Unique Index To create a unique index, use the db.collection.createIndex() method with the unique option set to true . db. collection . createIndex ( < key and index type specification > , { unique: true } ) Unique Index on a Single Field For example, to create a unique index on the user_id field of the members collection, use the following operation in mongosh : db. members . createIndex ( { "user_id" : 1 } , { unique : true } ) Unique Compound Index You can also enforce a unique constraint on compound indexes . A unique compound index enforces uniqueness on the combination of the
index key values. For example, to create a unique index on groupNumber , lastname ,
and firstname fields of the members collection, use the
following operation in mongosh : db. members . createIndex ( { groupNumber : 1 , lastname : 1 , firstname : 1 } , { unique : true } ) The created index enforces uniqueness for the combination of groupNumber , lastname , and firstname values. For another example, consider a collection with the following document: { _id : 1 , a : [ { loc : "A" , qty : 5 } , { qty : 10 } ] } Create a unique compound multikey index
on a.loc and a.qty : db. collection . createIndex ( { "a.loc" : 1 , "a.qty" : 1 } , { unique : true } ) The unique index permits the insertion of the following documents into
the collection since the index enforces uniqueness for the combination of a.loc and a.qty values: db. collection . insertMany ( [ { _id : 2 , a : [ { loc : "A" } , { qty : 5 } ] } , { _id : 3 , a : [ { loc : "A" , qty : 10 } ] } ] ) Tip See also: Unique Constraint Across Separate Documents Missing Document Field in a Unique Single-Field Index Behavior Restrictions MongoDB cannot create a unique index on the
specified index field(s) if the collection already contains data that
would violate the unique constraint for the index. You may not specify a unique constraint on a hashed
index . Building Unique Index on Replica Sets and Sharded Clusters For replica sets and sharded clusters, using a rolling procedure to create a unique index
requires that you stop all writes to the collection during the
procedure. If you cannot stop all writes to the collection during the
procedure, do not use the rolling procedure. Instead, to build your
unique index on the collection you must either: Run db.collection.createIndex() on the primary for a
replica set Run db.collection.createIndex() on the mongos for a sharded cluster Unique Constraint Across Separate Documents The unique constraint applies to separate documents in the collection.
That is, the unique index prevents separate documents from having the
same value for the indexed key. Because the constraint applies to separate documents, for a unique multikey index, a document may have array
elements that result in repeating index key values as long as the index
key values for that document do not duplicate those of another
document. In this case, the repeated index entry is inserted into the
index only once. For example, consider a collection with the following documents: { _id : 1 , a : [ { loc : "A" , qty : 5 } , { qty : 10 } ] } { _id : 2 , a : [ { loc : "A" } , { qty : 5 } ] } { _id : 3 , a : [ { loc : "A" , qty : 10 } ] } Create a unique compound multikey index on a.loc and a.qty : db. collection . createIndex ( { "a.loc" : 1 , "a.qty" : 1 } , { unique : true } ) The unique index permits the insertion of the following document into
the collection if no other document in the collection has an index key
value of { "a.loc": "B", "a.qty": null } . db. collection . insertOne ( { _id : 4 , a : [ { loc : "B" } , { loc : "B" } ] } ) Missing Document Field in a Unique Single-Field Index If a document has a null or missing value for the indexed field in a unique
single-field index, the index stores a null value for that document.
Because of the unique constraint, a single-field unique index can only
contain one document that contains a null value in its index entry. If there is
more than one document with a null value in its index entry, the index
build fails with a duplicate key error. For example, a collection has a unique single-field index on x : db. collection . createIndex ( { "x" : 1 } , { unique : true } ) The unique index allows the insertion of a document without the field x if the collection does not already contain a document missing the
field x : db. collection . insertOne ( { y : 1 } ) However, you cannot insert a document without the field x if the
collection already contains a document missing the field x : db. collection . insertOne ( { z : 1 } ) The operation fails to insert the document because of the violation of
the unique constraint on the value of the field x : WriteResult ( { "nInserted" : 0 , "writeError" : { "code" : 11000 , "errmsg" : "E11000 duplicate key error index: test.collection.$a.b_1 dup key: { : null }" } }) Missing Document Fields in a Unique Compound Index If a document has a null or missing value for one or more indexed
fields in a unique compound index, the index stores a null value for
each null or missing field in the document's index entry. Because of
the unique constraint, a unique compound index only permits one document
that has a null value for all indexed fields in an index entry. If
there is more than one index entry with a null value for all indexed
fields, the index build fails with a duplicate key error. MongoDB
permits multiple documents with missing fields in unique compound
indexes as long as each index entry is unique. For example, a collection students has a unique compound index on fields name , age , and grade : db. students . createIndex ( { "name" : 1 , "age" : - 1 , "grade" : 1 } , { unique : true } ) If the collection does not already contain identical documents, the
unique compound index allows the insertion of the following documents
that are all missing the grade field. db. students . insertMany ( { "name" : "Meredith" , "age" : 12 } , { "name" : "Olivia" , "age" : 11 } , { "name" : "Benjamin" } ) However, you cannot insert a document that has the same index key (value
for name , age , and grade ) as another document in the
collection. db. students . insertOne ( { name : "Meredith" , age : 12 } ) The operation fails to insert the document because of the violation of
the unique constraint on the values of the fields name , age , and grade : WriteResult ( { "nInserted" : 0 , "writeError" : { "code" : 11000 , "errmsg" : "E11000 duplicate key error collection: test.students index: name_1_age_-1_grade_1 dup key: { name: " Meredith ", age: 12, grade: null } } } ) You also cannot insert a document that is unique but shares an index
key with an existing index entry. db. students . insertOne ( { name : "Olivia" , "age" : 11 , "favorite color" : "red" } ) The operation fails to insert the document because of the violation of
the unique constraint on the values of the fields name , age , and grade : WriteResult ( { "nInserted" : 0 , "writeError" : { "code" : 11000 , "errmsg" : "E11000 duplicate key error collection: test.students index: name_1_age_-1_grade_1 dup key: { name: " Olivia ", age: 11, grade: null } } } ) Unique Partial Indexes Partial indexes only index the documents in a collection that meet a
specified filter expression. If you specify both the partialFilterExpression and a unique constraint , the unique constraint only applies to the
documents that meet the filter expression. A partial index with a unique constraint does not prevent the insertion
of documents that do not meet the unique constraint if the documents do
not meet the filter criteria. For an example, see Partial Index with Unique Constraint . Sharded Clusters and Unique Indexes You cannot specify a unique constraint on a hashed index . For a ranged sharded collection, only the following indexes can be unique : the index on the shard key a compound index where the shard key is a prefix the default _id index; however , the _id index only
enforces the uniqueness constraint per shard if the _id field
is not the shard key or the prefix of the shard key. Important Uniqueness and the _id Index If the _id field is not the shard key or the prefix of the
shard key, _id index only enforces the uniqueness constraint
per shard and not across shards. For example, consider a sharded collection (with shard key {x:
1} ) that spans two shards A and B. Because the _id key is
not part of the shard key, the collection could have a document
with _id value 1 in shard A and another document with _id value 1 in shard B. If the _id field is not the shard key nor the prefix of the
shard key, MongoDB expects applications to enforce the uniqueness
of the _id values across the shards. The unique index constraints mean that: For a to-be-sharded collection, you cannot shard the collection if
the collection has other unique indexes. For an already-sharded collection, you cannot create unique indexes
on other fields. To maintain uniqueness on a field that is not your shard key,
see Unique Constraints on Arbitrary Fields . Sparse and Non-Sparse Unique Indexes Starting in MongoDB 5.0, unique sparse and unique non-sparse indexes with the same key pattern can exist on a single collection. Unique and Sparse Index Creation This example creates multiple indexes with the same key pattern and
different sparse options: db. scoreHistory . createIndex ( { score : 1 } , { name : "unique_index" , unique : true } ) db. scoreHistory . createIndex ( { score : 1 } , { name : "unique_sparse_index" , unique : true , sparse : true } ) Basic and Sparse Index Creation You can also create basic indexes with the same key pattern with and
without the sparse option: db. scoreHistory . createIndex ( { score : 1 } , { name : "sparse_index" , sparse : true } ) db. scoreHistory . createIndex ( { score : 1 } , { name : "basic_index" } ) Basic and Unique Indexes With Duplicate Key Patterns Starting in MongoDB 5.0, basic and unique indexes can exist with the
same key pattern . This duplication in key patterns allows for adding a unique index to
already indexed fields. In this example: Create a basic index with the key pattern { score : 1 } and insert
three documents. db. scoreHistory . createIndex ( { score : 1 } , { name : "basic_index" } ) db. scoreHistory . insert ( { score : 1 } ) db. scoreHistory . insert ( { score : 2 } ) db. scoreHistory . insert ( { score : 3 } ) Create a unique index with the same key pattern { score : 1 } . db. scoreHistory . createIndex ( { score : 1 } , { name : "unique_index" , unique : true } ) Try to insert a duplicate score document that fails because of
the unique index. db. scoreHistory . insert ( { score : 3 } ) Back Expire Data Next Convert to Unique
