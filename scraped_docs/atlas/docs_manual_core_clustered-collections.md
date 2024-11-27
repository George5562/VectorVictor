# Clustered Collections - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections Clustered Collections On this page Benefits Behavior Limitations Set Your Own Clustered Index Key Values Examples New in version 5.3 . Clustered collections store indexed documents in the same WiredTiger file as the index specification.
Storing the collection's documents and index in the same file provides
benefits for storage and performance compared to regular indexes. Clustered collections are created with a clustered index . The clustered index specifies the
order in which documents are stored. To create a clustered collection, see Examples . Important Backward-Incompatible Feature You must drop clustered collections before you can downgrade to
a version of MongoDB earlier than 5.3. Benefits Clustered collections have the following benefits compared to
non-clustered collections: Faster queries on clustered collections without needing a secondary
index, such as queries with range scans and equality comparisons on
the clustered index key. Clustered collections have a lower storage size, which improves
performance for queries and bulk inserts. Clustered collections can eliminate the need for a secondary TTL
(Time To Live) index . A clustered index is also a TTL index if you specify the expireAfterSeconds field. To be used as a TTL index, the _id field must be a supported
date type. See TTL Indexes . If you use a clustered index as a TTL index, it improves document
delete performance and reduces the clustered collection storage
size. Clustered collections have additional performance improvements for
inserts, updates, deletes, and queries. All collections have an _id index . A non-clustered collection stores the _id index separately from
the documents. This requires two writes for inserts, updates, and
deletes, and two reads for queries. A clustered collection stores the index and the documents together
in _id value order. This requires one write for inserts,
updates, and deletes, and one read for queries. Behavior Clustered collections store documents ordered by the clustered
index key value. The clustered
index key must be { _id: 1 } . You can only have one clustered index in a collection because the
documents can be stored in only one order. Only collections with a
clustered index store the data in sorted order. You can have a clustered index and add secondary indexes to a clustered collection. Clustered indexes differ
from secondary indexes: A clustered index can only be created when you create the collection. The clustered index keys are stored with the collection. The
collection size returned by the collStats command
includes the clustered index size. Starting in MongoDB 6.0.7, if a usable clustered index exists, the MongoDB
query planner evaluates the clustered index against secondary indexes in
the query planning process. When a query uses a clustered index, MongoDB
performs a bounded collection scan . Prior to MongoDB 6.0.7, if a secondary index existed on a clustered collection and the secondary index was usable by
your query, the query planner selected the secondary index instead of the
clustered index by default. In MongoDB 6.1 and prior, to use the
clustered index, you must provide a hint because the query
optimizer does not automatically select the
clustered index. Limitations Clustered collection limitations: The clustered index key must be { _id: 1 } . You cannot transform a non-clustered collection to a clustered
collection, or the reverse. Instead, you can: Read documents from one collection and write them to another
collection using an aggregation pipeline with an $out stage or
a $merge stage. Export collection data with mongodump and import the
data into another collection with mongorestore . You cannot hide a clustered index. See Hidden indexes . If there are secondary indexes for the clustered collection, the
collection has a larger storage size. This is because secondary
indexes on a clustered collection with large clustered index keys may
have a larger storage size than secondary indexes on a non-clustered
collection. Clustered collections may not be capped collections . Set Your Own Clustered Index Key Values By default, the clustered index key values are the unique document object identifiers . You can set your own clustered index key values. Your key: Must contain unique values. Must be immutable. Should contain sequentially increasing values. This is not a
requirement but improves insert performance. Should be as small in size as possible. A clustered index supports keys up to 8 MB in size, but a much
smaller clustered index key is best. A large clustered index key causes the clustered collection to
increase in size and secondary indexes are also larger. This reduces
the performance and storage benefits of the clustered collection. Secondary indexes on clustered collections with large clustered
index keys may use more space compared to secondary indexes on
non-clustered collections. Warning Randomly generated key values may decrease a clustered collection's
performance. Examples This section shows clustered collection examples. Create Example The following create example adds a clustered
collection named products : db. runCommand ( { create : "products" , clusteredIndex : { "key" : { _id : 1 } , "unique" : true , "name" : "products clustered key" } } ) In the example, clusteredIndex specifies: "key": { _id: 1 } , which sets the clustered index key to the _id field. "unique": true , which indicates the clustered index key value must
be unique. "name": "products clustered key" , which sets the clustered index name. db.createCollection Example The following db.createCollection() example adds a clustered collection named stocks : db. createCollection ( "stocks" , { clusteredIndex : { "key" : { _id : 1 } , "unique" : true , "name" : "stocks clustered key" } } ) In the example, clusteredIndex specifies: "key": { _id: 1 } , which sets the clustered index key to the _id field. "unique": true , which indicates the clustered index key value must
be unique. "name": "stocks clustered key" , which sets the clustered index name. Date Clustered Index Key Example The following create example adds a clustered collection
named orders : db. createCollection ( "orders" , { clusteredIndex : { "key" : { _id : 1 } , "unique" : true , "name" : "orders clustered key" } } ) In the example, clusteredIndex specifies: "key": { _id: 1 } , which sets the clustered index key to the _id field. "unique": true , which indicates the clustered index key value must
be unique. "name": "orders clustered key" , which sets the clustered index name. The following example adds documents to the orders collection: db. orders . insertMany ( [ { _id : ISODate ( "2022-03-18T12:45:20Z" ) , "quantity" : 50 , "totalOrderPrice" : 500 } , { _id : ISODate ( "2022-03-18T12:47:00Z" ) , "quantity" : 5 , "totalOrderPrice" : 50 } , { _id : ISODate ( "2022-03-18T12:50:00Z" ) , "quantity" : 1 , "totalOrderPrice" : 10 } ] ) The _id clusteredIndex key stores the
order date. If you use the _id field in a range query, performance is improved.
For example, the following query uses _id and $gt to
return the orders where the order date is greater than the supplied
date: db. orders . find ( { _id : { $gt : ISODate ( "2022-03-18T12:47:00.000Z" ) } } ) Example output: [ { _id : ISODate ( "2022-03-18T12:50:00.000Z" ) , quantity : 1 , totalOrderPrice : 10 } ] Determine if a Collection is Clustered To determine if a collection is clustered, use the listCollections command: db. runCommand ( { listCollections : 1 } ) For clustered collections, you will see the clusteredIndex details in the output. For example, the
following output shows the details for the orders clustered
collection: ... name : 'orders' , type : 'collection' , options : { clusteredIndex : { v : 2 , key : { _id : 1 } , name : 'orders clustered key' , unique : true } } , ... v is the index version. Back Change Limits Next Documents
