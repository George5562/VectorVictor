# Iterate a Cursor in mongosh - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations / Query Iterate a Cursor in mongosh On this page Manually Iterate the Cursor Iterator Index Cursor Behaviors Cursor Information The db.collection.find() method returns a cursor. To access
the documents, you need to iterate the cursor. However, in mongosh , if the returned cursor is not assigned to a
variable using the var keyword, then the cursor is automatically
iterated up to 20 times [ 1 ] to print up to the
first 20 documents in the results. The following examples describe ways to manually iterate the cursor to
access the documents or to use the iterator index. Manually Iterate the Cursor In mongosh , when you assign the cursor returned from
the find() method to a variable using
the var keyword, the cursor does not automatically iterate. You can call the cursor variable in the shell to iterate up to 20 times [ 1 ] and print the matching documents, as in the
following example: var myCursor = db. users . find ( { type : 2 } ) ; myCursor You can also use the cursor method next() to
access the documents, as in the following example: var myCursor = db. users . find ( { type : 2 } ) ; while ( myCursor. hasNext ( )) { print ( tojson ( myCursor. next ( ))) ; } As an alternative print operation, consider the printjson() helper
method to replace print(tojson()) : var myCursor = db. users . find ( { type : 2 } ) ; while ( myCursor. hasNext ( )) { printjson ( myCursor. next ( )) ; } You can use the cursor method forEach() to
iterate the cursor and access the documents, as in the following
example: var myCursor = db. users . find ( { type : 2 } ) ; myCursor. forEach ( printjson) ; See JavaScript cursor methods and your driver documentation for more
information on cursor methods. [ 1 ] ( 1 , 2 ) You can set the DBQuery.shellBatchSize attribute to change the number of documents from the default value of 20 . Iterator Index In mongosh , you can use the toArray() method to iterate the cursor and return
the documents in an array, as in the following: var myCursor = db. inventory . find ( { type : 2 } ) ; var documentArray = myCursor. toArray ( ) ; var myDocument = documentArray [ 3 ] ; The toArray() method loads into RAM all
documents returned by the cursor; the toArray() method exhausts the cursor. Additionally, some Drivers provide
access to the documents by using an index on the cursor (i.e. cursor[index] ). This is a shortcut for first calling the toArray() method and then using an index
on the resulting array. Consider the following example: var myCursor = db. users . find ( { type : 2 } ) ; var myDocument = myCursor [ 1 ] ; The myCursor[1] is equivalent to the following example: myCursor. toArray ( ) [ 1 ] ; Cursor Behaviors Cursors Opened Within a Session Starting in MongoDB 5.0, cursors created within a client session close
when the corresponding server session ends with the killSessions command, if the session times
out, or if the client has exhausted the cursor. By default, server sessions have an expiration timeout of 30 minutes. To
change the value, set the localLogicalSessionTimeoutMinutes parameter when starting up mongod . Cursors Opened Outside of a Session Cursors that aren't opened under a session automatically close after 10
minutes of inactivity, or if client has exhausted the cursor. To
override this behavior in mongosh , you can use the cursor.noCursorTimeout() method: var myCursor = db. users . find ( ). noCursorTimeout ( ) ; After setting the noCursorTimeout option, you must either close the cursor
manually with cursor.close() or by exhausting the cursor's results. See your driver documentation for
information on setting the noCursorTimeout option. Cursor Isolation As a cursor returns documents, other operations may interleave with the
query. Cursor Batches The MongoDB server returns the query results in batches. The amount of
data in the batch will not exceed the maximum BSON document size . To override the default size of
the batch, see batchSize() and limit() . Operations of type find() , aggregate() , listIndexes , and listCollections return a maximum of 16 megabytes
per batch. batchSize() can enforce a smaller
limit, but not a larger one. find() and aggregate() operations have an initial batch size
of 101 documents by default. Subsequent getMore operations issued against the resulting cursor have no default batch
size, so they are limited only by the 16 megabyte message size. For queries that include a sort operation without an index, the
server must load all the documents in memory to perform the sort
before returning any results. As you iterate through the cursor and reach the end of the returned
batch, if there are more results, cursor.next() will perform
a getMore operation to retrieve the next batch.
To see how many documents remain in the batch as you iterate the
cursor, you can use the objsLeftInBatch() method, as
in the following example: var myCursor = db. inventory . find ( ) ; var myFirstDocument = myCursor. hasNext ( ) ? myCursor. next ( ) : null ; myCursor. objsLeftInBatch ( ) ; Cursor Results for Non-Existent mongos Databases Starting in MongoDB 7.2, aggregation pipeline queries that attempt to
use non-existent databases on mongos deployments return
validation errors. In previous versions, these aggregation queries return empty cursors. Cursor Information The db.serverStatus() method returns a document that includes
a metrics field. The metrics field contains a metrics.cursor field with the following
information: number of timed out cursors since the last server restart number of open cursors with the option DBQuery.Option.noTimeout set to prevent timeout after a
period of inactivity number of "pinned" open cursors total number of open cursors Consider the following example which calls the db.serverStatus() method and accesses the metrics field
from the results and then the cursor field from the metrics field: db. serverStatus ( ). metrics . cursor The result is the following document: { "timedOut" : < number > "open" : { "noTimeout" : < number > , "pinned" : < number > , "total" : < number > } } Tip See also: db.serverStatus() Back Long-Running Snapshots Next Update
