# $meta - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $meta On this page Definition Behavior Examples Definition $meta Returns the metadata associated with a document, e.g. "textScore" when performing text search. A $meta expression has the following syntax: { $meta : < metaDataKeyword > } The $meta expression can specify the following values as the <metaDataKeyword> : Keyword Description "textScore" Returns the score associated with the corresponding $text query for each matching document. The text score
signifies how well the document matched the search term or
terms . { $meta: "textScore" } must be used in conjunction with a $text query. In earlier versions, if not used in conjunction with a $text query, returns a score of null . $text provides text query capabilities for self-managed (non-Atlas)
deployments. For data hosted on MongoDB Atlas, MongoDB offers an improved
full-text query solution, Atlas Search . "indexKey" Returns an index key for the document if a non- text index is used. The { $meta: "indexKey" } expression is for debugging purposes only, and not for
application logic, and is preferred over cursor.returnKey() . MongoDB Atlas Search provides
additional $meta keywords, such as: "searchScore" "searchHighlights" "searchSequenceToken" Refer to the Atlas Search documentation for details. Important The following $meta keywords are not supported in Stable API V1: "textScore" "indexKey" "searchScore" "searchHighlights" Behavior Text Score Metadata $meta: "textScore" Requires $text Search The { $meta: "textScore" } expression must be used in
conjunction with $text . For example: In aggregation, you must specify a $match stage
with a $text query in the pipeline to use the {
$meta: "textScore" } expression in later stage(s). If you
do not specify the $text query in the $match stage, the operation fails. In find, you must specify the $text operator in the
query predicate to use { $meta: "textScore" } . If you do not specify
the $text operator in the query predicate, the operation fails. Note $text provides text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search . Availability In aggregation, the { $meta: "textScore" } expression can
be included in various stages that accept aggregation
expressions, such as $project , $group $sort , etc. In find, the { $meta: "textScore" } expression can be
included in projection and in sort() . Usage In Projection The { $meta: "textScore" } expression can be a part of the projection document to include the text score metadata. The $meta expression can be present in either an
inclusion or an exclusion projection. If you set the expression to a field name that already exists
in the document, the projected metadata value overwrites the
existing value. Filter on Text Score In aggregation, following a stage that outputs a field with
the text score value, you can specify a query condition or
operate on the field in subsequent stages. For example, see $text in the Aggregation Pipeline on Self-Managed Deployments . In find, you cannot specify a query condition on the text
score. Use aggregation instead. Usage In Sort The { $meta: "textScore" } expression can be used as a
part of a sort operation to sort by the text score metadata;
i.e., In aggregation, $sort stage. In find, sort() method. The "textScore" metadata sorts in descending order. To use in a sort operation, set the { $meta: "textScore" } expression to an arbitrary field name. The field name is
disregarded by the query system. Sort without Projection In aggregation, you can sort the resulting documents by {
$meta: "textScore" } without also having to project the textScore . In find, you can sort the resulting documents by { $meta: "textScore" } without also having to project the textScore . Sort with Projection In aggregation, if you include the { $meta: "textScore" } expression in both the projection and sort, the
projection and sort can have different field names for the
expression. The field name in the sort is disregarded by the query
system. In find, if you include the { $meta: "textScore" } expression in both the projection and sort, the projection and sort can have
different field names for the expression. The field name in the
sort is disregarded by the query system. Index Key Metadata $meta: "indexKey" (Aggregation and Find) Usage The { $meta: "indexKey" } expression is for debugging purposes
only and not for application logic. The { $meta: "indexKey" } expression is preferred over cursor.returnKey() . Availability In aggregation , the { $meta: "indexKey" } expression can
be included in various stages that accept aggregation
expressions, such as $project , $group $sortByCount , etc., but not $sort .
However, with an aggregation pipeline, you can first project
the { $meta: "indexKey" } expression (such as in a $project , $addFields , etc. ) and then,
sort by that field in a subsequent $sort stage. In find , the { $meta: "indexKey" } expression is only
available as part of the projection document. Return Value The value returned depends on how the database decides to
represent values in an index and may change across versions. The
represented value may not be the actual value for the field. The value returned depends on the execution plan chosen by the
system. For example, if there are two possible indexes which can
be used to answer the query, then the value of the "indexKey"
metadata depends on which index is selected. If an index is not used, the { $meta: "indexKey" } expression does not return a value and the field is not included
as part of the output. Examples $meta: "textScore" Create an articles collection with the following documents: db. articles . insertMany ( [ { "_id" : 1 , "title" : "cakes and ale" } , { "_id" : 2 , "title" : "more cakes" } , { "_id" : 3 , "title" : "bread" } , { "_id" : 4 , "title" : "some cakes" } , { "_id" : 5 , "title" : "two cakes to go" } , { "_id" : 6 , "title" : "pie" } ]) Create a text index on the title field: db. articles . createIndex ( { title : "text" } ) Aggregation Find and Project The following aggregation operation performs a text search and uses the $meta operator to group by the text search score: db. articles . aggregate ( [ { $match : { $text : { $search : "cake" } } } , { $group : { _id : { $meta : "textScore" } , count : { $sum : 1 } } } ] ) The operation returns the following results: { "_id" : 0.75 , "count" : 1 } { "_id" : 0.6666666666666666 , "count" : 1 } { "_id" : 1 , "count" : 2 } For more examples, see $text in the Aggregation Pipeline on Self-Managed Deployments . The following query performs a text search for the term cake and
uses the $meta operator in the projection document to
include the score assigned to each matching document: db. articles . find ( { $text : { $search : "cake" } } , { score : { $meta : "textScore" } } ) The operation returns the following documents with the text score: { "_id" : 4 , "title" : "some cakes" , "score" : 1 } { "_id" : 1 , "title" : "cakes and ale" , "score" : 0.75 } { "_id" : 5 , "title" : "two cakes to go" , "score" : 0.6666666666666666 } { "_id" : 2 , "title" : "more cakes" , "score" : 1 } For additional examples of "textScore" projections and sorts,
see Relevance Score Examples . $meta: "indexKey" Note The { $meta: "indexKey" } expression is for debugging
purposes only and not for application logic. MongoDB returns the
value associated with the index chosen by the query system. The
system can choose a different index upon subsequent execution. For the selected index, the value returned depends on how the
database decides to represent values in an index and may change
across versions. The represented value may not be the actual
value for the field. Create an orders collection with the following documents: db. orders . insertMany ( [ { "item" : "abc" , "price" : NumberDecimal ( "12" ) , "quantity" : 2 , "type" : "apparel" } , { "item" : "jkl" , "price" : NumberDecimal ( "20" ) , "quantity" : 1 , "type" : "electronics" } , { "item" : "abc" , "price" : NumberDecimal ( "10" ) , "quantity" : 5 , "type" : "apparel" } ]) Create the following compound index on the type and item fields: db. orders . createIndex ( { type : 1 , item : 1 } ) Aggregation Find and Project The following aggregation operation finds all documents with type equal to apparel and uses the $meta operator to
include the index key value for the matching document if an index was
used: db. orders . aggregate ( [ { $match : { type : "apparel" } } , { $addFields : { idxKey : { $meta : "indexKey" } } } ] ) The following operation finds all documents with type equal to apparel and uses the $meta operator to
include the index key value for the matching document if an index was
used: db. orders . find ( { type : "apparel" } , { idxKey : { $meta : "indexKey" } } ) The operation returns the matching documents with their
corresponding index key: { "_id" : ObjectId ( "5e98a33ceaf5e9dcf2b8dcde" ) , "item" : "abc" , "price" : NumberDecimal ( "12" ) , "quantity" : 2 , "type" : "apparel" , "idxKey" : { "type" : "apparel" , "item" : "abc" } } { "_id" : ObjectId ( "5e98a33ceaf5e9dcf2b8dce0" ) , "item" : "abc" , "price" : NumberDecimal ( "10" ) , "quantity" : 5 , "type" : "apparel" , "idxKey" : { "type" : "apparel" , "item" : "abc" } } If no index is used, the { $meta: "indexKey" } does not
return anything. Aggregation Find and Project For example, the following operation does not use
an index since no index exists on the price field to support the
match condition: db. orders . aggregate ( [ { $match : { price : { $gte : NumberDecimal ( "10" ) } } } , { $addFields : { idxKey : { $meta : "indexKey" } } } ] ) For example, the following operation does not use an index
since no index exists on the price field to support the
match condition: db. orders . find ( { price : { $gte : NumberDecimal ( "10" ) } } , { idxKey : { $meta : "indexKey" } } ) The operation returns the matching documents without the idxKey field: { "_id" : ObjectId ( "5e98a33ceaf5e9dcf2b8dcde" ) , "item" : "abc" , "price" : NumberDecimal ( "12" ) , "quantity" : 2 , "type" : "apparel" } { "_id" : ObjectId ( "5e98a33ceaf5e9dcf2b8dcdf" ) , "item" : "jkl" , "price" : NumberDecimal ( "20" ) , "quantity" : 1 , "type" : "electronics" } { "_id" : ObjectId ( "5e98a33ceaf5e9dcf2b8dce0" ) , "item" : "abc" , "price" : NumberDecimal ( "10" ) , "quantity" : 5 , "type" : "apparel" } Back $mergeObjects Next $min
