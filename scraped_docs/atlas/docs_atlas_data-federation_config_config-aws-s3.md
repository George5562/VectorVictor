# AWS S3 Bucket - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores AWS S3 Bucket On this page Example Configuration for S3 Data Store Configuration Format stores databases Atlas Data Federation supports S3 buckets as federated database instance stores. You must define
mappings in your federated database instance to your S3 bucket to run queries against
your data. Example Configuration for S3 Data Store Example Consider a S3 bucket datacenter-alpha containing data
collected from a datacenter: |--metrics |--hardware The /metrics/hardware path stores JSON files with metrics
derived from the datacenter hardware, where each filename is
the UNIX timestamp in milliseconds of the 24 hour period
covered by that file: /hardware/1564671291998.json The following configuration: Defines a federated database instance store on the datacenter-alpha S3 bucket in
the us-east-1 AWS region. The federated database instance store is specifically
restricted to only datafiles in the metrics folder path. Maps files from the hardware folder to a MongoDB database datacenter-alpha-metrics and collection hardware . The
configuration mapping includes parsing logic for capturing the
timestamp implied in the filename. { "stores" : [ { "name" : "datacenter-alpha" , "provider" : "s3" , "region" : "us-east-1" , "bucket" : "datacenter-alpha" , "additionalStorageClasses" : [ "STANDARD_IA" ] , "prefix" : "/metrics" , "delimiter" : "/" } ] , "databases" : [ { "name" : "datacenter-alpha-metrics" , "collections" : [ { "name" : "hardware" , "dataSources" : [ { "storeName" : "datacenter-alpha" , "path" : "/hardware/{date date}" } ] } ] } ] } Atlas Data Federation parses the S3 bucket datacenter-alpha and processes all
files under /metrics/hardware/ . The collections uses the path parsing syntax to map the filename to
the date field, which is an ISO-8601 date, in each document. If
a matching date field does not exist in a document, it will be
added. Users connected to the federated database instance can use the MongoDB Query Language
and supported aggregations to analyze data in the S3 bucket
through the datacenter-alpha-metrics.hardware collection. Tip See also: Querying Data on S3 Configuration Format The federated database instance configuration has the following format: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "region" : "<string>" , 7 "bucket" : "<string>" , 8 "additionalStorageClasses" : [ "<string>" ] , 9 "prefix" : "<string>" , 10 "includeTags" : <boolean> , 11 "delimiter" : "<string>" , 12 "public" : <boolean> 13 } 14 ] , 15 "databases" : [ 16 { 17 "name" : "<string>" , 18 "collections" : [ 19 { 20 "name" : "<string>" , 21 "dataSources" : [ 22 { 23 "storeName" : "<string>" , 24 "path" : "<string>" , 25 "defaultFormat" : "<string>" , 26 "provenanceFieldName" : "<string>" , 27 "omitAttributes" : true | false 28 } 29 ] 30 } 31 ] , 32 "maxWildcardCollections" : <integer> , 33 "views" : [ 34 { 35 "name" : "<string>" , 36 "source" : "<string>" , 37 "pipeline" : "<string>" 38 } 39 ] 40 } 41 ] 42 } stores The stores object defines each data store associated with the
federated database instance. The federated database instance store captures files in an S3 bucket,
documents in Atlas cluster, or files stored at publicly
accessible URL s. Data Federation can only access data stores defined in the stores object. databases The databases object defines the mapping between each
federated database instance store defined in stores and MongoDB collections
in the databases. stores 1 "stores" : [ 2 { 3 "name" : "<string>" , 4 "provider" : "<string>" , 5 "region" : "<string>" , 6 "bucket" : "<string>" , 7 "additionalStorageClasses" : [ "<string>" ] , 8 "prefix" : "<string>" , 9 "delimiter" : "<string>" , 10 "includeTags" : <boolean> , 11 "public" : <boolean> 12 } 13 ] stores Array of objects where each object represents a data store to
associate with the federated database instance. The federated database instance store captures files in an S3 bucket, documents in Atlas cluster, or files stored at
publicly accessible URL s. Atlas Data Federation can only access data stores
defined in the stores object. stores.[n].name Name of the federated database instance store. The databases.[n].collections.[n].dataSources.[n].storeName field references this value as part of mapping configuration. stores.[n].provider Defines where the data is stored. Value must be s3 for an AWS S3 bucket. stores.[n].region Name of the AWS region in which the S3 bucket is hosted. For a
list of valid region names, see Amazon Web Services (AWS) . stores.[n].bucket Name of the AWS S3 bucket. Must exactly match the name of an S3 bucket which Atlas Data Federation can access with the configured AWS IAM
credentials. stores.[n].additionalStorageClasses Optional. Array of AWS S3 storage classes . Atlas Data Federation will
include the files in these storage classes in the query results.
Valid values are: INTELLIGENT_TIERING to include files in the Intelligent
Tiering storage class STANDARD_IA to include files in the Standard-Infrequent
Access storage class Note Files in the Standard storage class are supported by default. stores.[n].prefix Optional. Prefix Atlas Data Federation applies when searching for files in the S3 bucket. For example, consider an S3 bucket metrics with the following
structure: metrics |--hardware |--software |--computed The federated database instance store prepends the value of prefix to the databases.[n].collections.[n].dataSources.[n].path to create the full path for files to ingest. Setting the prefix to /software restricts any databases objects
using the federated database instance store to only subpaths /software . If omitted, Atlas Data Federation searches all files from the root of the S3 bucket. stores.[n].delimiter Optional. The delimiter that separates databases.[n].collections.[n].dataSources.[n].path segments in the federated database instance store. Data Federation uses the delimiter to
efficiently traverse S3 buckets with a hierarchical directory
structure. You can specify any character supported by the S3 object keys as the delimiter. For example, you can specify an underscore ( _ )
or a plus sign ( + ) or multiple characters such as double
underscores ( __ ) as the delimiter. If omitted, defaults to "/" . stores.[n].includeTags Optional. Determines whether or not to use S3 tags on the files
in the given path as additional partition attributes. Valid values
are true and false . If omitted, defaults to false . If set to true , Atlas Data Federation does the following: Adds the S3 tags as additional partition attributes. Adds new top level BSON elements that associate each tag to each
document for the tagged files. Warning If set to true , Atlas Data Federation processes the files for additional
partition attributes by making extra calls to S3 to get the
tags. This behavior might impact performance. stores.[n].public Optional. Specifies whether the bucket is public. If set to true , Atlas Data Federation doesn't use the configured AWS IAM role to access the S3 bucket. If set to false , the configured AWS IAM must include permissions to access the S3 bucket, even
if that bucket is public. If omitted, defaults to false . databases 1 "databases" : [ 2 { 3 "name" : "<string>" , 4 "collections" : [ 5 { 6 "name" : "<string>" , 7 "dataSources" : [ 8 { 9 "storeName" : "<string>" , 10 "defaultFormat" : "<string>" , 11 "path" : "<string>" , 12 "provenanceFieldName" : "<string>" , 13 "omitAttributes" : <boolean> 14 } 15 ] 16 } 17 ] , 18 "maxWildcardCollections" : <integer> , 19 "views" : [ 20 { 21 "name" : "<string>" , 22 "source" : "<string>" , 23 "pipeline" : "<string>" 24 } 25 ] 26 } 27 ] databases Array of objects where each object represents a database, its
collections, and, optionally, any views on
the collections. Each database can have multiple collections and views objects. databases.[n].name Name of the database to which Atlas Data Federation maps the data contained in the
data store. databases.[n].collections Array of objects where each object represents a collection and data
sources that map to a stores federated database instance store. databases.[n].collections.[n].name Name of the collection to which Atlas Data Federation maps the data contained in
each databases.[n].collections.[n].dataSources.[n].storeName .
Each object in the array represents the mapping between the
collection and an object in the stores array. You can generate collection names dynamically from file paths by
specifying * for the collection name and the collectionName() function in the path field. See Generate Dynamic Collection Names from File Path for
examples. databases.[n].collections.[n].dataSources Array of objects where each object represents a stores federated database instance store to map with the
collection. databases.[n].collections.[n].dataSources.[n].storeName Name of a federated database instance store to map to the <collection> .
Must match the name of an object in
the stores array. databases.[n].collections.[n].dataSources.[n].path Controls how Atlas Data Federation searches for and parses files in the storeName before mapping them to the <collection> . federated database instance prepends the stores.[n].prefix to the path to build the
full path to search within. Specify / to capture all files and
folders from the prefix path. For example, consider an S3 bucket metrics with the following
structure: metrics |--hardware |--software |--computed A path of / directs Atlas Data Federation to search all files and folders
in the metrics bucket. A path of /hardware directs Atlas Data Federation to search only that path
for files to ingest. If the prefix is software , Atlas Data Federation
searches for files only in the path /software/computed . Appending the * wildcard character to the path directs Atlas Data Federation
to include all files and folders from that point in the path. For
example, /software/computed* would match files like /software/computed-detailed , /software/computedArchive , and /software/computed/errors . path supports additional syntax for parsing filenames, including: Generating document fields from filenames. Using regular expressions to control field generation. Setting boundaries for bucketing filenames by timestamp. See Define Path for S3 Data for more information. When specifying the path : Specify the data type for the partition attribute. Ensure that the partition attribute type matches the data type to parse. Use the delimiter specified in delimiter . When specifying attributes of the same type, do any of the following: Add a constant separator between the attributes. Use regular expressions to describe the search pattern. To learn more,
see Unsupported Parsing Functions . databases.[n].collections.[n].dataSources.[n].defaultFormat Optional. Default format that Data Federation assumes
if it encounters a file without an extension while searching the databases.[n].collections.[n].dataSources.[n].storeName . The following values are valid for the defaultFormat field: .json , .json.gz , .bson , .bson.gz , .avro, .avro.gz , .orc , .tsv , .tsv.gz , .csv , .csv.gz , .parquet Note If your file format is CSV or TSV , you must include a header
row in your data. See CSV and TSV for more
information. If omitted, Data Federation attempts to detect the file type by
processing a few bytes of the file. Tip See also: Supported Data Formats databases.[n].collections.[n].dataSources.[n].provenanceFieldName Name for the field that includes the provenance of the documents in
the results. If you specify this setting in the storage
configuration, Atlas Data Federation returns the following fields for each document
in the result: Field Name Description provider Provider ( stores.[n].provider ) in the
federated database instance storage configuration region AWS region ( stores.[n].region ) bucket Name of the AWS S3 bucket ( stores.[n].bucket ) key Path
( databases.[n].collections.[n].dataSources.[n].path )
to the document lastModified Date and time the document was last modified. You can't configure this setting using the Visual Editor in the Atlas UI. databases.[n].collections.[n].dataSources.[n].omitAttributes Optional. Flag that specifies whether to omit the attributes (key and value
pairs) that Atlas Data Federation adds to documents in the collection. You can specify one of the
following values: false - to add the attributes true - to omit the attributes If omitted, defaults to false and Atlas Data Federation adds the attributes. Example Consider a file named /employees/949-555-0195.json for which
you configure the path /employees/{phone string} . Atlas Data Federation adds the attribute phone:
949-555-0195 to documents in this file if omitAttributes is false , regardless of whether the key-value pair already exists in the document. If you set omitAttributes to true , Atlas Data Federation
doesn't add the attribute to the document in the virtual collection. databases.[n].maxWildcardCollections Optional. Maximum number of wildcard * collections in the database.
Each wildcard collection can have only one data source. Value can be between 1 and 1000 , inclusive. If omitted, defaults to 100 . databases.[n].views Array of objects where each object represents an aggregation pipeline on
a collection. To learn more about views, see Views . databases.[n].views.[n].name Name of the view. databases.[n].views.[n].source Name of the source collection for the view. If you want to create a
view with a $sql stage, you must omit this field
as the SQL statement will specify the source collection. databases.[n].views.[n].pipeline Aggregation pipeline stage(s) to apply to the source collection. You
can also create views using the $sql stage. Tip See also: Tutorial: Federated Queries and $out to S3 Back Define Data Stores Next Deploy
