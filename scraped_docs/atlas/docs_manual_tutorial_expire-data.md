# Expire Data from Collections by Setting TTL - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Properties / TTL Expire Data from Collections by Setting TTL On this page Expire Documents in the MongoDB Atlas UI Expire Documents after a Specified Number of Seconds Expire Documents with Filter Conditions Expire Documents at a Specific Clock Time Indexes Configured Using NaN This document provides an introduction to MongoDB's " time to live "
or TTL collection feature. TTL collections make it possible to
store data in MongoDB and have the mongod automatically
remove data after a specified number of seconds or at a specific clock
time. You can expire data for deployments hosted in the following
environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Data expiration is useful for some classes of information, including
machine generated event data, logs, and session information that only
need to persist for a limited period of time. A special TTL index property supports the
implementation of TTL collections. The TTL feature relies on a
background thread in mongod that reads the date-typed values
in the index and removes expired documents from the
collection. To create a TTL index, use createIndex() .
Specify an index field that is either a date type or an array that contains date type values.
Use the expireAfterSeconds option to specify a TTL value in seconds. Note The TTL index is a single field index. Compound indexes do not
support the TTL property. For more information on TTL indexes, see TTL Indexes . You can modify the expireAfterSeconds of an existing TTL index
using the collMod command. If a time series collection contains documents with timeField timestamps before 1970-01-01T00:00:00.000Z or after 2038-01-19T03:14:07.000Z , no documents are deleted from the
collection by the TTL "time to live" feature. Expire Documents in the MongoDB Atlas UI To expire data in the Atlas UI , follow
these steps: 1 In the MongoDB Atlas UI, go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Navigate to the collection For the cluster that contains the data you want to
expire, click Browse Collections . In the left navigation pane, select the database. In the left navigation pane, select the collection. 3 Open the Create Index modal Click the Indexes tab. Click Create Index . 4 Create the index with the expiresAfterSeconds option In the Fields section, enter the index key
specification document. For this example, enter the
following text to create an index on the expiresAfter field: { "expiresAfter": 1 } In the Options section, enter the expireAfterSeconds option. For this example, enter the
following text to expire the data 1 second after the expiresAfter field's value: { expireAfterSeconds: 1 } Click Review . Click Confirm . 5 Add a document that contains the expiresAfter field to the collection In the left navigation pane, select the collection that
contains the index. Click the Find tab. Click Insert Document . Click the text field under the _id field and enter
the field name expiresAfter . Click the text field next to expiresAfter and enter the
following value: 2023-10-01T12:00:00.000+00:00 This value expires data after 12:00 on October
1, 2023. Click the data type drop-down menu and change the data type
value to Date . Click Insert . The document will expire automatically one second after the expiredAfter field's value. The TTL index may take 1-2 seconds to expire the document.
You may need to refresh the UI to see that MongoDB Atlas deletes
the expired document. Expire Documents after a Specified Number of Seconds You can expire data after a specified number of seconds in the terminal.
To expire data after a specified number of seconds has passed since the
indexed field, create a TTL index on a field that holds values of BSON
date type or an array of BSON date-typed objects and specify a
positive non-zero value in the expireAfterSeconds field. A document
will expire when the number of seconds in the expireAfterSeconds field has passed since the time specified in its indexed field. [ 1 ] The TTL index expireAfterSeconds value must be within 0 and 2147483647 inclusive. For example, the following operation creates an index on the log_events collection's createdAt field and specifies the expireAfterSeconds value of 10 to set the expiration time to
be ten seconds after the time specified by createdAt . db. log_events . createIndex ( { "createdAt" : 1 } , { expireAfterSeconds : 10 } ) When adding documents to the log_events collection, set the createdAt field to the current time: db. log_events . insertOne ( { "createdAt" : new Date ( ) , "logEvent" : 2 , "logMessage" : "Success!" } ) MongoDB will automatically delete documents from the log_events collection when the document's createdAt value [ 1 ] is older than the number of seconds
specified in expireAfterSeconds . [ 1 ] ( 1 , 2 ) If the field contains an array of BSON
date-typed objects, data expires if at least one of BSON date-typed
object is older than the number of seconds specified in expireAfterSeconds . Expire Documents with Filter Conditions To expire documents with specific filter expressions, you can create
an index that is both a partial and a TTL index. Create a partial TTL index: db. foo . createIndex ( { F : 1 } , { name : "Partial-TTL-Index" , partialFilterExpression : { D : 1 } , expireAfterSeconds : 10 } ) Insert two documents, one of which matches the filter expression { D : 1 } of the partialFilterExpression : db. foo . insertMany ( [ { "F" : ISODate ( "2019-03-07T20:59:18.428Z" ) , "D" : 3 } , { "F" : ISODate ( "2019-03-07T20:59:18.428Z" ) , "D" : 1 } ] ) Wait for ten seconds then query the foo collection: db. foo . find ( { } , { _id : 0 , F : 1 , D : 1 }) The document that matches the partialFilterExpression of { D : 1 } is deleted (expired). As a result, only
one document remains in the foo collection: { "F" : ISODate ( "2019-03-07T20:59:18.428Z" ) , "D" : 3 } Expire Documents at a Specific Clock Time You can expire data at a specified clock time in the terminal. To
expire documents at a specific clock time, begin by creating a TTL
index on a field that holds values of BSON date type or an array of
BSON date-typed objects and specify an expireAfterSeconds value
of 0 . For each document in the collection, set the indexed date
field to a value corresponding to the time the document should expire.
If the indexed date field contains a date in the past, MongoDB
considers the document expired. For example, the following operation creates an index on the log_events collection's expireAt field and specifies the expireAfterSeconds value of 0 : db. log_events . createIndex ( { "expireAt" : 1 } , { expireAfterSeconds : 0 } ) For each document, set the value of expireAt to correspond to the
time the document should expire. For example, the following insertOne() operation adds a document that
expires at July 22, 2013 14:00:00 . db. log_events . insertOne ( { "expireAt" : new Date ( 'July 22, 2013 14:00:00' ) , "logEvent" : 2 , "logMessage" : "Success!" } ) MongoDB will automatically delete documents from the log_events collection when the documents' expireAt value is older than the
number of seconds specified in expireAfterSeconds , i.e. 0 seconds older in this case. As such, the data expires at the specified expireAt value. Indexes Configured Using NaN Warning Possible Data Loss When a TTL index has expireAfterSeconds set to NaN , upgrade,
downgrade, and certain syncing operations can lead to unexpected
behavior and possible data loss. Do not set expireAfterSeconds to NaN in your TTL index
configuration. Prior to MongoDB 5.0, when a TTL index has expireAfterSeconds set to NaN , MongoDB logs an error and does not remove any records. From MongoDB 5.0.0 - 5.0.13 (and 6.0.0 - 6.0.1), NaN is treated as 0 . If a TTL index is configured with expireAfterSeconds set to NaN , all TTL-indexed documents expire immediately. Starting in MongoDB 5.0.14 (and 6.0.2), the server will not use TTL
indexes that have expireAfterSeconds set to NaN . However, there are still some situations which may result in unexpected
behavior. Documents may expire: During an initial sync to an earlier version from MongoDB 5.0.0 -
5.0.13 (or 6.0.0 - 6.0.1). When upgrading from an earlier version to MongoDB 5.0.0 - 5.0.13. When restoring a collection from a pre-5.0 mongodump into a MongoDB 5.0.0 - 5.0.13 (or 6.0.0 - 6.0.1) instance. To avoid problems, either drop or correct any misconfigured TTL indexes. 1 Identify misconfigured indexes. Run the following script in the mongosh shell. The
script does not work in the legacy mongo shell. function getNaNIndexes ( ) { const nan_index = [ ] ; const dbs = db. adminCommand ( { listDatabases : 1 }). databases ; dbs. forEach ( ( d ) => { if ( d. name ! = 'local' ) { const listCollCursor = db . getSiblingDB ( d. name ) . runCommand ( { listCollections : 1 }). cursor ; const collDetails = { db : listCollCursor. ns . split ( ".$cmd" ) [ 0 ] , colls : listCollCursor. firstBatch . map ( ( c ) => c. name ) , } ; collDetails. colls . forEach ( ( c ) => db . getSiblingDB ( collDetails. db ) . getCollection ( c) . getIndexes ( ) . forEach ( ( entry ) => { if ( Object . is ( entry. expireAfterSeconds , NaN )) { nan_index. push ( { ns : ` ${collDetails.db} . ${c} ` , index : entry }) ; } }) ) ; } }) ; return nan_index ; } ; getNaNIndexes ( ) ; 2 Correct misconfigured indexes. Use the collMod command to update any misconfigured expireAfterSeconds values that the script found. As an alternative, you can drop any
misconfigured TTL indexes and recreate them later using the createIndexes command. Back TTL Next Unique
