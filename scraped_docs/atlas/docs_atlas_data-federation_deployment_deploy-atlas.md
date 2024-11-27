# Deploy a Federated Database Instance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / Atlas Cluster Deploy a Federated Database Instance On this page Required Access Prerequisites Procedure This page describes how to deploy a federated database instance for
accessing data in an Atlas cluster. Required Access To deploy a federated database instance, you must have Project Owner access to the project.
Users with Organization Owner access must add themselves as a Project Owner to the project before deploying a federated database instance. Prerequisites Before you begin, you will need to: Create a MongoDB Atlas account, if you do not have one already. Create an Atlas Cluster , if you do not
have one already. Atlas Data Federation supports Atlas clusters
deployed to AWS , Azure , or Google Cloud . Note To use your Atlas cluster as a data store, you must deploy it
to the same project as your federated database instance. Add data to at least one collection on your Atlas cluster if you
have not already. Procedure Atlas CLI Atlas UI To create a new Data Federation database using the
Atlas CLI, run the following command: atlas dataFederation create <name> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dataFederation create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI 1 Log in to MongoDB Atlas. 2 Select the Data Federation option on the left-hand navigation. 3 Create a federated database instance. Click the Create New Federated Database dropdown. Select Manual Setup . 4 Select the cloud provider where Atlas Data Federation will process your queries against your federated database instance. You can select AWS , Azure , or Google Cloud. Once your federated database instance is created, you
can't change the cloud provider where Atlas Data Federation processes your queries. If you want to query data in an Atlas cluster, we recommend that you select that same cloud provider as the cloud provider for your cluster. To query data in object storage such as AWS S3 or Azure Blob Storage, you must select the same cloud for your federated database instance as the cloud for your object storage. 5 Type a name for your federated database instance in the Federated Database Instance Name field and click Continue . Defaults to FederatedDatabaseInstance[n] . Once your federated database instance is
created, you can't change its name. 6 Select the configuration method. For a guided experience, click Visual Editor . To edit the raw JSON , click JSON Editor . 7 Specify your data store. Visual Editor JSON Editor Select the dataset for your federated database instance from the Data Sources section. Click Add Data Sources to select your data store. Specify your data source. Choose Atlas Cluster to configure a federated database instance for data on
your Atlas cluster. Corresponds to stores.[n].provider JSON configuration setting. Select the Atlas cluster that you want to use as a data
store in the Provide Namespaces in this
project section. Corresponds to stores.[n].clusterName JSON configuration setting. Expand the databases and select the collections that you
want to add to your federated database instance. To filter the databases and collections, enter text into
the Search database or collection field. The
dialog box displays only databases and collections with names
that match your search criteria. Corresponds to the databases.[n].collections.[n].dataSources.[n].database and databases.[n].collections.[n].dataSources.[n].collection JSON configuration settings. Optional . Specify the Cluster Read Preference settings by expanding the section. Corresponds to stores.[n].readPreference . Field Name Description Read Preference Mode Specifies the replica set member to which you want to
route the read requests. You can choose one of the
following from the dropdown: primary - to route all read requests to the replica set primary primaryPreferred - to route all read requests the replica set primary and to secondary members
only if primary is unavailable secondary - to route all read requests to the secondary members of the replica set secondaryPreferred - to route all read requests to the secondary members of
the replica set and the primary on sharded clusters only if secondary members are unavailable nearest - to route all read requests to random eligible replica
set member, irrespective of whether that member is a primary or secondary If you add an Atlas cluster as a store, the
value default value is secondary . If you don't set anything in your federated database instance storage
configuration, the default value is nearest . To
learn more, see Read preference mode . Corresponds to stores.[n].readPreference.mode . TagSets Specifies the list of tags or tag
specification documents that contain name and value
pairs for the replica set member to which you want to
route read requests. To learn more, see Read
Preference Tag Sets . Corresponds to stores.[n].readPreference.tagSets . Maxstaleness Seconds Specifies the maximum replication lag, or
"staleness", for reads from secondaries. To learn
more, see Read Preference
maxStalenessSeconds . Corresponds to stores.[n].readPreference.maxStalenessSeconds . Click Next . Create the virtual databases, collections, and views and map the
databases, collections, and views to your data store. (Optional) Click the for the: Database to edit the database name. Defaults to VirtualDatabase[n] . Corresponds to databases.[n].name JSON configuration
setting. Collection to edit the collection name. Defaults to VirtualCollection[n] . Corresponds to databases.[n].collections.[n].name JSON configuration setting. View to edit the view name. You can click: Add Database to add databases and collections. associated with the database to add collections
to the database. associated with the collection to add views on the collection. To create a
view, you must specify: The name of the view. The pipeline to apply to the view. The view definition pipeline cannot include the $out or
the $merge stage. If the view definition includes
nested pipeline stages such as $lookup or $facet ,
this restriction applies to those nested pipelines as well. To learn more about views, see: Views db.createView associated with the database, collection, or
view to remove it. Select Atlas Cluster from the dropdown in the Data Sources section. Drag and drop the data store to map with the collection. Corresponds to databases.[n].collections.[n].dataSources JSON configuration setting. Your configuration for an Atlas cluster data store should
look similar to the following: 1 { 2 "stores" : [ 3 { 4 "name" : "<string>" , 5 "provider" : "<string>" , 6 "clusterName" : "<string>" , 7 "projectId" : "<string>" , 8 "readPreference" : { 9 "mode" : "<string>" , 10 "tagSets" : [ 11 [ { "name" : "<string>" , "value" : "<string>" } , ... ] , 12 ... 13 ] , 14 "maxStalenessSeconds" : <int> 15 } 16 } 17 ] , 18 "databases" : [ 19 { 20 "name" : "<string>" , 21 "collections" : [ 22 { 23 "name" : "<string>" , 24 "dataSources" : [ 25 { 26 "storeName" : "<string>" , 27 "database" : "<string>" , 28 "databaseRegex" : "<string>" , 29 "collection" : "<string>" , 30 "collectionRegex" : "<string>" , 31 "provenanceFieldName" : "<string>" 32 } 33 ] 34 } 35 ] , 36 "views" : [ 37 { 38 "name" : "<string>" , 39 "source" : "<string>" , 40 "pipeline" : "<string>" 41 } 42 ] 43 } 44 ] 45 } To learn more about these configuration settings, see Define Data Stores for a Federated Database Instance . Define your Atlas data store. Edit the JSON configuration settings shown in the UI for stores . Your stores cofiguration setting should resemble the
following: "stores" : [ { "name" : "<string>" , "provider" : "<string>" , "clusterName" : "<string>" , "projectId" : "<string>" "readPreference" : { "mode" : "<string>" , "tagSets" : [ [ { "name" : "<string>" , "value" : "<string>" } , ... ] , ... ] , "maxStalenessSeconds" : <int> } , "readConcern" : { "level" : "<string>" } } ] To learn more about these configuration settings, see stores . Define your federated database instance virtual databases, collections, and views. Edit the JSON configuration settings shown in the UI for databases . Your databases cofiguration setting should
resemble the following: "databases" : [ { "name" : "<string>" , "collections" : [ { "name" : "<string>" , "dataSources" : [ { "storeName" : "<string>" , "database" : "<string>" , "databaseRegex" : "<string>" , "collection" : "<string>" , "collectionRegex" : "<string>" , "provenanceFieldName" : "<string>" } ] } ] } ] To learn more about these configuration settings, see databases . 8 Optional: Repeat steps in the Visual Editor or JSON Editor tab above to define additional Atlas clusters. To add other data stores for federated queries, see: Create AWS Data Store From the UI or Create Azure Data Store From the UI Create HTTP or HTTPS Data Store From the
UI Create Online Archive Data Store From the UI 9 Click Save to create the federated database instance. Back Atlas Cluster Next Generate Collections
