# Online Archives - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores Online Archives On this page Example Configuration for Atlas Online Archive Data Store Configuration Format stores databases Note You can only use new Online Archives as a data source in Atlas Data Federation. Read the MongoDB blog post New Online Archive with Performance Improvements and Enhanced Metrics for more information. Atlas Data Federation supports Atlas online archives as federated database instance stores. You must define mappings
in your federated database instance storage configuration to your online archive to run
queries against your data. Important Information in your storage configuration is visible internally at
MongoDB and stored as operational data to monitor and improve the
performance of Atlas Data Federation. So, we recommend that you do not use PII in your
configurations. Example Configuration for Atlas Online Archive Data Store Example Consider an Atlas online archive backed by AWS with the
following ID: v1$atlas$archive$V3metrics$hardware$69437250-b9da-4ae9-a1cd-8811462c38a4$64679f7c09f07374b4dcc914 The online archive contains the archived data from the metrics.hardware in an Atlas cluster. The following
configuration: Specifies the Atlas online archive in the us-east-1 AWS region as a federated database instance store. Maps documents from the Atlas online archive to the dataCenter.inventory collection in the storage configuration. { "stores" : [ { "name" : "atlasOnlineArchiveStore" , "provider" : "dls:aws" , "region" : "us-east-1" } ] , "databases" : [ { "name" : "dataCenter" , "collections" : [ { "name" : "inventory" , "dataSources" : [ { "storeName" : "atlasOnlineArchiveStore" , "datasetName" : "v1$atlas$archive$V3metrics$hardware$69437250-b9da-4ae9-a1cd-8811462c38a4$64679f7c09f07374b4dcc914" , "provider" : "dls:aws" } ] } ] } ] } Note Since AWS backs the online archive, the provider is set to dls:aws in the example. If Azure backed the online archive,
the provider would be dls:azure . Atlas Data Federation maps all the documents in the online archive
to the dataCenter.inventory collection in the storage
configuration. Users connected to the federated database instance can use the MongoDB Query Language
and supported aggregations to analyze data in the Atlas cluster
through the dataCenter.inventory collection. Configuration Format The federated database instance configuration for an Atlas online archive has the
following format: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "region" : "<string>" 7 } 8 ] , 9 "databases" : [ 10 { 11 "name" : "<string>" , 12 "collections" : [ 13 { 14 "name" : "<string>" , 15 "dataSources" : [ 16 { 17 "storeName" : "<string>" , 18 "datasetName" : "<string>" , 19 "datasetPrefix" : "<string>" , 20 "trimLevel" : <int> , 21 "provenanceFieldName" : "<string>" , 22 "maxDatasets" : <int> 23 } 24 ] 25 } 26 ] , 27 "views" : [ 28 { 29 "name" : "<string>" , 30 "source" : "<string>" , 31 "pipeline" : "<string>" 32 } 33 ] 34 } 35 ] 36 } 37 stores 1 "stores" : [ 2 { 3 "name" : "<string>" , 4 "provider" : "<string>" , 5 "region" : "<string>" 6 } 7 ] stores Array of objects where each object represents a data store to
associate with the federated database instance. The federated database instance store references files in an S3 bucket, documents in an Atlas cluster, files stored at
publicly accessible URL s, or Atlas online archives. Atlas Data Federation
can only access data stores defined in the stores object. stores.[n].name Name of the federated database instance store. The databases.[n].collections.[n].dataSources.[n].storeName field references this value as part of mapping configuration. stores.[n].provider Cloud provider where the snapshot data is stored. Value must be dls:<subtype> for a snapshot. Atlas Data Federation supports the following
subtypes: aws , for which the value must be dls:aws stores.[n].region Region name of your online archive. Each store is associated with a
single region, where the archived data is stored. If you have
multiple online archives in different regions, you must add a store
for each region to map data in that region to virtual databases and
collection in federated database instance. To learn more about the supported regions for AWS , see Atlas Data Federation Regions . databases 1 "databases" : [ 2 { 3 "name" : "<string>" , 4 "collections" : [ 5 { 6 "name" : "<string>" , 7 "dataSources" : [ 8 { 9 "storeName" : "<string>" , 10 "datasetName" : "<string>" , 11 "datasetPrefix" : "<string>" , 12 "trimLevel" : <int> , 13 "provenanceFieldName" : "<string>" , 14 "maxDatasets" : <int> 15 } 16 ] 17 } 18 ] , 19 "views" : [ 20 { 21 "name" : "<string>" , 22 "source" : "<string>" , 23 "pipeline" : "<string>" 24 } 25 ] 26 } 27 ] databases Array of objects that define the mapping between each federated database instance
store defined in stores and online archives. Each object
represents a database, its collections, and, optionally, any views on the collections. Each database
can have multiple collections and views objects. databases.[n].name Name of the database to which Atlas Data Federation maps the data contained in the
data store. databases.[n].collections Array of objects where each object represents a collection and data
sources that map to a stores federated database instance store. databases.[n].collections.[n].name Name of the collection to which Atlas Data Federation maps the data contained in
each databases.[n].collections.[n].dataSources.[n].storeName .
Each object in the array represents the mapping between the
collection and an object in the stores array. You can generate collection names dynamically by specifying * for the collection name. To dynamically generate collection names,
you must also specify the following: databases.[n].collections.[n].dataSources.[n].datasetPrefix databases.[n].collections.[n].dataSources.[n].trimLevel For wildcard collections, Atlas Data Federation maps a dataset name to a
collection name first by splitting the namespace into a list of fields on the $ delimiter, then by trimming a number of fields from the left of the
list, and finally by combining the remaining fields using _ . databases.[n].collections.[n].dataSources Array of objects where each object represents a federated database instance store in the stores array to map with the collection. You can
specify multiple dataSources for a wildcard collection only if
all the dataSources for the collection map to the online archive stores . databases.[n].collections.[n].dataSources.[n].storeName Name of a federated database instance store to map to the <collection> . Must match
the name of an object in the stores array. databases.[n].collections.[n].dataSources.[n].datasetName Name of the online archive dataset to map with the collection. The datasetName is in the following format: <version>$<type>$<subtype>$<clusterName>$<dbName>$<collectionName>$<archiveId> Example Consider the following online archive name. v1$atlas$archive$clusterName$dbName$collections$archiveId Here: v1 is the version atlas is the type of data source archive is the subtype clusterName is the name of the Atlas cluster dbName is the name of the database on the Atlas cluster collection is the the collections in the database archiveId is the unique identifier of the archived data Note For a non-wildcard collection, you can't specify this option if you
specify the databases.[n].collections.[n].dataSources.[n].datasetPrefix option because Atlas Data Federation automatically generates collections for the
latest dataset using the name specified through databases.[n].collections.[n].dataSources.[n].datasetPrefix option. databases.[n].collections.[n].dataSources.[n].datasetPrefix Required for wildcard collections. Dataset name prefix to match against the online archive dataset name.
When you set this for wildcard collections, Atlas Data Federation maps collections
to only to the online archive dataset names whose prefix match the
value specified here. If you specify this setting for a non-wildcard collection, Atlas Data Federation maps only
the latest dataset (for the most recently captured snapshot) to the
collection. You can't specify the databases.[n].collections.[n].dataSources.[n].datasetName also if you specify this option for a non-wildcard collection. Example { ..., "name": "myFederatedDbCollection", "dataSources": [ { "storeName": "aws-dl-store", "datasetPrefix": "v1$atlas$archive$MyCluster$MyDB$MyArchiveId" } ] } databases.[n].collections.[n].dataSources.[n].trimLevel Unsigned integer that specifies how many fields of the dataset name
to trim from the left of the dataset name before mapping the
remaining fields to a wildcard collection name. Value must be
greater than 0 and less than 7 . You can set this setting for
wildcard collections only. You can't configure this setting using the Visual Editor in the Atlas UI. Therefore, this setting defaults to trim level 5 for configurations using the Visual Editor. databases.[n].collections.[n].dataSources.[n].provenanceFieldName Name for the field that includes the provenance of the documents in
the results. If you specify this setting in the storage
configuration, Atlas Data Federation returns the following fields for each document
in the result: Field Name Description provider Provider ( stores.[n].provider )
in the federated database instance storage configuration clusterName Name of the Atlas cluster databaseName Name of the database on the Atlas cluster collectionName Name of the collection snapshotID Unique 24-hexadecimal character string that identifies the
snapshot dataSetName Name of the online archive dataset ( databases.[n].collections.[n].dataSources.[n].datasetName ) You can't configure this setting using the Visual Editor in the Atlas UI. databases.[n].collections.[n].dataSources.[n].maxDatasets Unsigned integer that specifies the maximum number of datasets from
which to dynamically generate collections for the data source. You must
provide a value greater than 0 . You can set this setting for wildcard
collections only. Atlas Data Federation returns datasets in reverse lexicographical
order. Note You can't configure this setting using the Visual Editor in the Atlas UI. Therefore, Atlas Data Federation configuration doesn't include a
limit on the number of datasets for configurations using the Visual
Editor. Back Deploy Next Create from the UI
