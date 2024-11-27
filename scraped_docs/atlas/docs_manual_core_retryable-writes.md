# Retryable Writes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations Retryable Writes On this page Prerequisites Retryable Writes and Multi-Document Transactions Enabling Retryable Writes Retryable Write Operations Behavior Retryable writes allow MongoDB drivers to automatically retry certain
write operations a single time if they encounter network errors, or if
they cannot find a healthy primary in the replica set or sharded cluster . Prerequisites Retryable writes have the following requirements: Supported Deployment Topologies Retryable writes require a replica set or sharded cluster , and do not support standalone instances . Supported Storage Engine Retryable writes require a storage engine supporting document-level
locking, such as the WiredTiger or in-memory storage engines. 3.6+ MongoDB Drivers Clients require MongoDB drivers updated for MongoDB 3.6 or greater: Java 3.6+ Python 3.6+ C 1.9+ Go 1.8+ C# 2.5+ Node 3.0+ Ruby 2.5+ Rust 2.1+ Swift 1.2+ Perl 2.0+ PHPC 1.4+ Scala 2.2+ C++ 3.6.6+ MongoDB Version The MongoDB version of every node in the cluster must be 3.6 or
greater, and the featureCompatibilityVersion of each node in the
cluster must be 3.6 or greater. See setFeatureCompatibilityVersion for more information on
the featureCompatibilityVersion flag. Write Acknowledgment Write operations issued with a Write Concern of 0 are not retryable. Retryable Writes and Multi-Document Transactions The transaction commit and abort operations are retryable write operations. If the commit operation or the abort
operation encounters an error, MongoDB drivers retry the operation a
single time regardless of whether retryWrites is set to false . The write operations inside the transaction are not individually
retryable, regardless of value of retryWrites . For more information on transactions, see Transactions . Enabling Retryable Writes MongoDB Drivers Drivers compatible with MongoDB 4.2 and higher enable Retryable Writes by default. Earlier drivers require the retryWrites=true option. The retryWrites=true option can be omitted in
applications that use drivers compatible with MongoDB 4.2 and
higher. To disable retryable writes, applications that use drivers
compatible with MongoDB 4.2 and higher must include retryWrites=false in the connection
string. mongosh Retryable writes are enabled by default in mongosh . To
disable retryable writes, use the --retryWrites=false command line option: mongosh --retryWrites= false Retryable Write Operations The following write operations are retryable when issued with
acknowledged write concern; e.g., Write Concern cannot be {w: 0} . Note The write operations inside the transactions are not individually retryable. Methods Descriptions db.collection.insertOne() db.collection.insertMany() Insert operations db.collection.updateOne() db.collection.replaceOne() Single-document update operations db.collection.deleteOne() db.collection.remove() where justOne is true Single document delete operations db.collection.findAndModify() db.collection.findOneAndDelete() db.collection.findOneAndReplace() db.collection.findOneAndUpdate() findAndModify operations. All findAndModify operations
are single document operations. db.collection.bulkWrite() with the following write
operations: insertOne updateOne replaceOne deleteOne Bulk write operations that only consist of the single-document
write operations. A retryable bulk operation can include any
combination of the specified write operations but cannot include
any multi-document write operations, such as updateMany . Bulk operations for: Bulk.find.removeOne() Bulk.find.replaceOne() Bulk.find.updateOne() Bulk write operations that only consist of the single-document
write operations. A retryable bulk operation can include any
combination of the specified write operations but cannot include
any multi-document write operations, such as update which
specifies true for the multi option. Behavior Persistent Network Errors MongoDB retryable writes make only one retry attempt. This helps
address transient network errors and replica set elections , but not persistent
network errors. Failover Period If the driver cannot find a healthy primary in the destination
replica set or sharded cluster shard, the drivers wait serverSelectionTimeoutMS milliseconds to determine the new
primary before retrying. Retryable writes do not address instances where
the failover period exceeds serverSelectionTimeoutMS . Warning If the client application becomes temporarily unresponsive for more
than the localLogicalSessionTimeoutMinutes after
issuing a write operation, there is a chance that when the client
applications starts responding (without a restart), the write
operation may be retried and applied again. Diagnostics The serverStatus command, and its mongosh shell helper db.serverStatus() includes statistics on
retryable writes in the transactions section. Retryable Writes Against local Database The official MongoDB drivers enable retryable writes by default.
Applications which write to the local database will encounter write errors unless retryable writes are explicitly disabled. To disable retryable writes, specify retryWrites=false in the connection string for the MongoDB cluster. Error Handling Starting in MongoDB 6.1, if both the first and second attempt of a
retryable write fail without a single write being performed, MongoDB
returns an error with the NoWritesPerformed label. The NoWritesPerformed label differentiates the results of batch
operations like insertMany() . In an insertMany operation, one of the following outcomes can occur: Outcome MongoDB Output No documents are inserted. Error returned with NoWritesPerformed label. Partial work done. (At least one document is inserted, but not
all.) Error returned without NoWritesPerformed label. All documents are inserted. Success returned. Applications can use the NoWritesPerformed label to definitively
determine that no documents were inserted. This error reporting lets the
application maintain an accurate state of the database when handling
retryable writes. In previous versions of MongoDB, an error is returned when both the
first and second attempts of a retryable write fail. However, there is
no distinction made to indicate that no writes were performed. Back Bulk Write Next Retryable Reads
