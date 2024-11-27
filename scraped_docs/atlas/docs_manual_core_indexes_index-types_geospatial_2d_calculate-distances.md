# Convert Distance to Radians for Spherical Operators - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2d Convert Distance to Radians for Spherical Operators On this page About this Task Procedure Examples Convert Miles to Radians Convert Kilometers to Radians 2d indexes support certain query operators that calculate distances
using spherical geometry. Spherical query operators use radians for
distance. To use spherical query operators with a 2d index, you must
convert distances to radians. 2d indexes support the following spherical query operators: $centerSphere $geoNear pipeline stage with the spherical: true option $near $nearSphere About this Task Using a 2d index for queries on spherical data can return incorrect
results or an error. For example, 2d indexes don't support spherical
queries that wrap around the poles. If your data is stored as longitude and latitude and you often run
queries on spherical surfaces, use a 2dsphere index instead of a 2d index. When you specify longitude and latitude coordinates, list the longitude first, and then latitude . Valid longitude values are between -180 and 180 , both
inclusive. Valid latitude values are between -90 and 90 , both
inclusive. Procedure To convert distance to radians, divide the distance by the radius of the
sphere (for example, the Earth) in the same units as the distance
measurement. The equatorial radius of Earth is approximately 3,963.2 miles or 6,378.1
kilometers. Examples The following examples use the $centerSphere operator to
perform queries. The $centerSphere operator uses radians to
calculate distance. Create the contacts collection: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) The address field contains legacy coordinate pairs . Convert Miles to Radians The following query returns documents where the address field is
within a circle with center point [ -72, 44 ] and a radius of 200
miles: db. contacts . find ( { address : { $geoWithin : { $centerSphere : [ [ - 72 , 44 ] , 200 / 3963.2 ] } } } ) Output: [ { _id : ObjectId ( "647e565c6cdaf4dc323ec92d" ) , name : 'Georgine Lestaw' , phone : '714-555-0107' , address : [ - 74 , 44.74 ] } ] In the preceding query, to convert 200 miles to radians, the specified
miles were divided by 3963.2. Convert Kilometers to Radians The following query returns documents where the address field is
within a circle with center point [ 55, 42 ] and a radius of 500
kilometers: db. contacts . find ( { address : { $geoWithin : { $centerSphere : [ [ 55 , 42 ] , 500 / 6378.1 ] } } } ) Output: [ { _id : ObjectId ( "647e565c6cdaf4dc323ec92c" ) , name : 'Evander Otylia' , phone : '202-555-0193' , address : [ 55.5 , 42.3 ] } ] In the preceding query, to convert 500 kilometers to radians, the
specified kilometers were divided by 6378.1. Back Internals Next Restrictions
