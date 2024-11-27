# Rolling Index Builds on Replica Sets - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Builds Rolling Index Builds on Replica Sets On this page Considerations Prerequisites Procedure Index builds can impact replica set performance. By default,
MongoDB builds indexes simultaneously on all data-bearing
replica set members. For workloads which cannot tolerate performance
decrease due to index builds, consider using the following
procedure to build indexes in a rolling fashion. Rolling index builds take at most one replica set member out at a time,
starting with the secondary members, and builds the index on that member
as a standalone. Rolling index builds require at least one replica set
election. Note For information about creating indexes in Atlas, refer to the index management page in the Atlas
documentation. Considerations Unique Indexes To create unique indexes using the following
procedure, you must stop all writes to the collection during this
procedure. If you cannot stop all writes to the collection during this procedure,
do not use the procedure on this page. Instead, build your unique index
on the collection by issuing db.collection.createIndex() on
the primary for a replica set. Oplog Size Ensure that your oplog is large enough to permit the indexing
or re-indexing operation to complete without falling too far behind to
catch up. See the oplog sizing documentation for additional information. Prerequisites For building unique indexes To create unique indexes using the
following procedure, you must stop all writes to the collection
during the index build. Otherwise, you may end up with inconsistent
data across the replica set members. Warning If you cannot stop all writes to the collection, do not use the
following procedure to create unique indexes. Procedure Important The following procedure to build indexes in a rolling fashion
applies to replica set deployments, and not sharded clusters. For
the procedure for sharded clusters, see Rolling Index Builds on Sharded Clusters instead. A. Stop One Secondary and Restart as a Standalone Stop the mongod process associated with a secondary.
Restart after making the following configuration updates: Configuration File Command-line Options If you are using a configuration file, make the following
configuration updates: Comment out the replication.replSetName option. Change the net.port to a different port. [ 1 ] Make a note of the original port setting as a comment. Set parameter disableLogicalSessionCacheRefresh to true in the setParameter section. For example, the updated configuration file for a replica
set member will include content like the following example: net: bindIp: localhost,<hostname(s)|ip address(es)> port: 27217 #   port: 27017 #replication: #   replSetName: myRepl setParameter: disableLogicalSessionCacheRefresh: true Other settings (e.g. storage.dbPath , etc.) remain the same. And restart: mongod --config <path/To/ConfigFile> If using command-line options, make the following
configuration updates: Remove --replSet . Modify --port to a different port. [ 1 ] Set parameter disableLogicalSessionCacheRefresh to true in the --setParameter option. For example, if your replica set member normally runs
with on the default port of 27017 and the --replSet option, you would
specify a different port, omit the --replSet option,
and set disableLogicalSessionCacheRefresh parameter
to true: mongod --port 27217 --setParameter disableLogicalSessionCacheRefresh= true Other settings (e.g. --dbpath , etc.) remain the same. [ 1 ] ( 1 , 2 ) By running the mongod on a different
port, you ensure that the other members of the replica set and all
clients will not contact the member while you are building the
index. B. Build the Index Connect directly to the mongod instance running as a
standalone on the new port and create the new index for this
instance. For example, connect mongosh to the instance, and
use the createIndex() to create an ascending
index on the username field of the records collection: db.records.createIndex( { username: 1 } ) C. Restart the Program mongod as a Replica Set Member When the index build completes, shutdown the mongod instance. Undo the configuration changes made when starting as a
standalone to return the its original configuration and restart as
a member of the replica set. Important Be sure to remove the disableLogicalSessionCacheRefresh parameter. For example, to restart your replica set member: Configuration File Command-line Options If you are using a configuration file: Revert to the original port number. Uncomment the replication.replSetName . Remove parameter disableLogicalSessionCacheRefresh in the setParameter section. For example: net: bindIp: localhost,<hostname(s)|ip address(es)> port: 27017 replication: replSetName: myRepl Other settings (e.g. storage.dbPath , etc.) remain the same. And restart: mongod --config <path/To/ConfigFile> If you are using command-line options, Revert to the original port number Include the --replSet option. Remove parameter disableLogicalSessionCacheRefresh . For example: mongod --port 27017 --replSet myRepl Other settings (e.g. --dbpath , etc.) remain the same. Allow replication to catch up on this member. D. Repeat the Procedure for the Remaining Secondaries Once the member catches up with the other members of the set, repeat
the procedure one member at a time for the remaining secondary members: A. Stop One Secondary and Restart as a Standalone B. Build the Index C. Restart the Program mongod as a Replica Set Member E. Build the Index on the Primary When all the secondaries have the new index, step down the primary,
restart it as a standalone using the procedure described above,
and build the index on the former primary: Use the rs.stepDown() method in mongosh to step down the primary. Upon successful stepdown, the current primary
becomes a secondary and the replica set members elect a new primary. A. Stop One Secondary and Restart as a Standalone B. Build the Index C. Restart the Program mongod as a Replica Set Member Back Builds Next Create on Sharded Clusters
