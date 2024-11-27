# Aggregate Data in MongoDB Atlas - Functions - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions Aggregate Data in MongoDB Atlas - Functions On this page Data Model Snippet Setup Run an Aggregation Pipeline Find Data with Atlas Search Aggregation Stages Filter Documents Group Documents Project Document Fields Add Fields to Documents Unwind Array Values Aggregation Framework Limitations The examples on this page demonstrate how to use the MongoDB Query API
in an Atlas Function to aggregate documents in your Atlas cluster. MongoDB aggregation pipelines run
all documents in a collection through a series of data aggregation
stages that allow you to filter and shape
documents as well as collect summary data about groups of related
documents. Note Supported Aggregation Stages Atlas Functions support nearly all MongoDB aggregation pipeline stages and
operators, but some stages and operators must be executed within a system function . See Aggregation Framework
Limitations for more
information. Data Model The examples on this page use a collection named store.purchases that contains information about historical item sales in an online
store. Each document contains a list of the purchased items ,
including the item name and the purchased quantity , as well as a
unique ID value for the customer that purchased the items. { "title": "Purchase", "required": ["_id", "customerId", "items"], "properties": { "_id": { "bsonType": "objectId" }, "customerId": { "bsonType": "objectId" }, "items": { "bsonType": "array", "items": { "bsonType": "object", "required": ["name", "quantity"], "properties": { "name": { "bsonType": "string" }, "quantity": { "bsonType": "int" } } } } } } Snippet Setup To use a code snippet in a function , you
must first instantiate a MongoDB collection handle: exports = function ( ) { const mongodb = context. services . get ( "mongodb-atlas" ) ; const itemsCollection = mongodb. db ( "store" ). collection ( "items" ) ; const purchasesCollection = mongodb. db ( "store" ). collection ( "purchases" ) ; // ... paste snippet here ... } Run an Aggregation Pipeline You can execute an aggregation pipeline using the collection.aggregate() method. The following Function snippet groups all documents
in the purchases collection by their customerId value and
aggregates a count of the number of items each customer purchases as
well as the total number of purchases that they made. After grouping the
documents the pipeline adds a new field that calculates the average
number of items each customer purchases at a time, averageNumItemsPurchased , to each customer's document: const pipeline = [ { "$group" : { "_id" : "$customerId" , "numPurchases" : { "$sum" : 1 } , "numItemsPurchased" : { "$sum" : { "$size" : "$items" } } } } , { "$addFields" : { "averageNumItemsPurchased" : { "$divide" : [ "$numItemsPurchased" , "$numPurchases" ] } } } ] return purchasesCollection. aggregate ( pipeline). toArray ( ) . then ( customers => { console . log ( `Successfully grouped purchases for ${customers.length} customers.` ) for ( const customer of customers) { console . log ( `customer: ${customer._id} ` ) console . log ( `num purchases: ${customer.numPurchases} ` ) console . log ( `total items purchased: ${customer.numItemsPurchased} ` ) console . log ( `average items per purchase: ${customer.averageNumItemsPurchased} ` ) } return customers }) . catch ( err => console . error ( `Failed to group purchases by customer: ${err} ` )) Find Data with Atlas Search You can run |service| Search queries on a collection
with collection.aggregate() and the $search aggregation
stage. Important Atlas Functions perform $search operations as a system user and
enforce field-level rules on the returned search results. This means that a
user may search on a field for which they do not have read access. In this
case, the search is based on the specified field but no returned documents
include the field. exports = async function searchMoviesAboutBaseball ( ) { // 1. Get a reference to the collection you want to search. const movies = context. services . get ( "mongodb-atlas" ) . db ( "sample_mflix" ) . collection ( "movies" ) ; // 2. Run an aggregation with $search as the first stage. const baseballMovies = await movies . aggregate ( [ { $search : { text : { query : "baseball" , path : "plot" , } , } , } , { $limit : 5 , } , { $project : { _id : 0 , title : 1 , plot : 1 , } , } , ]) . toArray ( ) ; return baseballMovies ; } ; HIDE OUTPUT { "plot" : "A trio of guys try and make up for missed opportunities in childhood by forming a three-player baseball team to compete against standard children baseball squads." , "title" : "The Benchwarmers" } { "plot" : "A young boy is bequeathed the ownership of a professional baseball team." , "title" : "Little Big League" } { "plot" : "A trained chimpanzee plays third base for a minor-league baseball team." , "title" : "Ed" } { "plot" : "The story of the life and career of the famed baseball player, Lou Gehrig." , "title" : "The Pride of the Yankees" } { "plot" : "Babe Ruth becomes a baseball legend but is unheroic to those who know him." , "title" : "The Babe" } Note $$SEARCH_META Variable Availability The $$SEARCH_META aggregation variable is only available for Functions that run as system or if the first role on the searched collection has its apply_when and read expressions set to true . If neither of these two scenarios apply, $$SEARCH_META is undefined and
the aggregation will fail. Aggregation Stages Filter Documents You can use the $match stage
to filter incoming documents using standard MongoDB query syntax . { "$match" : { "<Field Name>" : < Query Expression > , ... } } Example The following $match stage filters incoming documents to include
only those where the graduation_year field has a value between 2019 and 2024 , inclusive. { "$match" : { "graduation_year" : { "$gte" : 2019 , "$lte" : 2024 } , } } Group Documents You can use the $group stage to aggregate summary
data for groups of one or more documents. MongoDB groups documents based
on the _id expression. Note You can reference a specific document field by prefixing the field
name with a $ . { "$group" : { "_id" : <Group By Expression>, "<Field Name>": <Aggregation Expression>, ... } } Example The following $group stage groups documents by the value of their customerId field and calculates the number of purchase documents
that each customerId appears in. { "$group" : { "_id" : "$customerId" , "numPurchases" : { "$sum" : 1 } } } Project Document Fields You can use the $project stage to include or omit
specific fields from documents or to calculate new fields using aggregation operators .
To include a field, set its value to 1 . To omit a field, set its
value to 0 . Note You can't simultaneously omit and include fields other than _id .
If you explicitly include a field other than _id , any fields you
did not explicitly include are automatically omitted (and
vice-versa). { "$project" : { "<Field Name>" : <0 | 1 | Expression>, ... } } Example The following $project stage omits the _id field, includes
the customerId field, and creates a new field named numItems where the value is the number of documents in the items array: { "$project" : { "_id" : 0 , "customerId" : 1 , "numItems" : { "$sum" : { "$size" : "$items" } } } } Add Fields to Documents You can use the $addFields stage to add new fields
with calculated values using aggregation operators . Note $addFields is similar to $project but does not allow you to
include or omit fields. Example The following $addFields stages creates a new field named numItems where the value is the number of documents in the items array: { "$addFields" : { "numItems" : { "$sum" : { "$size" : "$items" } } } } Unwind Array Values You can use the $unwind stage to aggregate
individual elements of array fields. When you unwind an array field,
MongoDB copies each document once for each element of the array field
but replaces the array value with the array element in each copy. { $unwind : { path : <Array Field Path>, includeArrayIndex: <string>, preserveNullAndEmptyArrays: <boolean> } } Example The following $unwind stage creates a new document for each
element of the items array in each document. It also adds a field
called itemIndex to each new document that specifies the
element's position index in the original array: { "$unwind" : { "path" : "$items" , "includeArrayIndex" : "itemIndex" } } Consider the following document from the purchases collection: { _id : 123 , customerId : 24601 , items : [ { name : "Baseball" , quantity : 5 } , { name : "Baseball Mitt" , quantity : 1 } , { name : "Baseball Bat" , quantity : 1 } , ] } If we apply the example $unwind stage to this document, the stage
outputs the following three documents: { _id : 123 , customerId : 24601 , itemIndex : 0 , items : { name : "Baseball" , quantity : 5 } } , { _id : 123 , customerId : 24601 , itemIndex : 1 , items : { name : "Baseball Mitt" , quantity : 1 } } , { _id : 123 , customerId : 24601 , itemIndex : 2 , items : { name : "Baseball Bat" , quantity : 1 } } Aggregation Framework Limitations Aggregation Methods Atlas Functions support aggregation on the both the database and collection
level using the following commands: db.aggregate() db.collection.aggregate() Aggregation Pipeline Stage Availability All aggregation pipeline stages stages are available to the system user except for $indexStats . Aggregation Pipeline Operator Availability Atlas Functions support all aggregation pipeline operators when you run an aggregation pipeline
in the system user context. Back Write Next Define and Manage Secrets
