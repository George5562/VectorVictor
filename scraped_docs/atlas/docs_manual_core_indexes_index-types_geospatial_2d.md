# 2d Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial 2d Indexes On this page Use Cases Get Started Details Supported Calculations Compound 2d Indexes sparse Property Learn More 2d indexes support queries on data stored as points on a two-dimensional plane . The 2d index is
intended for queries on legacy coordinate pairs . To create a 2d index, specify the string 2d as the index
type: db. < collection > . createIndex ( { < location field > : "2d" } ) You cannot use 2d indexes for queries on GeoJSON objects. To
enable queries on GeoJSON objects, use 2dsphere indexes . Note When creating a 2d index , the first value (longitude) must
be between -180 and 180, inclusive. The second value (latitude) must be between
-90 and 90, inclusive. However, these default limits can be overridden with the min and max options on 2d indexes . Unlike 2dsphere index coordinates, 2d indexes values do
not "wrap" around a sphere. Use Cases Use a 2d index to query and perform calculation on data represented
within a two-dimensional plane. For example: An application analyzing visual similarities between two art pieces. A calculator that can perform calculations on two-dimensional graphs. A mobile game that calculates distances between players on a
two-dimensional map. Get Started To learn how to create and query 2d indexes, see: Create a 2d Index Query for Locations Near a Point on a Flat Surface Query for Locations within a Shape on a Flat Surface Details Supported Calculations 2d indexes support calculations on a flat, Euclidean plane . For spherical geometry calculations, store your data as as GeoJSON objects and use a 2dsphere index
to support geospatial queries. Compound 2d Indexes You can create compound 2d indexes that reference two fields: The first field must be the location field. The index constructs
queries that first select on this field. The second field further filters results based on additional
criteria. A compound 2d index can cover queries. sparse Property 2d indexes are always sparse and
ignore the sparse option. If a
document lacks a 2d index field (or the field is null or an
empty array), MongoDB does not add an entry for the document to the
2d index. For inserts, MongoDB inserts the document but does not
add to the 2d index. For a compound index that includes a 2d index key along with keys
of other types, only the 2d index field determines whether the
index references a document. Learn More Geospatial Queries Query a 2dsphere Index Geospatial Index Restrictions Back Versions Next Create
