# $collStats (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $collStats (aggregation) On this page Definition Behavior Definition $collStats Returns statistics regarding a collection or view. The $collStats stage has the following prototype form: { $collStats : { latencyStats : { histograms : < boolean > } , storageStats : { scale : < number > } , count : { } , queryExecStats : { } } } The $collStats stage accepts an argument document with the
following optional fields: Field Name Description latencyStats Adds latency statistics to the
return document. latencyStats.histograms Adds latency histogram information to the embedded documents
in latencyStats if true . storageStats Adds storage statistics to the
return document. Specify an empty document (i.e. storageStats: {} ) to
use the default scale factor of 1 for the various size
data. Scale factor of 1 displays the returned sizes in
bytes. Specify the scale factor (i.e. storageStats: { scale:
<number> } ) to use the specified scale factor for the
various size data. For example, to display kilobytes rather
than bytes, specify a scale value of 1024. If you specify a non-integer scale factor, MongoDB uses the integer
part of the specified factor. For example, if you specify a scale
factor of 1023.999 , MongoDB uses 1023 as the scale factor. The scale factor does not affect those sizes that specify
the unit of measurement in the field name, such as "bytes
currently in the cache" . count Adds the total number of documents in the collection to the
return document. The count is based on the collection's metadata, which
provides a fast but sometimes inaccurate count for sharded
clusters. See count Field queryExecStats Adds query execution statistics to the return document. For a collection in a replica set or a non-sharded collection in
a cluster, $collStats outputs a single document. For a sharded collection , $collStats outputs one document per shard. The output document
includes the following fields: Field Name Description ns The namespace of the requested collection or view. shard The name of the shard the output document corresponds to. Only present when $collStats runs on a sharded cluster. Both sharded and non-sharded collections will produce this field. host The hostname and port of the mongod process which produced
the output document. localTime The current time on the MongoDB server, expressed as UTC
milliseconds since the UNIX epoch . latencyStats Statistics related to request latency for a collection or view . See latencyStats Document for details on this document. Only present when the latencyStats: {} option is specified. storageStats Statistics related to a collection's storage engine. See storageStats Document for details on this
document. The various size data is scaled by the specified factor (with
the exception of those sizes that specify the unit of
measurement in the field name). Only present when the storageStats option is specified. Returns an error if applied to a view. count The total number of documents in the collection. This data is
also available in storageStats.count . The count is based on the collection's metadata, which
provides a fast but sometimes inaccurate count for sharded
clusters. Only present when the count: {} option is specified. Returns
an error if applied to a view. queryExecStats Statistics related to query execution for the collection. Only present when the queryExecStats: {} option is
specified. Returns an error if applied to a view . Behavior $collStats must be the first stage in an aggregation pipeline, or
else the pipeline returns an error. Accuracy After Unexpected Shutdown After an unclean shutdown of a mongod using the Wired Tiger storage engine, size and count statistics reported by $collStats may be inaccurate. The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, mongod instances running
with non-default --syncdelay settings may have more or less frequent
checkpoints. Run validate on each collection on the mongod to restore statistics after an unclean shutdown. After an unclean shutdown: validate updates the count statistic in the collStats output with the latest value. Other statistics like the number of documents inserted or removed in
the collStats output are
estimates. Redaction When using Queryable Encryption , $collStats output redacts certain information for encrypted
collections: The output omits "queryExecStats" The output omits "latencyStats" The output redacts "WiredTiger" , if present, to include only the url field. Transactions $collStats is not allowed in transactions . latencyStats Document The latencyStats embedded document only exists in the output if
you specify the latencyStats option. Field Name Description reads Latency statistics for read requests. writes Latency statistics for write requests. commands Latency statistics for database commands. transactions Latency statistics for database transactions. Each of these fields contains an embedded document bearing the
following fields: Field Name Description latency A 64-bit integer giving the total combined
latency in microseconds. ops A 64-bit integer giving the total number of
operations performed on the collection since startup. histogram An array of embedded documents, each representing a latency range.
Each document covers twice the previous document's range. For
lower values between 2048 microseconds and roughly 1 second,
the histogram includes half-steps. This field only exists given the latencyStats: { histograms: true } option. Empty ranges with
a zero count are omitted from the output. Each document bears the following fields: Field Name Description micros A 64-bit integer giving the inclusive
lower time bound of the current latency range in
microseconds. The document's range spans between the previous document's micros value, exclusive, and this document's micros value, inclusive. count A 64-bit integer giving the number of
operations with latency less than or equal to micros . For example, if collStats returns the following histogram: histogram : [ { micros : NumberLong ( 0 ) , count : NumberLong ( 10 ) } , { micros : NumberLong ( 2 ) , count : NumberLong ( 1 ) } , { micros : NumberLong ( 4096 ) , count : NumberLong ( 1 ) } , { micros : NumberLong ( 16384 ) , count : NumberLong ( 1000 ) } , { micros : NumberLong ( 49152 ) , count : NumberLong ( 100 ) } ] This indicates that there were [ 1 ] : 10 operations taking 2 microsecond or less 1 operation in the range [2, 4) microseconds 1 operation in the range [4096, 6144) microseconds 1000 operations in the range [16384, 24576) microseconds 100 operations in the range [49152, 65536) microseconds [ 1 ] The ( symbol notation on this page means the value is exclusive. The ] symbol notation on this page means the value is inclusive. For example, if you run $collStats with the latencyStats: {} option
on a matrices collection: db. matrices . aggregate ( [ { $collStats : { latencyStats : { histograms : true } } } ] ) This query returns a result similar to the following: { "ns" : "test.matrices" , "host" : "mongo.example.net:27017" , "localTime" : ISODate ( "2017-10-06T19:43:56.599Z" ) , "latencyStats" : { "reads" : { "histogram" : [ { "micros" : NumberLong ( 16 ) , "count" : NumberLong ( 3 ) } , { "micros" : NumberLong ( 32 ) , "count" : NumberLong ( 1 ) } , { "micros" : NumberLong ( 128 ) , "count" : NumberLong ( 1 ) } ] , "latency" : NumberLong ( 264 ) , "ops" : NumberLong ( 5 ) } , "writes" : { "histogram" : [ { "micros" : NumberLong ( 32 ) , "count" : NumberLong ( 1 ) } , { "micros" : NumberLong ( 64 ) , "count" : NumberLong ( 3 ) } , { "micros" : NumberLong ( 24576 ) , "count" : NumberLong ( 1 ) } ] , "latency" : NumberLong ( 27659 ) , "ops" : NumberLong ( 5 ) } , "commands" : { "histogram" : [ { "micros" : NumberLong ( 196608 ) , "count" : NumberLong ( 1 ) } ] , "latency" : NumberLong ( 0 ) , "ops" : NumberLong ( 0 ) } , "transactions" : { "histogram" : [ ] , "latency" : NumberLong ( 0 ) , "ops" : NumberLong ( 0 ) } } } storageStats Document The storageStats embedded document only exists in the output if you
specify the storageStats option. The contents of this document are dependent on the storage engine in use.
See Output for a reference on this document. For example, if you run $collStats with the storageStats: {} option on a matrices collection using the WiredTiger Storage Engine : db. matrices . aggregate ( [ { $collStats : { storageStats : { } } } ] ) This query returns a result similar to the following: { "ns" : "test.matrices" , "host" : "mongo.example.net:27017" , "localTime" : ISODate ( "2020-03-06T01:44:57.437Z" ) , "storageStats" : { "size" : 608500363 , "count" : 1104369 , "avgObjSize" : 550 , "storageSize" : 352878592 , "freeStorageSize" : 2490380 , "capped" : false , "wiredTiger" : { ... } , "nindexes" : 2 , "indexDetails" : { ... } , "indexBuilds" : [ "_id_1_abc_1" ] , "totalIndexSize" : 260337664 , "totalSize" : 613216256 , "indexSizes" : { "_id_" : 9891840 , "_id_1_abc_1" : 250445824 } , "scaleFactor" : 1 } } See Output for a reference on this document. Note In-progress Indexes The returned storageStats includes information on indexes being built. For details, see: collStats.nindexes collStats.indexDetails collStats.indexBuilds collStats.totalIndexSize collStats.indexSizes Performing $collStats with the storageStats option on a
view results in an error. count Field The count field only exists in the output if you specify the count option. For example, if you run $collStats with the count: {} option on
a matrices collection: db. matrices . aggregate ( [ { $collStats : { count : { } } } ] ) The query returns a result similar to the following: { "ns" : "test.matrices" , "host" : "mongo.example.net:27017" , "localTime" : ISODate ( "2017-10-06T19:43:56.599Z" ) , "count" : 1103869 } Note The count is based on the collection's metadata, which provides a
fast but sometimes inaccurate count for sharded clusters. The total number of documents in the collection is also available as storageStats.count when storageStats: {} is specified. For more
information, see storageStats Document . queryExecStats Document The queryExecStats embedded document only exists in the output if
you specify the queryExecStats option. The collectionScans field contains an embedded document bearing the
following fields: Field Name Description total A 64-bit integer giving the total number of queries that
performed a collection scan. The total consists of queries that
did and did not use a tailable cursor . nonTailable A 64-bit integer giving the number of queries that performed a
collection scan that did not use a tailable cursor . For example, if you run $collStats with the queryExecStats: {} option on a matrices collection: db. matrices . aggregate ( [ { $collStats : { queryExecStats : { } } } ] ) The query returns a result similar to the following: { "ns" : "test.matrices" , "host" : "mongo.example.net:27017" , "localTime" : ISODate ( "2020-06-03T14:23:29.711Z" ) , "queryExecStats" : { "collectionScans" : { "total" : NumberLong ( 33 ) , "nonTailable" : NumberLong ( 31 ) } } } $collStats on Sharded Collections $collStats outputs one document per shard when run on sharded collections . Each
output document contains a shard field with the name of the shard
the document corresponds to. For example, if you run $collStats on a sharded collection with the count: {} option on a collection named matrices : db. matrices . aggregate ( [ { $collStats : { count : { } } } ] ) The query returns a result similar to the following: { "ns" : "test.matrices" , "shard" : "s1" , "host" : "s1-mongo1.example.net:27017" , "localTime" : ISODate ( "2017-10-06T15:14:21.258Z" ) , "count" : 661705 } { "ns" : "test.matrices" , "shard" : "s2" , "host" : "s2-mongo1.example.net:27017" , "localTime" : ISODate ( "2017-10-06T15:14:21.258Z" ) , "count" : 442164 } Tip See also: collStats db.collection.stats() Back $changeStreamSplitLargeEvent Next $count
