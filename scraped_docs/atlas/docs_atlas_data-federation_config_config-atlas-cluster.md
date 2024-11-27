# Atlas Cluster - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores Atlas Cluster On this page Example Configuration for Atlas Data Store Configuration Format stores databases Atlas Data Federation supports Atlas clusters as federated database instance stores. You must define
mappings in your federated database instance to your Atlas cluster to run queries
against your data. Important Information in your storage configuration is visible internally at
MongoDB and stored as operational data to monitor and improve the
performance of Atlas Data Federation. So, we recommend that you do not use PII in your
configurations. Example Configuration for Atlas Data Store Example Consider a M10 or higher Atlas cluster named myDataCenter containing data in the metrics.hardware collection. The metrics.hardware collection contains JSON
documents with metrics derived from the hardware in a datacenter.
The following configuration: Specifies the Atlas cluster named myDataCenter in the
specified project as a federated database instance store. Maps documents from the metrics.hardware collection in the Atlas cluster to the dataCenter.inventory collection in
the storage configuration. { "stores" : [ { "name" : "atlasClusterStore" , "provider" : "atlas" , "clusterName" : "myDataCenter" , "projectId" : "5e2211c17a3e5a48f5497de3" } ] , "databases" : [ { "name" : "dataCenter" , "collections" : [ { "name" : "inventory" , "dataSources" : [ { "storeName" : "atlasClusterStore" , "database" : "metrics" , "collection" : "hardware" } ] } ] } ] } Atlas Data Federation maps all the documents in the metrics.hardware collection to the dataCenter.inventory collection in the storage
configuration. Users connected to the federated database instance can use the MongoDB Query Language
and supported aggregations to analyze data in the Atlas cluster
through the dataCenter.inventory collection. When you run
queries, the query first goes to Atlas Data Federation. Therefore, if you run
aggregation queries that are supported by your Atlas cluster but
not by Atlas Data Federation, the queries will fail. To learn more about supported
and unsupported commands in Data Federation, see Supported MongoDB Commands . Tip See also: Querying Data in Your Atlas Cluster Configuration Format The federated database instance configuration has the following format: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "clusterName" : "<string>" , 7 "projectId" : "<string>" , 8 "readPreference" : { 9 "mode" : "<string>" , 10 "tagSets" : [ 11 [ { "name" : "<string>" , "value" : "<string>" } , ... ] , 12 ... 13 ] , 14 "maxStalenessSeconds" : <int> 15 } 16 } 17 ] , 18 "databases" : [ 19 { 20 "name" : "<string>" , 21 "collections" : [ 22 { 23 "name" : "<string>" , 24 "dataSources" : [ 25 { 26 "storeName" : "<string>" , 27 "database" : "<string>" , 28 "databaseRegex" : "<string>" , 29 "collection" : "<string>" , 30 "collectionRegex" : "<string>" , 31 "provenanceFieldName" : "<string>" 32 } 33 ] 34 } 35 ] , 36 "views" : [ 37 { 38 "name" : "<string>" , 39 "source" : "<string>" , 40 "pipeline" : "<string>" 41 } 42 ] 43 } 44 ] 45 } stores The stores object defines each data store associated with the
federated database instance. The federated database instance store captures files in documents in Atlas cluster. federated database instance can only access data stores defined in the stores object. databases The databases object defines the mapping between each
federated database instance store defined in stores and MongoDB collections
in the databases. stores 1 "stores" : [ 2 { 3 "name" : "<string>" , 4 "provider" : "<string>" , 5 "clusterName" : "<string>" , 6 "projectId" : "<string>" 7 "readPreference" : { 8 "mode" : "<string>" , 9 "tagSets" : [ 10 [ { "name" : "<string>" , "value" : "<string>" } , ... ] , 11 ... 12 ] , 13 "maxStalenessSeconds" : <int> 14 } , 15 "readConcern" : { 16 "level" : "<string>" 17 } 18 } 19 ] stores Array of objects where each object represents a data store to
associate with the federated database instance. The federated database instance store captures files in an S3 bucket, documents in Atlas cluster, or files stored at
publicly accessible URL s. Atlas Data Federation can only access data stores
defined in the stores object. stores.[n].name Name of the federated database instance store. The databases.[n].collections.[n].dataSources.[n].storeName field references this value as part of mapping configuration. stores.[n].provider Defines where the data is stored. Value must be atlas for a
collection in an Atlas cluster. stores.[n].clusterName Name of the Atlas cluster on which the store is based. The
cluster must exist in the same project as your federated database instance. The source field on the data partition is the name of the Atlas cluster. stores.[n].projectId Unique identifier of the project that contains the Atlas cluster on which the store is based. stores.[n].readPreference Optional. Cluster read preference , which describes how to route read
requests to the cluster. Example The following readPreference setting specifies secondary mode and ANALYTICS nodeType . { ... "stores" : [ { "provider" : "atlas" , "clusterName" : <CLUSTER_NAME> , "name" : <STORE_NAME> , "projectId" : <PROJECT_ID> , "readPreference" : { "mode" : "secondary" , "tagSets" : [ [ { "name" : "nodeType" , "value" : "ANALYTICS" } ] , ... ] } } ] } stores.[n].readPreference.mode Optional. Read preference mode that specifies which
replica set member to route the read requests to. Value can be one
of the following: primary - to route all read requests to the replica set primary primaryPreferred - to route all read requests the replica set primary and to secondary members
only if primary is unavailable secondary - to route all read requests to the secondary members of the replica set secondaryPreferred - to route all read requests to the secondary members of
the replica set and the primary on sharded clusters only if secondary members are unavailable nearest - to route all read requests to random eligible replica
set member, irrespective of whether that member is a primary or secondary If omitted, defaults to local . stores.[n].readPreference.tagSets Optional. Arrays of tag sets or tag specification documents that
contain name and value pairs for the replica set member. If
specified, Atlas Data Federation routes read requests to replica set member or
members that are associated with the specified tags. To learn more, Read Preference Tag Sets . Note Atlas Data Federation doesn't support tagSets for sharded clusters. stores.[n].readPreference.maxStalenessSeconds Optional. Maximum replication lag, or "staleness", for reads from
secondaries. To learn more about maxStalenessSeconds , see Read Preference maxStalenessSeconds . stores.[n].readConcern Optional. Consistency and isolation properties of the data read
from an Atlas cluster. To learn more, see Read Concern . The value for the level of consistency
and availability can be one of the following: local - to return data from an instance with no guarantee that the
data has been written to a majority of the replica set members. To
learn more, see Read Concern "local" . available - to return data from an instance with no guarantee that
the data has been written to a majority of the replica set members.
This can return orphaned documents when
reading from a sharded collection. To learn more, see Read
Concern "available" . majority - to return data that has been acknowledged by a
majority of the nodes on the Atlas cluster. To learn more, see Read Concern "majority" . linearizable - to return data that reflects all successful
majority-acknowledged writes that completed prior to the start of the
read operation. To learn more, see Read Concern
"linearizable" . snapshot - to return majority-committed data as it appears across
shards from a specific single point in time in the recent past. To
learn more, see Read Concern "snapshot" . databases 1 "databases" : [ 2 { 3 "name" : "<string>" , 4 "collections" : [ 5 { 6 "name" : "<string>" , 7 "dataSources" : [ 8 { 9 "storeName" : "<string>" , 10 "database" : "<string>" , 11 "databaseRegex" : "<string>" , 12 "collection" : "<string>" , 13 "collectionRegex" : "<string>" , 14 "provenanceFieldName" : "<string>" 15 } 16 ] 17 } 18 ] 19 } 20 ] databases Array of objects where each object represents a database, its
collections, and, optionally, any views on
the collections. Each database can have multiple collections and views objects. databases.[n].name Name of the database to which Atlas Data Federation maps the data contained in the
data store. You can generate databases dynamically by specifying * for the database name. Dynamically generated databases: Can exist alongside explicitly defined databases. However, Atlas Data Federation
won't dynamically generate databases with names that conflict with
explicitly defined databases in the storage configuration. Can only be from a single Atlas cluster. Atlas Data Federation won't
dynamically generate databases from multiple Atlas clusters or
other data stores. databases.[n].collections Array of objects where each object represents a collection and data
sources that map to a stores federated database instance store.
For dynamically generated databases, you can define only one
wildcard ( * ) collection object in the storage configuration. databases.[n].collections.[n].name Name of the collection to which Atlas Data Federation maps the data contained in
each databases.[n].collections.[n].dataSources.[n].storeName .
Each object in the array represents the mapping between the
collection and an object in the stores array. You can generate collection names dynamically by specifying * for the collection name and omitting the collection field. To dynamically generate wildcard ( * ) collections for
dynamically generated wilcard ( * ) databases, specify the databases.[n].collections.[n].dataSources.[n].storeName option and omit the databases.[n].collections.[n].dataSources.[n].database option. Note that for dynamically generated databases, you can
define only one wildcard ( * ) collection object in the storage
configuration. For wildcard ( * ) collections, you can also define regex patterns
using databases.[n].collections.[n].dataSources.[n].collectionRegex field to filter the collections only. databases.[n].collections.[n].dataSources Array of objects where each object represents a stores federated database instance store to map with the
collection. databases.[n].collections.[n].dataSources.[n].storeName Name of a federated database instance store to map to the <collection> .
Must match the name of an object in the stores array. databases.[n].collections.[n].dataSources.[n].database Name of the database on the Atlas cluster that contains the
collection. You must omit this setting to: Create a wildcard ( * ) collection for a wilcard ( * ) database. Glob multiple databases. databases.[n].collections.[n].dataSources.[n].databaseRegex Optional . Regex pattern to use for globbing databases to combine
multiple collections. If you specify this option, the federated database instance
instance contains a single database with collections from multiple
databases. For globbing databases, you must do the following: Omit the database field. Specify a valid name for the databases.[n].collections.[n].dataSources.[n].collection field. Example Suppose you have 2 databases named foo and bar that each
have a collection named Sales . You can combine the Sales collection from foo and bar using the databaseRegex option in your storage configuration: { "databases" : [ { "name" : "Transactions" , "collections" : [ { "name" : "AllSales" , "dataSources" : [ { "storeName" : "atlasStore" , "databaseRegex" : ".*" , "collection" : "Sales" } ] } ] } ] } For the preceding databases object, Atlas Data Federation
generates the following in your federated database instance: A virtual database named Transactions . A virtual collection named AllSales that contains data from
the collection named Sales in all the databases whose name
match the regex pattern specified in the databaseRegex option. If you specify this option, you must specify the name of
the collection. You can't specify this option for wildcard collections. databases.[n].collections.[n].dataSources.[n].collection Name of the collection in the Atlas cluster on which the federated database instance
store is based. You must omit this setting for: Creating a wildcard ( * ) collection. Creating wildcard collection names that match regex patterns. Combining multiple collections in a database using regex patterns. databases.[n].collections.[n].dataSources.[n].collectionRegex Conditional: Optional for wildcard collections, required for
combining collections in a database . Regex pattern to use for creating the wildcard ( * )
collection or for combining mulitple collections in a database. To use regex patterns for wildcard (``*``) collection names , you
must do the following: Specify wildcard ( * ) as the value for databases.[n].collections.[n].name . Omit databases.[n].collections.[n].dataSources.[n].collection . If you specify this field for generating wildcard collections, the
federated database instance instance only contains collections with names that match the
specified regular expression. The collections in the federated database instance storage
configuration use their original names in the Atlas cluster. To use regex patterns for combining multiple collections in a
database , you must do the following: Specify a name that isn't the wildcard ( * ) as the value for databases.[n].collections.[n].name . Omit databases.[n].collections.[n].dataSources.[n].collection . If you specify this field for combining multiple collections, the
collection in the federated database instance instance contains data from all the Atlas collections with names that match the specified regular
expression. The collection in the federated database instance storage configuration uses
the name that you specify as value for databases.[n].collections.[n].name . To learn more about the regex syntax, see Go programming language . databases.[n].collections.[n].dataSources.[n].provenanceFieldName Name for the field that includes the provenance of the documents in
the results. If you specify this setting in the storage
configuration, Atlas Data Federation returns the following fields for each document
in the result: Field Name Description provider Provider ( stores.[n].provider ) in the
federated database instance storage configuration clusterName Name of the Atlas cluster
( stores.[n].clusterName ) databaseName Name of the database
( databases.[n].collections.[n].dataSources.[n].database )
in the Atlas cluster collectionName Name of the collection
( databases.[n].collections.[n].name ) You can't configure this setting using the Visual Editor in the Atlas UI. databases.[n].views Array of objects where each object represents an aggregation pipeline on
a collection. To learn more about views, see Views . databases.[n].views.[n].name Name of the view. databases.[n].views.[n].source Name of the source collection for the view. If you want to create a
view with a $sql stage, you must omit this field
as the SQL statement will specify the source collection. databases.[n].views.[n].pipeline Aggregation pipeline stage(s) to apply to the source collection. You
can also create views using the $sql stage. Tip See also: Configure Atlas Data Federation Tutorial: Federated Queries and $out to S3 Back Deploy Next Deploy
