# Create a Wildcard Index on All Fields - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Wildcard Create a Wildcard Index on All Fields On this page About this Task Before You Begin Procedure Results Learn More You can create a wildcard index that supports queries on all possible
document fields. Wildcard indexes support queries on arbitrary or
unknown field names. To create a wildcard index on all fields (excluding _id ), use the
wildcard specifier ( $** ) as the index key: db. < collection > . createIndex ( { "$**" : < sortOrder > } ) About this Task Only use wildcard indexes when the fields you want to index are unknown
or may change. Wildcard indexes don't perform as well as targeted
indexes on specific fields. If your collection contains arbitrary field
names that prevent targeted indexes, consider remodeling your schema to
have consistent field names. To learn more about targeted indexes, see Create Indexes to Support Your Queries . Before You Begin Create an artwork collection that contains the following documents: db. artwork . insertMany ( [ { "name" : "The Scream" , "artist" : "Edvard Munch" , "style" : "modern" , "themes" : [ "humanity" , "horror" ] } , { "name" : "Acrobats" , "artist" : { "name" : "Raoul Dufy" , "nationality" : "French" , "yearBorn" : 1877 } , "originalTitle" : "Les acrobates" , "dimensions" : [ 65 , 49 ] } , { "name" : "The Thinker" , "type" : "sculpture" , "materials" : [ "bronze" ] , "year" : 1904 } ] ) Each document contains details about the artwork. The field names vary
between documents depending on the information available about the
piece. Procedure The following operation creates a wildcard index on all document fields
in the artwork collection (excluding _id ): db. artwork . createIndex ( { "$**" : 1 } ) Results This index supports single-field queries on any field in the collection.
If a document contains an embedded document or array, the wildcard index
traverses the document or array and stores the value for all fields in
the document or array. For example, the index supports the following queries: Query: db. artwork . find ( { "style" : "modern" } ) Output: [ { _id : ObjectId ( "6352c401b1fac2ee2e957f09" ) , name : 'The Scream' , artist : 'Edvard Munch' , style : 'modern' , themes : [ 'humanity' , 'horror' ] } ] Query: db. artwork . find ( { "artist.nationality" : "French" } ) Output: [ { _id : ObjectId ( "6352c525b1fac2ee2e957f0d" ) , name : 'Acrobats' , artist : { name : 'Raoul Dufy' , nationality : 'French' , yearBorn : 1877 } , originalTitle : 'Les acrobates' , dimensions : [ 65 , 49 ] } ] Query: db. artwork . find ( { "materials" : "bronze" } ) Output: [ { _id : ObjectId ( "6352c387b1fac2ee2e957f08" ) , name : 'The Thinker' , type : 'sculpture' , materials : [ 'bronze' ] , year : 1904 } ] Learn More To learn how to create a wildcard index that projects specific fields to
cover, see the following pages: Filter Fields with a wildcardProjection Include or Exclude Fields in a Wildcard Index To learn more about behaviors for wildcard indexes, see: Wildcard Indexes on Embedded Objects and Arrays Wildcard Index Restrictions Back Include or Exclude Fields Next Compound
