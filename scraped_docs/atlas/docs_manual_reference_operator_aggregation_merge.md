# $merge (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $merge (aggregation) On this page Definition Compatibility Syntax Considerations Restrictions Examples Definition Note This page describes the $merge stage, which outputs the
aggregation pipeline results to a collection. For the $mergeObjects operator, which merges documents into a
single document, see $mergeObjects . $merge Writes the results of the aggregation pipeline to a specified collection. The $merge operator must be the last stage in the
pipeline. The $merge stage: Can output to a collection in the same or different database. Can output to the same collection that is being aggregated. For more
information, see Output to the Same Collection that is Being Aggregated . Consider the following points when using $merge or $out stages in an aggregation pipeline : Starting in MongoDB 5.0, pipelines with a $merge stage can run on
replica set secondary nodes if all the nodes in the cluster
have the featureCompatibilityVersion set to 5.0 or higher and the read preference allows secondary reads. $merge and $out stages run on secondary nodes, but write
operations are sent to the primary node. Not all driver versions support $merge operations sent to
the secondary nodes. For details, see the driver documentation. In earlier MongoDB versions, pipelines with $out or $merge stages always run on the primary node and read preference isn't
considered. Creates a new collection if the output collection does not already
exist. Can incorporate results (insert new documents, merge documents,
replace documents, keep existing documents, fail the operation,
process documents with a custom update pipeline) into an existing
collection. Can output to a sharded collection. Input collection can
also be sharded. For a comparison with the $out stage which also outputs
the aggregation results to a collection, see $merge and $out Comparison . Note On-Demand Materialized Views $merge can incorporate the pipeline results into an
existing output collection rather than perform a full replacement of
the collection. This functionality allows users to create on-demand
materialized views, where the content of the output collection is
incrementally updated when the pipeline is run. For more information on this use case, see On-Demand Materialized Views as well as the examples on this page. Materialized views are separate from read-only views. For
information on creating read-only views, see read-only views . Compatibility You can use $merge for deployments hosted in the following
environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Syntax $merge has the following syntax: { $merge : { into : < collection > - or - { db : < db > , coll : < collection > } , on : <identifier field> -or- [ <identifier field1>, ...],  // Optional let: <variables>,                                         // Optional whenMatched: <replace|keepExisting|merge|fail|pipeline>,  // Optional whenNotMatched: <insert|discard|fail>                     // Optional } } For example: { $merge : { into : "myOutput" , on : "_id" , whenMatched : "replace" , whenNotMatched : "insert" } } If using all default options for $merge , including writing
to a collection in the same database, you can use the simplified form: { $merge : < collection > } // Output collection is in the same database The $merge takes a document with the following fields: Field Description into The output collection. Specify either: The collection name as a string to output to a collection in
the same database where the aggregation is run. For example: into: "myOutput" The database and collection name in a document to output to a
collection in the specified database. For example: into: { db:"myDB", coll:"myOutput" } If the output collection does not exist, $merge creates the collection: For a replica set or a standalone, if the output
database does not exist, $merge also creates the database. For a sharded cluster , the specified output
database must already exist. The output collection can be a sharded collection. on Optional. Field or fields that act as a unique identifier for a
document. The identifier determines if a results document matches an existing document in the
output collection. Specify either: A single field name as a string. For example: on: "_id" A combination of fields in an array. For example: on: [ "date", "customerId" ] The order of the fields in the array does not matter, and you
cannot specify the same field multiple times. For the specified field or fields: The aggregation results documents must contain the field(s)
specified in the on , unless the on field is the _id field. If the _id field is missing from a
results document, MongoDB adds it automatically. The specified field or fields cannot contain a null or an array
value. $merge requires a unique ,
index with keys that correspond to the on identifier fields. Although the order of the index key
specification does not matter, the unique index must only contain
the on fields as its keys. The index must also have the same collation as the aggregation's collation. The unique index can be a sparse index. The unique index cannot be a partial index. For output collections that already exist, the corresponding
index must already exist. The default value for on depends on the output collection: If the output collection does not exist, the on identifier must be and defaults to the _id field. The
corresponding unique _id index is automatically created. To use a different on identifier field(s)
for a collection that does not exist, you can create the
collection first by creating a unique index on the desired
field(s). See the section on non-existent output
collection for an example. If the existing output collection is unsharded, the on identifier defaults to the _id field. If the existing output collection is a sharded collection, the on identifier defaults to all the shard
key fields and the _id field. If specifying a different on identifier, the on must contain all the shard key
fields. whenMatched Optional. The behavior of $merge if a result document
and an existing document in the collection have the same value
for the specified on field(s). You can specify either: One of the pre-defined action strings: Action Description "replace" Replace the existing document in the output
collection with the matching results
document. When performing a replace, the replacement document
cannot result in a modification of the _id value or,
if the output collection is sharded, the shard key
value. Otherwise, the operation generates an error. To avoid this error, if the on field does not
include the _id field, remove the _id field in the
aggregation results to avoid the error, such as with a preceding $unset stage, and so on. "keepExisting" Keep the existing document in the output
collection . "merge" (Default) Merge the matching documents (similar to the $mergeObjects operator). If the results document contains fields not in the
existing document, add these new fields to the
existing document. If the results document contains fields in the existing
document, replace the existing field values with those
from the results document. For example, if the output collection has the document: { _id: 1, a: 1, b: 1 } And the aggregation results has the document: { _id: 1, b: 5, z: 1 } Then, the merged document is: { _id: 1, a: 1, b: 5, z: 1 } When performing a merge, the merged document cannot
result in a modification of the _id value or, if the
output collection is sharded, the shard key value.
Otherwise, the operation generates an error. To avoid this error, if the on field does not
include the _id field, remove the _id field in the
aggregation results to avoid the error, such as with a preceding $unset stage, and so on. "fail" Stop and fail the aggregation operation. Any changes to
the output collection from previous documents are not
reverted. An aggregation pipeline to update the document in the
collection. [ <stage1>, <stage2> ... ] The pipeline can only consist of the following stages: $addFields and its alias $set $project and its alias $unset $replaceRoot and its alias $replaceWith The pipeline cannot modify the on field's
value. For example, if you are matching on the field month ,
the pipeline cannot modify the month field. The whenMatched pipeline can directly access the fields of
the existing documents in the output collection using $<field> . To access the fields from the aggregation results documents,
use either: The built-in $$new variable to access the field.
Specifically, $$new.<field> . The $$new variable is
only available if the let specification is
omitted. The user-defined variables in the let field. Specify the double dollar sign ($$) prefix together with the variable
name in the form $$<variable_name> . For example, $$year . If the
variable is set to a document, you can also include a document field in
the form $$<variable_name>.<field> . For example, $$year.month . For more examples, see Use Variables to Customize the Merge . let Optional. Specifies variables for use in the whenMatched
pipeline . Specify a document with the variable names and value expressions: { < variable_name_1 > : < expression_1 > , ... , < variable_name_n > : < expression_n > } If unspecified, defaults to { new: "$$ROOT" } (see ROOT ). The whenMatched pipeline can access the $$new variable. To access the variables in the whenMatched pipeline : Specify the double dollar sign ($$) prefix together with the variable
name in the form $$<variable_name> . For example, $$year . If the
variable is set to a document, you can also include a document field in
the form $$<variable_name>.<field> . For example, $$year.month . For examples, see Use Variables to Customize the Merge . whenNotMatched Optional. The behavior of $merge if a result document
does not match an existing document in the out collection. You can specify one of the pre-defined action strings: Action Description "insert" (Default) Insert the document into the output collection. "discard" Discard the document. Specifically, $merge does
not insert the document into the output collection. "fail" Stop and fail the aggregation operation. Any changes
already written to the output collection are not
reverted. Considerations _id Field Generation If the _id field is not present in a document from the
aggregation pipeline results, the $merge stage generates
it automatically. For example, in the following aggregation pipeline, $project excludes the _id field from the documents
passed into $merge . When $merge writes these
documents to the "newCollection" , $merge generates a
new _id field and value. db. sales . aggregate ( [ { $project : { _id : 0 } } , { $merge : { into : "newCollection" } } ] ) Create a New Collection if Output Collection is Non-Existent The $merge operation creates a new collection if the
specified output collection does not exist. The output collection is created when $merge writes
the first document into the collection and is immediately visible. If the aggregation fails, any writes completed by the $merge before the error will not be rolled back. Note For a replica set or a standalone, if the
output database does not exist, $merge also creates
the database. For a sharded cluster , the specified
output database must already exist. If the output collection does not exist, $merge requires
the on identifier to be the _id field. To use a
different on field value for a collection that does not exist, you
can create the collection first by creating a unique index on the
desired field(s) first. For example, if the output collection newDailySales201905 does not exist and you want to specify the salesDate field as the on identifier: db. newDailySales201905 . createIndex ( { salesDate : 1 } , { unique : true } ) db. sales . aggregate ( [ { $match : { date : { $gte : new Date ( "2019-05-01" ) , $lt : new Date ( "2019-06-01" ) } } } , { $group : { _id : { $dateToString : { format : "%Y-%m-%d" , date : "$date" } } , totalqty : { $sum : "$quantity" } } } , { $project : { _id : 0 , salesDate : { $toDate : "$_id" } , totalqty : 1 } } , { $merge : { into : "newDailySales201905" , on : "salesDate" } } ] ) Output to a Sharded Collection The $merge stage can output to a sharded collection.
When the output collection is sharded, $merge uses
the _id field and all the shard key fields as the default on identifier. If you override the default, the on identifier must include all the shard key fields: { $merge : { into : "<shardedColl>" or { db : "<sharding enabled db>" , coll : "<shardedColl>" } , on : [ "<shardkeyfield1>" , "<shardkeyfield2>" , ... ] , // Shard key fields and any additional fields let : < variables > , // Optional whenMatched : <replace|keepExisting|merge|fail|pipeline>,  // Optional whenNotMatched: <insert|discard|fail>                     // Optional } } For example, use the sh.shardCollection() method
to create a new sharded collection newrestaurants with the postcode field as the shard key. sh. shardCollection ( "exampledb.newrestaurants" , // Namespace of the collection to shard { postcode : 1 } , // Shard key ) ; The newrestaurants collection will contain documents with
information on new restaurant openings by month ( date field) and
postcode (shard key); specifically, the on identifier is ["date", "postcode"] (the ordering of the fields
does not matter). Because $merge requires a unique
index with keys that correspond to the on identifier fields, create the unique index
(the ordering of the fields do not matter): [ 1 ] use exampledb db. newrestaurants . createIndex ( { postcode : 1 , date : 1 } , { unique : true } ) With the sharded collection restaurants and the unique index
created, you can use $merge to output the aggregation
results to this collection, matching on [ "date", "postcode" ] as in this example: use exampledb db. openings . aggregate ( [ { $group : { _id : { date : { $dateToString : { format : "%Y-%m" , date : "$date" } } , postcode : "$postcode" } , restaurants : { $push : "$restaurantName" } } } , { $project : { _id : 0 , postcode : "$_id.postcode" , date : "$_id.date" , restaurants : 1 } } , { $merge : { into : "newrestaurants" , "on" : [ "date" , "postcode" ] , whenMatched : "replace" , whenNotMatched : "insert" } } ]) [ 1 ] The sh.shardCollection() method can also create a
unique index on the shard key when passed the { unique: true
} option if: the shard key is range-based , the collection is empty, and a unique
index on the shard key doesn't already exist. In the previous example, because the on identifier is the
shard key and another field, a separate operation to create the
corresponding index is required. Replace Documents ( $merge ) vs Replace Collection ( $out ) $merge can replace an existing document in the output
collection if the aggregation results contain a document or
documents that match based on the on specification. As such, $merge can replace all documents
in the existing collection if the aggregation results include
matching documents for all existing documents in the collection and
you specify "replace" for whenMatched . However, to replace an existing collection regardless of the
aggregation results, use $out instead. Existing Documents and _id and Shard Key Values The $merge errors if the $merge results in a
change to an existing document's _id value. Tip To avoid this error, if the on field does not
include the _id field, remove the _id field in the
aggregation results to avoid the error, such as with a preceding $unset stage, and so on. Additionally, for a sharded collection, $merge also
generates an error if it results in a change to the shard key value
of an exising document. Any writes completed by the $merge before the error will
not be rolled back. Unique Index Constraints If the unique index used by $merge for on field(s) is dropped mid-aggregation, there is no
guarantee that the aggregation will be killed. If the aggregation
continues, there is no guarantee that documents do not have
duplicate on field values. If the $merge attempts to write a document that violates
any unique index on the output collection, the operation generates an
error. For example: Insert a non-matching document that violates a unique index other
than the index on the on field(s). Fail if there is a matching
document in the collection. Specifically, the operation attempts
to insert the matching document which violates the unique index on
the on field(s). Replace an existing document with a new document that
violates a unique index other than the index on the on field(s). Merge the matching documents that
results in a document that violates a unique index other than the
index on the on field(s). Schema Validation If your collection uses schema validation and has validationAction set to error , inserting an invalid document or updating a document with
invalid values with $merge throws a MongoServerError and the
document is not written to the target collection. If there are multiple
invalid documents, only the first invalid document encountered throws an
error. All valid documents are written to the target collection, and all
invalid documents fail to write. whenMatched Pipeline Behavior If all of the following are true for a $merge stage, $merge inserts the document directly into the output
collection: The value of whenMatched is an
aggregation pipeline, The value of whenNotMatched is insert , and There is no match for a document in the output collection, $merge inserts the document directly into the output
collection. $merge and $out Comparison With the introduction of $merge , MongoDB provides two
stages, $merge and $out , for writing the
results of the aggregation pipeline to a collection: $merge $out Can output to a collection in the same or different database. Can output to a collection in the same or different database. Creates a new collection if the output collection does not
already exist. Creates a new collection if the output collection does not
already exist. Can incorporate results (insert new documents, merge
documents, replace documents, keep existing documents, fail
the operation, process documents with a custom update pipeline) into
an existing collection. See also Replace Documents ( $merge ) vs Replace Collection ( $out ) . Replaces the output collection completely if it already exists. Can output to a sharded collection. Input collection can
also be sharded. Cannot output to a sharded collection. Input collection,
however, can be sharded. Corresponds to SQL statements: MERGE . INSERT INTO T2 SELECT FROM T1 . SELECT INTO T2 FROM T1 . Create/Refresh Materialized Views. Corresponds to SQL statement: INSERT INTO T2 SELECT FROM T1 . SELECT INTO T2 FROM T1 . Output to the Same Collection that is Being Aggregated Warning When $merge outputs to the same collection that is being
aggregated, documents may get updated multiple times or the operation
may result in an infinite loop. This behavior occurs when the update
performed by $merge changes the physical location of
documents stored on disk. When the physical location of a document
changes, $merge may view it as an entirely new document,
resulting in additional updates. For more information on this
behavior, see Halloween Problem . $merge can output to the same collection that is being aggregated.
You can also output to a collection which appears in other stages of the
pipeline, such as $lookup . Restrictions Restrictions Description transactions An aggregation pipeline cannot use $merge inside a transaction . Time Series Collections An aggregation pipeline cannot use $merge to output to
a time series collection. view definition Separate from materialized view A view definition cannot include the $merge stage.
If the view definition includes nested pipeline (for example,
the view definition includes $facet stage), this $merge stage restriction applies to the nested
pipelines as well. $lookup stage $lookup stage's nested pipeline cannot include the $merge stage. $facet stage $facet stage's nested pipeline cannot include the $merge stage. $unionWith stage $unionWith stage's nested pipeline cannot include the $merge stage. "linearizable" read concern The $merge stage cannot be used in conjunction with read
concern "linearizable" . That is, if you specify "linearizable" read concern for db.collection.aggregate() , you cannot include the $merge stage in the pipeline. Examples On-Demand Materialized View: Initial Creation If the output collection does not exist, the $merge creates
the collection. For example, a collection named salaries in the zoo database
is populated with the employee salary and department history: db. getSiblingDB ( "zoo" ). salaries . insertMany ( [ { "_id" : 1 , employee : "Ant" , dept : "A" , salary : 100000 , fiscal_year : 2017 } , { "_id" : 2 , employee : "Bee" , dept : "A" , salary : 120000 , fiscal_year : 2017 } , { "_id" : 3 , employee : "Cat" , dept : "Z" , salary : 115000 , fiscal_year : 2017 } , { "_id" : 4 , employee : "Ant" , dept : "A" , salary : 115000 , fiscal_year : 2018 } , { "_id" : 5 , employee : "Bee" , dept : "Z" , salary : 145000 , fiscal_year : 2018 } , { "_id" : 6 , employee : "Cat" , dept : "Z" , salary : 135000 , fiscal_year : 2018 } , { "_id" : 7 , employee : "Gecko" , dept : "A" , salary : 100000 , fiscal_year : 2018 } , { "_id" : 8 , employee : "Ant" , dept : "A" , salary : 125000 , fiscal_year : 2019 } , { "_id" : 9 , employee : "Bee" , dept : "Z" , salary : 160000 , fiscal_year : 2019 } , { "_id" : 10 , employee : "Cat" , dept : "Z" , salary : 150000 , fiscal_year : 2019 } ]) You can use the $group and $merge stages to
initially create a collection named budgets (in the reporting database) from the data currently in the salaries collection: Note For a replica set or a standalone deployment, if the output
database does not exist, $merge also creates the
database. For a sharded cluster deployment, the specified output database
must already exist. db. getSiblingDB ( "zoo" ). salaries . aggregate ( [ { $group : { _id : { fiscal_year : "$fiscal_year" , dept : "$dept" } , salaries : { $sum : "$salary" } } } , { $merge : { into : { db : "reporting" , coll : "budgets" } , on : "_id" , whenMatched : "replace" , whenNotMatched : "insert" } } ] ) $group stage to group the salaries by the fiscal_year and dept . $merge stage writes the output of the preceding $group stage to the budgets collection in the reporting database. To view the documents in the new budgets collection: db. getSiblingDB ( "reporting" ). budgets . find ( ). sort ( { _id : 1 } ) The budgets collection contains the following documents: { "_id" : { "fiscal_year" : 2017 , "dept" : "A" } , "salaries" : 220000 } { "_id" : { "fiscal_year" : 2017 , "dept" : "Z" } , "salaries" : 115000 } { "_id" : { "fiscal_year" : 2018 , "dept" : "A" } , "salaries" : 215000 } { "_id" : { "fiscal_year" : 2018 , "dept" : "Z" } , "salaries" : 280000 } { "_id" : { "fiscal_year" : 2019 , "dept" : "A" } , "salaries" : 125000 } { "_id" : { "fiscal_year" : 2019 , "dept" : "Z" } , "salaries" : 310000 } Tip See also: On-Demand Materialized Views On-Demand Materialized View: Update/Replace Data The following example uses the collections in the previous example. The example salaries collection contains the
employee salary and department history: { "_id" : 1 , employee : "Ant" , dept : "A" , salary : 100000 , fiscal_year : 2017 } , { "_id" : 2 , employee : "Bee" , dept : "A" , salary : 120000 , fiscal_year : 2017 } , { "_id" : 3 , employee : "Cat" , dept : "Z" , salary : 115000 , fiscal_year : 2017 } , { "_id" : 4 , employee : "Ant" , dept : "A" , salary : 115000 , fiscal_year : 2018 } , { "_id" : 5 , employee : "Bee" , dept : "Z" , salary : 145000 , fiscal_year : 2018 } , { "_id" : 6 , employee : "Cat" , dept : "Z" , salary : 135000 , fiscal_year : 2018 } , { "_id" : 7 , employee : "Gecko" , dept : "A" , salary : 100000 , fiscal_year : 2018 } , { "_id" : 8 , employee : "Ant" , dept : "A" , salary : 125000 , fiscal_year : 2019 } , { "_id" : 9 , employee : "Bee" , dept : "Z" , salary : 160000 , fiscal_year : 2019 } , { "_id" : 10 , employee : "Cat" , dept : "Z" , salary : 150000 , fiscal_year : 2019 } The example budgets collection contains the cumulative yearly
budgets: { "_id" : { "fiscal_year" : 2017 , "dept" : "A" } , "salaries" : 220000 } { "_id" : { "fiscal_year" : 2017 , "dept" : "Z" } , "salaries" : 115000 } { "_id" : { "fiscal_year" : 2018 , "dept" : "A" } , "salaries" : 215000 } { "_id" : { "fiscal_year" : 2018 , "dept" : "Z" } , "salaries" : 280000 } { "_id" : { "fiscal_year" : 2019 , "dept" : "A" } , "salaries" : 125000 } { "_id" : { "fiscal_year" : 2019 , "dept" : "Z" } , "salaries" : 310000 } During the current fiscal year ( 2019 in this example), new employees
are added to the salaries collection and new head counts are
pre-allocated for the next year: db. getSiblingDB ( "zoo" ). salaries . insertMany ( [ { "_id" : 11 , employee : "Wren" , dept : "Z" , salary : 100000 , fiscal_year : 2019 } , { "_id" : 12 , employee : "Zebra" , dept : "A" , salary : 150000 , fiscal_year : 2019 } , { "_id" : 13 , employee : "headcount1" , dept : "Z" , salary : 120000 , fiscal_year : 2020 } , { "_id" : 14 , employee : "headcount2" , dept : "Z" , salary : 120000 , fiscal_year : 2020 } ]) To update the budgets collection to reflect the new
salary information, the following aggregation pipeline uses: $match stage to find all documents with fiscal_year greater than or equal to 2019 . $group stage to group the salaries by the fiscal_year and dept . $merge to write the result set to the budgets collection, replacing documents with the same _id value (in
this example, a document with the fiscal year and dept). For
documents that do not have matches in the collection, $merge inserts the new documents. db. getSiblingDB ( "zoo" ). salaries . aggregate ( [ { $match : { fiscal_year : { $gte : 2019 } } } , { $group : { _id : { fiscal_year : "$fiscal_year" , dept : "$dept" } , salaries : { $sum : "$salary" } } } , { $merge : { into : { db : "reporting" , coll : "budgets" } , on : "_id" , whenMatched : "replace" , whenNotMatched : "insert" } } ] ) After the aggregation is run, view the documents in the budgets collection: db. getSiblingDB ( "reporting" ). budgets . find ( ). sort ( { _id : 1 } ) The budgets collection incorporates the new salary data for fiscal
year 2019 and adds new documents for fiscal year 2020: { "_id" : { "fiscal_year" : 2017 , "dept" : "A" } , "salaries" : 220000 } { "_id" : { "fiscal_year" : 2017 , "dept" : "Z" } , "salaries" : 115000 } { "_id" : { "fiscal_year" : 2018 , "dept" : "A" } , "salaries" : 215000 } { "_id" : { "fiscal_year" : 2018 , "dept" : "Z" } , "salaries" : 280000 } { "_id" : { "fiscal_year" : 2019 , "dept" : "A" } , "salaries" : 275000 } { "_id" : { "fiscal_year" : 2019 , "dept" : "Z" } , "salaries" : 410000 } { "_id" : { "fiscal_year" : 2020 , "dept" : "Z" } , "salaries" : 240000 } Tip See also: On-Demand Materialized Views Only Insert New Data To ensure that the $merge does not overwrite existing data
in the collection, set whenMatched to keepExisting or fail . The example salaries collection in the zoo database contains
the employee salary and department history: { "_id" : 1 , employee : "Ant" , dept : "A" , salary : 100000 , fiscal_year : 2017 } , { "_id" : 2 , employee : "Bee" , dept : "A" , salary : 120000 , fiscal_year : 2017 } , { "_id" : 3 , employee : "Cat" , dept : "Z" , salary : 115000 , fiscal_year : 2017 } , { "_id" : 4 , employee : "Ant" , dept : "A" , salary : 115000 , fiscal_year : 2018 } , { "_id" : 5 , employee : "Bee" , dept : "Z" , salary : 145000 , fiscal_year : 2018 } , { "_id" : 6 , employee : "Cat" , dept : "Z" , salary : 135000 , fiscal_year : 2018 } , { "_id" : 7 , employee : "Gecko" , dept : "A" , salary : 100000 , fiscal_year : 2018 } , { "_id" : 8 , employee : "Ant" , dept : "A" , salary : 125000 , fiscal_year : 2019 } , { "_id" : 9 , employee : "Bee" , dept : "Z" , salary : 160000 , fiscal_year : 2019 } , { "_id" : 10 , employee : "Cat" , dept : "Z" , salary : 150000 , fiscal_year : 2019 } A collection orgArchive in the reporting database
contains historical departmental organization records for the past
fiscal years. Archived records should not be modified. { "_id" : ObjectId ( "5cd8c68261baa09e9f3622be" ) , "employees" : [ "Ant" , "Gecko" ] , "dept" : "A" , "fiscal_year" : 2018 } { "_id" : ObjectId ( "5cd8c68261baa09e9f3622bf" ) , "employees" : [ "Ant" , "Bee" ] , "dept" : "A" , "fiscal_year" : 2017 } { "_id" : ObjectId ( "5cd8c68261baa09e9f3622c0" ) , "employees" : [ "Bee" , "Cat" ] , "dept" : "Z" , "fiscal_year" : 2018 } { "_id" : ObjectId ( "5cd8c68261baa09e9f3622c1" ) , "employees" : [ "Cat" ] , "dept" : "Z" , "fiscal_year" : 2017 } The orgArchive collection has a unique compound index on the fiscal_year and dept fields. Specifically, there should be at
most one record for the same fiscal year and department combination: db. getSiblingDB ( "reporting" ). orgArchive . createIndex ( { fiscal_year : 1 , dept : 1 } , { unique : true } ) At the end of current fiscal year ( 2019 in this example), the salaries collection contain the following documents: { "_id" : 1 , "employee" : "Ant" , "dept" : "A" , "salary" : 100000 , "fiscal_year" : 2017 } { "_id" : 2 , "employee" : "Bee" , "dept" : "A" , "salary" : 120000 , "fiscal_year" : 2017 } { "_id" : 3 , "employee" : "Cat" , "dept" : "Z" , "salary" : 115000 , "fiscal_year" : 2017 } { "_id" : 4 , "employee" : "Ant" , "dept" : "A" , "salary" : 115000 , "fiscal_year" : 2018 } { "_id" : 5 , "employee" : "Bee" , "dept" : "Z" , "salary" : 145000 , "fiscal_year" : 2018 } { "_id" : 6 , "employee" : "Cat" , "dept" : "Z" , "salary" : 135000 , "fiscal_year" : 2018 } { "_id" : 7 , "employee" : "Gecko" , "dept" : "A" , "salary" : 100000 , "fiscal_year" : 2018 } { "_id" : 8 , "employee" : "Ant" , "dept" : "A" , "salary" : 125000 , "fiscal_year" : 2019 } { "_id" : 9 , "employee" : "Bee" , "dept" : "Z" , "salary" : 160000 , "fiscal_year" : 2019 } { "_id" : 10 , "employee" : "Cat" , "dept" : "Z" , "salary" : 150000 , "fiscal_year" : 2019 } { "_id" : 11 , "employee" : "Wren" , "dept" : "Z" , "salary" : 100000 , "fiscal_year" : 2019 } { "_id" : 12 , "employee" : "Zebra" , "dept" : "A" , "salary" : 150000 , "fiscal_year" : 2019 } { "_id" : 13 , "employee" : "headcount1" , "dept" : "Z" , "salary" : 120000 , "fiscal_year" : 2020 } { "_id" : 14 , "employee" : "headcount2" , "dept" : "Z" , "salary" : 120000 , "fiscal_year" : 2020 } To update the orgArchive collection to include the fiscal
year 2019 that has just ended, the following aggregation pipeline
uses: $match stage to find all documents with fiscal_year equal to 2019 . $group stage to group the employees by the fiscal_year and dept . $project stage to suppress the _id field and add
separate dept and fiscal_year field. When the documents
are passed to $merge , $merge automatically
generates a new _id field for the documents. $merge to write the result set to orgArchive . The $merge stage matches documents on the dept and fiscal_year fields and fails when matched. That is, if a document already exists for the same
department and fiscal year, the $merge errors. db. getSiblingDB ( "zoo" ). salaries . aggregate ( [ { $match : { fiscal_year : 2019 }} , { $group : { _id : { fiscal_year : "$fiscal_year" , dept : "$dept" } , employees : { $push : "$employee" } } } , { $project : { _id : 0 , dept : "$_id.dept" , fiscal_year : "$_id.fiscal_year" , employees : 1 } } , { $merge : { into : { db : "reporting" , coll : "orgArchive" } , on : [ "dept" , "fiscal_year" ] , whenMatched : "fail" } } ] ) After the operation, the orgArchive collection contains the following
documents: { "_id" : ObjectId ( "5caccc6a66b22dd8a8cc419f" ) , "employees" : [ "Ahn" , "Bess" ] , "dept" : "A" , "fiscal_year" : 2017 } { "_id" : ObjectId ( "5caccc6a66b22dd8a8cc419e" ) , "employees" : [ "Ahn" , "Gee" ] , "dept" : "A" , "fiscal_year" : 2018 } { "_id" : ObjectId ( "5caccd0b66b22dd8a8cc438e" ) , "employees" : [ "Ahn" , "Zeb" ] , "dept" : "A" , "fiscal_year" : 2019 } { "_id" : ObjectId ( "5caccc6a66b22dd8a8cc41a0" ) , "employees" : [ "Carl" ] , "dept" : "Z" , "fiscal_year" : 2017 } { "_id" : ObjectId ( "5caccc6a66b22dd8a8cc41a1" ) , "employees" : [ "Bess" , "Carl" ] , "dept" : "Z" , "fiscal_year" : 2018 } { "_id" : ObjectId ( "5caccd0b66b22dd8a8cc438d" ) , "employees" : [ "Bess" , "Carl" , "Wen" ] , "dept" : "Z" , "fiscal_year" : 2019 } If the orgArchive collection already contained a document for
2019 for department "A" and/or "B" , the aggregation fails because of the duplicate key error . However, any document inserted
before the error will not be rolled back. If you specify keepExisting for the matching document, the
aggregation does not affect the matching document and does not error
with duplicate key error. Similarly, if you specify replace , the
operation would not fail; however, the operation would replace the
existing document. Merge Results from Multiple Collections By default, if a document in the aggregation results matches a
document in the collection, the $merge stage merges the documents. An example collection purchaseorders is populated with the
purchase order information by quarter and regions: db. purchaseorders . insertMany ( [ { _id : 1 , quarter : "2019Q1" , region : "A" , qty : 200 , reportDate : new Date ( "2019-04-01" ) } , { _id : 2 , quarter : "2019Q1" , region : "B" , qty : 300 , reportDate : new Date ( "2019-04-01" ) } , { _id : 3 , quarter : "2019Q1" , region : "C" , qty : 700 , reportDate : new Date ( "2019-04-01" ) } , { _id : 4 , quarter : "2019Q2" , region : "B" , qty : 300 , reportDate : new Date ( "2019-07-01" ) } , { _id : 5 , quarter : "2019Q2" , region : "C" , qty : 1000 , reportDate : new Date ( "2019-07-01" ) } , { _id : 6 , quarter : "2019Q2" , region : "A" , qty : 400 , reportDate : new Date ( "2019-07-01" ) } , ] ) Another example collection reportedsales is populated with the
reported sales information by quarter and regions: db. reportedsales . insertMany ( [ { _id : 1 , quarter : "2019Q1" , region : "A" , qty : 400 , reportDate : new Date ( "2019-04-02" ) } , { _id : 2 , quarter : "2019Q1" , region : "B" , qty : 550 , reportDate : new Date ( "2019-04-02" ) } , { _id : 3 , quarter : "2019Q1" , region : "C" , qty : 1000 , reportDate : new Date ( "2019-04-05" ) } , { _id : 4 , quarter : "2019Q2" , region : "B" , qty : 500 , reportDate : new Date ( "2019-07-02" ) } , ] ) Assume that, for reporting purposes, you want to view the data by
quarter in the following format: { "_id" : "2019Q1" , "sales" : 1950 , "purchased" : 1200 } { "_id" : "2019Q2" , "sales" : 500 , "purchased" : 1700 } You can use the $merge to merge in results from the purchaseorders collection and the reportedsales collection
to create a new collection quarterlyreport . To create the quarterlyreport collection, you can use the
following pipeline: db. purchaseorders . aggregate ( [ { $group : { _id : "$quarter" , purchased : { $sum : "$qty" } } } , // group purchase orders by quarter { $merge : { into : "quarterlyreport" , on : "_id" , whenMatched : "merge" , whenNotMatched : "insert" } } ]) First stage: The $group stage groups by the quarter and uses $sum to add the qty fields into a new purchased field. For example: To create the quarterlyreport collection, you can use this
pipeline: { "_id" : "2019Q2" , "purchased" : 1700 } { "_id" : "2019Q1" , "purchased" : 1200 } Second stage: The $merge stage writes the documents to the quarterlyreport collection in the same database. If the stage
finds an existing document in the collection that matches
on the _id field, the stage merges the matching
documents. Otherwise, the stage inserts the document. For the
initial creation, no documents should match. To view the documents in the collection, run the following operation: db. quarterlyreport . find ( ). sort ( { _id : 1 } ) The collection contains the following documents: { "_id" : "2019Q1" , "sales" : 1200 , "purchased" : 1200 } { "_id" : "2019Q2" , "sales" : 1700 , "purchased" : 1700 } Similarly, run the following aggregation pipeline against the reportedsales collection to merge the sales results into the quarterlyreport collection. db. reportedsales . aggregate ( [ { $group : { _id : "$quarter" , sales : { $sum : "$qty" } } } , // group sales by quarter { $merge : { into : "quarterlyreport" , on : "_id" , whenMatched : "merge" , whenNotMatched : "insert" } } ]) First stage: The $group stage groups by the quarter and uses $sum to add the qty fields into a new sales field. For example: { "_id" : "2019Q2" , "sales" : 500 } { "_id" : "2019Q1" , "sales" : 1950 } Second stage: The $merge stage writes the documents to the quarterlyreport collection in the same database. If the stage
finds an existing document in the collection that matches
on the _id field (the quarter), the stage merges
the matching documents. Otherwise, the stage inserts the document. To view the documents in the quarterlyreport collection after
the data has been merged, run the following operation: db. quarterlyreport . find ( ). sort ( { _id : 1 } ) The collection contains the following documents: { "_id" : "2019Q1" , "sales" : 1950 , "purchased" : 1200 } { "_id" : "2019Q2" , "sales" : 500 , "purchased" : 1700 } Use the Pipeline to Customize the Merge The $merge can use a custom update pipeline when documents match. The whenMatched pipeline can have
the following stages: $addFields and its alias $set $project and its alias $unset $replaceRoot and its alias $replaceWith An example collection votes is populated with the daily vote
tally. Create the collection with the following documents:s db. votes . insertMany ( [ { date : new Date ( "2019-05-01" ) , "thumbsup" : 1 , "thumbsdown" : 1 } , { date : new Date ( "2019-05-02" ) , "thumbsup" : 3 , "thumbsdown" : 1 } , { date : new Date ( "2019-05-03" ) , "thumbsup" : 1 , "thumbsdown" : 1 } , { date : new Date ( "2019-05-04" ) , "thumbsup" : 2 , "thumbsdown" : 2 } , { date : new Date ( "2019-05-05" ) , "thumbsup" : 6 , "thumbsdown" : 10 } , { date : new Date ( "2019-05-06" ) , "thumbsup" : 13 , "thumbsdown" : 16 } ] ) Another example collection monthlytotals has the up-to-date
monthly vote totals. Create the collection with the following
document: db. monthlytotals . insertOne ( { "_id" : "2019-05" , "thumbsup" : 26 , "thumbsdown" : 31 } ) At the end of each day, that day's votes is inserted into the votes collection: db. votes . insertOne ( { date : new Date ( "2019-05-07" ) , "thumbsup" : 14 , "thumbsdown" : 10 } ) You can use $merge with an custom pipeline to update the
existing document in the collection monthlytotals : db. votes . aggregate ( [ { $match : { date : { $gte : new Date ( "2019-05-07" ) , $lt : new Date ( "2019-05-08" ) } } } , { $project : { _id : { $dateToString : { format : "%Y-%m" , date : "$date" } } , thumbsup : 1 , thumbsdown : 1 } } , { $merge : { into : "monthlytotals" , on : "_id" , whenMatched : [ { $addFields : { thumbsup : { $add : [ "$thumbsup" , "$$new.thumbsup" ] } , thumbsdown : { $add : [ "$thumbsdown" , "$$new.thumbsdown" ] } } } ] , whenNotMatched : "insert" } } ]) First stage: The $match stage finds the specific day's votes. For
example: { "_id" : ObjectId ( "5ce6097c436eb7e1203064a6" ) , "date" : ISODate ( "2019-05-07T00:00:00Z" ) , "thumbsup" : 14 , "thumbsdown" : 10 } Second stage: The $project stage sets the _id field to a
year-month string. For example: { "thumbsup" : 14 , "thumbsdown" : 10 , "_id" : "2019-05" } Third stage: The $merge stage writes the documents to the monthlytotals collection in the same database. If the stage
finds an existing document in the collection that matches
on the _id field, the stage uses a pipeline to
add the thumbsup votes and the thumbsdown votes. This pipeline cannot directly accesses the fields from the
results document. To access the thumbsup field and the thumbsdown field in the results document, the pipeline uses
the $$new variable; i.e. $$new.thumbsup and $new.thumbsdown . This pipeline can directly accesses the thumbsup field
and the thumbsdown field in the existing document in the
collection; i.e. $thumbsup and $thumbsdown . The resulting document replaces the existing document. To view documents in the monthlytotals collection after the merge
operation, run the following operation: db. monthlytotals . find ( ) The collection contains the following document: { "_id" : "2019-05" , "thumbsup" : 40 , "thumbsdown" : 41 } Use Variables to Customize the Merge You can use variables in the $merge stage whenMatched field. Variables must
be defined before they can be used. Define variables in one or both of the following: $merge stage let aggregate command let (starting in MongoDB 5.0) To use variables in whenMatched : Specify the double dollar sign ($$) prefix together with the variable
name in the form $$<variable_name> . For example, $$year . If the
variable is set to a document, you can also include a document field in
the form $$<variable_name>.<field> . For example, $$year.month . The tabs below demonstrate behavior when variables are defined in the
merge stage, the aggregate command, or both. Merge Stage Aggregate Command Merge and Aggregate Use Variables Defined in the Merge Stage You can define variables in the $merge stage let and use the variables in the whenMatched field. Example: db. cakeSales . insertOne ( [ { _id : 1 , flavor : "chocolate" , salesTotal : 1580 , salesTrend : "up" } ] ) db. runCommand ( { aggregate : db. cakeSales . getName ( ) , pipeline : [ { $merge : { into : db. cakeSales . getName ( ) , let : { year : "2020" } , whenMatched : [ { $addFields : { "salesYear" : "$$year" } } ] } } ] , cursor : { } } ) db. cakeSales . find ( ) The example: creates a collection named cakeSales runs an aggregate command that defines a year variable in the $merge let and adds the year to cakeSales using whenMatched retrieves the cakeSales document Output: { "_id" : 1 , "flavor" : "chocolate" , "salesTotal" : 1580 , "salesTrend" : "up" , "salesYear" : "2020" } Use Variables Defined in the Aggregate Command New in version 5.0 . You can define variables in the aggregate command let and use the
variables in the $merge stage whenMatched field. Example: db. cakeSales . insertOne ( { _id : 1 , flavor : "chocolate" , salesTotal : 1580 , salesTrend : "up" } ) db. runCommand ( { aggregate : db. cakeSales . getName ( ) , pipeline : [ { $merge : { into : db. cakeSales . getName ( ) , whenMatched : [ { $addFields : { "salesYear" : "$$year" } } ] } } ] , cursor : { } , let : { year : "2020" } } ) db. cakeSales . find ( ) The example: creates a collection named cakeSales runs an aggregate command that defines a year variable in the aggregate command let and adds the year to cakeSales using whenMatched retrieves the cakeSales document Output: { "_id" : 1 , "flavor" : "chocolate" , "salesTotal" : 1580 , "salesTrend" : "up" , "salesYear" : "2020" } Use Variables Defined in the Merge Stage and Aggregate Command You can define variables in the $merge stage
and, starting in MongoDB 5.0, the aggregate command. If two variables with the same name are defined in the $merge stage and the aggregate command, the $merge stage variable is used. In this example, the year: "2020" $merge stage variable is used instead of the year: "2019" aggregate command variable: db. cakeSales . insertOne ( { _id : 1 , flavor : "chocolate" , salesTotal : 1580 , salesTrend : "up" } ) db. runCommand ( { aggregate : db. cakeSales . getName ( ) , pipeline : [ { $merge : { into : db. cakeSales . getName ( ) , let : { year : "2020" } , whenMatched : [ { $addFields : { "salesYear" : "$$year" } } ] } } ] , cursor : { } , let : { year : "2019" } } ) db. cakeSales . find ( ) Output: { _id : 1 , flavor : 'chocolate' , salesTotal : 1580 , salesTrend : 'up' , salesYear : '2020' } Back $match Next $out