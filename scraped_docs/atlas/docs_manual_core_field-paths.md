# Field Paths - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Aggregation Pipeline Field Paths On this page Use Cases Learn More You can use field path expressions to access
fields in input documents. To specify a field path, prefix the field
name or the dotted field path (if the
field is in an embedded document) with a dollar sign $ . Use Cases You can use field paths for the following use cases: Nested Fields Array of Nested Fields Array of Nested Arrays Nested Fields The following example uses the planets collection from the Atlas Sample Databases . Each document in
this collection has the following structure: { _id : new ObjectId ( "6220f6b78a733c51b416c80e" ) , name : "Uranus" , orderFromSun : 7 , hasRings : true , mainAtmosphere : [ "H2" , "He" , "CH4" ] , surfaceTemperatureC : { min : null , max : null , mean : - 197.2 } } To specify the nested field mean within the surfaceTemperatureC field, use dot notation ( "field.nestedField" ) with a dollar
sign $ . The following aggregation pipeline projects only the mean nested field value for each document: db. planets . aggregate ( [ { $project : { nested_field : "$surfaceTemperatureC.mean" } } ] ) Below is an example returned document: { _id : ObjectId ( '6220f6b78a733c51b416c80e' ) , nested_field : - 197.2 } Array of Nested Fields You can use dot notation in a field path to access a field that
is nested within an array. For example, consider a products collection that contains an instock field. The instock field contains an array of nested warehouse fields. db. products . insertMany ( [ { item : "journal" , instock : [ { warehouse : "A" } , { warehouse : "C" } ] } , { item : "notebook" , instock : [ { warehouse : "C" } ] } , { item : "paper" , instock : [ { warehouse : "A" } , { warehouse : "B" } ] } , { item : "planner" , instock : [ { warehouse : "A" } , { warehouse : "B" } ] } , { item : "postcard" , instock : [ { warehouse : "B" } , { warehouse : "C" } ] } ] ) The following aggregation pipeline uses $instock.warehouse to access
the nested warehouse fields. db. products . aggregate ( [ { $project : { item : 1 , warehouses : "$instock.warehouse" } } ] ) In this example, $instock.warehouse outputs an array of values that
are in the nested warehouse field for each document. The pipeline
returns the following documents: [ { _id : ObjectId ( '6740b55e33b29cf6b1d884f7' ) , item : "journal" , warehouses : [ "A" , "C" ] } , { _id : ObjectId ( '6740b55e33b29cf6b1d884f8' ) , item : "notebook" , warehouses : [ "C" ] } , { _id : ObjectId ( '6740b55e33b29cf6b1d884f9' ) , item : "paper" , warehouses : [ "A" , "B" ] } , { _id : ObjectId ( '6740b55e33b29cf6b1d884fa' ) , item : "planner" , warehouses : [ "A" , "B" ] } , { _id : ObjectId ( '6740b55e33b29cf6b1d884fb' ) , item : "postcard" , warehouses : [ "B" , "C" ] } ] Array of Nested Arrays You can also use dot notation with a dollar sign $ in a
field path to access an array within a nested array. This example uses a fruits collection that contains the
following document: db. fruits . insertOne ( { _id : ObjectId ( "5ba53172ce6fa2fcfc58e0ac" ) , inventory : [ { apples : [ "macintosh" , "golden delicious" , ] } , { oranges : [ "mandarin" , ] } , { apples : [ "braeburn" , "honeycrisp" , ] } ] } ) The document in the collection contains an inventory array where
each element in the array is an object that contains a nested array
field. Consider the following aggregation pipeline: db. fruits . aggregate ( [ { $project : { all_apples : "$inventory.apples" } } ] ) In this pipeline, $inventory.apples resolves to an array of nested
arrays. The pipeline returns the following document: { _id : ObjectId ( '5ba53172ce6fa2fcfc58e0ac' ) , all_apples : [ [ "macintosh" , "golden delicious" ] , [ "braeburn" , "honeycrisp" ] ] } Learn More For more information on accessing and interacting with nested elements,
see Dot Notation and Query an Array of Embedded Documents . Back Aggregation Pipeline Next Optimization