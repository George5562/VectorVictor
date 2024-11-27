# Manage Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes Manage Indexes On this page View Existing Indexes Remove Indexes Modify an Index Find Inconsistent Indexes Across Shards This page shows how to manage existing indexes. For instructions on
creating indexes, refer to the specific index type pages. View Existing Indexes MongoDB Shell Compass The following sections provide methods for viewing existing indexes
on a collection or an entire database. List All Indexes on a Collection To return a list of all indexes on a collection, use the db.collection.getIndexes() method or a similar method
for your driver . For example, to view all indexes on the people collection, run the
following command: db. people . getIndexes ( ) List All Indexes for a Database To list all the collection indexes in a database, run the following
command in mongosh : db. getCollectionNames ( ). forEach ( function ( collection ) { indexes = db [ collection]. getIndexes ( ) ; print ( "Indexes for " + collection + ":" ) ; printjson ( indexes) ; }) ; List Specific Type of Indexes To list all indexes of a certain type (such as hashed or text ) for
all collections in all database, run the following command in mongosh : // The following finds all hashed indexes db. adminCommand ( "listDatabases" ). databases . forEach ( function ( d ) { let mdb = db. getSiblingDB ( d. name ) ; mdb. getCollectionInfos ( { type : "collection" }). forEach ( function ( c ) { let currentCollection = mdb. getCollection ( c. name ) ; currentCollection. getIndexes ( ). forEach ( function ( idx ) { let idxValues = Object . values ( Object . assign ( { } , idx. key )) ; if ( idxValues. includes ( "hashed" )) { print ( "Hashed index: " + idx. name + " on " + d. name + "." + c. name ) ; printjson ( idx) ; } ; }) ; }) ; }) ; To view a list of all indexes on a collection in MongoDB Compass ,
click on the target collection in the left-hand pane and
select the Indexes tab. For details on the information displayed in this tab, refer to
the Compass documentation . Remove Indexes Tip Hide an Index Before Dropping It If you drop an index that is actively used in production, your
application may incur a performance degradation. Before you drop an
index, you can evaluate the potential impact of the drop by hiding the index . Hidden indexes are not used to support queries. If you hide an index
and observe substantial negative performance impact, consider keeping
and unhiding the index so queries can resume using it. To learn how to remove an existing index, see Drop an Index . To learn how to remove an index in MongoDB Compass , see Manage Indexes in Compass . Modify an Index MongoDB Shell Compass To modify an existing index in the MongoDB Shell, you need to
drop and recreate the index. The exception to this rule is TTL indexes , which can be modified
via the collMod command in conjunction with the index collection flag. To modify an existing index in MongoDB Compass , you need to drop and
recreate the index. Minimize Performance Impact With a Temporary Index If you drop an index that is actively used in production, your
application may incur a performance degradation. To ensure queries can
still use an index during modification, you can create a temporary,
redundant index that contains the same fields as the modified index. Example This example creates a new index and modifies that index to make it unique . 1 Create a siteAnalytics collection with an index on the url field Run this command: db. siteAnalytics . createIndex ( { "url" : 1 } ) The command returns the name of the index: url_1 2 Create a temporary index that contains the url field Run this command: db. siteAnalytics . createIndex ( { "url" : 1 , "dummyField" : 1 } ) The command returns the name of the index: url_1_dummyField_1 This temporary index lets you safely drop the original { "url":
1 } index without impacting performance. 3 Drop the original index Run this command: db. siteAnalytics . dropIndex ( { "url_1" } ) The command returns: { nIndexesWas : 3 , ok : 1 } 4 Recreate the { "url": 1 } index with the unique property Run this command: db. siteAnalytics . createIndex ( { "url" : 1 } , { "unique" : true } ) The command returns the name of the index: url_1 The url_1 index is recreated and you can drop the temporary
index without impacting performance. Queries on the url field
can use the new unique index. 5 Drop the temporary index Run this command: db. siteAnalytics . dropIndex ( { "url_1_dummyField_1" } ) The command returns: { nIndexesWas : 3 , ok : 1 } 6 Confirm that the index was updated To view the indexes on the siteAnalytics collection, run this
command: db. siteAnalytics . getIndexes ( ) The command returns these indexes, indicating that the url_1 index is now unique: [ { v : 2 , key : { _id : 1 } , name : '_id_' } , { v : 2 , key : { url : 1 } , name : 'url_1' , unique : true } ] Find Inconsistent Indexes Across Shards A sharded collection has an inconsistent index if the collection does
not have the exact same indexes (including the index options) on each
shard that contains chunks for the collection. Although inconsistent
indexes should not occur during normal operations, inconsistent indexes
can occur , such as: When a user is creating an index with a unique key constraint and
one shard contains a chunk with duplicate documents. In such cases,
the create index operation may succeed on the shards without
duplicates but not on the shard with duplicates. When a user is creating an index across the shards in a rolling
manner (i.e. manually building the index one by one across the
shards) but either
fails to build the index for an associated shard or incorrectly
builds an index with different specification. The config server primary, by default, checks
for index inconsistencies across the shards for sharded collections, and
the command serverStatus , when run on the config server
primary, returns the field shardedIndexConsistency field to report on the number of sharded collections with index
inconsistencies. If shardedIndexConsistency reports any index
inconsistencies, you can run the following pipeline for your
sharded collections until you find the inconsistencies. Define the following aggregation pipeline : const pipeline = [ // Get indexes and the shards that they belong to. { $indexStats : { }} , // Attach a list of all shards which reported indexes to each document from $indexStats. { $group : { _id : null , indexDoc : { $push : "$$ROOT" } , allShards : { $addToSet : "$shard" }}} , // Unwind the generated array back into an array of index documents. { $unwind : "$indexDoc" } , // Group by index name. { $group : { "_id" : "$indexDoc.name" , "shards" : { $push : "$indexDoc.shard" } , // Convert each index specification into an array of its properties // that can be compared using set operators. "specs" : { $push : { $objectToArray : { $ifNull : [ "$indexDoc.spec" , { }]}}} , "allShards" : { $first : "$allShards" } } } , // Compute which indexes are not present on all targeted shards and // which index specification properties aren't the same across all shards. { $project : { missingFromShards : { $setDifference : [ "$allShards" , "$shards" ]} , inconsistentProperties : { $setDifference : [ { $reduce : { input : "$specs" , initialValue : { $arrayElemAt : [ "$specs" , 0 ]} , in : { $setUnion : [ "$$value" , "$$this" ]}}} , { $reduce : { input : "$specs" , initialValue : { $arrayElemAt : [ "$specs" , 0 ]} , in : { $setIntersection : [ "$$value" , "$$this" ]}}} ] } } } , // Only return output that indicates an index was inconsistent, i.e. either a shard was missing // an index or a property on at least one shard was not the same on all others. { $match : { $expr : { $or : [ { $gt : [ { $size : "$missingFromShards" } , 0 ]} , { $gt : [ { $size : "$inconsistentProperties" } , 0 ]} , ] } } } , // Output relevant fields. { $project : { _id : 0 , indexName : "$$ROOT._id" , inconsistentProperties : 1 , missingFromShards : 1 }} ] ; Run the aggregation pipeline for the sharded collection to test. For
example, to test if the sharded collection test.reviews has
inconsistent indexes across its associated shards: db. getSiblingDB ( "test" ). reviews . aggregate ( pipeline) If the collection has inconsistent indexes, the aggregation for that
collection returns details regarding the inconsistent indexes: { "missingFromShards" : [ "shardB" ] , "inconsistentProperties" : [ ] , "indexName" : "page_1_score_1" } { "missingFromShards" : [ ] , "inconsistentProperties" : [ { "k" : "expireAfterSeconds" , "v" : 60 } , { "k" : "expireAfterSeconds" , "v" : 600 } ] , "indexName" : "reviewDt_1" } The returned documents indicate two inconsistencies for the sharded
collection test.reviews : An index named page_1_score_1 is missing from the collection
on shardB . An index named reviewDt_1 has inconsistent properties across
the collection's shards, specifically, the expireAfterSeconds properties differ. To resolve the inconsistency where an index is missing  from the collection on a particular shard(s), You can either: Perform a rolling index build for the collection
on the affected shard(s). -OR- Issue an index build db.collection.createIndex() from a mongos instance. The operation only builds the
collection's index on the shard(s) missing the index. To resolve where the index properties differ across the shards, Drop the incorrect index from the collection on the affected
shard(s) and rebuild the index. To rebuild the index, you can either: Perform a rolling index build for the collection
on the affected shard. -OR- Issue an index build db.collection.createIndex() from a mongos instance. The operation only builds the
collection's index on the shard(s) missing the index. Alternatively, if the inconsistency is the expireAfterSeconds property,
you can run the collMod command to update the number of
seconds instead of dropping and rebuilding the index. Back Create on Sharded Clusters Next Measure Use
