# Query for Locations Bound by a Polygon - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2dsphere / Query Query for Locations Bound by a Polygon On this page About this Task Before You Begin Procedure Learn More You can query for location data within the perimeter of a specified
polygon. To query for location data within a perimeter, use the $geoWithin operator and specify the coordinates of the
polygon's vertices: db. < collection > . find ( { <location field> : { $geoWithin : { $geometry : { type : "Polygon", coordinates : [ <coordinates> ] } } } } ) About this Task The values in the field you query with the $geoWithin operator
must be in GeoJSON format. When you specify longitude and latitude coordinates, list the longitude first, and then latitude . Valid longitude values are between -180 and 180 , both
inclusive. Valid latitude values are between -90 and 90 , both
inclusive. When you specify Polygon coordinates , the first and last
coordinates in the array must be the same. This closes the bounds of
the polygon. $geoWithin does not require a geospatial index. However, a
geospatial index improves query performance. Only the 2dsphere geospatial index supports $geoWithin . For
more information see Create a 2dsphere Index . Before You Begin Create a places collection that contains these documents: db. places . insertMany ( [ { loc : { type : "Point" , coordinates : [ - 73.97 , 40.77 ] } , name : "Central Park" , category : "Park" } , { loc : { type : "Point" , coordinates : [ - 73.88 , 40.78 ] } , name : "La Guardia Airport" , category : "Airport" } , { loc : { type : "Point" , coordinates : [ - 1.83 , 51.18 ] } , name : "Stonehenge" , category : "Monument" } ] ) Procedure Use $geoWithin to query the collection. The following $geoWithin query specifies a polygon with four vertices (a rectangle) and returns
points within that polygon: db. places . find ( { loc : { $geoWithin : { $geometry : { type : "Polygon" , coordinates : [ [ [ - 73.95 , 40.80 ] , [ - 73.94 , 40.79 ] , [ - 73.97 , 40.76 ] , [ - 73.98 , 40.76 ] , [ - 73.95 , 40.80 ] ] ] } } } } ) Output: [ { _id : ObjectId ( "63a4a8d67348ebdcd0a061f0" ) , loc : { type : 'Point' , coordinates : [ - 73.97 , 40.77 ] } , name : 'Central Park' , category : 'Park' } ] Learn More $geoWithin Polygon Geospatial Index Restrictions Back Query Next Spheres
