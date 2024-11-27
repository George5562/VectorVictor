# Capped Collections - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections Capped Collections On this page Restrictions Command Syntax Use Cases Get Started Behavior Oplog Collection _id Index Updates Query Efficiency Tailable Cursor Multiple Concurrent Writes Read Concern Snapshot Learn More Capped collections are fixed-size collections that insert and retrieve
documents based on insertion order. Capped collections work similarly to
circular buffers: once a collection fills its allocated space, it makes
room for new documents by overwriting the oldest documents in the
collection. Restrictions Capped collections cannot be sharded. You cannot create capped collections on serverless instances . Capped collections are not supported in Stable API V1. You cannot write to capped collections in transactions . The $out aggregation pipeline stage cannot write results
to a capped collection. Command Syntax The following example creates a capped collection called log with a
maximum size of 100,000 bytes. db. createCollection ( "log" , { capped : true , size : 100000 } ) For more information on creating capped collections, see createCollection() or create . Use Cases Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index. Capped collections serialize write operations and therefore have worse
concurrent insert, update, and delete performance than non-capped
collections. Before you create a capped collection, consider if you
can use a TTL index instead. The most common use case for a capped collection is to store log
information. When the capped collection reaches its maximum size, old
log entries are automatically overwritten with new entries. Get Started To create and query capped collections, see these pages: Create a Capped Collection Query a Capped Collection Check if a Collection is Capped Convert a Collection to Capped Change the Size of a Capped Collection Change Maximum Documents in a Capped Collection Behavior Consider these behavioral details for capped collections. Oplog Collection The oplog.rs collection that stores a log
of the operations in a replica set uses a capped collection. Unlike other capped collections, the oplog can grow past its configured
size limit to avoid deleting the majority commit point . Note MongoDB rounds the capped size of the oplog up to the nearest
integer multiple of 256, in bytes. _id Index Capped collections have an _id field and an index on the _id field by default. Updates Avoid updating data in a capped collection. Because capped collections
are fixed-size, updates can cause your data to expand beyond the
collection's allocated space, which can cause unexpected behavior. Query Efficiency Use natural ordering to retrieve the most
recently inserted elements from the collection efficiently. This is
similar to using the tail command on a log file. Tailable Cursor You can use a tailable cursor with capped collections. Similar to the
Unix tail -f command, the tailable cursor "tails" the end of a
capped collection. As new documents are inserted into the capped
collection, you can use the tailable cursor to continue retrieving
documents. For information on creating a tailable cursor, see Tailable Cursors . Multiple Concurrent Writes If there are concurrent writers to a capped collection, MongoDB does not
guarantee that documents are returned in insertion order. Read Concern Snapshot Starting in MongoDB 8.0, you can use read concern "snapshot" on capped collections. Learn More TTL Indexes Index Properties Indexing Strategies Back On-Demand Materialized Views Next Create
