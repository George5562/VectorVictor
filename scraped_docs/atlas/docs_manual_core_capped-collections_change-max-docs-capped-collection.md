# Change Maximum Documents in a Capped Collection - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections / Capped Collections Change Maximum Documents in a Capped Collection On this page About this Task Before you Begin Steps Learn More New in version 6.0 . To change the maximum number of documents in a capped collection , use the collMod command's cappedMax option. If cappedMax is less than or equal to 0 , there is no maximum
document limit. If cappedMax is less than the current number of documents in the
collection, MongoDB removes the excess documents on the next insert
operation. About this Task Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index. Capped collections serialize write operations and therefore have worse
concurrent insert, update, and delete performance than non-capped
collections. Before you create a capped collection, consider if you
can use a TTL index instead. Before you Begin Create a capped collection called log that can store a maximum of
20,000 documents: db. createCollection ( "log" , { capped : true , size : 5242880 , max : 20000 } ) Steps Run the following command to set the maximum number of documents in the log collection to 5,000: db. runCommand ( { collMod : "log" , cappedMax : 5000 } ) Learn More Change the Size of a Capped Collection Check if a Collection is Capped Query a Capped Collection Back Change Size Next Clustered Collections
