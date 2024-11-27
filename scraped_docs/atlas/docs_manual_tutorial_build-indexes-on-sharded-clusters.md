# Rolling Index Builds on Sharded Clusters - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Builds Rolling Index Builds on Sharded Clusters On this page Considerations Before You Begin Procedure Additional Information Index builds can impact sharded cluster performance. By default, MongoDB
builds indexes simultaneously on all data-bearing replica
set members. Index builds on sharded clusters occur only on those
shards which contain data for the collection being indexed. For
workloads which cannot tolerate performance decrease due to index
builds, consider using the following procedure to build indexes in a
rolling fashion. Rolling index builds take at most one shard replica set member out at a
time, starting with the secondary members, and builds the index on that
member as a standalone. Rolling index builds require at least one
replica set election per shard. Note For information about creating indexes in Atlas, refer to the index management page in the Atlas
documentation. Considerations Unique Indexes To create unique indexes using the following
procedure, you must stop all writes to the collection during this
procedure. If you cannot stop all writes to the collection during this procedure,
do not use the procedure on this page. Instead, build your unique index
on the collection by issuing db.collection.createIndex() on
the mongos for a sharded cluster. Oplog Size Ensure that your oplog is large enough to permit the indexing
or re-indexing operation to complete without falling too far behind to
catch up. See the oplog sizing documentation for additional information. Before You Begin For building unique indexes To create unique indexes using the following
procedure, you must stop all writes to the collection during the index
build. Otherwise, you may end up with inconsistent data across the
replica set members. If you cannot stop all writes to the collection,
do not use the following procedure to create unique indexes. Warning If you cannot stop all writes to the collection, do not use the
following procedure to create unique indexes. Before creating the index, validate that no documents in the
collection violate the index constraints. If a collection is
distributed across shards and a shard contains a chunk with
duplicate documents, the create index operation may succeed on the
shards without duplicates but not on the shard with duplicates.
To avoid leaving inconsistent indexes across shards, you can issue the db.collection.dropIndex() from a mongos to
drop the index from the collection. Starting in MongoDB 8.0, you can use the directShardOperations role to perform maintenance operations
that require you to execute commands directly against a shard. Warning Running commands using the directShardOperations role can cause
your cluster to stop working correctly and may cause data corruption.
Only use the directShardOperations role for maintenance purposes
or under the guidance of MongoDB support. Once you are done
performing maintenance operations, stop using the directShardOperations role. Procedure Important The following procedure to build indexes in a rolling fashion applies
to sharded clusters deployments, and not replica set deployments. For
the procedure for replica sets, see Rolling Index Builds on Replica Sets instead. A. Stop the Balancer Connect mongosh to a mongos instance in the sharded cluster, and run sh.stopBalancer() to
disable the balancer: [ 1 ] sh. stopBalancer ( ) Note If a migration is in progress, the system will complete the
in-progress migration before stopping the balancer. To verify that the balancer is disabled, run sh.getBalancerState() , which returns false if the balancer
is disabled: sh. getBalancerState ( ) [ 1 ] Starting in MongoDB 6.0.3, automatic chunk splitting is not performed.
This is because of balancing policy improvements. Auto-splitting commands
still exist, but do not perform an operation. In MongoDB versions earlier than 6.0.3, sh.stopBalancer() also disables auto-splitting for the sharded cluster. B. Determine the Distribution of the Collection From mongosh connected to the mongos , refresh the cached routing table for that mongos to avoid returning stale distribution information
for the collection. Once refreshed, run db.collection.getShardDistribution() for the collection you
wish to build the index. For example, if you want to create an ascending index
on the records collection in the test database: db. adminCommand ( { flushRouterConfig : "test.records" } ) ; db. records . getShardDistribution ( ) ; The method outputs the shard distribution. For example, consider a
sharded cluster with 3 shards shardA , shardB , and shardC and the db.collection.getShardDistribution() returns the
following: Shard shardA at shardA/s1-mongo1.example.net:27018,s1-mongo2.example.net:27018,s1-mongo3.example.net:27018 data : 1KiB docs : 50 chunks : 1 estimated data per chunk : 1KiB estimated docs per chunk : 50 Shard shardC at shardC/s3-mongo1.example.net:27018,s3-mongo2.example.net:27018,s3-mongo3.example.net:27018 data : 1KiB docs : 50 chunks : 1 estimated data per chunk : 1KiB estimated docs per chunk : 50 Totals data : 3KiB docs : 100 chunks : 2 Shard shardA contains 50% data, 50% docs in cluster, avg obj size on shard : 40B Shard shardC contains 50% data, 50% docs in cluster, avg obj size on shard : 40B From the output, you only build the indexes for test.records on shardA and shardC . C. Build Indexes on the Shards That Contain Collection Chunks For each shard that contains chunks for the collection, follow the
procedure to build the index on the shard. C1. Stop One Secondary and Restart as a Standalone For an affected shard, stop the mongod process
associated with one of its secondary. Restart after making the following
configuration updates: Configuration File Command-line Options If you are using a configuration file, make the following
configuration updates: Change the net.port to a different port. [ 2 ] Make a note of the original port setting as a comment. Comment out the replication.replSetName option. Comment out the sharding.clusterRole option. Set parameter skipShardingConfigurationChecks to true in the setParameter section. Set parameter disableLogicalSessionCacheRefresh to true in the setParameter section. For example, for a shard replica set member, the
updated configuration file will include content like
the following example: net: bindIp: localhost,<hostname(s)|ip address(es)> port: 27218 #   port: 27018 #replication: #   replSetName: shardA #sharding: #   clusterRole: shardsvr setParameter: skipShardingConfigurationChecks: true disableLogicalSessionCacheRefresh: true And restart: mongod --config <path/To/ConfigFile> Other settings (e.g. storage.dbPath , etc.) remain the same. If using command-line options, make the following
configuration updates: Modify --port to a different port. [ 2 ] Remove --replSet . Remove --shardsvr if a
shard member and --configsvr if a config server member. Set parameter skipShardingConfigurationChecks to true in the --setParameter option. Set parameter disableLogicalSessionCacheRefresh to true in the --setParameter option. For example, restart your shard replica set member
without the --replSet and --shardsvr options.
Specify a new port number and set both the skipShardingConfigurationChecks and disableLogicalSessionCacheRefresh parameters to
true: mongod --port 27218 --setParameter skipShardingConfigurationChecks= true --setParameter disableLogicalSessionCacheRefresh= true Other settings (e.g. --dbpath , etc.) remain the same. [ 2 ] ( 1 , 2 ) By running the mongod on a different
port, you ensure that the other members of the replica set and all
clients will not contact the member while you are building the
index. C2. Build the Index Connect directly to the mongod instance running as a
standalone on the new port and create the new index for this
instance. For example, connect mongosh to the instance,
and use the db.collection.createIndex() method to create
an ascending index on the username field of the records collection: db.records.createIndex( { username: 1 } ) C3. Restart the Program mongod as a Replica Set Member When the index build completes, shutdown the mongod instance. Undo the configuration changes made when starting as a
standalone to return to its original configuration and restart. Important Be sure to remove the skipShardingConfigurationChecks parameter and disableLogicalSessionCacheRefresh parameter. For example, to restart your replica set shard member: Configuration File Command-line Options If you are using a configuration file: Revert to the original port number. Uncomment the replication.replSetName . Uncomment the sharding.clusterRole . Remove parameter skipShardingConfigurationChecks in the setParameter section. Remove parameter disableLogicalSessionCacheRefresh in the setParameter section. net: bindIp: localhost,<hostname(s)|ip address(es)> port: 27018 replication: replSetName: shardA sharding: clusterRole: shardsvr Other settings (e.g. storage.dbPath , etc.) remain the same. And restart: mongod --config <path/To/ConfigFile> If you are using command-line options: Revert to the original port number. Include --replSet . Include --shardsvr if
a shard member or --configsvr if a config server member. Remove parameter skipShardingConfigurationChecks . Remove parameter disableLogicalSessionCacheRefresh . For example: mongod --port 27018 --replSet shardA --shardsvr Other settings (e.g. --dbpath , etc.) remain the same. Allow replication to catch up on this member. C4. Repeat the Procedure for the Remaining Secondaries for the Shard Once the member catches up with the other members of the set, repeat
the procedure one member at a time for the remaining secondary
members for the shard: C1. Stop One Secondary and Restart as a Standalone C2. Build the Index C3. Restart the Program mongod as a Replica Set Member C5. Build the Index on the Primary When all the secondaries for the shard have the new index, step down
the primary for the shard, restart it as a standalone using the
procedure described above, and build the index on the former primary: Use the rs.stepDown() method in mongosh to step down the primary. Upon successful stepdown, the current primary
becomes a secondary and the replica set members elect a new primary. C1. Stop One Secondary and Restart as a Standalone C2. Build the Index C3. Restart the Program mongod as a Replica Set Member D. Repeat for the Other Affected Shards Once you finish building the index for a shard, repeat C. Build Indexes on the Shards That Contain Collection Chunks for the other
affected shards. E. Restart the Balancer Once you finish the rolling index build for the affected shards,
restart the balancer. Connect mongosh to a mongos instance in the sharded cluster, and run sh.startBalancer() : [ 3 ] sh. startBalancer ( ) [ 3 ] Starting in MongoDB 6.0.3, automatic chunk splitting is not performed.
This is because of balancing policy improvements. Auto-splitting commands
still exist, but do not perform an operation. In MongoDB versions earlier than 6.0.3, sh.startBalancer() also enables auto-splitting for the sharded cluster. Additional Information A sharded collection has an inconsistent index if the collection does
not have the exact same indexes (including the index options) on each
shard that contains chunks for the collection. Although inconsistent
indexes should not occur during normal operations, inconsistent indexes
can occur, such as: When a user is creating an index with a unique key constraint and
one shard contains a chunk with duplicate documents. In such cases,
the create index operation may succeed on the shards without
duplicates but not on the shard with duplicates. When a user is creating an index across the shards in a rolling
manner but either fails to build the index for an associated shard or
incorrectly builds an index with different specification. The config server primary periodically checks
for index inconsistencies across the shards for sharded collections. To
configure these periodic checks, see enableShardedIndexConsistencyCheck and shardedIndexConsistencyCheckIntervalMS . The command serverStatus returns the field shardedIndexConsistency to report on index
inconsistencies when run on the config server primary. To check if a sharded collection has inconsistent indexes, see Find Inconsistent Indexes Across Shards . Back Create on Replica Sets Next Manage
