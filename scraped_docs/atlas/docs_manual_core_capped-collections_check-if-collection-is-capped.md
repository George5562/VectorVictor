# Check if a Collection is Capped - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections / Capped Collections Check if a Collection is Capped On this page About this Task Before you Begin Steps Learn More To check if a collection is capped, use the isCapped() method. About this Task Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index. Capped collections serialize write operations and therefore have worse
concurrent insert, update, and delete performance than non-capped
collections. Before you create a capped collection, consider if you
can use a TTL index instead. Before you Begin Create a non-capped collection and a capped collection: db. createCollection ( "nonCappedCollection1" ) db. createCollection ( "cappedCollection1" , { capped : true , size : 100000 } ) Steps To check if the collections are capped, use the isCapped() method: db. nonCappedCollection1 . isCapped ( ) db. cappedCollection1 . isCapped ( ) HIDE OUTPUT false true Learn More Create a Capped Collection Convert a Collection to Capped $collStats Back Query Next Convert
