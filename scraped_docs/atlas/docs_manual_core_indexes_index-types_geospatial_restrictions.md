# Geospatial Index Restrictions - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial Geospatial Index Restrictions On this page Collation Option Covered Queries Shard Key Multiple Geospatial Indexes with $geoNear Supported Data Types Number of Index Keys Exact Matches on a Flat Surface Learn More 2d and 2dsphere indexes are
geospatial indexes. Geospatial indexes have these restrictions: Collation Option 2d indexes do not support the collation option, only
binary comparison. Binary comparison compares the numeric Unicode value
of each character in each string, and does not account for letter case
or accent marks. To create a 2d index on a collection that has a non-simple
collation, you must explicitly specify { collation: { locale: "simple"
} } when you create the index. For example, consider a collection named collationTest with a
collation of { locale: "en" } : db. createCollection ( "collationTest" , { collation : { locale : "en" } } ) To create a 2d index on the collationTest collection, you must
specify { collation: { locale: "simple" } } . This command creates a
2d index on the loc field: db. collationTest . createIndex ( { loc : "2d" } , { collation : { locale : "simple" } } ) Covered Queries Geospatial indexes cannot cover a query . Shard Key You cannot use a geospatial index as a shard key .
However, you can create a geospatial index on a sharded collection by
using a different field as the shard key. Multiple Geospatial Indexes with $geoNear If your collection has multiple geospatial indexes, when you run the $geoNear pipeline stage, you must specify the $geoNear key option. The key option specifies which index to use to
support the query. Supported Data Types A field indexed with a 2dsphere index must contain geometry data.
Geometry data can either be: GeoJSON data Legacy coordinate pairs You cannot: Insert a document with non-geometry data into a field that is indexed
with a 2dsphere index. Build a 2dsphere index on a field that contains non-geometry data. Number of Index Keys When you create a 2dsphere index, mongod maps GeoJSON shapes to an internal
representation. The resulting internal representation may be a large
array of values. The indexMaxNumGeneratedKeysPerDocument setting limits the
maximum number of keys generated for a single document to prevent out of
memory errors. If an operation requires more keys than the indexMaxNumGeneratedKeysPerDocument parameter specifies, the
operation fails. By default, the server allows up to 100,000 index keys per document.
To allow more index keys, raise the indexMaxNumGeneratedKeysPerDocument value. Exact Matches on a Flat Surface A 2d index cannot improve performance for exact matches on a coordinate
pair. For example, consider a contacts collection with these documents: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) A 2d index on the address field does not improve performance for
the following query: db. contacts . find ( { address : [ 55.5 , 42.3 ] } ) To improve performance for this query, create either an ascending or
descending index on the address field: db. contacts . createIndex ( { address : 1 } ) Learn More 2d Index Internals Index Properties Back Calculate to Radians Next Hashed
