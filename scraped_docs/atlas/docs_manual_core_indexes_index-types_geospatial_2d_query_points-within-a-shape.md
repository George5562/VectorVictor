# Query for Locations within a Shape on a Flat Surface - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2d / Query Query for Locations within a Shape on a Flat Surface On this page About this Task Before You Begin Procedure Learn More To query for location data within a specified shape on a flat surface,
use the $geoWithin operator. To use $geoWithin with data
that appears on a flat surface, use this syntax: db. < collection > . find ( { <location field> : { $geoWithin : { <shape operator> : <coordinates> } } } ) Replace these values for your query: Field Description <collection> The collection to query. <location field> The field that contains your location data. For queries on a
flat surface, your data must be stored as legacy
coordinate pairs . <shape operator> The shape to query within. You can specify one of the following
shapes: $box $polygon $center (defines a circle) The example on this page uses the $box operator. To see examples
of queries using other shapes, refer to those operator pages. <coordinates> The coordinates that define the edges of the shape to query
within. When used with the $box operator, the coordinates
represent the bottom-left and top-right corners of a rectangle. When you specify longitude and latitude coordinates, list the longitude first, and then latitude . Valid longitude values are between -180 and 180 , both
inclusive. Valid latitude values are between -90 and 90 , both
inclusive. About this Task $geoWithin does not require a geospatial index. However, a
geospatial index improves query performance. Before You Begin Create the contacts collection: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) The address field contains legacy coordinate pairs . Procedure Use $geoWithin to query the contacts collection. The following $geoWithin query uses the $box operator to return documents
that appear within a specified rectangle: db. contacts . find ( { address : { $geoWithin : { $box : [ [ 49 , 40 ] , [ 60 , 60 ] ] } } } ) Output: [ { _id : ObjectId ( "647e4e496cdaf4dc323ec92a" ) , name : 'Evander Otylia' , phone : '202-555-0193' , address : [ 55.5 , 42.3 ] } ] The values of the $box operator represent the bottom-left and
top-right corners of of the rectangle to query within. The $geoWithin query shown earlier returns documents that are within
a rectangle that has these vertices: [ 49, 40 ] [ 49, 60 ] [ 60, 60 ] [ 60, 40 ] Learn More To learn how to use the $geoWithin operator with other shapes, see
these pages: To query within a polygon, see $polygon . To query within a circle, see $center . Back Point on a Surface Next Internals
