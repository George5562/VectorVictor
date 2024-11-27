# Query a Capped Collection - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections / Capped Collections Query a Capped Collection On this page About this Task Multiple Concurrent Writes Before you Begin Create a capped collection Insert sample data Steps Return Documents in Insertion Order Return Most Recent Documents Learn More When you query a capped collection without specifying a sort order,
MongoDB returns results in the same order that they were inserted,
meaning the oldest documents are returned first. Use natural ordering to retrieve the most
recently inserted elements from the collection efficiently. This is
similar to using the tail command on a log file. About this Task Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index. Capped collections serialize write operations and therefore have worse
concurrent insert, update, and delete performance than non-capped
collections. Before you create a capped collection, consider if you
can use a TTL index instead. Multiple Concurrent Writes If there are concurrent writers to a capped collection, MongoDB does not
guarantee that documents are returned in insertion order. Before you Begin 1 Create a capped collection db. createCollection ( "log" , { capped : true , size : 100000 } ) 2 Insert sample data db. log . insertMany ( [ { message : "system start" , type : "startup" , time : 1711403508 } , { message : "user login attempt" , type : "info" , time : 1711403907 } , { message : "user login fail" , type : "warning" , time : 1711404209 } , { message : "user login success" , type : "info" , time : 1711404367 } , { message : "user logout" , type : "info" , time : 1711404555 } ] ) Steps The following examples show you how to: Return Documents in Insertion Order Return Most Recent Documents Return Documents in Insertion Order Query the log collection for documents where type is info ,
and use the default sort order: db. log . find ( { type : "info" } ) HIDE OUTPUT [ { _id : ObjectId ( "660204b74cabd75abebadbc2" ) , message : 'user login attempt' , type : 'info' , time : 1711403907 } , { _id : ObjectId ( "660204b74cabd75abebadbc4" ) , message : 'user login success' , type : 'info' , time : 1711404367 } , { _id : ObjectId ( "660204b74cabd75abebadbc5" ) , message : 'user logout' , type : 'info' , time : 1711404555 } ] Documents are returned in the order that they were inserted. Return Most Recent Documents To return documents in reverse insertion order (meaning the most recent
documents are first), specify the sort() method with
the $natural parameter set to -1 . The following query returns the three most recent documents from the log collection, starting with the most recent document: db. log . find ( ). sort ( { $natural : - 1 } ). limit ( 3 ) HIDE OUTPUT [ { _id : ObjectId ( "6601f2484cabd75abebadbbb" ) , message : 'user logout' , type : 'info' , time : 1711404555 } , { _id : ObjectId ( "6601f2484cabd75abebadbba" ) , message : 'user login success' , type : 'info' , time : 1711404367 } , { _id : ObjectId ( "6601f2484cabd75abebadbb9" ) , message : 'user login fail' , type : 'warning' , time : 1711404209 } ] Learn More TTL Indexes Query Optimization Create Indexes to Support Your Queries Back Create Next Verify
