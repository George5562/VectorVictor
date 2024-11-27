# Insert Methods - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations / Insert Insert Methods MongoDB provides the following methods for inserting documents into a collection: Method Description db.collection.insertOne() Inserts a single document into a collection. db.collection.insertMany() Inserts multiple documents into a
collection. If you use MongoDB Atlas, the fully managed service for MongoDB deployments
in the cloud, you can use these methods to insert documents after
you connect to your cluster.
To learn more, see the following resources in the
MongoDB Atlas documentation: Connect to Your Cluster Insert and View a Document Additional Methods for Inserts The following methods can also add new documents to a collection,
including collections hosted in MongoDB Atlas: db.collection.updateOne() when used with the upsert:
true option. db.collection.updateMany() when used with the upsert:
true option. db.collection.findAndModify() when used with the upsert:
true option. db.collection.findOneAndUpdate() when used with the upsert: true option. db.collection.findOneAndReplace() when used with the upsert: true option. db.collection.bulkWrite() . See the individual reference pages for the methods for more information
and examples. Back Insert Next Query
