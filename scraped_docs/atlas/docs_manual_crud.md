# MongoDB CRUD Operations - MongoDB Manual v8.0


Docs Home / MongoDB Manual MongoDB CRUD Operations On this page Create Operations Read Operations Update Operations Delete Operations Bulk Write CRUD operations create , read , update , and delete documents . You can connect with driver methods and perform CRUD operations
for deployments hosted in the following environments: You can perform CRUD operations in the UI for deployments hosted in MongoDB Atlas . Create Operations Create or insert operations add new documents to a collection . If the
collection does not currently exist, insert operations will create the
collection. MongoDB provides the following methods to insert documents into a
collection: db.collection.insertOne() db.collection.insertMany() In MongoDB, insert operations target a single collection . All
write operations in MongoDB are atomic on the level of a single document . For examples, see Insert Documents . Read Operations Read operations retrieve documents from a collection ; i.e. query a collection for
documents. MongoDB provides the following methods to read documents from
a collection: db.collection.find() You can specify query filters or criteria that identify the documents to return. For examples, see: Query Documents Query on Embedded/Nested Documents Query an Array Query an Array of Embedded Documents Update Operations Update operations modify existing documents in a collection . MongoDB
provides the following methods to update documents of a collection: db.collection.updateOne() db.collection.updateMany() db.collection.replaceOne() In MongoDB, update operations target a single collection. All write
operations in MongoDB are atomic on the level of a single document. You can specify criteria, or filters, that identify the documents to
update. These filters use the same
syntax as read operations. For examples, see Update Documents . Delete Operations Delete operations remove documents from a collection. MongoDB provides
the following methods to delete documents of a collection: db.collection.deleteOne() db.collection.deleteMany() In MongoDB, delete operations target a single collection . All
write operations in MongoDB are atomic on the level of a single document. You can specify criteria, or filters, that identify the documents to
remove. These filters use the same
syntax as read operations. For examples, see Delete Documents . Bulk Write MongoDB provides the ability to perform write operations in bulk. For
details, see Bulk Write Operations . Back Extended JSON (v1) Next Insert
