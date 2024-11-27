# HTTP URL - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores HTTP URL On this page Example Configuration for HTTP Data Store Configuration Format stores databases Atlas Data Federation supports publicly accessible URL s as federated database instance stores. You
must define mappings in your federated database instance to your HTTP data stores to run
queries against your data. Important Information in your storage configuration is visible internally at
MongoDB and stored as operational data to monitor and improve the
performance of Atlas Data Federation. So, we recommend that you do not use PII in your
configurations. Example Configuration for HTTP Data Store Consider URL s https://www.datacenter-hardware.com/data.json , https://www.datacenter-software.com/data.json , and https://www.datacenter-metrics.com/data.json containing data
collected from a datacenter. The following configuration: Specifies the publicly accessible URLs that contain data in files as
a federated database instance store. Creates a partition for each URL . { "stores" : [ { "name" : "httpStore" , "provider" : "http" , "allowInsecure" : false , "urls" : [ "https://www.datacenter-hardware.com/data.json" , "https://www.datacenter-software.com/data.json" ] , "defaultFormat" : ".json" } ] , "databases" : [ { "name" : "dataCenter" , "collections" : [ { "name" : "inventory" , "dataSources" : [ { "storeName" : "httpStore" , "allowInsecure" : false , "urls" : [ "https://www.datacenter-metrics.com/data" ] , "defaultFormat" : ".json" } ] } ] } ] } Tip See also: Querying Data at a HTTP or HTTPS URL Configuration Format The federated database instance configuration has the following format: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "defaultFormat" : "<string>" , 7 "allowInsecure" : <boolean> , 8 "urls" : [ "<string>" ] 9 } 10 ] , 11 "databases" : [ 12 { 13 "name" : "<string>" , 14 "collections" : [ 15 { 16 "name" : "<string>" , 17 "dataSources" : [ 18 { 19 "storeName" : "<string>" , 20 "allowInsecure" : <boolean> , 21 "urls" : [ "<string>" ] , 22 "defaultFormat" : "<string>" , 23 "provenanceFieldName" : "<string>" 24 } 25 ] 26 } 27 ] , 28 "views" : [ 29 { 30 "name" : "<string>" , 31 "source" : "<string>" , 32 "pipeline" : "<string>" 33 } 34 ] 35 } 36 ] 37 } stores The stores object defines each data store associated with the
federated database instance. The federated database instance store captures files stored at publicly
accessible URL s. Data Federation can only access data stores defined in
the stores object. databases The databases object defines the mapping between each
federated database instance store defined in stores and MongoDB collections
in the databases. stores 1 "stores" : [ 2 { 3 "name" : "<string>" , 4 "provider" : "<string>" , 5 "allowInsecure" : <boolean> , 6 "urls" : [ "<string>" ] , 7 "defaultFormat" : "<string>" 8 } 9 ] stores Array of objects where each object represents a data store to
associate with the federated database instance. The federated database instance store captures files in an S3 bucket, documents in Atlas cluster, or files stored at
publicly accessible URL s. Atlas Data Federation can only access data stores
defined in the stores object. stores.[n].name Name of the federated database instance store. The databases.[n].collections.[n].dataSources.[n].storeName field references this value as part of mapping configuration. stores.[n].provider Defines where the data is stored. Value can be one of the following: s3 for an AWS S3 bucket. atlas for a collection in an Atlas cluster. http for data in files hosted at publicly accessible URL s. stores.[n].allowInsecure Optional. Validates the scheme in the specified URL s. Value can be one
of the following: true to allow insecure HTTP scheme false to only allow secure HTTPS scheme (default) If true, Atlas Data Federation: Does not verify the server's certificate chain and hostname. Accepts any certificate with any hostname presented by the server. WARNING: If you set this to true , your data might become vulnerable to a
man-in-the-middle attack, which can compromise the confidentiality
and integrity of your data. Set this to true only for testing
and getting started with Atlas Data Federation. If omitted, defaults to false . If set to false , Data Federation returns an
error similar to the following if a specified URL contains insecure HTTP scheme: The insecure HTTP scheme is not supported by default - please add a "allowInsecure: true" flag to query from such URLs. stores.[n].urls Optional. Comma-separated list of publicly accessible HTTP URL s where data is stored. You can't specify URL s that require
authentication. stores.[n].defaultFormat Optional. Default format that Data Federation assumes
if it encounters a file without an extension while searching the databases.[n].collections.[n].dataSources.[n].storeName . The following values are valid for the defaultFormat field: .json , .json.gz , .bson , .bson.gz , .avro, .avro.gz , .orc , .tsv , .tsv.gz , .csv , .csv.gz , .parquet Note If your file format is CSV or TSV , you must include a header
row in your data. See CSV and TSV for more
information. If omitted, Data Federation attempts to detect the file type by
processing a few bytes of the file. The specified format only applies to the URL s specified in the stores object. Tip See also: Supported Data Formats databases 1 "databases" : [ 2 { 3 "name" : "<string>" , 4 "collections" : [ 5 { 6 "name" : "<string>" , 7 "dataSources" : [ 8 { 9 "storeName" : "<string>" , 10 "allowInsecure" : <boolean> , 11 "urls" : [ "<string>" ] , 12 "defaultFormat" : "<string>" , 13 "provenanceFieldName" : "<string>" 14 } 15 ] 16 } 17 ] 18 } 19 ] databases Array of objects where each object represents a database, its
collections, and, optionally, any views on
the collections. Each database can have multiple collections and views objects. databases.[n].name Name of the database to which Atlas Data Federation maps the data contained in the
data store. databases.[n].collections Array of objects where each object represents a collection and data
sources that map to a stores federated database instance store.
For dynamically generated databases, you can define only one
wildcard ( * ) collection object in the storage configuration. databases.[n].collections.[n].name Name of the collection to which Atlas Data Federation maps the data contained in
each databases.[n].collections.[n].dataSources.[n].storeName .
Each object in the array represents the mapping between the
collection and an object in the stores array. Note You can't generate wildcard * collections. databases.[n].collections.[n].dataSources Array of objects where each object represents a stores federated database instance store to map with the
collection. databases.[n].collections.[n].dataSources.[n].storeName Name of a federated database instance store to map to the <collection> .
Must match the name of an object in
the stores array. databases.[n].collections.[n].dataSources.[n].allowInsecure Optional. Validates the scheme in the specified URL s. Value can be one
of the following: true to allow insecure HTTP scheme false to only allow secure HTTPS scheme (default) If true, Atlas Data Federation: Does not verify the server's certificate chain and hostname. Accepts any certificate with any hostname presented by the server. WARNING: If you set this to true , your data might become vulnerable to a
man-in-the-middle attack, which can compromise the confidentiality
and integrity of your data. Set this to true only for testing
and getting started with Atlas Data Federation. If omitted, defaults to false . If set to false , Data Federation returns an
error similar to the following if a specified URL contains insecure HTTP scheme: The insecure HTTP scheme is not supported by default - please add a "allowInsecure: true" flag to query from such URLs. databases.[n].collections.[n].dataSources.[n].urls Optional . Comma-separated list of publicly accessible URL s
where the data is stored. Federated Database Instance creates a partition for each URL . You can specify URL s that are not in the urls ; however, the collection will
contain a union of data from URL s in both the urls and urls .
If omitted, Data Federation uses the urls in
the specified storeName . databases.[n].collections.[n].dataSources.[n].defaultFormat Optional. Default format that Data Federation assumes
if it encounters a file without an extension while searching the databases.[n].collections.[n].dataSources.[n].storeName . The following values are valid for the defaultFormat field: .json , .json.gz , .bson , .bson.gz , .avro, .avro.gz , .orc , .tsv , .tsv.gz , .csv , .csv.gz , .parquet Note If your file format is CSV or TSV , you must include a header
row in your data. See CSV and TSV for more
information. If omitted, Data Federation attempts to detect the file type by
processing a few bytes of the file. The specified format only applies to the URL s specified in the databases.[n].collections.[n].dataSources object. Tip See also: Supported Data Formats databases.[n].collections.[n].dataSources.[n].provenanceFieldName Name for the field that includes the provenance of the documents in
the results. If you specify this setting in the storage
configuration, Atlas Data Federation returns the following fields for each document
in the result: Field Name Description provider Provider ( stores.[n].provider ) in the
federated database instance storage configuration uri HTTP or HTTPS URL ( databases.[n].collections.[n].dataSources.[n].urls )
of the document You can't configure this setting using the Visual Editor in the Atlas UI. databases.[n].views Array of objects where each object represents an aggregation pipeline on
a collection. To learn more about views, see Views . databases.[n].views.[n].name Name of the view. databases.[n].views.[n].source Name of the source collection for the view. If you want to create a
view with a $sql stage, you must omit this field
as the SQL statement will specify the source collection. databases.[n].views.[n].pipeline Aggregation pipeline stage(s) to apply to the source collection. You
can also create views using the $sql stage. Tip See also: Tutorial: Federated Queries and $out to S3 Back Generate Collections Next Deploy
