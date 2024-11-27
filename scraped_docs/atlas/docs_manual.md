# What is MongoDB? - MongoDB Manual v8.0


What is MongoDB? MongoDB is a document database designed for ease of application
development and scaling. You can run MongoDB in the following environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Get started with MongoDB Atlas What You Can Do Work with your data in MongoDB Store and query your data Transform data with Aggregations Secure access to your data Deploy and scale your database 1 Deploy MongoDB Create a cluster in the MongoDB Atlas UI or the Atlas CLI
quickly and easily. To learn more, see Create a Cluster in the MongoDB Atlas documentation
and Get Started with Atlas in the Atlas CLI
documentation. For self-hosted deployments,
see Replication in the MongoDB manual
to create a replica
set. 2 Connect to your deployment Access deployments in the
MongoDB Atlas UI or connect with drivers or the MongoDB Shell (mongosh) in the MongoDB
manual. To learn more, see Find Your Connection String in the MongoDB manual. 3 Insert, query, update, or delete documents Perform CRUD operations in the MongoDB Atlas UI or by using the
MongoDB Query API - with or without transactions. To learn more, see Create, View, Update, and Delete Documents in the MongoDB Atlas documentation and MongoDB CRUD Operations in the MongoDB manual. 4 Model your data Design your data schema to support frequent access patterns.
You can update or enforce your schema at any point. To learn more, see Data Modeling Introduction in the MongoDB manual. â atlas setup ? Do you want to setup your Atlas database with default settings ? ( Y / n) â Y We are deploying Cluster9876543 ... Please store your database authentication access details in a secure location. Database User Username : Cluster9876543 Database User Password : abcdef12345 Creating your cluster ... [ Its safe to 'Ctrl + C' ] 1 Import your data Import data from a CSV or JSON file with database tools. To learn more, see Migrate or Import Data in the MongoDB Atlas
documentation and mongoimport in the database tools documentation. 2 Aggregate your data Use aggregation pipelines to process your data in multiple
stages and return the computed results. You can
preview the results at each pipeline stage when you
run aggregation pipelines in MongoDB Atlas. To learn more, see Run Aggregation Pipelines in the MongoDB Atlas documentation
and Aggregation Operations in the MongoDB manual. test > db. orders . insertMany ( [ { "item" : "almonds" , "price" : 12 , "quantity" : 2 } , { "item" : "pecans" , "price" : 20 , "quantity" : 1 } , ]) test > db. inventory . insertMany ( [ { "sku" : "almonds" , "description" : "product 1" , "instock" : 120 } , { "sku" : "cashews" , "description" : "product 3" , "instock" : 60 } , { "sku" : "pecans" , "description" : "product 4" , "instock" : 70 } ]) test > db. orders . aggregate ( [ { $match : { price : { $lt : 15 } } } , { $lookup : { from : "inventory" , localField : "item" , foreignField : "sku" , as : "inventory_docs" } } , { $sort : { price : 1 } } , ]) 1 Authenticate a client Verify the identity of a user, replica set member, or
sharded cluster member with authentication. To learn more, see Atlas UI Authenication in the MongoDB Atlas documentation
and Authentication in the MongoDB
manual. 2 Control access to your database Enable Role-Based Access Controls to manage user privileges
on your entire database cluster or individual collections. To learn more, see Atlas UI Authorization in the MongoDB Atlas documentation
and Role-Based Access Controls in the MongoDB manual. 3 Encrypt your most sensitive data Client-Side Field Level Encryption protects data while it is
in-use by the database. Fields are encrypted before they
leave your application, protecting them over the network, in
memory and at rest. To learn more, see Client-Side Field Level Encryption in the MongoDB manual. 1 Create a cluster Create a free cluster, an auto-scaling cluster, or a
serverless instance in the MongoDB Atlas UI. To learn
more, see Choose a Cluster Type in the MongoDB Atlas
documentation. For self-hosted deployments, provide redundancy and
resilience for your database by deploying a replica set. To
learn more, see Replication in the
MongoDB manual. 2 Scale out your database Use sharding to horizontally scale your database or to
ensure location-based separation of data. To learn more, see Shard a Collection in the MongoDB Atlas
documentation and Sharding in the MongoDB manual. Related Products & Resources Go Further with MongoDB Explore libraries and tools for MongoDB. Use MongoDB in your application's language Learn about Drivers Visually explore your data with MongoDB Compass View Compass Docs Manage and monitor your deployments View Ops Manager
