# Define Location Precision for a 2d Index - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2d / Create Define Location Precision for a 2d Index On this page About this Task Before You Begin Procedure Next Steps Learn More In a 2d index, location precision is defined by the size in bits of the geohash values used to store the indexed data. By default, 2d
indexes use 26 bits of precision, which is equivalent to approximately
two feet (60 centimeters). Location precision affects performance for insert and read operations. To change the default precision, specify a bits value when you
create the 2d index. You can specify a bits value between 1 and 32,
inclusive. db. < collection > . createIndex ( { <location field>: "2d" }, { bits: <bit precision> } ) About this Task Location precision affects query performance: Lower precision improves performance for insert and update operations,
and uses less storage. Higher precision improves performance for read operations because
queries scan smaller portions of the index to return results. Location precision does not affect query accuracy. Grid coordinates are
always used in the final query processing. Before You Begin Create the contacts collection: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) The address field contains legacy coordinate pairs . Procedure Create a 2d index on the address field. Specify a location precision
of 32 bits: db. contacts . createIndex ( { address : "2d" } , { bits : 32 } ) Next Steps You can use the 2d index to perform calculations on location data, such
as proximity queries . Learn More Geohash Values Geospatial Models Legacy Coordinate Pairs Back Create Next Location Range
