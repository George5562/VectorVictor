# Read Data from MongoDB Atlas - Functions - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions Read Data from MongoDB Atlas - Functions On this page Data Model Snippet Setup Query Methods Find a Single Document ( findOne() ) Find One or More Documents ( find() ) Count Documents in the Collection ( count() ) Query Patterns Find by Document ID Find by Date Match a Root-Level Field Match Multiple Fields Match an Embedded Document Field Match an Array of Values Match an Array Element Query Operators Compare Values Evaluate a Logical Expression Evaluate a Regular Expression The examples on this page demonstrate how to use the MongoDB Query API
in an Atlas Function to read documents from your Atlas cluster. Learn about the methods that you
can call to query data, the operators that let you write expressive match filters, and some patterns for combining them to handle common use cases. Data Model The examples on this page use a collection named store.items that
models various items available for purchase in an online store. Each
item has a name , an inventory quantity , and an array of customer reviews . The JSON schema for store.items { "title" : "Item" , "required" : [ "_id" , "name" , "quantity" , "reviews" ] , "properties" : { "_id" : { "bsonType" : "objectId" } , "name" : { "bsonType" : "string" } , "quantity" : { "bsonType" : "int" } , "reviews" : { "bsonType" : "array" , "items" : { "bsonType" : "object" , "required" : [ "username" , "comment" ] , "properties" : { "username" : { "bsonType" : "string" } , "comment" : { "bsonType" : "string" } } } } } } Snippet Setup To use a code snippet in a function , you
must first instantiate a MongoDB collection handle: exports = function ( ) { const mongodb = context. services . get ( "mongodb-atlas" ) ; const itemsCollection = mongodb. db ( "store" ). collection ( "items" ) ; const purchasesCollection = mongodb. db ( "store" ). collection ( "purchases" ) ; // ... paste snippet here ... } Query Methods Find a Single Document ( findOne() ) You can find a single document using the collection.findOne() method. The following function snippet finds a single
document from the items collection that has a quantity greater
than or equal to 25 : const query = { "quantity" : { "$gte" : 25 } } ; const projection = { "title" : 1 , "quantity" : 1 , } return itemsCollection. findOne ( query , projection) . then ( result => { if ( result) { console . log ( `Successfully found document: ${result} .` ) ; } else { console . log ( "No document matches the provided query." ) ; } return result ; }) . catch ( err => console . error ( `Failed to find document: ${err} ` )) ; Find One or More Documents ( find() ) You can find multiple documents using the collection.find() method. The following function snippet finds all documents in
the items collection that have at least one review and returns them
sorted by name with the _id field omitted: const query = { "reviews.0" : { "$exists" : true } } ; const projection = { "_id" : 0 } ; return itemsCollection. find ( query , projection) . sort ( { name : 1 }) . toArray ( ) . then ( items => { console . log ( `Successfully found ${items.length} documents.` ) items. forEach ( console . log ) return items }) . catch ( err => console . error ( `Failed to find documents: ${err} ` )) Count Documents in the Collection ( count() ) You can count documents in a collection using the collection.count() method. You can specify a query to
control which documents to count. If you don't specify a query, the
method counts all documents in the collection. The following function snippet counts the number of
documents in the items collection that have at least one review: return itemsCollection. count ( { "reviews.0" : { "$exists" : true } }) . then ( numDocs => console . log ( ` ${numDocs} items have a review.` )) . catch ( err => console . error ( "Failed to count documents: " , err)) Query Patterns Find by Document ID You can query a collection to find a document that has a specified ID.
MongoDB automatically stores each document's ID as an ObjectId value
in the document's _id field. { "_id" : < ObjectId > } Example The following query matches a document in the collection that has an _id value of 5ad84b81b8b998278f773c1b : { "_id" : BSON . ObjectId ( "5ad84b81b8b998278f773c1b" ) } Find by Date You can query a collection to find documents that have a field with a
specific date value, or query for a documents within a range of dates. { "<Date Field Name>" : < Date | Expression > } Example The following query matches documents in the collection that have a createdAt date of January 23, 2019: { "createdAt" : new Date ( "2019-01-23T05:00:00.000Z" ) } Example The following query matches documents in the collection that have a createdAt date some time in the year 2019: { "createdAt" : { "$gte" : new Date ( "2019-01-01T00:00:00.000Z" ) , "$lt" : new Date ( "2020-01-01T00:00:00.000Z" ) , } } Match a Root-Level Field You can query a collection based on the value of a root-level field in
each document. You can specify either a specific value or a nested
expression that MongoDB evaluates for each document. For more information, see the Query Documents tutorial in the MongoDB Server Manual. { "<Field Name>" : < Value | Expression > } Example The following query matches documents where the name field has a
value of Basketball : { "name" : "Basketball" } Match Multiple Fields You can specify multiple query conditions in a single query document.
Each root-level field of a query document maps to a field in the
collection. MongoDB only returns documents that fulfill all query
conditions. For more information, see the Query on Embedded/Nested
Documents tutorial in the MongoDB
Server Manual. { "<Field Name 1>" : <Value | Expression>, "<Field Name 2>": <Value | Expression> } Example The following query matches documents where the name field has a
value of Basketball and the quantity value is greater than
zero: { "name" : "Basketball" , "quantity" : { "$gt" : 0 } } Match an Embedded Document Field You can query a collection based on the value of embedded document
fields. To specify an embedded document field, use multiple nested query
expressions or standard document dot notation . For more information, see the Query on Embedded/Nested
Documents tutorial in the MongoDB
Server Manual. Nested Query Expressions { "<Field Name>" : { "<Nested Field Name>" : < Value | Expression > } } Dot Notation { "<Field Name>.<Nested Field Name>" : < Value | Expression > } Example The following query matches documents where the first review in the reviews array was left by someone with the username JoeMango : { "reviews.0.username" : "JoeMango" } Match an Array of Values You can query a collection based on all the elements contained in an
array field. If you query an array field for a specific array of values, MongoDB
returns documents where the array field exactly matches the specified
array of values.
If you want MongoDB to return documents where the array field contains all elements in the specified array of values, use the $all operator. For more information, see the Query an Array tutorial in the MongoDB Server Manual. { "<Array Field Name>" : [< Value > , ... ] } Example The following query matches documents where the reviews array
contains exactly one element and the element matches the specified
document: { "reviews" : [ { username : "JoeMango" , comment : "This rocks!" }] } Example The following query matches documents where the reviews array
contains one or more elements that match all of the specified
documents: { "reviews" : { "$all" : [ { username : "JoeMango" , comment : "This rocks!" }] } } Match an Array Element You can query a collection based on the value of one or more elements in
an array field. If you query an array field with a query expression that has multiple
conditions, MongoDB returns documents where any combination of the
array's elements satisfy the expression. If you want MongoDB to return
documents where a single array element satisfies all of the expression
conditions, use the $elemMatch operator. For more information, see the Query an Array tutorial in the MongoDB Server Manual. { "<Array Field Name>" : < Value | Expression > } Example The following query matches documents where both conditions in the
embedded expression are met by any combination of elements in the reviews array. The specified username and comment values
do not need to be in the same document: { "reviews" : { "username" : "JoeMango" , "comment" : "This is a great product!" } } Example The following query matches documents where both conditions in the
embedded expression are met by a single element in the reviews array. The specified username and comment must be in the same
document: { "reviews" : { "$elemMatch" : { "username" : "JoeMango" , "comment" : "This is a great product!" } } } Query Operators Compare Values You can use a comparison operator to compare the value of a
document field to another value. { "<Field Name>" : { "<Comparison Operator>" : < Comparison Value > } } The following comparison operators are available: Comparison Operator Description $eq Matches documents where the value of a field equals a specified
value. $ne Matches documents where the value of a field does not equal a
specified value. $gt Matches documents where the value of a field is strictly greater
than a specified value. $gte Matches documents where the value of a field is greater than or
equal to a specified value. $lt Matches documents where the value of a field is strictly less
than a specified value. $lte Matches documents where the value of a field is less than or
equal to a specified value. $in Matches documents where the value of a field is included in a
specified array of values. $nin Matches documents where the value of a field is not included in
a specified array of values. Example The following query matches documents where quantity is greater
than zero and less than or equal to ten. { "quantity" : { "$gt" : 0 , "$lte" : 10 } } Evaluate a Logical Expression You can use a logical operator to evaluate multiple expressions
for a single field. { "<Field Name>" : { "<Logical Operator>" : [< Expression > , ... ] } } The following logical operators are available: Logical Operator Description $and Matches documents where the value of a field matches all of the
specified expressions. $or Matches documents where the value of a field matches any of the
specified expressions. $nor Matches documents where the value of a field matches none of
the specified expressions. $not Inverts the boolean result of the specified logical expression. Example The following query matches documents where either quantity is
greater than zero or there are no more than five documents in the reviews array. { "$or" : [ { "quantity" : { "$gt" : 0 } } , { "reviews" : { "$size" : { "$lte" : 5 } } } ] } Evaluate a Regular Expression You can use the $regex query
operator to return documents with fields that match a regular expression . To avoid ambiguity
with the $regex EJSON type, you must use a atlas-BSON.BSONRegExp object. { "<Field Name>" : { "$regex" : BSON . BSONRegExp ( <RegEx String>, <RegEx Options>) } } Example The following query matches documents where the name value
contains the substring ball (case-insensitive). { "name" : { "$regex" : BSON . BSONRegExp ( ".+ball" , "i" ) } } Back JavaScript Support Next Write
