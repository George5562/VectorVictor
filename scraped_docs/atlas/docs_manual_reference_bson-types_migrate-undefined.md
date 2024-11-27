# Migrate Undefined Data and Queries - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / BSON Types Migrate Undefined Data and Queries On this page Remove Undefined Fields Remove Field with Known Name Remove Fields with Unknown Names Update Undefined Values to Null Update Field with Known Name Update Fields with Unknown Names Update Queries to Match Undefined Values Learn More Starting in MongoDB 8.0, comparisons to null in equality match
expressions don't match undefined values. For example, consider these documents and query: // people collection [ { _id : 1 , name : null } , { _id : 2 , name : undefined } , { _id : 3 , name : [ "Gabriel" , undefined ] , { _id : 4 , names : [ "Alice" , "Charu" ] } ] db. people . find ( { name : null } ) Prior to MongoDB 8.0, the preceding query would match documents where: The name field is null ( _id: 1 ) The name field is undefined or contains an undefined array
element ( _id: 2 and _id: 3 ) The name field does not exist ( _id: 4 ) Starting in MongoDB 8.0, the preceding query does not match documents
where the name field is undefined or contains undefined array elements. The query only matches documents where: The name field is null or contains a null array element
( _id: 1 ) The name field does not exist ( _id: 4 ) This query behavior change also impacts these operations: $eq $in $lookup , because a null local field no longer matches
an undefined foreign field. To account for this behavior change, you can: Remove Undefined Fields . Update Undefined Values to Null . Update Queries to Match Undefined Values . Note undefined is a deprecated BSON type. Recent versions of the
MongoDB Shell and drivers automatically convert undefined values
to null when performing inserts and updates. The guidance on this
page applies to deployments that have undefined values from older
driver versions or legacy mongo shell. Remove Undefined Fields If you don't need to keep fields with undefined values in your
documents, you can remove those fields. MongoDB's flexible data model
means your collection's document fields do not need to be consistent, so
you can remove a particular field from a subset of documents. How to remove undefined fields from your documents depends on whether
you know the field name to remove. If you know the field name, the
operation is more performant because it can use an index. See either: Remove Field with Known Name Remove Fields with Unknown Names Remove Field with Known Name If you know the name of the field that contains undefined values
that you want to remove, use the following example. The example updates
the people collection to remove: The name field if its value is the scalar value undefined . undefined array elements in the name field. db. people . updateMany ( { name : { $type : "undefined" } } , [ { $set : { "name" : { $cond : { // When "name" is an array, convert { name: [ "Alice", undefined ] } // to { name: [ "Alice" ] } if : { $eq : [ { $type : "$name" } , "array" ] } , then : { $filter : { input : "$name" , cond : { $not : { $eq : [ { $type : "$$this" } , "undefined" ] } } } , } , // When "name" is scalar undefined, remove it else : "$$REMOVE" } } } } ] ) After you run the operation, the people collection contains these
documents: [ { _id : 1 , name : null } , { _id : 2 } , { _id : 3 , name : [ "Gabriel" ] } { _id : 4 , names : [ "Alice" , "Charu" ] } ] Remove Fields with Unknown Names If you don't know which fields contain undefined values, use the
following example to remove all undefined top-level fields. Note When you don't specify a field name for the update, the operation is
not performant because the query can't use an index. If you run the
following example on a large collection, the query might be slow and
resource-intensive. The following example removes top-level document fields from the people collection where the value is undefined : db. people . updateMany ( { } , [ { $replaceWith : { // Detect undefined top-level fields under the root and remove them $arrayToObject : { $filter : { input : { $objectToArray : "$$ROOT" } , cond : { $not : { $eq : [ { $type : "$$this.v" } , "undefined" ] } } } } } } ] ) After you run the operation, the people collection contains these
documents: [ { _id : 1 , name : null } , { _id : 2 } , { _id : 3 , name : [ "Gabriel" , undefined ] } { _id : 4 , names : [ "Alice" , "Charu" ] } ] Note The preceding approach only modifies top-level fields. The document
with _id: 3 still contains an undefined value because the
value appears in an array. Update Undefined Values to Null You can update undefined data values to the null data type. Use
this approach to migrate your data off of the deprecated undefined data type while retaining your document fields. How to update undefined fields depends on whether you know the field
name to update. If you know the field name, the operation is more
performant because it can use an index. See either: Update Field with Known Name Update Fields with Unknown Names Update Field with Known Name If you know the name of the field that contains undefined values
that you want to set to null , use the following example. The example
updates the people collection to set the following values to null : The name field if its value is the scalar value undefined . undefined array elements that appear in the name field. db. people . updateMany ( { name : { $type : "undefined" } } , [ { $set : { "name" : { $cond : { // When "name" is an array, convert { name: [ "Alice", undefined ] } // to { name: [ "Alice", null ] } if : { $eq : [ { $type : "$name" } , "array" ] } , then : { $map : { input : "$name" , in : { $cond : { if : { $eq : [ { $type : "$$this" } , "undefined" ] } , then : null , else : "$$this" } } } , } , // When "name" is the scalar undefined, convert to null else : null } } } } ] ) After you run the operation, the people collection contains these
documents: [ { _id : 1 , name : null } , { _id : 2 , name : null } , { _id : 3 , name : [ "Gabriel" , null ] } { _id : 4 , names : [ "Alice" , "Charu" ] } ] Update Fields with Unknown Names If you don't know which fields contain undefined values, use the
following example to set all undefined top-level fields to null . Note When you don't specify a field name for the update, the operation is
not performant because the query can't use an index. If you run the
following example on a large collection, the query might be slow and
resource-intensive. The following example updates the people collection to set undefined top-level document fields to null : db. people . updateMany ( { } , [ { $replaceWith : { // Detect undefined top-level fields under the root and replace them with null $arrayToObject : { $map : { input : { $objectToArray : "$$ROOT" } , in : { $cond : { if : { $eq : [ { $type : "$$this.v" } , "undefined" ] } , then : { k : "$$this.k" , v : null } , else : "$$this" } } } } } } ] ) After you run the operation, the people collection contains these
documents: [ { _id : 1 , name : null } , { _id : 2 , name : null } , { _id : 3 , name : [ "Gabriel" , undefined ] } { _id : 4 , names : [ "Alice" , "Charu" ] } ] Note The preceding approach only modifies top-level fields. The document
with _id: 3 still contains an undefined value because the
value appears in an array. Update Queries to Match Undefined Values If you can't migrate your data types from null to undefined , you
can rewrite your queries to match undefined values. If you use this
approach, your data will still contain the deprecated undefined BSON
type. To have queries for null match undefined values, add a query
predicate that explicitly matches the undefined type. For example,
the following query matches documents where name is undefined , null , or missing: db. people . find ( { $or : [ { name : null } , { name : { $type : "undefined" } } ] } ) The query returns all documents in the people collection: [ { _id : 1 , name : null } , { _id : 2 , name : undefined } , { _id : 3 , name : [ "Gabriel" , undefined ] , { _id : 4 , names : [ "Alice" , "Charu" ] } ] Learn More BSON Types $type $ifNull Back Comparison and Sort Order Next Extended JSON (v2)
