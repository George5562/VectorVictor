# Google Cloud Storage Bucket - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores Google Cloud Storage Bucket On this page Example Configuration for Google Cloud Storage Bucket Configuration Format Atlas Data Federation supports Google Cloud Storage buckets as federated database instance stores. You must
define mappings in your federated database instance to your Cloud Storage bucket to run
queries against your data. Note We refer to objects as files and delimiter-separated prefixes as
directories in this page. However, these object storage services
aren't actually file systems and don't have the same behaviors in
all cases as files on a hard drive. Example Configuration for Google Cloud Storage Bucket Consider a Google Cloud Storage bucket datacenter-alpha containing data
collected from a datacenter: |--metrics |--hardware The /metrics/hardware path stores JSON files with metrics
derived from the datacenter hardware, where each filename is
the UNIX timestamp in milliseconds of the 24 hour period
covered by that file: /hardware/1564671291998.json The following configuration: Defines a federated database instance store on the datacenter-alpha Google Cloud Storage bucket
in the us-central1 Google Cloud region. The federated database instance store is
specifically restricted to include only data files in the metrics directory path. A delimiter of / is defined to
simulate a file system hierarchy for ease of navigation and
retrieval. Maps files from the hardware directory to a MongoDB database datacenter-alpha-metrics and collection hardware . The
configuration mapping includes parsing logic for capturing the
timestamp implied in the filename. { "stores" : [ { "name" : "datacenter-alpha" , "provider" : "gcs" , "region" : "us-central1" , "bucket" : "datacenter-alpha" , "prefix" : "metrics" , "delimiter" : "/" } ] , "databases" : [ { "name" : "datacenter-alpha-metrics" , "collections" : [ { "name" : "hardware" , "dataSources" : [ { "storeName" : "datacenter-alpha" , "path" : "/hardware/{date date}" } ] } ] } ] } Atlas Data Federation parses the Google Cloud Storage bucket datacenter-alpha and processes
all files under /metrics/hardware/ . The collections object
uses the path parsing syntax to map the
filename to the date field, which is an ISO-8601 date, in each
document. If a matching date field does not exist in a document,
Atlas Data Federation adds it. Users connected to the federated database instance can use the MongoDB Query Language and
supported aggregations to analyze data in the Google Cloud Storage bucket through
the datacenter-alpha-metrics.hardware collection. Configuration Format To support Atlas Data Federation on Google Cloud, the federated database instance configuration has the
following prototype form: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "region" : "<string>" , 7 "bucket" : "<string>" , 8 "prefix" : "<string>" , 9 "delimiter" : "<string>" 10 } 11 ] , 12 "databases" : [ 13 { 14 "name" : "<string>" , 15 "collections" : [ 16 { 17 "name" : "<string>" , 18 "dataSources" : [ 19 { 20 "storeName" : "<string>" , 21 "path" : "<string>" , 22 "defaultFormat" : "<string>" , 23 "provenanceFieldName" : "<string>" , 24 "omitAttributes" : <boolean> 25 } 26 ] 27 } 28 ] , 29 "maxWildcardCollections" : <integer> , 30 "views" : [ 31 { 32 "name" : "<string>" , 33 "source" : "<string>" , 34 "pipeline" : "<string>" 35 } 36 ] 37 } 38 ] 39 } 40 Field Type Necessity Description stores array Required Array of objects where each object represents a data store to
associate with the federated database instance. The federated database instance store captures: Files in a Google Cloud Storage bucket Documents in an Atlas cluster Files stored at publicly accessible URL s. Atlas Data Federation can only access data stores
defined in the stores object. stores.[n]. name string Required Name of the federated database instance store. The databases.[n].collections.[n].dataSources.[n].storeName field references this value as part of mapping configuration. stores.[n]. provider string Required Name of the cloud provider where the data is stored. Value must
be gcs for a Google Cloud Storage bucket. stores.[n]. region string Required Name of the Google Cloud region in which the Google Cloud Storage bucket is hosted.
For a list of valid region names, see Google Cloud Platform (GCP) . stores.[n]. bucket string Required Name of the Google Cloud Storage bucket. Must exactly match the name of a Google Cloud Storage
bucket that Atlas Data Federation must access. stores.[n]. prefix string Optional Prefix Atlas Data Federation applies when searching for files in the Google Cloud Storage
bucket. For example, consider a Google Cloud Storage bucket metrics with the
following structure: metrics |--hardware |--software |--computed The federated database instance store prepends the value of prefix to databases.[n].collections.[n].dataSources.[n].path to create the
full path for files to ingest. Setting prefix to /software restricts any databases objects using the federated database instance to only subpaths
of /software . Defaults to the root of the Google Cloud Storage bucket, retrieving all files. stores.[n]. delimiter string Optional Delimiter that separates databases.[n].collections.[n].dataSources.[n].path segments in
the federated database instance store. Atlas Data Federation uses the delimiter to efficiently traverse
Google Cloud Storage buckets with a simulated hierarchical directory structure. databases array Required Array of objects where each object represents a database, its
collections, and, optionally, any views on the collections. Each database can have multiple collections and views objects. databases.[n]. name string Required Name of the database to which Atlas Data Federation maps the
data contained in the data store. databases.[n]. collections array Required Array of objects where each object represents a collection
and data sources that map to a stores federated database
instance store. databases.[n]. collections.[n]. name string Required Name of the collection to which Atlas Data Federation maps
the data contained in each databases.[n].collections.[n].dataSources.[n].storeName .
Each object in the array represents the mapping between
the collection and an object in the stores array. You can generate collection names dynamically from file paths
by specifying * for the collection name and the collectionName() function in the path field. See Generate Dynamic Collection Names from File Path for examples. databases.[n]. collections.[n]. dataSources array Required Array of objects where each object represents a stores federated database instance store to map with the
collection. databases.[n]. collections.[n]. dataSources.[n]. storeName string Required Name of a federated database instance store to map to the <collection> .
Must match the name of an object in the stores array. databases.[n]. collections.[n]. dataSources.[n]. path string Required Controls how Atlas Data Federation searches for and parses files in
the databases.[n].collections.[n].dataSources.[n].storeName before mapping them to the <collection> . federated database instance
prepends the stores.[n].prefix to the path to
build the full path to search within. Specify / to capture all files and folders from the prefix path. For example, consider a Google Cloud Storage bucket named metrics with
the following structure: metrics |--hardware |--software |--computed A path of / directs Atlas Data Federation to search all
files and folders in the metrics bucket. A path of /hardware directs Atlas Data Federation to search
only that path for files to ingest. If the stores.[n].prefix is software , Atlas Data Federation
searches for files only in the path /software/computed . Appending the * wildcard character to the path
directs Atlas Data Federation to include all files and folders from
that point in the path. For example, /software/computed* would match files like /software/computed-detailed , /software/computedArchive , and /software/computed/errors . databases.[n].collections.[n].dataSources.[n].path supports additional syntax for parsing filenames,
including: Generating document fields from filenames. Using regular expressions to control field
generation. Setting boundaries for bucketing filenames by
timestamp. See Define Path for S3 Data for more information. When specifying the path : Specify the data type for the partition attribute. Ensure that the partition attribute type matches the data type to parse. Use the delimiter specified in delimiter . When specifying attributes of the same type, do any of the following: Add a constant separator between the attributes. Use regular expressions to describe the search pattern. To learn more,
see Unsupported Parsing Functions . databases.[n]. collections.[n]. dataSources.[n]. defaultFormat string Optional Default format that Data Federation assumes if it encounters
a file without an extension while searching the databases.[n].collections.[n].dataSources.[n].storeName . The following values are valid for the defaultFormat field: .json , .json.gz , .bson , .bson.gz , .avro, .avro.gz , .orc , .tsv , .tsv.gz , .csv , .csv.gz , .parquet Note If your file format is CSV or TSV , you
must include a header row in your data. See CSV and TSV for more information. If omitted, Data Federation attempts to detect the file type by
processing a few bytes of the file. Tip See also: Supported Data Formats databases.[n]. collections.[n]. dataSources.[n]. provenanceFieldName string Optional Name for the field that includes the provenance of the
documents in the results. If you specify this setting in the
storage configuration, Atlas Data Federation returns the following fields for
each document in the result: Field Name Description provider Provider ( stores.[n].provider ) in the
federated database instance storage configuration region Google Cloud region ( stores.[n].region ) bucket Name of the Google Cloud Storage bucket ( stores.[n].bucket ) key Path
( databases.[n].collections.[n].dataSources.[n].path )
to the document lastModified Date and time the document was last modified. You can't configure this setting using the Visual Editor in the Atlas UI. databases.[n]. collections.[n]. dataSources.[n]. omitAttributes boolean Optional Flag that specifies whether to omit the attributes
(key and value pairs) that Atlas Data Federation adds to documents
in the collection. You can specify one of the
following values: false - to add the attributes true - to omit the attributes If omitted, defaults to false and Atlas Data Federation adds
the attributes. For example, consider a file named /employees/949-555-0195.json for which you
configure the databases.[n].collections.[n].dataSources.[n].path /employees/{phone string} . Atlas Data Federation adds the
attribute phone: 949-555-0195 to documents in
this file if omitAttributes is false ,
regardless of whether the key-value pair already
exists in the document. If you set omitAttributes to true , Atlas Data Federation doesn't add the attribute to
the document in the virtual collection. Back Deploy Next Deploy
