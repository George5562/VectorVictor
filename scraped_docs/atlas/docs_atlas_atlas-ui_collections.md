# Create, View, Drop, and Shard Collections - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data Create, View, Drop, and Shard Collections On this page Required Roles Create a Collection View Collections Drop a Collection Shard a Collection You can use the Atlas UI to manage the collections in your
clusters. Required Roles The following table describes the roles required to perform
various actions to a database in the Atlas UI: Action Required Roles Create Collections One of the following roles: Project Owner or Organization Owner Project Data Access Admin Project Data Access Read/Write View Collections At least the Project Data Access Read Only role. Drop Collections One of the following roles: Project Owner Project Data Access Admin Shard Collections One of the following roles: Project Owner Organization Owner Create a Collection Tip To create the first collection in a new database, see Create a Database . Important You cannot create new collections on the config and system databases. Atlas will deprecate writing to existing
collections on these databases in the near future. To create a collection in an existing database through the Atlas UI: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. 3 Click on the plus sign + icon for a database. Either select or hover over the database to drop and click on the
plus sign + icon. 4 Enter the Collection Name . Important Don't include sensitive information in
your collection name. For more information on MongoDB collection names, see Naming Restrictions . 5 Optional. Specify a capped collection. Select whether the collection is a capped collection . If you select to create a capped
collection, specify the maximum size in bytes. 6 Optional. Specify a time series collection. Select whether the collection is a time series collection .
If you select to create a time series collection, specify the time
field and granularity. You can optionally specify the meta field and
the time for old data in the collection to expire. 7 Click Create . Upon successful creation, the collection appears underneath the
database in the Atlas UI. View Collections To view the databases and collections in the deployment: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. 3 View the collections in a database. Click on the name of the database. Note Atlas bases the document count that appears on this tab
on cached metadata using collStats . This count might differ from
the actual document count in the collection. For example, an unexpected shutdown can throw off the
count. Use the db.collection.countDocuments() method for
the most accurate document count. Visualize Collection Data To launch MongoDB Charts to visualize data in your databases and collections. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. 3 Launch MongoDB Charts . To visualize data in MongoDB Charts from the Atlas UI, click Visualize Your Data when viewing a specific database
or collection. Charts loads the data source and you can
start building a chart in the Charts view. For detailed
steps, see Build Charts . Drop a Collection To drop a collection, including its documents and indexes, through the
Atlas UI: 1 Drop the collection. Either select or hover of the collection to drop and click on its
trash can icon. 2 Confirm action. Confirm by typing the name of the collection, and click Drop . Shard a Collection If you have large data sets and perform high throughput operations, you
can shard a collection to distribute data across
the shards. Note Before you start, you must have the following: A sharded Atlas cluster mongosh on your local machine To shard a collection through the Atlas UI: 1 Connect to MongoDB from mongosh . See Connect via mongosh . 2 Enable sharding for the databases you want to shard. To enable sharding, run the following command: sh.enableSharding("<database-name>") Example To enable sharding for the sample_analytics dataset: sh.enableSharding("sample_analytics") To learn more, see Enable Sharding for a Database in the MongoDB manual. 3 Optional: Create an index on the shard key if the collection that you wish to shard has data and is not empty. To create an index on the shard key, run the following command: db.<collection-name>.createIndex({<shard_key_definition>}) Example To create an index on the shard key for the sample_analytics.customers collection: db.sample_analytics.runCommand( { createIndexes: "customers", indexes: [ { key: { "username": 1 }, "name": "usernameIndex" }], "commitQuorum": "majority" } ) To learn  more, see: Choose a Shard Key createIndexes 4 Shard the collection that you want to shard. To shard a collection, run the following command: sh.shardCollection("<database>.<collection>", { "<indexed-field>" : 1 } ) Example To shard the sample_analytics.customers collection: sh.shardCollection("sample_analytics.customers",{"username":1}) Warning If you shard a collection that already has an Atlas Search index, you might
experience a brief period of query downtime when the collection
begins to appear on a shard. Also, if you add a shard for an already
sharded collection that contains an Atlas Search index, your search queries
against that collection will fail until the initial sync process
completes on the added shards. To learn more, see initial sync process . To learn more, see Shard a Collection in the MongoDB
manual. Back Databases Next Documents
