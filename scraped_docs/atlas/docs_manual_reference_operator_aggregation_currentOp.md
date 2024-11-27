# $currentOp (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $currentOp (aggregation) On this page Definition Constraints Examples Output Fields Definition $currentOp Returns a stream of documents containing information on active
and/or dormant operations as well as inactive sessions that are
holding locks as part of a transaction. The stage returns a document
for each operation or session. To run $currentOp , use
the db.aggregate() helper on the admin database. The $currentOp aggregation stage is preferred over the currentOp command and its mongosh helper method db.currentOp() . Because the currentOp command and db.currentOp() helper
method return the results in a single document, the total size of the currentOp result set is subject to the maximum 16MB BSON
size limit for documents. The $currentOp stage returns a
cursor over a stream of documents, each of which reports a single
operation. Each operation document is subject to the 16MB BSON limit,
but unlike the currentOp command, there is no limit on
the overall size of the result set. $currentOp also enables you to perform arbitrary
transformations of the results as the documents pass through the
pipeline. Syntax { $currentOp : { allUsers : < boolean > , idleConnections : < boolean > , idleCursors : < boolean > , idleSessions : < boolean > , localOps : < boolean > } } $currentOp takes an options document as its operand: Option Description allUsers Boolean. If set to false , $currentOp only reports
on operations/idle connections/idle cursors/idle sessions
belonging to the user who ran the command. If set to true , $currentOp reports
operations belonging to all users. For standalone and replica sets that enforce access control, inprog privilege is required if allUsers: true . For sharded clusters that enforce access control, the inprog privilege is required to run $currentOp . Defaults to false . idleConnections Boolean. If set to false , $currentOp only reports active
operations. If set to true , $currentOp returns all
operations, including idle connections. Defaults to false . idleCursors Boolean. If set to true , $currentOp reports on
cursors that are "idle"; i.e. open but not currently active
in a getMore operation. Information on idle cursors have the type set to "idleCursor" . Information on cursors currently active in a getMore operation information have the type set to "op" and op set to getmore . Defaults to false . idleSessions Boolean. If set to true , in addition to active/dormant operations, $currentOp reports on: Inactive sessions that are holding locks as part of a
transaction. Each inactive session appears as a separate
document in the $currentOp stream. The document for a session includes information on the session
ID in the lsid field and the transaction
in the transaction field. Information on idle sessions have the type set to "idleSession" . $currentOp.twoPhaseCommitCoordinator in inactive state If set to false , $currentOp doesn't report on: Inactive sessions $currentOp.twoPhaseCommitCoordinator information in inactive state Defaults to true . localOps Boolean. If set to true for an aggregation running on mongos , $currentOp reports only
operations running locally on that mongos . If false , then $currentOp instead reports operations running
on the shards. The localOps parameter has no effect for $currentOp aggregations running on mongod . Defaults to false . targetAllNodes Boolean.  If set to true , $currentOp outputs a document
for each data-bearing node for all shards.  If set to false , $curentOp outputs a document for each shard. For example, in a sharded cluster with three shards where each shard
is a replica set with three nodes: targetAllNodes=false outputs three documents targetAllNodes=true outputs nine documents Defaults to false . New in version 7.1 . Omitting any of the above parameters will cause $currentOp to use
that parameter's default value. Specify an empty document, as shown
below, to use the default values of all parameters. { $currentOp : { } } Constraints Pipeline $currentOp must be the first stage in the pipeline. Pipelines that start with $currentOp can only be run on
the admin database. Access Control For standalone and replica sets that enforce access control, inprog privilege is required to run $currentOp if allUsers: true . For sharded clusters that enforce access control, the inprog privilege is required to run $currentOp . Transactions $currentOp is not allowed in transactions . Redaction When using Queryable Encryption , $currentOp output redacts certain information: The output omits all fields after "command" . The output redacts "command" to include only the first element, $comment , and $db . Examples The following examples show how to use the $currentOp aggregation
stage. Inactive Sessions This example returns information on inactive sessions that are
holding locks as part of a transaction. Specifically: The first stage returns documents for all active operations as well
as inactive sessions that are holding locks as part of a transaction. The second stage filters for documents related to inactive
sessions that are holding locks as part of a transaction. db. getSiblingDB ( "admin" ). aggregate ( [ { $currentOp : { allUsers : true , idleSessions : true } } , { $match : { active : false , transaction : { $exists : true } } } ] ) You can use $currentOp.type to specify
an equivalent filter: db. getSiblingDB ( "admin" ). aggregate ( [ { $currentOp : { allUsers : true , idleSessions : true } } , { $match : { type : "idleSession" } } ] ) Tip For transactions on a sharded cluster, include localOps:true in the previous
examples for a composite view of the transactions. Both operations return documents of the form: Replica Set Sharded Cluster (localOps: true) Sharded Cluster When run on a mongod that is part of a replica set: { "type" : "idleSession" , "host" : "example.mongodb.com:27017" , "desc" : "inactive transaction" , "client" : "198.51.100.1:50428" , "connectionId" : NumberLong ( 32 ) , "appName" : "" , "clientMetadata" : { "driver" : { "name" : "PyMongo" , "version" : "3.9.0" } , "os" : { "type" : "Darwin" , "name" : "Darwin" , "architecture" : "x86_64" , "version" : "10.14.5" } , "platform" : "CPython 3.7.1.final.0" } , "lsid" : { "id" : UUID ( "ff21e1a9-a130-4fe0-942f-9e6b6c67ea3c" ) , "uid" : BinData ( 0 , "3pxqkATNUYKV/soT7qqKE0zC0BFb0pBz1pk4xXcSHsI=" ) } , "transaction" : { "parameters" : { "txnNumber" : NumberLong ( 4 ) , "autocommit" : false , "readConcern" : { "level" : "snapshot" , "afterClusterTime" : Timestamp ( 1563892246 , 1 ) } } , "readTimestamp" : Timestamp ( 0 , 0 ) , "startWallClockTime" : "2019-07-23T10:30:49.461-04:00" , "timeOpenMicros" : NumberLong ( 1913590 ) , "timeActiveMicros" : NumberLong ( 55 ) , "timeInactiveMicros" : NumberLong ( 1913535 ) , "expiryTime" : "2019-07-23T10:31:49.461-04:00" } , "waitingForLock" : false , "active" : false , "locks" : { "ReplicationStateTransition" : "w" , "Global" : "w" , "Database" : "w" , "Collection" : "w" } , "lockStats" : { "ReplicationStateTransition" : { "acquireCount" : { "w" : NumberLong ( 5 ) } } , "Global" : { "acquireCount" : { "r" : NumberLong ( 3 ) , "w" : NumberLong ( 1 ) } } , "Database" : { "acquireCount" : { "r" : NumberLong ( 2 ) , "w" : NumberLong ( 1 ) } } , "Collection" : { "acquireCount" : { "w" : NumberLong ( 1 ) } } , "Mutex" : { "acquireCount" : { "r" : NumberLong ( 3 ) } } , "oplog" : { "acquireCount" : { "r" : NumberLong ( 2 ) } } } , "waitingForFlowControl" : false , "flowControlStats" : { } , } Running $currentOp with localOps:true provides a
composite view (rather than per shard information) of the
in-progress transactions run on that mongos . db. getSiblingDB ( "admin" ). aggregate ( [ { $currentOp : { allUsers : true , idleSessions : true , localOps : true } } , { $match : { type : "idleSession" } } ] ) ; // or db. getSiblingDB ( "admin" ). aggregate ( [ { $currentOp : { allUsers : true , idleSessions : true , localOps : true } } , { $match : { active : false , transaction : { $exists : true } } } ] ) { "type" : "idleSession" , "host" : "example.mongodb.com:27017" , "desc" : "inactive transaction" , "client" : "198.51.100.1:49618" , "connectionId" : NumberLong ( 48 ) , "appName" : "" , "clientMetadata" : { "driver" : { "name" : "PyMongo" , "version" : "3.9.0" } , "os" : { "type" : "Darwin" , "name" : "Darwin" , "architecture" : "x86_64" , "version" : "10.14.6" } , "platform" : "CPython 3.7.1.final.0" , "mongos" : { "host" : "example.mongodb.com:27017" , "client" : "198.51.100.1:53268" , "version" : "4.2.1" } } , "lsid" : { "id" : UUID ( "2c9ce111-133e-45b7-a00f-a7871005cae1" ) , "uid" : BinData ( 0 , "3pxqkATNUYKV/soT7qqKE0zC0BFb0pBz1pk4xXcSHsI=" ) } , "active" : false , "transaction" : { "parameters" : { "txnNumber" : NumberLong ( 2 ) , "autocommit" : false , "readConcern" : { "level" : "snapshot" , "afterClusterTime" : Timestamp ( 1571869019 , 2 ) } } , "globalReadTimestamp" : Timestamp ( 1571869019 , 2 ) , "startWallClockTime" : "2019-10-23T18:16:59.341-04:00" , "timeOpenMicros" : NumberLong ( 169244639 ) , "timeActiveMicros" : NumberLong ( 535 ) , "timeInactiveMicros" : NumberLong ( 169244104 ) , "numParticipants" : 2 , "participants" : [ { "name" : "shardB" , "coordinator" : true , "readOnly" : false } , { "name" : "shardA" , "coordinator" : false , "readOnly" : false } ] , "numReadOnlyParticipants" : 0 , "numNonReadOnlyParticipants" : 2 } } When run without localOps:true on
the mongos , the transaction information is per
shard. When run on a mongos without localOps:true , the transaction information is per
shard. { "shard" : "shardB" , "type" : "idleSession" , "host" : "shardB.mongodb.com:27018" , "desc" : "inactive transaction" , "client_s" : "198.51.100.1:53961" , "connectionId" : NumberLong ( 63 ) , "appName" : "" , "clientMetadata" : { "driver" : { "name" : "PyMongo" , "version" : "3.9.0" } , "os" : { "type" : "Darwin" , "name" : "Darwin" , "architecture" : "x86_64" , "version" : "10.14.6" } , "platform" : "CPython 3.7.1.final.0" , "mongos" : { "host" : "example.mongodb.com:27017" , "client" : "198.51.100.1:53976" , "version" : "4.2.0" } } , "lsid" : { "id" : UUID ( "720d403c-8daf-40bb-b61e-329e20b0493b" ) , "uid" : BinData ( 0 , "3pxqkATNUYKV/soT7qqKE0zC0BFb0pBz1pk4xXcSHsI=" ) } , "transaction" : { "parameters" : { "txnNumber" : NumberLong ( 1 ) , "autocommit" : false , "readConcern" : { "level" : "snapshot" } } , "readTimestamp" : Timestamp ( 0 , 0 ) , "startWallClockTime" : "2019-10-21T18:31:12.192-04:00" , "timeOpenMicros" : NumberLong ( 24137008 ) , "timeActiveMicros" : NumberLong ( 52 ) , "timeInactiveMicros" : NumberLong ( 24136956 ) , "expiryTime" : "2019-10-21T18:32:12.192-04:00" } , "waitingForLock" : false , "active" : false , "locks" : { "ReplicationStateTransition" : "w" , "Global" : "w" , "Database" : "w" , "Collection" : "w" } , "lockStats" : { "ReplicationStateTransition" : { "acquireCount" : { "w" : NumberLong ( 3 ) } } , "Global" : { "acquireCount" : { "r" : NumberLong ( 1 ) , "w" : NumberLong ( 1 ) } } , "Database" : { "acquireCount" : { "r" : NumberLong ( 1 ) , "w" : NumberLong ( 1 ) } } , "Collection" : { "acquireCount" : { "r" : NumberLong ( 1 ) , "w" : NumberLong ( 1 ) } } , "Mutex" : { "acquireCount" : { "r" : NumberLong ( 6 ) } } } } { "shard" : "shardA" , "type" : "idleSession" , ... } Sampled Queries This example returns information on query sampling progess. The first stage returns documents for all active operations. The second stage filters for documents related to the query
analyzer. db. getSiblingDB ( "admin" ). aggregate ( [ { $currentOp : { allUsers : true , localOps : true } } , { $match : { desc : "query analyzer" } } ] ) This pipeline returns output similar to the following: Replica Set Sharded Cluster: mongos Sharded Cluster: mongod --shardsvr When run on a mongod that is part of a replica set: { "desc" : "query analyzer", "ns" : "testDb.testColl", "collUuid" : UUID("ed9dfb1d-5b7c-4c6b-82e9-b0f537335795"), "samplesPerSecond" : 5, "startTime" : ISODate("2023-08-08T16:23:22.846Z"), "sampledReadsCount" : NumberLong(2), "sampledReadsBytes" : NumberLong(346), "sampledWritesCount" : NumberLong(3), "sampledWritesBytes" : NumberLong(904) } When run on a mongos that is part of a sharded cluster: { "desc" : "query analyzer", "ns" : "testDb.testColl", "collUuid" : UUID("5130b4df-5966-434f-85f0-f8956b5ca74e"), "samplesPerSecond" : 5, "startTime" : ISODate("2023-08-08T16:15:07.427Z"), "sampledReadsCount" : NumberLong(2), "sampledWritesCount" : NumberLong(3) } When run on a mongod --shardsvr that is part of a sharded
cluster: { "desc" : "query analyzer", "ns" : "testDb.testColl", "collUuid" : UUID("5130b4df-5966-434f-85f0-f8956b5ca74e"), "startTime" : ISODate("2023-08-08T16:15:07.427Z"), "sampledReadsCount" : NumberLong(2), "sampledReadsBytes" : NumberLong(346), "sampledWritesCount" : NumberLong(3), "sampledWritesBytes" : NumberLong(904) } Output Fields Each output document may contain a subset of the following fields, as
relevant for the operation: $currentOp.type The type of operation. Values are either: op idleSession idleCursor If the $currentOp.type is op , $currentOp.op provides details on the specific operation. $currentOp.host The name of the host against which the operation is run. $currentOp.shard The name of the shard where the operation is running. Only present for sharded clusters. $currentOp.desc A description of the operation. $currentOp.connectionId An identifier for the connection where the specific operation
originated. $currentOp.client The IP address (or hostname) and the ephemeral port of the client
connection where the operation originates. For multi-document transactions, $currentOp.client stores
information about the most recent client to run an operation inside
the transaction. For standalones and replica sets only $currentOp.client_s The IP address (or hostname) and the ephemeral port of the mongos where the operation originates. For sharded clusters only $currentOp.clientMetadata Additional information on the client. For multi-document transactions, $currentOp.client stores
information about the most recent client to run an operation inside
the transaction. $currentOp.appName The identifier of the client application which ran the operation. Use
the appName connection string option to set a custom value
for the appName field. $currentOp.active A boolean value specifying whether the operation has started. Value
is true if the operation has started or false if the
operation is idle, such as an idle connection, an inactive session, or
an internal thread that is currently idle. An operation can be
active even if the operation has yielded to another operation. $currentOp.twoPhaseCommitCoordinator Information on either: The commit coordination metrics for a transaction whose
write operations span multiple shards . Commit coordination is handled by a shard, and $currentOp (run either on a mongos or a
shard member) returns a shard's coordination information only for
transactions the shard is currently coordinating. To filter for only the commit coordination metrics: db. getSiblingDB ( "admin" ). aggregate ( [ { $currentOp : { allUsers : true , idleSessions : true } } , { $match : { desc : "transaction coordinator" } } ] ) A specific commit coordination operation (i.e. type is op and desc is "TransactionCoordinator" ) spawned by the transaction
coordinator. Note If run with idleSessions: false , $currentOp does not
return the $currentOp.twoPhaseCommitCoordinator information in inactive state If access control is enabled and allUsers: false , $currentOp does not
return $currentOp.twoPhaseCommitCoordinator information. $currentOp.twoPhaseCommitCoordinator.lsid The session identifier for the multi-shard transaction. The combination of the lsid and txnNumber identifies
the transaction. Available for both the commit coordination metrics and for specific coordination
operation . $currentOp.twoPhaseCommitCoordinator.txnNumber The transaction number for the multi-shard transaction. The combination of the txnNumber and lsid identifies the
transaction. Available for both the commit coordination metrics and for specific coordination
operation . $currentOp.twoPhaseCommitCoordinator.action The specific commit coordination operation spawned by the
transaction coordinator: "sendingPrepare" "sendingCommit" "sendingAbort" "writingParticipantList" "writingDecision" "deletingCoordinatorDoc" Only available for specific coordination operation . $currentOp.twoPhaseCommitCoordinator.startTime The start date and time of the action . Only available for specific coordination operation . $currentOp.twoPhaseCommitCoordinator.numParticipants Number of shards participating in this commit. Only available for the commit coordination metrics . $currentOp.twoPhaseCommitCoordinator.state The current step/state of the commit coordination process. Step/stage Description inactive Not actively part of a commit. writingParticipantList Writing a local record of the list of shards that are part
of this multi-shard transaction. waitingForVotes Waiting for the participants to respond with vote to commit or abort. writingDecision Writing a local record of the coordinator's decision to commit or
abort based on votes. waitingForDecisionAck Waiting for participants to acknowledge the coordinator's
decision to commit or abort. deletingCoordinatorDoc Deleting the local record of commit decision. Only available for the commit coordination metrics . See also $currentOp.twoPhaseCommitCoordinator.stepDurations . $currentOp.twoPhaseCommitCoordinator.commitStartTime The date and time when the commit started. Only available for the commit coordination metrics . $currentOp.twoPhaseCommitCoordinator.hasRecoveredFromFailover A boolean that indicates whether the commit coordination was
restarted due to failover on the shard that is coordinating the
commit. If hasRecoveredFromFailover is true, then the times specified in $currentOp.twoPhaseCommitCoordinator.stepDurations may
not be accurate for all steps. Only available for the commit coordination metrics . $currentOp.twoPhaseCommitCoordinator.stepDurations A document that contains the duration, in microseconds, of the
completed or in-progress steps/state of the active
process as well as the cumulative total duration; for example: "stepDurations" : { "writingParticipantListMicros" : NumberLong ( 17801 ) , "totalCommitDurationMicros" : NumberLong ( 42488463 ) , "waitingForVotesMicros" : NumberLong ( 30378502 ) , "writingDecisionMicros" : NumberLong ( 15015 ) , "waitingForDecisionAcksMicros" : NumberLong ( 12077145 ) , "deletingCoordinatorDocMicros" : NumberLong ( 6009 ) } , If $currentOp.twoPhaseCommitCoordinator.hasRecoveredFromFailover is true, then the times specified in stepDurations may
not be accurate for all steps. For a coordinator in an inactive state, the document is empty: "stepDurations" : { } Only available for the commit coordination metrics . See $currentOp.twoPhaseCommitCoordinator.state . $currentOp.twoPhaseCommitCoordinator.decision A document that contains the commit/abort decision, for example: For a commit decision: "decision" : { "decision" : "commit" , "commitTimestamp" : Timestamp ( 1572034669 , 3 ) } For an abort decision: "decision" : { "decision" : "abort" , "abortStatus" : { "code" : 282 , "codeName" : "TransactionCoordinatorReachedAbortDecision" , "errmsg" : "Transaction exceeded deadline" } } Only available for the commit coordination metrics . $currentOp.twoPhaseCommitCoordinator.deadline The date and time by which the commit must finish. Only available for the commit coordination metrics . $currentOp.currentOpTime The start time of the operation. $currentOp.effectiveUsers An array that contains a document for each user associated with the
operation. Each user document contains the user name and the
authentication db . Tip See also: $currentOp.runBy $currentOp.runBy An array that contains a document for each user who is impersonating
the effectiveUser(s) for the
operation. The runBy document contains the user name
and the authentication db . In general, the impersonating user is
the __system user; e.g. "runBy" : [ { "user" : "__system" , "db" : "local" } ] $currentOp.opid The identifier for the operation. You can pass this value to db.killOp() in mongosh to terminate the
operation. Warning Terminate running operations with extreme caution. Only use db.killOp() to terminate operations initiated by clients
and do not terminate internal database operations. $currentOp.secs_running The duration of the operation in seconds. MongoDB calculates this
value by subtracting the current time from the start time of the
operation. Only present if the operation is running; i.e. if active is true . $currentOp.microsecs_running The duration of the operation in microseconds. MongoDB calculates this
value by subtracting the current time from the start time of the
operation. Only present if the operation is running; i.e. if active is true . $currentOp.lsid The session identifier. Only present if the operation is associated with a
session. $currentOp.transaction A document that contains multi-document transaction information. Only present if the operation is part of a transaction: On a replica set. On a sharded cluster if $currentOp is run without localOps:true . The transaction
information is per shard. On a sharded cluster if $currentOp is run with localOps:true . The transaction information is a
composite view rather than per shard. $currentOp.transaction.parameters A document that contains information on multi-document
transaction. Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.parameters.txnNumber The transaction number. Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.parameters.autocommit A boolean flag that indicates if autocommit is on for the
transaction. Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.parameters.readConcern The read concern for the
transaction. Multi-document transactions support read concern "snapshot" , "local" , and "majority" . Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.globalReadTimestamp The timestamp of the snapshot read by the operations in the
sharded cluster transaction that uses "snapshot" read
concern . For
transactions on sharded clusters, the read concern "snapshot" of the data is synchronized across
shards; i.e. other read concerns cannot guarantee that the
data is from the same snapshot view across the shards. Only present when run with localOps: true for sharded cluster transactions. $currentOp.transaction.readTimestamp The timestamp of the snapshot being read by the operations in
this transaction Only present if the operation is part of a multi-document
transaction. However, the field is not returned if: the transaction is on a sharded cluster and uses "snapshot" read concern , and $currentOp is run with localOps: true . Instead, $currentOp.transaction.globalReadTimestamp is
returned. $currentOp.transaction.startWallClockTime The date and time (with time zone) of the transaction start. Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.timeOpenMicros The duration, in microseconds, for the transaction. The timeActiveMicros value added to the timeInactiveMicros should equal the timeOpenMicros . Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.timeActiveMicros The total amount of time that the transaction has been active;
i.e. when the transaction had operations running. The timeActiveMicros value added to the timeInactiveMicros should equal the timeOpenMicros . Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.timeInactiveMicros The total amount of time that the transaction has been
inactive; i.e. when the transaction had no operations running. The timeInactiveMicros value added to the timeActiveMicros should equal the timeOpenMicros . Only present if the operation is part of a multi-document
transaction. $currentOp.transaction.numParticipants Number of shards participating in this transaction. Only present if the operation is part of a transaction on a
sharded cluster and $currentOp is run with localOps: true $currentOp.transaction.participants An array of documents detailing the participating shards in
this transaction. Each document contains the name, a flag
indicating if the shard acts as the commit coordinator, and a
flag indicating if the shard is only involved in read
operations for the transaction. { "name" : "shardA" , "coordinator" : false , "readOnly" : false } Only present if the operation is part of a transaction on a
sharded cluster and $currentOp is run with localOps: true $currentOp.transaction.numReadOnlyParticipants Number of shards only affected by read operations in this
transaction. Only present if the operation is part of a transaction on a
sharded cluster and $currentOp is run with localOps: true $currentOp.transaction.numNonReadOnlyParticipants Number of shards affected by operations other than reads in
this transaction. Only present if the operation is part of a transaction on a
sharded cluster and $currentOp is run with localOps: true $currentOp.transaction.expiryTime The date and time (with time zone) when the transaction will
time out and abort. The $currentOp.transaction.expiryTime equals the $currentOp.transaction.startWallClockTime + the transactionLifetimeLimitSeconds . For more information, see Runtime Limit for
transactions. Only present if the operation is part of a multi-document
transaction. $currentOp.op A string that identifies the specific operation type. Only present if $currentOp.type is op . The possible values are: "none" "update" "insert" "query" "command" "getmore" "remove" "killcursors" "command" operations include most commands such as the createIndexes , aggregate , and findAndModify . "query" operations include find operations and OP_QUERY operations. $currentOp.ns The namespace the operation targets. A namespace consists of
the database name and the collection name
concatenated with a dot ( . ); that is, "<database>.<collection>" . $currentOp.command A document containing the full command object associated with this
operation. For example, the following output contains the command object for a find operation on a collection named items in a
database named test : "command" : { "find" : "items" , "filter" : { "sku" : 1403978 } , ... "$db" : "test" } The following example output contains the command object for a getMore operation generated by
a command with cursor ID 19234103609 on a collection named items in a database named test : "command" : { "getMore" : NumberLong ( "19234103609" ) , "collection" : "items" , "batchSize" : 10 , ... "$db" : "test" } , If the command document exceeds 1 kilobyte, the
document has the following form: "command" : { "$truncated" : < string > , "comment" : < string > } The $truncated field contains a string summary of the document excluding
the document's comment field if present. If the summary still exceeds
1 kilobyte then it is further truncated, denoted by an ellipsis
(...) at the end of the string. The comment field is present if a comment was passed to the operation.
A comment may be attached to any database command . $currentOp.cursor A document that contains the cursor information for idleCursor and getmore operations; i.e. where type is idleCursor or op is getmore . If reporting on a getmore operation before the getmore has
accessed its cursor information, the cursor field
is not available. $currentOp.cursor.cursorId The ID of the cursor. $currentOp.cursor.createdDate The date and time when the cursor was created. $currentOp.cursor.lastAccessDate The date and time when the cursor was last used. If the cursor is actively in use (i.e. op is getmore and the type is not idleCursor ), then lastAccessDate reports either the time the previous getmore ended
or the time the cursor was created if this is the first getmore . $currentOp.cursor.nDocsReturned The cumulative number of documents returned by the cursor. $currentOp.cursor.nBatchesReturned The cumulative number of batches returned by the cursor. $currentOp.cursor.noCursorTimeout The flag that indicates that the cursor doesn't timeout when idle;
i.e. if the cursor has the noTimeout option set. If true, the cursor does not time out when idle. If false, the cursor times out when idle. Tip See also: cursor.addOption() $currentOp.cursor.tailable The flag that indicates if the cursor is a tailable cursor for a capped collection. Tailable cursors
remain open after the client exhausts the results in the initial
cursor. Tip See also: find cursor.tailable() cursor.addOption() $currentOp.cursor.awaitData The flag that indicates whether the tailable cursor should temporarily block a getMore command on the cursor while waiting for new
data rather than returning no data. For non-tailable cursors, the value is always false. Tip See also: find cursor.tailable() cursor.addOption() $currentOp.cursor.originatingCommand The originatingCommand field contains the full command object
(e.g. find or aggregate ) which originally created the
cursor. $currentOp.cursor.planSummary A string that specifies whether the cursor uses a collection scan
( COLLSCAN ) or an index scan ( IXSCAN { ... } ). The IXSCAN also includes the specification document of the index
used. Not available when running with localOps: true on mongos or when reporting on idleCursors . $currentOp.cursor.operationUsingCursorId The opid of the operation using the cursor. Only present if the cursor is not idle. $currentOp.cursor.queryFramework New in version 6.2 . A string that specifies the query framework used to process an
operation. $currentOp.planSummary A string that specifies whether the cursor uses a collection scan
( COLLSCAN ) or an index scan ( IXSCAN { ... } ). Not available when running with localOps: true on mongos . $currentOp.prepareReadConflicts The number of times the current operation had to wait for a
prepared transaction with a write to commit or abort. While waiting, the operation continues to hold any necessary locks
and storage engine resources. $currentOp.writeConflicts The number of times the current operation conflicted with
another write operation on the same document. $currentOp.numYields numYields is a counter that reports the number of times the
operation has yielded to allow other operations to complete. Typically, operations yield when they need access to data that
MongoDB has not yet fully read into memory. This allows
other operations that have data in memory to complete quickly
while MongoDB reads in data for the yielding operation. $currentOp.queryShapeHash New in version 8.0 . queryShapeHash is a hexadecimal string with the hash of a query shape . For details, see Query Shapes . $currentOp.dataThroughputLastSecond Amount of data (in MiB) processed by the validate operation in the last second. Only available for a validate operation that is currently scanning
documents. For example: "msg" : "Validate: scanning documents Validate: scanning documents: 7258/24000 30%" , "progress" : { "done" : 7258 , "total" : 24000 } , "numYields" : 0 , "dataThroughputLastSecond" : 15.576952934265137 , "dataThroughputAverage" : 15.375944137573242 , $currentOp.dataThroughputAverage The average amount of data (in MiB) processed by the validate operation. Only available for a validate operation that is currently scanning
documents. For example: "msg" : "Validate: scanning documents Validate: scanning documents: 7258/24000 30%" , "progress" : { "done" : 7258 , "total" : 24000 } , "numYields" : 0 , "dataThroughputLastSecond" : 15.576952934265137 , "dataThroughputAverage" : 15.375944137573242 , $currentOp.locks The locks document reports the type and mode of
locks the operation currently holds. The possible lock types are as
follows: Lock Type Description ParallelBatchWriterMode Represents a lock for parallel batch writer mode. In earlier versions, PBWM information was reported as part of
the Global lock information. ReplicationStateTransition Represents lock taken for replica set member state transitions. Global Represents global lock. Database Represents database lock. Collection Represents collection lock. Mutex Represents mutex. Metadata Represents metadata lock. DDLDatabase Represents a DDL database lock. New in version 7.1 . DDLCollection Represents a DDL collection
lock. New in version 7.1 . oplog Represents lock on the oplog . The possible modes are as follows: Lock Mode Description R Represents Shared (S) lock. W Represents Exclusive (X) lock. r Represents Intent Shared (IS) lock. w Represents Intent Exclusive (IX) lock. $currentOp.lockStats For each lock type and mode (see locks for
descriptions of lock types and modes), returns the following
information: $currentOp.lockStats.acquireCount Number of times the operation acquired the lock in the specified
mode. $currentOp.lockStats.acquireWaitCount Number of times the operation had to wait for the acquireCount lock acquisitions
because the locks were held in a conflicting mode. acquireWaitCount is less than or
equal to acquireCount . $currentOp.lockStats.timeAcquiringMicros Cumulative time in microseconds that the operation had to wait to
acquire the locks. timeAcquiringMicros divided by acquireWaitCount gives an
approximate average wait time for the particular lock mode. $currentOp.lockStats.deadlockCount Number of times the operation encountered deadlocks while waiting
for lock acquisitions. $currentOp.waitingForLock Returns a boolean value. waitingForLock is true if the
operation is waiting for a lock and false if the operation has
the required lock. $currentOp.msg The msg provides a message that describes the status and
progress of the operation. In the case of indexing or mapReduce
operations, the field reports the completion percentage. $currentOp.progress Reports on the progress of mapReduce or indexing operations. The progress fields corresponds to the completion percentage in
the msg field. The progress specifies the following
information: $currentOp.progress.done Reports the number of work items completed. $currentOp.progress.total Reports the total number of work items. $currentOp.killPending Returns true if the operation is currently flagged for
termination.  When the operation encounters its next safe termination point, the
operation terminates. $currentOp.waitingForFlowControl A boolean that indicates if the operation had to wait because
of flow control . $currentOp.flowControlStats The flow control statistics for this operation. $currentOp.flowControlStats.acquireCount The number of times this operation acquired a ticket. $currentOp.flowControlStats.acquireWaitCount The number of times this operation waited to acquire a ticket. $currentOp.flowControlStats.timeAcquiringMicros The total time this operation has waited to acquire a ticket. $currentOp.totalOperationTimeElapsed The total time elapsed, in seconds, for the current resharding
operation . The time is set to 0 when a new
resharding operation starts. Only present if a resharding operation is taking place. New in version 5.0 . $currentOp.remainingOperationTimeEstimated The estimated time remaining in seconds for the current resharding operation . The time is set to
-1 when a new resharding operation starts. Only present when a resharding operation is taking place. This
field may not be present if an estimate cannot not be computed. New in version 5.0 . $currentOp.approxDocumentsToCopy The approximate number of documents to be copied from the donor
shards to the recipient shards during the resharding operation . This number is an estimate that is set at the
beginning of the resharding operation and does not change after it
has been set. The number is set to 0 when a new resharding operation
starts. It is possible for $currentOp.documentsCopied and $currentOp.bytesCopied to end up exceeding $currentOp.approxDocumentsToCopy and $currentOp.approxBytesToCopy , respectively, if the
post-resharding data distribution is not perfectly uniform. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.documentsCopied The number of documents copied form donor shards to recipient shards
during the resharding operation . The
number is set to 0 when a new resharding operation starts. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.approxBytesToCopy The approximate number of bytes to be copied from the donor shards to
the recipient shards during the resharding operation . This number is an estimate that is set at the
beginning of the resharding operation and does not change after it
has been set. The number is set to 0 when a new resharding operation
starts. It is possible for $currentOp.documentsCopied and $currentOp.bytesCopied to end up exceeding $currentOp.approxDocumentsToCopy and $currentOp.approxBytesToCopy , respectively, if the
post-resharding data distribution is not perfectly uniform. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.bytesCopied The number of bytes copied from donor shards to recipient shards
during the resharding operation . The
number is set to 0 when a new resharding operation starts. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.totalCopyTimeElapsed The total elapsed time, in seconds, for ongoing data copy tasks from
donor shards to recipient shards for the current resharding
operation. The time is set to 0 when a new resharding operation starts. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.oplogEntriesFetched The number of entries fetched from the oplog for the current resharding operation . The number is set
to 0 when a new resharding operation starts. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.oplogEntriesApplied The number of entries applied to the oplog for the current resharding operation . The number is set
to 0 when a new resharding operation starts. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.totalApplyTimeElapsed The total elapsed time, in seconds, for the apply step of the
current resharding operation . In the
apply step, recipient shards apply oplog entries to modify
their data based on new incoming writes from donor shards. The time
is set to 0 when a new resharding operation starts. Only present on a recipient shard when a resharding operation is
taking place. New in version 5.0 . $currentOp.countWritesDuringCriticalSection The number of writes performed in the critical section for the current resharding operation . The critical
section prevents new incoming writes to the collection currently
being resharded. The number is set to 0 when a new resharding
operation starts. Only present on a donor shard when a resharding operation is taking
place. New in version 5.0 . $currentOp.totalCriticalSectionTimeElapsed The total elapsed time, in seconds, for the critical section of the
current resharding operation . The
critical section prevents new incoming writes to the collection
currently being resharded. The time is set to 0 when a new
resharding operation starts. Only present on a donor shard when a resharding operation is taking
place. New in version 5.0 . $currentOp.donorState The current state of a donor shard for the resharding operation . The state is set to unused when a new
resharding operation starts. Only present on a donor shard when a resharding operation is taking place. State Description unused The resharding operation is about to start or recovering from
a primary failover. preparing-to-donate The donor shard is preparing to donate data to the recipient
shards. donating-initial-data The donor shard is donating data to the recipient shards. donating-oplog-entries The donor shard is donating oplog entries to the
recipient shards. preparing-to-block-writes The donor shard is about to prevent new incoming write
operations to the collection that is being resharded. error An error occurred during the resharding operation. blocking-writes The donor shard is preventing new incoming write operations
and the donor shard has notified all recipient shards that new
incoming writes are prevented. done The donor shard has dropped the old sharded collection and the
resharding operation is complete. New in version 5.0 . $currentOp.recipientState The current state of a recipient shard for a resharding
operation . The state is set to unused when
a new resharding operation starts. Only present on a donor shard when a resharding operation is taking
place. State Description unused The resharding operation is about to start or recovering from
a primary failover. awaiting-fetch-timestamp The recipient shard is waiting for the donor shards to be
prepared to donate their data. creating-collection The recipient shard is creating the new sharded collection. cloning The recipient shard is receiving data from the donor shards. applying The recipient shard is applying oplog entries to
modify its copy of the data based on the new incoming writes
from donor shards. error An error occurred during the resharding operation . strict-consistency The recipient shard has all data changes stored in a temporary
collection. done The resharding operation is complete. New in version 5.0 . $currentOp.coordinatorState The state of the resharding coordinator for the current resharding operation . The resharding
coordinator is an operation that runs on the config server primary. The state is set to unused when a new resharding operation starts. Only present on the coordinating config server. State Description unused The resharding operation is about to start or recovering from
a primary failover. initializing The resharding coordinator has inserted the coordinator
document into config.reshardingOperations and has added
the reshardingFields to the config.collections entry
for the original collection. preparing-to-donate The resharding coordinator has created a config.collections entry for the temporary
resharding collection. has inserted entries into config.chunks for ranges based
on the new shard key. has inserted entries into config.tags for any zones
associated with the new shard key. The coordinator informs participant shards to begin the
resharding operation. The coordinator then waits until all
donor shards have picked a minFetchTimestamp and are ready
to donate. cloning The resharding coordinator informs donor shards to donate data
to recipient shards. The coordinator waits for all recipients
to finish cloning the data from the donor. applying The resharding coordinator informs recipient shards to modify
their copies of data based on new incoming writes from donor
shards. The coordinator waits for all recipients to finish
applying oplog entries. blocking-writes The resharding coordinator informs donor shards to prevent new
incoming write operations to the collection being resharded.
The coordinator then waits for all recipients to have all data
changes. aborting An unrecoverable error occurred during the resharding
operation or the abortReshardCollection command
(or the sh.abortReshardCollection() method) was run. committing The resharding coordinator removes the config.collections entry for the temporary resharding collection. The coordinator
then adds the recipientFields to the source collection's
entry. New in version 5.0 . $currentOp.opStatus The current state of a resharding operation . Only present if a resharding operation is taking place. Once the
operation has completed, the operation is removed from currentOp output. State Description actively running The resharding operation is actively running. success The resharding operation has succeeded. failure The resharding operation has failed. canceled The resharding operation was canceled. New in version 5.0 . $currentOp.collUuid The UUID of the sampled collection . This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . $currentOp.startTime The time at which query sampling began. This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . $currentOp.samplesPerSecond The maximum number of queries to sample per second. Only reported when running $currentOp on mongos . This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . $currentOp.sampledReadsCount The number of sampled read queries. This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . $currentOp.sampledWritesCount The number of sampled write queries. This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . $currentOp.sampledReadsBytes The size of the sampled read queries, in bytes. On a replica set, this is reported on every mongod . On a sharded cluster, this only reported on mongod with --shardsvr . This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . $currentOp.sampledWritesBytes The size of the sampled write queries, in bytes. On a replica set, this is reported on every mongod . On a sharded cluster, this only reported on mongod with --shardsvr . This field only appears on documents related to query sampling.
For details, see Sampled Queries . New in version 7.0 . Back $count Next $densify
