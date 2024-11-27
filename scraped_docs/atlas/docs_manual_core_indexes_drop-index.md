# Drop an Index - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes Drop an Index On this page About this Task Before You Begin Procedures Drop a Single Index Drop Multiple Indexes Drop All Indexes Except the _id Index Results Learn More You can remove a specific index from a collection. You may need to drop
an index if you see a negative performance impact, want to replace it
with a new index, or no longer need the index. To drop an index, use one of the following shell methods: Method Description db.collection.dropIndex() Drops a specific index from the collection. db.collection.dropIndexes() Drops all removable indexes from the collection or an array of
indexes, if specified. About this Task You can drop any index except the default index on the _id field.
To drop the _id index, you must drop the entire collection. If you drop an index that's actively used in production, you
may experience performance degradation. Before you drop an index,
consider hiding the index to evaluate
the potential impact of the drop. Before You Begin To drop an index, you need its name. To get all index names for a
collection, run the getIndexes() method: db. < collection > . getIndexes ( ) Procedures After you identify which indexes to drop, use one of the following drop
methods for the specified collection: Drop a Single Index To drop a specific index, use the dropIndex() method and specify the index name: db. < collection > . dropIndex ( "<indexName>" ) Drop Multiple Indexes To drop multiple indexes, use the dropIndexes() method and specify an array of index names: db. < collection > . dropIndexes ( [ "<index1>" , "<index2>" , "<index3>" ] ) Drop All Indexes Except the _id Index To drop all indexes except the _id index, use
the dropIndexes() method: db. < collection > . dropIndexes ( ) Results After you drop an index, the system returns information about
the status of the operation. Example output: ... { "nIndexesWas" : 3 , "ok" : 1 } ... The value of nIndexesWas reflects the number of indexes before
removing an index. To confirm that the index was dropped, run the db.collection.getIndexes() method: db. < collection > . getIndexes ( ) The dropped index no longer appears in the getIndexes() output. Learn More To learn more about managing your existing indexes, see Manage Indexes . To learn how to remove an index in MongoDB Compass , see Manage Indexes in Compass . Back Specify a Name Next Types
