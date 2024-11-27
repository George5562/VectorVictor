# Query for Locations Near a Point on a Flat Surface - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2d / Query Query for Locations Near a Point on a Flat Surface On this page About this Task Before you Begin Procedure Learn More You can query for location data that appears near a specified point on a
flat surface. To query for location data near a specified point, use the $near operator: db. < collection > . find ( { <location field> : { $near : [ <longitude>, <latitude> ], $maxDistance : <distance in meters> } } ) About this Task When specifying coordinate pairs in the $near operator, list the longitude first, and then latitude . Valid longitude values are between -180 and 180 , both
inclusive. Valid latitude values are between -90 and 90 , both
inclusive. Specify distance in the $maxDistance field in meters . Before you Begin Create the contacts collection: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) The address field contains legacy coordinate pairs . To query for location data with the $near operator, you must create
a geospatial index on the field that contains
the location data. Create a 2d index on the address field: db. contacts . createIndex ( { address : "2d" } ) Procedure Use $near to query the collection. The following $near query
returns documents that have an address field within 50 meters of the
coordinate pair [ -73.92, 40.78 ] : db. contacts . find ( { address : { $near : [ - 73.92 , 40.78 ] , $maxDistance : 50 } } ) Output: [ { _id : ObjectId ( "640a3dd9c639b6f094b00e89" ) , name : 'Georgine Lestaw' , phone : '714-555-0107' , address : [ - 74 , 44.74 ] } ] Results are sorted by distance from the queried point, from nearest to
farthest. Learn More $near $geoNear Geospatial Index Restrictions To perform proximity queries on a spherical surface, see Query for Locations Near a Point on a Sphere . Back Query Next Shape on a Surface
