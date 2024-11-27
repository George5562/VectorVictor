# Databases and Collections in MongoDB - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction Databases and Collections in MongoDB On this page Overview Databases Collections Overview MongoDB stores data records as documents (specifically BSON documents ) which are
gathered together in collections .  A database stores one or more collections of documents. You can manage databases and collections on the Atlas cluster from
the Atlas UI, mongosh , or MongoDB Compass . This page describes
how to manage databases and collections on the Atlas cluster from the
Atlas UI. For self-managed deployments, you can use mongosh or MongoDB Compass to manage databases and collections. Select the client that you want to use to manage databases and
collections. Atlas UI mongosh MongoDB Compass MongoDB Atlas is a multi-cloud database service that simplifies
deploying and managing your databases on the cloud providers of
your choice. The MongoDB Shell, mongosh , is a JavaScript and Node.js REPL environment for interacting
with MongoDB deployments. To learn more, see mongosh . MongoDB Compass is a powerful GUI for querying, aggregating, and
analyzing your MongoDB data in a visual environment. To learn
more, see MongoDB Compass . Databases In MongoDB, databases hold one or more collections of documents. Atlas UI mongosh MongoDB Compass To select a database to use, log in to Atlas and do the following: 1 Navigate to the Collections tab. 2 Select the database from the list of databases in the left pane. To select a database to use, in mongosh , issue the use <db> statement, as in the following example: use myDB To select a database to use, complete the following steps: 1 Start MongoDB Compass and connect to your cluster. To learn more, see Connect to MongoDB . 2 Select Databases from the left navigation. The Databases tab opens to list the existing databases
for your MongoDB deployment. Create a Database Atlas UI mongosh MongoDB Compass To create a new database, log in to Atlas and do the following: 1 Navigate to the Collections tab. 2 Click Create Database . 3 Enter the Database Name and the Collection Name . Enter the database and the collection name to create the
database and its first collection. 4 Click Create . Upon successful creation, the database and the collection
displays in the left pane in the Atlas UI. If a database does not exist, MongoDB creates the database when you
first store data for that database. As such, you can switch to a
non-existent database and perform the following operation in mongosh : use myNewDB db. myNewCollection1 . insertOne ( { x : 1 } ) The insertOne() operation creates both the
database myNewDB and the collection myNewCollection1 if they do
not already exist. Be sure that both the database and collection names
follow MongoDB Naming Restrictions . 1 Open the Databases tab. 2 Click the Create database button. 3 Enter database and first collection names in the Create Database dialog. 4 Click Create Database to create the database and its first collection. Collections MongoDB stores documents in collections. Collections are analogous to
tables in relational databases. click to enlarge Create a Collection If a collection does not exist, MongoDB creates the collection when you
first store data for that collection. Atlas mongosh MongoDB Compass To create a new collection, log in to Atlas and do the following: 1 Navigate to the Collections tab. 2 Click the + icon for the database. 3 Enter the name of the collection. 4 Click Create . Upon successful creation, the collection displays underneath
the database in the Atlas UI. db. myNewCollection2 . insertOne ( { x : 1 } ) db. myNewCollection3 . createIndex ( { y : 1 } ) Both the insertOne() and the createIndex() operations create their
respective collection if they do not already exist. Be sure that the
collection name follows MongoDB Naming Restrictions . 1 Click the name of the database where you to want to create a collection in the left navigation. 2 Click the + icon next to the database name. 3 Enter the name of the collection in the Create Collection dialog. 4 Click Create Collection to create the collection. Explicit Creation Atlas mongosh MongoDB Compass To create a new collection, log in to Atlas and do the following: 1 Navigate to the Collections tab. 2 Click the + icon for the database. 3 Enter the name of the collection. 4 Optional. From the Additional Preferences dropdown, select the type of collection that you want to create. You can create one of the following types of collections: Capped collection If you select to create a capped collection, specify the
maximum size in bytes. Time Series Collection If you select to create a time series collection, specify
the time field and granularity. You can optionally specify
the meta field and the time for old data in the collection
to expire. Clustered Index Collection If you select to create a clustered collection, you must
specify clustered index key value and a name for the
clustered index. 5 Click Create . Upon successful creation, the collection displays underneath
the database in the Atlas UI. MongoDB provides the db.createCollection() method to
explicitly create a collection with various options, such as setting
the maximum size or the documentation validation rules. If you are not
specifying these options, you do not need to explicitly create the
collection since MongoDB creates new collections when you first store
data for the collections. To modify these collection options, see collMod . 1 Click the name of the database where you to want to create a collection in the left navigation. 2 Click the Create collection button. 3 Enter the name of the collection and optionally, configure additional preferences. 4 Click Create Collection to create the collection. MongoDB Compass provides the following additional preferences that
you can configure for your collection: Create a Capped Collection Create a Clustered Collection Create a Collection with Collation Create a Collection with Encrypted Field Create a Time Series Collection Document Validation By default, a collection does not require its documents to have the
same schema; i.e. the documents in a single collection do not need to
have the same set of fields and the data type for a field can differ
across documents within a collection. However, you can enforce document validation rules for a collection during update and insert operations.
See Schema Validation for details. For deployments hosted in MongoDB Atlas, the Performance Advisor and the MongoDB Atlas UI detect common schema
design issues and suggest modifications that follow MongoDB best
practices. To learn more, see Schema Suggestions . Modifying Document Structure To change the structure of the documents in a collection, such as add
new fields, remove existing fields, or change the field values to a new
type, update the documents to the new structure. Unique Identifiers Collections are assigned an immutable UUID . The
collection UUID remains the same across all members of a replica set
and shards in a sharded cluster. Atlas mongosh MongoDB Compass To retrieve the UUID for a collection, run either the listCollections command
or the db.getCollectionInfos() method. Back Get Started Next Views
