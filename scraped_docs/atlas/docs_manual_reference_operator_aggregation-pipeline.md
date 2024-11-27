# Aggregation Stages - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference Aggregation Stages On this page Compatibility db.collection.aggregate() Stages db.aggregate() Stages Stages Available for Updates In the db.collection.aggregate() method and db.aggregate() method, pipeline stages appear in an array. In the Atlas UI, you can arrange pipeline
stages using the aggregation pipeline builder . Documents pass
through the stages in sequence. Compatibility You can use pipeline stages for deployments hosted in the following
environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB db.collection.aggregate() Stages All stages except the $out , $merge , $geoNear , $changeStream , and $changeStreamSplitLargeEvent stages can appear multiple
times in a pipeline. Note For details on a specific operator, including syntax and examples,
click on the link to the operator's reference page. db. collection . aggregate ( [ { < stage > } , ... ] ) Stage Description $addFields Adds new fields to documents. Similar to $project , $addFields reshapes each
document in the stream; specifically, by adding new fields to
output documents that contain both the existing fields
from the input documents and the newly added fields. $set is an alias for $addFields . $bucket Categorizes incoming documents into groups, called buckets,
based on a specified expression and bucket boundaries. $bucketAuto Categorizes incoming documents into a specific number of
groups, called buckets, based on a specified expression.
Bucket boundaries are automatically determined in an attempt
to evenly distribute the documents into the specified number
of buckets. $changeStream Returns a Change Stream cursor for the
collection.  This stage can only occur once in an aggregation
pipeline and it must occur as the first stage. $changeStreamSplitLargeEvent Splits large change stream events that exceed 16
MB into smaller fragments returned in a change stream cursor. You can only use $changeStreamSplitLargeEvent in a $changeStream pipeline and it must be the final stage in the pipeline. $collStats Returns statistics regarding a collection or view. $count Returns a count of the number of documents at this stage of
the aggregation pipeline. Distinct from the $count aggregation accumulator. $densify Creates new documents in a sequence of documents where certain values
in a field are missing. $documents Returns literal documents from input expressions. $facet Processes multiple aggregation pipelines within a single stage on the same set
of input documents. Enables the creation of multi-faceted
aggregations capable of characterizing data across multiple
dimensions, or facets, in a single stage. $fill Populates null and missing field values within documents. $geoNear Returns an ordered stream of documents based on the proximity to a
geospatial point. Incorporates the functionality of $match , $sort , and $limit for
geospatial data. The output documents include an additional distance
field and can include a location identifier field. $graphLookup Performs a recursive search on a collection. To each output
document, adds a new array field that contains the traversal
results of the recursive search for that document. $group Groups input documents by a specified identifier expression
and applies the accumulator expression(s), if specified, to
each group. Consumes all input documents and outputs one
document per each distinct group. The output documents only
contain the identifier field and, if specified, accumulated
fields. $indexStats Returns statistics regarding the use of each index for the
collection. $limit Passes the first n documents unmodified to the pipeline
where n is the specified limit. For each input document,
outputs either one document (for the first n documents) or
zero documents (after the first n documents). $listSampledQueries Lists sampled queries for all collections or a specific
collection. $listSearchIndexes Returns information about existing Atlas Search indexes on a specified
collection. $listSessions Lists all sessions that have been active long enough to
propagate to the system.sessions collection. $lookup Performs a left outer join to another collection in the same database to filter in documents from the "joined"
collection for processing. $match Filters the document stream to allow only matching documents
to pass unmodified into the next pipeline stage. $match uses standard MongoDB queries. For each
input document, outputs either one document (a match) or zero
documents (no match). $merge Writes the resulting documents of the aggregation pipeline to
a collection. The stage can incorporate (insert new
documents, merge documents, replace documents, keep existing
documents, fail the operation, process documents with a
custom update pipeline) the results into an output
collection. To use the $merge stage, it must be
the last stage in the pipeline. $out Writes the resulting documents of the aggregation pipeline to
a collection. To use the $out stage, it must be
the last stage in the pipeline. $planCacheStats Returns plan cache information for a
collection. $project Reshapes each document in the stream, such as by adding new
fields or removing existing fields. For each input document,
outputs one document. See also $unset for removing existing fields. $querySettings Returns query settings previously added with setQuerySettings . New in version 8.0 . $queryStats Returns runtime statistics for recorded queries. WARNING: The $queryStats aggregation stage is unsupported
and is not guaranteed to be stable in a future release. Don't build
functionality that relies on a specific output format of this stage,
since the output may change in a future release. $redact Reshapes each document in the stream by restricting the
content for each document based on information stored in the
documents themselves. Incorporates the functionality of $project and $match . Can be used to
implement field level redaction. For each input document,
outputs either one or zero documents. $replaceRoot Replaces a document with the specified embedded document. The
operation replaces all existing fields in the input document,
including the _id field. Specify a document embedded in
the input document to promote the embedded document to the
top level. $replaceWith is an alias for $replaceRoot stage. $replaceWith Replaces a document with the specified embedded document. The
operation replaces all existing fields in the input document,
including the _id field. Specify a document embedded in
the input document to promote the embedded document to the
top level. $replaceWith is an alias for $replaceRoot stage. $sample Randomly selects the specified number of documents from its
input. $search Performs a full-text search of the field or fields in an Atlas collection. $search is only available for MongoDB Atlas clusters, and is not
available for self-managed deployments. To learn more, see Atlas Search Aggregation Pipeline Stages . $searchMeta Returns different types of metadata result documents for the Atlas Search query against an Atlas collection. $searchMeta is only available for MongoDB Atlas clusters,
and is not available for self-managed deployments. To learn
more, see Atlas Search Aggregation Pipeline Stages . $set Adds new fields to documents. Similar to $project , $set reshapes each
document in the stream; specifically, by adding new fields to
output documents that contain both the existing fields
from the input documents and the newly added fields. $set is an alias for $addFields stage. $setWindowFields Groups documents into windows and applies one or more
operators to the documents in each window. New in version 5.0 . $skip Skips the first n documents where n is the specified skip
number and passes the remaining documents unmodified to the
pipeline. For each input document, outputs either zero
documents (for the first n documents) or one document (if
after the first n documents). $sort Reorders the document stream by a specified sort key. Only
the order changes; the documents remain unmodified. For each
input document, outputs one document. $sortByCount Groups incoming documents based on the value of a specified
expression, then computes the count of documents in each
distinct group. $unionWith Performs a union of two collections; i.e. combines
pipeline results from two collections into a single
result set. $unset Removes/excludes fields from documents. $unset is an alias for $project stage
that removes fields. $unwind Deconstructs an array field from the input documents to
output a document for each element. Each output document
replaces the array with an element value. For each input
document, outputs n documents where n is the number of
array elements and can be zero for an empty array. $vectorSearch Performs an ANN or ENN search on a
vector in the specified field of an Atlas collection. $vectorSearch is only available for MongoDB Atlas clusters
running MongoDB v6.0.11 or higher, and is not available for
self-managed deployments. New in version 7.0.2 . For aggregation expression operators to use in the pipeline stages, see Aggregation Operators . db.aggregate() Stages MongoDB also provides the db.aggregate() method: db. aggregate ( [ { < stage > } , ... ] ) The following stages use the db.aggregate() method and not
the db.collection.aggregate() method. Stage Description $changeStream Returns a Change Stream cursor for the
collection.  This stage can only occur once in an aggregation
pipeline and it must occur as the first stage. $currentOp Returns information on active and/or dormant operations for
the MongoDB deployment. $documents Returns literal documents from input values. $listLocalSessions Lists all active sessions recently in use on the currently
connected mongos or mongod instance. These sessions may have not yet propagated to the system.sessions collection. Stages Available for Updates You can use the aggregation pipeline for updates in: Command mongosh Methods findAndModify db.collection.findOneAndUpdate() db.collection.findAndModify() update db.collection.updateOne() db.collection.updateMany() Bulk.find.update() Bulk.find.updateOne() Bulk.find.upsert() For the updates, the pipeline can consist of the following stages: $addFields and its alias $set $project and its alias $unset $replaceRoot and its alias $replaceWith . Back Commands Next $addFields
