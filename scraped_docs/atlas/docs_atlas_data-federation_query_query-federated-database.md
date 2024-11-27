# Query a Federated Database Instance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data Query a Federated Database Instance On this page Querying Data on S3 Querying Data on Azure Blob Storage Querying Data on Google Cloud Storage Querying Data in Your Atlas Cluster Querying Data in Your Online Archives Querying Data at a HTTP or HTTPS URL Running Federated Queries Configuring Query Limits Troubleshooting You can use the MongoDB Query Language (MQL) on Atlas Data Federation to query and
analyze data on your data store. Atlas Data Federation supports most, but not all
standard server commands. To learn more about the supported and
unsupported MongoDB server commands and aggregation pipleline stages,
see Supported MongoDB Commands . To query data on your data store, your federated database instance storage configuration must
contain settings that define: Your federated database instance store. Federated Database Instance virtual databases and collections that map to your
federated database instance store. You can create or update your federated database instance storage configuration for your data store using the Atlas UI Visual Editor or JSON Editor , Atlas Data Federation CLI commands, and Atlas Data Federation API endpoints. To learn more about federated database instance storage configuration, see Define Data Stores for a Federated Database Instance . Atlas Data Federation creates the virtual databases and collections you specified in
your federated database instance configuration for the data in your data store. When you connect to your federated database instance and run queries , Atlas Data Federation
processes your queries against the data and returns the query results.
You can, optionally, configure limits on the
amount of data that Atlas Data Federation processes for your queries to control costs. Note Atlas Data Federation uses columnar storage that doesn't preserve the order of
fields within documents. Therefore, Atlas Data Federation doesn't support queries
that are field-order sensitive, such as an embedded document
equality query or sorting on a document field. A database user must have one of the following roles to run queries
against a federated database instance: readWriteAnyDatabase readAnyDatabase A custom role with the find privilege for the namespace against which you
want to run queries You can run up to 30 simultaneous queries on your federated database instance against: Data in your S3 bucket or Azure Blob Storage container. Documents in your MongoDB Atlas cluster. Archived data in your Online Archive. Data in files hosted at publicly accessible URL s. Tip See: How to Connect to Your Federated Database Instance How to Run Queries Against Your Data Using Your Federated
Database Instance The following sections contain information pertaining to running
queries against data in your data store. Querying Data on S3 When deploying your federated database instance,
if you specified an S3 bucket with both read and write permissions or AWS S3 s3:PutObject permission, you can also save your query results in your S3 bucket
using $out to S3 . If you successfully create or update an object on your S3 data store,
Data Federation returns the latest version of that object for any subsequent
read requests and all list operations of the objects also reflect the
changes. If your query contains multiple stages, each stage receives
the most recent data available from the data store as that stage is
processed. By default, Atlas Data Federation does not return documents in any specific order
for queries on Data Federations for S3 data stores. Atlas Data Federation reads the
partitions concurrently and the underlying storage response order
determines which documents Atlas Data Federation returns first, unless you define
order using $sort in your query. For example, if you run
the same findOne() query twice, you could see different documents,
and if you use $skip , different documents might be skipped
if $sort is not used in the query. You incur "Data Processed" costs for the amount of data that
Atlas Data Federation processes to return results for your queries in addition to the
"Data Returned" cost for the amount of data that Atlas Data Federation returns. For
example, for a 10 GB file, you incur the following "Data
Processed" cost in addition to the "Data Returned" cost: If you have no partitions, Atlas Data Federation reads the entire file to return
results for the query. Therefore, you incur 10 GB of "Data
Processed" cost. If you have 10 partitions of 1 GB each, Atlas Data Federation targets and reads a
single partition. Therefore, you incur 1 GB of "Data Processed" cost. You can configure query limits per
federated database instance and for all federated database instances in your project to limit the amount of processed data . To learn more,
see Manage Atlas Data Federation Query Limits . Note Data partitioning doesn't guarantee reduced data processing cost.
For example, if you run a blank $match query, which
queries all the data, Atlas Data Federation needs to read the entire collection to
return the results for the query regardless of the number of
partitions. Querying Data on Azure Blob Storage When deploying your federated database instance,
you can specify an Azure Blob Storage container with both read and write
permissions. You incur "Data Processed" costs for the amount of data that
Atlas Data Federation processes to return results for your queries in addition to the
"Data Returned" cost for the amount of data that Atlas Data Federation returns. For
example, for a 10 GB file, you incur the following "Data
Processed" cost in addition to the "Data Returned" cost: If you have no partitions, Atlas Data Federation reads the entire file to return
results for the query. Therefore, you incur 10 GB of "Data
Processed" cost. If you have 10 partitions of 1 GB each, Atlas Data Federation targets and reads a
single partition. Therefore, you incur 1 GB of "Data Processed" cost. You can configure query limits per
federated database instance and for all federated database instances in your project to limit the amount of processed data . To learn more,
see Manage Atlas Data Federation Query Limits . Querying Data on Google Cloud Storage When deploying your federated database instance,
you can specify a Google Cloud Storage bucket with both read and write permissions. You incur "Data Processed" costs for the amount of data that
Atlas Data Federation processes to return results for your queries in addition to the
"Data Returned" cost for the amount of data that Atlas Data Federation returns. For
example, for a 10 GB file, you incur the following "Data
Processed" cost in addition to the "Data Returned" cost: If you have no partitions, Atlas Data Federation reads the entire file to return
results for the query. Therefore, you incur 10 GB of "Data
Processed" cost. If you have 10 partitions of 1 GB each, Atlas Data Federation targets and reads a
single partition. Therefore, you incur 1 GB of "Data Processed" cost. You can configure query limits per
federated database instance and for all federated database instances in your project to limit the amount of processed data . To learn more,
see Manage Atlas Data Federation Query Limits . Querying Data in Your Atlas Cluster When you run queries against your Atlas cluster through your
federated database instance, Atlas Data Federation sets the appName , when querying your cluster,
based on the appName that you used to connect to your federated database instance. For
example, if you connect to your federated database instance with appName set to myApp (i.e. appName = "myApp" ), Atlas Data Federation sets the appName when connecting to your cluster to the following: atlas-data-federation|myApp If you query a collection in Atlas Data Federation that is mapped to only one Atlas collection, Atlas Data Federation acts as a proxy and forwards your query
to Atlas . When acting as a proxy, Atlas Data Federation doesn't scan data into
its virtual collection to process the query thus improving performance
and reducing cost. This optimization is not available for queries on
Atlas Data Federation collections that are mapped to multiple Atlas collections. Example Consider the following federated database instance storage configuration: { "stores" : [ { "name" : "atlas-store" , "provider" : "atlas" , "clusterName" : "myCluster" , "projectId" : "5e2211c17a3e5a48f5497de3" } ] , "databases" : [ { "name" : "atlas-db" , "collections" : [ { "name" : "foo" , "dataSources" : [ { "storeName" : "atlas-store" , "database" : "myFooData" , "collection" : "foo" } ] } , { "name" : "barbaz" , "dataSources" : [ { "storeName" : "atlas-store" , "database" : "myBarData" , "collection" : "bar" } , { "storeName" : "atlas-store" , "database" : "myBazData" , "collection" : "baz" } ] } ] } ] } For the above storage configuration, Atlas Data Federation acts as a proxy for
queries on foo collection and forwards the queries to Atlas .
This performance and cost optimization is not available for queries
on barbaz collection because barbaz is mapped to multiple Atlas collections. You can also save your query results in your Atlas cluster using $out to Atlas . If you successfully create or update a document in your collection on
the Atlas cluster, Data Federation returns the latest version of that
document for any subsequent read requests and all list operations of
the collection also reflect the changes. If your query contains
multiple stages, each stage receives the most recent data available
from the data store as that stage is processed. Atlas logs your queries against your cluster data in the Atlas cluster audit logs. The log entry for a database user is in the
following format: <SERVICE_NAME>-<CUSTOMER_DATA_LAKE_NAME>-<DATABASE_USER_NAME> For example, for a database user configured in Atlas as "user" : "CN=atlasDataLake-DataLake0-test_datalake0" , a log entry in
the Atlas cluster audit log looks similar to the following: { "atype" : "authenticate", "ts" : { "$date" : "2022-04-29T13:17:54.020+00:00" }, "local" : { "ip" : "XXXX", "port" : 27017 }, "remote" : { "ip" : "XXXXX", "port" : 10844 }, "users" : [ { "user" : "CN=atlasDataLake-DataLake0-test_datalake0", "db" : "$external" } ], "roles" : [ { "role" : "backup", "db" : "admin" }, { "role" : "readWriteAnyDatabase", "db" : "admin" }, { "role" : "clusterMonitor", "db" : "admin" }, { "role" : "enableSharding", "db" : "admin" }, { "role" : "atlasAdmin", "db" : "admin" }, { "role" : "dbAdminAnyDatabase", "db" : "admin" } ], "param" : { "user" : "CN=atlasDataLake-DataLake0-test_datalake0", "db" : "$external", "mechanism" : "MONGODB-X509" }, "result" : 0 } Note The connection mechanism is always MONGODB-X509 in the Atlas cluster audit logs. Querying Data in Your Online Archives For queries, Atlas Data Federation uses the partitions that you created on fields
during the creation of the Atlas Online Archive. The order of
fields in the partitions is important in the same way as it is for Compound Indexes . Data is optimized
for queries by the first field, followed by the second field, and so on.
Atlas Data Federation parses the partitions in order; if a query omits a particular
partition, Atlas Data Federation is less efficient in making use of any partitions
that follow the omitted partition. Atlas Data Federation is less performant in supporting queries on fields that don't
have partitions. Querying Data at a HTTP or HTTPS URL Data Federation also creates one partition for each URL in your collection.
When you connect to your
federated database instance and run queries, Data Federation processes your queries against the data
and returns the query results. Running Federated Queries You can use Atlas Data Federation to query and analyze a unified view of data in your Atlas cluster, S3 bucket or Azure Blob Storage container, HTTP URL, and
online archives. For federated queries, your federated database instance storage configuration must contain the settings that define: Your S3 or Azure , Atlas , Online Archive, and HTTP stores. Note Atlas Data Federation doesn't support federated queries across cloud providers.
Therefore, you can't run federated queries against data stored on AWS S3 buckets and Azure Blob Storage containers. Regardless of the
cloud provider backing your Atlas cluster, you can run
federated queries against data on your Atlas cluster and AWS S3 bucket or Azure Blob Storage container simultaneously. Federated Database Instances with virtual collections that map to your S3 bucket or
Azure Blob Storage, Atlas cluster, Online Archive, and HTTP stores. You can create or update your federated database instance storage configuration using the Atlas UI Visual Editor or
the JSON Editor , Atlas Data Federation CLI commands, and Atlas Data Federation API endpoints. To learn more about federated database instance storage configuration, see Define Data Stores for a Federated Database Instance . When you connect to your
federated database instance and run federated queries, Data Federation combines data from your Atlas cluster, S3 bucket or Azure Blob Storage container, and HTTP URL s in virtual databases and collections and returns a union of data
in the results. Configuring Query Limits You can limit the amount of data that Atlas Data Federation processes for your queries
to control costs. To limit the amount of data that Atlas Data Federation processes for
your queries, you can configure query limits per federated database instance or for all
federated database instances in your project. When the amount of processed data reaches any
applicable configured limit, Atlas Data Federation won't execute any new queries and
returns an error to the client application that a limit has been reached.
To learn more, see Manage Atlas Data Federation Query Limits . Troubleshooting Error: We are currently experiencing increased query processing
wait times for Atlas Data Federation. Our Engineering team is investigating. Normal
service will resume shortly, please try again. Atlas Data Federation returns this error only when Atlas Data Federation can't execute queries
because of resource contention. We recommend that you run your queries
again. Back Download Query Logs Next SQL
