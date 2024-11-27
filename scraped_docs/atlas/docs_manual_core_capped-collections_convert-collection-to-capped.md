# Convert a Collection to Capped - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections / Capped Collections Convert a Collection to Capped On this page About this Task Before you Begin Steps Convert the collection to a capped collection Confirm that the collection is capped Learn More To convert a non-capped collection to a capped collection , use the convertToCapped database command. The convertToCapped command holds a database-exclusive lock for the
duration of the operation. Other operations that lock the same database
are blocked until the convertToCapped operation completes. About this Task Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index. Capped collections serialize write operations and therefore have worse
concurrent insert, update, and delete performance than non-capped
collections. Before you create a capped collection, consider if you
can use a TTL index instead. Before you Begin Create a non-capped collection called log2 : db. createCollection ( "log2" ) Steps 1 Convert the collection to a capped collection To convert the log2 collection to a capped collection, run the convertToCapped command: db. runCommand ( { convertToCapped : "log2" , size : 100000 } ) The log2 collection has a maximum size of 100,000 bytes. 2 Confirm that the collection is capped To confirm that the log2 collection is now capped, use the isCapped() method: db. log2 . isCapped ( ) HIDE OUTPUT true Learn More Which administrative commands lock a database? Change the Size of a Capped Collection Query a Capped Collection Back Verify Next Change Size
