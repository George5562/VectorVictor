# Azure Blob Storage - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores Azure Blob Storage On this page Example Configuration for Azure Blob Storage Data Store Configuration Format stores databases Atlas Data Federation supports Azure Blob Storage containers as federated database instance stores. You
must define mappings in your federated database instance to your Azure Blob Storage containers to run queries
against your data. Note While we refer to blobs as files and delimiter-separated prefixes as
directories in this page, these blob storage services are not actually
file systems and don't have the same behaviors in all cases as files
on a hard drive. Example Configuration for Azure Blob Storage Data Store Example Consider Azure Blob Storage container datacenter-alpha containing data
collected from a datacenter: |--metrics |--hardware The /metrics/hardware path stores JSON files with metrics
derived from the datacenter hardware, where each filename is
the UNIX timestamp in milliseconds of the 24 hour period
covered by that file: /hardware/1564671291998.json The following configuration: Defines a federated database instance store on the datacenter-alpha Azure Blob Storage
container in the eastus2 Azure region. The federated database instance store is
specifically restricted to include only data files in the metrics directory path. Maps files from the hardware directory to a MongoDB database datacenter-alpha-metrics and collection hardware . The
configuration mapping includes parsing logic for capturing the
timestamp implied in the filename. { "stores" : [ { "name" : "datacenter" , "provider" : "azure" , "region" : "eastus2" , "containerName" : "datacenter-alpha" , "serviceURL" : "https://mystorageaccount.blob.core.windows.net/" } ] , "databases" : [ { "name" : "datacenter-alpha-metrics" , "collections" : [ { "name" : "hardware" , "dataSources" : [ { "storeName" : "datacenter" , "path" : "/hardware/{date date}" } ] } ] } ] } Atlas Data Federation parses the Azure Blob Storage container datacenter-alpha and
processes all files under /metrics/hardware/ . The collections uses the path parsing syntax to map the
filename to the date field, which is an ISO-8601 date, in each
document. If a matching date field does not exist in a document,
Atlas Data Federation adds it. Users connected to the federated database instance can use the MongoDB Query Language
and supported aggregations to analyze data in the Azure Blob Storage container
through the datacenter-alpha-metrics.hardware collection. Configuration Format The federated database instance configuration has the following format: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "region" : "<string>" , 7 "serviceURL" : "<string>" , 8 "containerName" : "<string>" , 9 "delimiter" : "<string>" , 10 "prefix" : "<string>" , 11 "public" : <boolean> 12 } 13 ] , 14 "databases" : [ 15 { 16 "name" : "<string>" , 17 "collections" : [ 18 { 19 "name" : "<string>" , 20 "dataSources" : [ 21 { 22 "storeName" : "<string>" , 23 "path" : "<string>" , 24 "defaultFormat" : "<string>" , 25 "provenanceFieldName" : "<string>" , 26 "omitAttributes" : <boolean> 27 } 28 ] 29 } 30 ] , 31 "maxWildcardCollections" : <integer> , 32 "views" : [ 33 { 34 "name" : "<string>" , 35 "source" : "<string>" , 36 "pipeline" : "<string>" 37 } 38 ] 39 } 40 ] 41 } 42 stores The stores object defines each data store associated with the
federated database instance. The federated database instance store captures files in an AWS S3 bucket or
Azure Blob Storage container, documents in an Atlas cluster, or files
stored at publicly accessible URL s. Data Federation can only access data
stores defined in the stores object. databases The databases object defines the mapping between each
federated database instance store defined in stores and MongoDB collections
in the databases. stores 1 "stores" : [ 2 { 3 "name" : "<string>" , 4 "provider" : "<string>" , 5 "region" : "<string>" , 6 "serviceURL" : "<string>" , 7 "containerName" : "<string>" , 8 "delimiter" : "<string" , 9 "prefix" : "<string>" , 10 "public" : <boolean> 11 } 12 ] stores Array of objects where each object represents a data store to
associate with the federated database instance. The federated database instance store captures: Files in an Azure Blob Storage container Documents in an Atlas cluster Files stored at publicly accessible URL s. Atlas Data Federation can only access data stores
defined in the stores object. stores.[n].name Name of the federated database instance store. The databases.[n].collections.[n].dataSources.[n].storeName field references this value as part of mapping configuration. stores.[n].provider Defines where the data is stored. Value must be azure for an
Azure Blob Storage container. stores.[n].region Name of the Azure region in which the data is stored. stores.[n].serviceURL URL of the Azure Blob Storage account that contains your blob containers. The serviceURL must be in the following format: https://<storage-account-name>.blob.core.windows.net/ where storage-account-name is the name of your Azure Blob Storage account. stores.[n].containerName Name of the Azure Blob Storage container that contains the files. stores.[n].prefix Optional. Prefix Atlas Data Federation applies when searching for files in the
Azure Blob Storage. For example, consider an an Azure Blob Storage container metrics with
the following structure: metrics |--hardware |--software |--computed The federated database instance store prepends the value of prefix to the databases.[n].collections.[n].dataSources.[n].path to create the full path for files to ingest. Setting the prefix to /software restricts any databases objects
using the federated database instance store to only subpaths /software . If omitted, Atlas Data Federation searches all files from the root of the
Azure Blob Storage container. stores.[n].delimiter Optional. The delimiter that separates databases.[n].collections.[n].dataSources.[n].path segments in the federated database instance store. Data Federation uses the delimiter to
efficiently traverse Azure Blob Storage containers with a hierarchical
directory structure. If omitted, defaults to "/" . stores.[n].public Optional. Specifies whether the Azure Blob Storage container is public. If set to true , Atlas Data Federation doesn't use the configured Azure Service Principal to access your Azure Blob Storage. If set to false , the
configured Service Principal must include permissions to access the
blob container, even if that blob container is public. If omitted, defaults to false . databases 1 "databases" : [ 2 { 3 "name" : "<string>" , 4 "collections" : [ 5 { 6 "name" : "<string>" , 7 "dataSources" : [ 8 { 9 "storeName" : "<string>" , 10 "defaultFormat" : "<string>" , 11 "path" : "<string>" , 12 "provenanceFieldName" : "<string>" , 13 "omitAttributes" : <boolean> 14 } 15 ] 16 } 17 ] , 18 "maxWildcardCollections" : <integer> , 19 "views" : [ 20 { 21 "name" : "<string>" , 22 "source" : "<string>" , 23 "pipeline" : "<string>" 24 } 25 ] 26 } 27 ] databases Array of objects where each object represents a database, its
collections, and, optionally, any views on
the collections. Each database can have multiple collections and views objects. databases.[n].name Name of the database to which Atlas Data Federation maps the data contained in the
data store. databases.[n].collections Array of objects where each object represents a collection and data
sources that map to a stores federated database instance store. databases.[n].collections.[n].name Name of the collection to which Atlas Data Federation maps the data contained in
each databases.[n].collections.[n].dataSources.[n].storeName .
Each object in the array represents the mapping between the
collection and an object in the stores array. You can generate collection names dynamically from file paths by
specifying * for the collection name and the collectionName() function in the path field. databases.[n].collections.[n].dataSources Array of objects where each object represents a stores federated database instance store to map with the
collection. databases.[n].collections.[n].dataSources.[n].storeName Name of a federated database instance store to map to the <collection> .
Must match the name of an object in
the stores array. databases.[n].collections.[n].dataSources.[n].path Controls how Atlas Data Federation searches for and parses files in the storeName before mapping them to the <collection> . Atlas Data Federation prepends the stores.[n].prefix to the path to build the
full path to search within. Specify / to capture all files and
directories from the prefix path. For example, consider an Azure Blob Storage container metrics with the
following structure: metrics |--hardware |--software |--computed A path of / directs Atlas Data Federation to search all files and directories
in the metrics bucket. A path of /hardware directs Atlas Data Federation to search only that path
for files to ingest. If the prefix is software , Atlas Data Federation
searches for files only in the path /software/computed . Appending the * wildcard character to the path directs Atlas Data Federation
to include all files and directories from that point in the path. For
example, /software/computed* would match files like /software/computed-detailed , /software/computedArchive , and /software/computed/errors . path supports additional syntax for parsing filenames, including: Generating document fields from filenames. Using regular expressions to control field generation. Setting boundaries for bucketing filenames by timestamp. See Define Path for S3 Data for more information. When specifying the path : Specify the data type for the partition attribute. Ensure that the partition attribute type matches the data type to parse. Use the delimiter specified in delimiter . When specifying attributes of the same type, do any of the following: Add a constant separator between the attributes. Use regular expressions to describe the search pattern. To learn more,
see Unsupported Parsing Functions . databases.[n].collections.[n].dataSources.[n].defaultFormat Optional. Default format that Data Federation assumes
if it encounters a file without an extension while searching the databases.[n].collections.[n].dataSources.[n].storeName . The following values are valid for the defaultFormat field: .json , .json.gz , .bson , .bson.gz , .avro, .avro.gz , .orc , .tsv , .tsv.gz , .csv , .csv.gz , .parquet Note If your file format is CSV or TSV , you must include a header
row in your data. See CSV and TSV for more
information. If omitted, Data Federation attempts to detect the file type by
processing a few bytes of the file. Tip See also: Supported Data Formats databases.[n].collections.[n].dataSources.[n].provenanceFieldName Name for the field that includes the provenance of the documents in
the results. If you specify this setting in the storage
configuration, Atlas Data Federation returns the following fields for each document
in the result: Field Name Description provider Provider ( stores.[n].provider ) in the
federated database instance storage configuration. region Azure region ( stores.[n].region ). serviceURL URL of the Azure Blob Storage account that contains your blob
containers ( stores.[n].serviceURL ). containerName Name of the Azure Blob Storage container ( stores.[n].containerName ) key Path
( databases.[n].collections.[n].dataSources.[n].path )
to the file. You can't configure this setting using the Visual Editor in the Atlas UI. databases.[n].collections.[n].dataSources.[n].omitAttributes Optional. Flag that specifies whether to omit the attributes (key and value
pairs) that Atlas Data Federation adds to the collection. You can specify one of the
following values: false - to add the attributes true - to omit the attributes If omitted, defaults to false and Atlas Data Federation adds the attributes. Example Consider a file named /employees/949-555-0195.json for which
you configure the path /employees/{phone string} . Atlas Data Federation adds the attribute phone:
949-555-0195 to the document if you set omitAttributes to false . If you set omitAttributes to true , Atlas Data Federation
doesn't add the attribute to the document in the virtual collection. databases.[n].maxWildcardCollections Optional. Maximum number of wildcard * collections in the database.
Each wildcard collection can have only one data source. Value can be between 1 and 1000 , inclusive. If omitted, defaults to 100 . databases.[n].views Array of objects where each object represents an aggregation pipeline on
a collection. To learn more about views, see Views . databases.[n].views.[n].name Label that identifies the view. databases.[n].views.[n].source Name of the source collection for the view. If you want to create a
view with a $sql stage, you must omit this field
as the SQL statement will specify the source collection. databases.[n].views.[n].pipeline Aggregation pipeline stage(s) to apply to the source collection. You
can also create views using the $sql stage. Tip See also: Tutorial: Federated Queries and $out to S3 Back Limitations Next Deploy
