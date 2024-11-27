# $shardedDataDistribution (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $shardedDataDistribution (aggregation) On this page Definition Syntax Output Fields Behavior Examples Return All Sharded Data Distibution Metrics Return Metrics for a Specific Shard Return Metrics for a Namespace Confirm No Orphaned Documents Remain Definition $shardedDataDistribution New in version 6.0.3 . Returns information on the distribution of data in sharded collections. Note This aggregation stage is only available on mongos . This aggregation stage must be run on the admin database.  The user must
have the shardedDataDistribution privilege action. Syntax The shardedDataDistribution stage has the following syntax: db. aggregate ( [ { $shardedDataDistribution : { } } ] ) Output Fields The $shardedDataDistribution stage outputs an array of documents
for each sharded collection in the database.  These documents contain the
following fields: Field Name Data Type Description ns string Namespace of the sharded collection. shards array Shards in the collection with the data distribution
information for each shard. shards.numOrphanedDocs integer Number of orphaned documents in the shard. shards.numOwnedDocuments integer Number of documents owned by the shard. shards.ownedSizeBytes integer Size in bytes of documents owned by the shard when
uncompressed. shards.orphanedSizeBytes integer Size in bytes of orphaned documents in the shard when
uncompressed. Starting in MongoDB 8.0, $shardedDataDistribution only returns
output for a collection's primary shard if the primary shard
has chunks or orphaned documents . Behavior After an unclean shutdown of a mongod using the Wired Tiger storage engine, size and count statistics reported by $shardedDataDistribution may be inaccurate. The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, mongod instances running
with non-default --syncdelay settings may have more or less frequent
checkpoints. Run validate on each collection on the mongod to restore statistics after an unclean shutdown. After an unclean shutdown: validate updates the count statistic in the collStats output with the latest value. Other statistics like the number of documents inserted or removed in
the collStats output are
estimates. Examples Return All Sharded Data Distibution Metrics To return all sharded data distribution metrics, run the following: db. aggregate ( [ { $shardedDataDistribution : { } } ]) Example output: [ { "ns" : "test.names" , "shards" : [ { "shardName" : "shard-1" , "numOrphanedDocs" : 0 , "numOwnedDocuments" : 6 , "ownedSizeBytes" : 366 , "orphanedSizeBytes" : 0 } , { "shardName" : "shard-2" , "numOrphanedDocs" : 0 , "numOwnedDocuments" : 6 , "ownedSizeBytes" : 366 , "orphanedSizeBytes" : 0 } ] } ] Return Metrics for a Specific Shard To return sharded data distribution metrics for a specific shard,
run the following: db. aggregate ( [ { $shardedDataDistribution : { } } , { $match : { "shards.shardName" : "<name of the shard>" } } ]) Return Metrics for a Namespace To return sharded data distribution data for a namespace, run the
following: db. aggregate ( [ { $shardedDataDistribution : { } } , { $match : { "ns" : "<database>.<collection>" } } ]) Confirm No Orphaned Documents Remain Starting in MongoDB 6.0.3, you can run an aggregation using the $shardedDataDistribution stage to confirm no orphaned
documents remain: db. aggregate ( [ { $shardedDataDistribution : { } } , { $match : { "ns" : "<database>.<collection>" } } ]) $shardedDataDistribution has output similar to the following: [ { "ns" : "test.names" , "shards" : [ { "shardName" : "shard-1" , "numOrphanedDocs" : 0 , "numOwnedDocuments" : 6 , "ownedSizeBytes" : 366 , "orphanedSizeBytes" : 0 } , { "shardName" : "shard-2" , "numOrphanedDocs" : 0 , "numOwnedDocuments" : 6 , "ownedSizeBytes" : 366 , "orphanedSizeBytes" : 0 } ] } ] Ensure that "numOrphanedDocs" is 0 for each shard in the
cluster. Back $setWindowFields Next $skip
