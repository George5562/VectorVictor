# $changeStream (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $changeStream (aggregation) On this page Definition Stable API Support Examples Definition $changeStream Returns a Change Stream cursor on a collection, a database,
or an entire cluster. Must be used as the first stage in an aggregation pipeline. The $changeStream stage has the following syntax: { $changeStream: { allChangesForCluster: <boolean>, fullDocument: <string>, fullDocumentBeforeChange: <string>, resumeAfter: <document> showExpandedEvents: <boolean>, startAfter: <document> startAtOperationTime: <timestamp> } } Parameter Description allChangesForCluster Optional: Sets whether the change stream should include all changes
in the cluster. May only be opened on the admin database. fullDocument Optional: Specifies whether change notifications include a copy of the
full document when modified by update operations. default : Change notifications do not include the full document
for update operations. required : Change notifications includes a copy of the modified
document as it appeared immediately after the change. If the
document cannot be found, the change stream throws an error. To use this option, you must first use the collMod command to enable the changeStreamPreAndPostImages option. New in version 6.0 . updateLookup : Change notifications includes a copy of the
document modified by the change.  This document is the current
majority-committed document or null if it no longer exists. whenAvailable : Change notification includes a copy of the
modified document as it appeared immediately after the change or null if the document is unavailable. To use this option, you must first use the collMod command to enable the changeStreamPreAndPostImages option. New in version 6.0 . In the case of partial updates, the change notification also
provides a description of the change. fullDocumentBeforeChange Include the full document from before the change.
This field accepts the following values: off : Disables inclusion of the document from before the change. whenAvailable : Includes document from before the change.
The query does not fail if the unmodified document is not available. required : Includes document from before the change. The query
fails if the unmodified document is not available. resumeAfter Optional. Specifies a resume token as the
logical starting point for the change stream. Cannot be used to resume
the change stream after an invalidate event. resumeAfter is mutually exclusive with startAfter and startAtOperationTime . showExpandedEvents Specifies whether to include additional change events, such as
such as DDL and index operations. New in version 6.0 . startAfter Optional. Specifies a resume token as the
logical starting point for the change stream. Unlike resumeAfter , startAfter can resume notifications after an invalidate event by creating a new change stream. startAfter is mutually exclusive with resumeAfter and startAtOperationTime . startAtOperationTime Specifies a time as the logical starting point for the change stream.
Cannot be used with resumeAfter or startAfter fields. Stable API Support Change streams are included in Stable API V1.
However, the showExpandedEvents option is not included in Stable API V1. Examples To create a change stream cursor using the aggregation stage, run
the aggregate command. var cur = db. names . aggregate ( [ { $changeStream : { } } ] ) To open the cursor, run cur . When the change stream detects a change, the next() method returns
a change event notification. For example, after running cur.next() ,
MongoDB returns a document similar to the following: { "_id" : { _data : "8262E2EE54000000022B022C0100296E5A100448E5E3DD01364019AE8FE8C6859527E046645F6964006462E2EE54C8756C0D5CF6F0720004" } , "operationType" : "insert" , "clusterTime" : Timestamp( { t : 1659039316 , i : 2 } ) , "wallTime" : ISODate( "2022-07-28T20:15:16.148Z" ) , "fullDocument" : { "_id" : ObjectId( "62e2ee54c8756c0d5cf6f072" ) , "name" : "Walker Percy" } , "ns" : { "db" : "test" , "coll" : "names" } , "documentKey" : { _id : ObjectId( "62e2ee54c8756c0d5cf6f072" ) } } For more information on change stream notifications, see Change Events . Back $bucketAuto Next $changeStreamSplitLargeEvent
