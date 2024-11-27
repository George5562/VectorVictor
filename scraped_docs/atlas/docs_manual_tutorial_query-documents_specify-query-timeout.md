# Query Timeouts - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations / Query Query Timeouts On this page Specify a Time Limit for Queries Learn More You can specify a timeout for read operations to complete. If a query
exceeds the specified time limit, MongoDB stops the query and the query
does not return any results. To prevent ongoing queries from negatively impacting deployment
performance for long periods of time, specify a suitable query timeout
for your application. For details on how MongoDB stops queries that exceed a specified
timeout, see cursor.maxTimeMS Behaviors . Specify a Time Limit for Queries To specify a time limit for a query, perform one of these actions: Specify the maxTimeMS() option for a query. The maxTimeMS option lets you specify a query timeout at the operation
level, meaning you can specify different time limits for different
queries. Specify a global default time limit for all queries. The defaultMaxTimeMS cluster parameter specifies a default
time limit for individual read operations to complete, and applies to
all queries that do not include the maxTimeMS() option. If a query specifies a maxTimeMS() option, that value
overrides the defaultMaxTimeMS value. Learn More Perform Long-Running Snapshot Queries Analyze Query Performance cursor.noCursorTimeout() Back Null or Missing Fields Next Long-Running Snapshots
