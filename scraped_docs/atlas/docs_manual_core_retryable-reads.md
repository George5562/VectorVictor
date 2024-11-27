# Retryable Reads - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations Retryable Reads On this page Prerequisites Enabling Retryable Reads Retryable Read Operations Behavior Retryable reads allow MongoDB drivers to automatically retry certain
read operations a single time if they encounter certain network
or server errors. Prerequisites Minimum Driver Version Official MongoDB drivers compatible with MongoDB Server 4.2 and later
support retryable reads. For more information on official MongoDB drivers, see MongoDB Drivers . Minimum Server Version Drivers can only retry read operations if connected to
MongoDB Server 3.6 or later. Enabling Retryable Reads Official MongoDB drivers compatible with MongoDB Server 4.2 and later
enable retryable reads by default. To explicitly disable retryable
reads, specify retryReads=false in the connection string for the deployment. mongosh does not support retryable reads. Retryable Read Operations MongoDB drivers support retrying the following read operations. The
list references a generic description of each method. For specific
syntax and usage, defer to the driver documentation for that method. Methods Descriptions Collection.aggregate Collection.count Collection.countDocuments Collection.distinct Collection.estimatedDocumentCount Collection.find Database.aggregate For Collection.aggregate and Database.aggregate , drivers
can only retry aggregation pipelines which do not include
write stages, such as $out or $merge . CRUD API Read Operations Collection.watch Database.watch MongoClient.watch Change Stream Operations MongoClient.listDatabases Database.listCollections Collection.listIndexes Enumeration Operations GridFS Operations backed by Collection.find (e.g. GridFSBucket.openDownloadStream ) GridFS File Download Operations MongoDB drivers may include retryable support for other operations,
such as helper methods or methods that wrap a retryable read operation.
Defer to the driver documentation to determine whether a method explicitly supports retryable reads. Tip See also: Retryable Read Specification: Supported Read Operations Unsupported Read Operations The following operations do not support retryable reads: db.collection.mapReduce() getMore Any read command passed to a generic Database.runCommand helper,
which is agnostic about read or write commands. Behavior Persistent Network Errors MongoDB retryable reads make only one retry attempt. This helps
address transient network errors or replica set elections , but not persistent
network errors. Failover Period The driver performs server selection using the read command's
original read preference before retrying the
read operation. If the driver cannot select a server
for the retry attempt using the original read preference,
the driver returns the original error. The drivers wait serverSelectionTimeoutMS milliseconds
before performing server selection. Retryable reads do not address
instances where no eligible servers exist after waiting serverSelectionTimeoutMS . Back Retryable Writes Next SQL to MongoDB
