# Create a 2d Index - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2d Create a 2d Index On this page About this Task Before You Begin Procedure Next Steps Learn More 2d indexes support queries on location data in a flat, Euclidean
plane . To create a 2d index, use the db.collection.createIndex() method. The index type is "2d" : db. < collection > . createIndex ( { < location field > : "2d" } ) About this Task The values in the <location field> must be legacy coordinate
pairs . When specifying legacy coordinate pairs, list the longitude first,
and then latitude . Valid longitude values are between -180 and 180 , both
inclusive. Valid latitude values are between -90 and 90 , both
inclusive. Before You Begin Create the contacts collection: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) The address field contains legacy coordinate pairs . Procedure Create a 2d index on the address field: db. contacts . createIndex ( { address : "2d" } ) Next Steps After you create a 2d index, you can use your 2d index to support
calculations on location data. To see examples of queries that use 2d
indexes, see: Query for Locations Near a Point on a Flat Surface Learn More Define Location Precision for a 2d Index Define Location Range for a 2d Index Geospatial Index Restrictions To create an index that supports calculations on spherical surfaces,
see 2dsphere Indexes . Back 2d Next Location Precision
