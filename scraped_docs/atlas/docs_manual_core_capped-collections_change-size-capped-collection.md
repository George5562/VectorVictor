# Change the Size of a Capped Collection - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections / Capped Collections Change the Size of a Capped Collection On this page About this Task Before you Begin Steps Learn More New in version 6.0 . To change the size of a capped collection , use the collMod command's cappedSize option. cappedSize is specified in bytes, and must be
greater than 0 and less than or equal to 1024^5 (1 PB ). If cappedSize is less than the current size of the collection,
MongoDB removes the excess documents on the next insert operation. About this Task Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index. Capped collections serialize write operations and therefore have worse
concurrent insert, update, and delete performance than non-capped
collections. Before you create a capped collection, consider if you
can use a TTL index instead. Before you Begin Create a capped collection called log that has a maximum size of
2,621,440 bytes: db. createCollection ( "log" , { capped : true , size : 2621440 } ) Steps Run the following command to set the maximum size of the log collection to 5,242,880 bytes: db. runCommand ( { collMod : "log" , cappedSize : 5242880 } ) Learn More Change Maximum Documents in a Capped Collection Check if a Collection is Capped Query a Capped Collection Back Convert Next Change Limits
