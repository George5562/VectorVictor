# Bulk Write Operations - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations Bulk Write Operations On this page Overview Ordered vs Unordered Operations bulkWrite() Methods Example Strategies for Bulk Inserts to a Sharded Collection Overview MongoDB provides clients the ability to perform write operations in
bulk. Bulk write operations affect a single collection. MongoDB
allows applications to determine the acceptable level of
acknowledgment required for bulk write operations. The db.collection.bulkWrite() method provides the ability to
perform bulk insert, update, and delete operations. MongoDB also supports bulk insert through the db.collection.insertMany() method. Ordered vs Unordered Operations Bulk write operations can be either ordered or unordered . With an ordered list of operations, MongoDB executes the operations serially.
If an error occurs during the processing of one of the write
operations, MongoDB will return without processing any remaining write
operations in the list.
See ordered Bulk Write With an unordered list of operations, MongoDB can execute the
operations in parallel, but this behavior is not guaranteed.
If an error occurs during the processing of one
of the write operations, MongoDB will continue to process remaining
write operations in the list.
See Unordered Bulk Write Example . Executing an ordered list of operations on a sharded collection will
generally be slower than executing an unordered list since with an
ordered list, each operation must wait for the previous operation to
finish. By default, bulkWrite() performs ordered operations. To specify unordered write operations, set ordered : false in the options document. See Execution of Operations bulkWrite() Methods bulkWrite() supports the following write operations: insertOne updateOne updateMany replaceOne deleteOne deleteMany Each write operation is passed to bulkWrite() as a
document in an array. Example The example in this section uses the pizzas collection: db. pizzas . insertMany ( [ { _id : 0 , type : "pepperoni" , size : "small" , price : 4 } , { _id : 1 , type : "cheese" , size : "medium" , price : 7 } , { _id : 2 , type : "vegan" , size : "large" , price : 8 } ] ) The following bulkWrite() example runs
these operations on the pizzas collection: Adds two documents using insertOne . Updates a document using updateOne . Deletes a document using deleteOne . Replaces a document using replaceOne . try { db. pizzas . bulkWrite ( [ { insertOne : { document : { _id : 3 , type : "beef" , size : "medium" , price : 6 } } } , { insertOne : { document : { _id : 4 , type : "sausage" , size : "large" , price : 10 } } } , { updateOne : { filter : { type : "cheese" } , update : { $set : { price : 8 } } } } , { deleteOne : { filter : { type : "pepperoni" } } } , { replaceOne : { filter : { type : "vegan" } , replacement : { type : "tofu" , size : "small" , price : 4 } } } ] ) } catch ( error ) { print ( error ) } Example output, which includes a summary of the completed operations: { acknowledged : true , insertedCount : 2 , insertedIds : { '0' : 3 , '1' : 4 } , matchedCount : 2 , modifiedCount : 2 , deletedCount : 1 , upsertedCount : 0 , upsertedIds : { } } For more examples, see bulkWrite() Examples . Strategies for Bulk Inserts to a Sharded Collection Large bulk insert operations, including initial data inserts or routine
data import, can affect sharded cluster performance. For
bulk inserts, consider the following strategies: Pre-Split the Collection If the sharded collection is empty, then the collection has only
one initial chunk , which resides on a single shard.
MongoDB must then take time to receive data, create splits, and
distribute the split chunks to the available shards. To avoid this
performance cost, you can pre-split the collection, as described in Split Chunks in a Sharded Cluster . Unordered Writes to mongos To improve write performance to sharded clusters, use bulkWrite() with the optional parameter ordered set to false . mongos can attempt to send the writes to
multiple shards simultaneously. For empty collections,
first pre-split the collection as described in Split Chunks in a Sharded Cluster . Avoid Monotonic Throttling If your shard key increases monotonically during an insert, then all
inserted data goes to the last chunk in the collection, which will
always end up on a single shard. Therefore, the insert capacity of the
cluster will never exceed the insert capacity of that single shard. If your insert volume is larger than what a single shard can process,
and if you cannot avoid a monotonically increasing shard key, then
consider the following modifications to your application: Reverse the binary bits of the shard key. This preserves the
information and avoids correlating insertion order with increasing
sequence of values. Swap the first and last 16-bit words to "shuffle" the inserts. Example The following example, in C++, swaps the leading and
trailing 16-bit word of BSON ObjectIds generated so they are no longer monotonically increasing. using namespace mongo; OID make_an_id () { OID x = OID:: gen () ; const unsigned char *p = x. getData () ; swap ( ( unsigned short &) p[ 0 ], ( unsigned short &) p[ 10 ] ) ; return x; } void foo () { // create an object BSONObj o = BSON ( "_id" << make_an_id () << "x" << 3 << "name" << "jane" ) ; // now we may insert o into a sharded collection } Tip See also: Shard Keys for information
on choosing a sharded key. Also see Shard Key
Internals (in particular, Choose a Shard Key ). Back Methods Next Retryable Writes
