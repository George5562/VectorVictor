# Define Location Range for a 2d Index - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2d / Create Define Location Range for a 2d Index On this page About this Task Before You Begin Procedure Results Next Steps Learn More You can define the range of coordinates included in a 2d index . By default, 2d indexes have longitude and latitude
boundaries of: Greater than or equal to -180 Less than 180 To change the location range of a 2d index, specify the min and max options when you create the index: db. < collection > . createIndex ( { <location field>: "2d" }, { min: <lower bound>, max: <upper bound> } ) The min and max bounds are inclusive and apply to both
longitude and latitude. About this Task Important The default location bounds for 2d indexes allow latitudes less than
-90 and greater than 90, which are invalid values. The behavior of
geospatial queries with these invalid points is not defined. Defining a smaller location range for a 2d index reduces the amount of
data stored in the index, and can improve query performance. You cannot create a 2d index if your collection contains coordinate data
outside of the index's location range. After you create a 2d index, you cannot insert a document that contains
coordinate data outside of the index's location range. Before You Begin Create the contacts collection: db. contacts . insertMany ( [ { name : "Evander Otylia" , phone : "202-555-0193" , address : [ 55.5 , 42.3 ] } , { name : "Georgine Lestaw" , phone : "714-555-0107" , address : [ - 74 , 44.74 ] } ] ) The address field contains legacy coordinate pairs . Procedure Create a 2d index on the address field. Specify the following
location bounds: min bound of -75 max bound of 60 db. contacts . createIndex ( { address : "2d" } , { min : - 75 , max : 60 } ) Results The index covers a smaller location range and has increased performance
than a default 2d index. After you create the index, you cannot insert a document that contains
coordinate data outside of the index's location range. For example, you cannot insert the following document: db. contacts . insertOne ( { name : "Paige Polson" , phone : "402-555-0190" , address : [ 70 , 42.3 ] } ) The address field has a longitude value of 70 , which is higher
than the max bound of 60 . Next Steps You can use the 2d index to perform calculations on location data, such
as proximity queries . Learn More Define Location Precision for a 2d Index Geospatial Models Legacy Coordinate Pairs Back Location Precision Next Query
