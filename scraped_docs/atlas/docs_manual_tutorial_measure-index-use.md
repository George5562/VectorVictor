# Measure Index Use - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes Measure Index Use On this page Get Index Access Information with $indexStats Return Query Plan with explain() Control Index Use with hint() Index Metrics Get Index Access Information with $indexStats Use the $indexStats aggregation stage to get statistics
regarding the use of each index for a collection. For example, the
following aggregation operation returns statistics on the index use on
the orders collection: db. orders . aggregate ( [ { $indexStats : { } } ] ) Tip See also: $indexStats Return Query Plan with explain() Use the db.collection.explain() or the cursor.explain() method in executionStats mode to return statistics about the
query process, including the index used, the number of documents
scanned, and the time the query takes to process in milliseconds. Run db.collection.explain() or the cursor.explain() method in allPlansExecution mode to view partial execution statistics collected during plan
selection. Tip See also: planCacheKey Control Index Use with hint() To force MongoDB to use a particular index for a db.collection.find() operation, specify the index with the hint() method. Append the hint() method to the find() method. Consider the
following example: db. people . find ( { name : "John Doe" , zipcode : { $gt : "63000" } } ). hint ( { zipcode : 1 } ) To view the execution statistics for a specific index, append to the db.collection.find() the hint() method
followed by cursor.explain() , e.g.: db. people . find ( { name : "John Doe" , zipcode : { $gt : "63000" } } ). hint ( { zipcode : 1 } ). explain ( "executionStats" ) Or, append hint() method to db.collection.explain().find() : db. people . explain ( "executionStats" ). find ( { name : "John Doe" , zipcode : { $gt : "63000" } } ). hint ( { zipcode : 1 } ) Specify the $natural operator to the hint() method to prevent MongoDB from using any index: db. people . find ( { name : "John Doe" , zipcode : { $gt : "63000" } } ). hint ( { $natural : 1 } ) Index Metrics In addition to the $indexStats aggregation stage, MongoDB
provides various index statistics that you may want to consider when
analyzing index use for your database: In the output of serverStatus : metrics.queryExecutor.scanned metrics.operation.scanAndOrder In the output of collStats : totalIndexSize indexSizes In the output of dbStats : dbStats.indexes dbStats.indexSize Back Manage Next Strategies
