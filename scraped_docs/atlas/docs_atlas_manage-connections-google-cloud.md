# Manage Connections with Google Cloud - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Manage Connections with Google Cloud On this page Best Practices Google Cloud Connection Example You can interact with your Atlas clusters by
using Google Cloud Functions and Google Cloud Run . Best Practices Use the following best practices to properly manage connections
between Google Cloud functions and Atlas : Create your Cloud Function with a globally-scoped database connection
rather than a function-scoped database connection. Don't define a new MongoClient object each time you invoke your
function. Doing so causes the driver to create a new database
connection with each function call. This can be expensive and
can result in your application exceeding database connection limits.
When you define a new MongoClient , you should: Create the MongoClient object once. Store the object so your function can reuse the MongoClient across function invocations. The connection example reuses
existing database connections to speed up communication with the
database and keep connection counts to the database at a reasonable
level with respect to application traffic. If you have a function that connects to a sharded cluster
with many shards, you might experience performance issues. For
example, with a ten shard Atlas cluster, the driver connects to all
thirty mongos instances by default. You can use the srvMaxHosts option in your connection string to set the maximum
number of hosts that the driver connects to. To improve driver
performance, set srvMaxHosts=3 . For example: mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority&srvMaxHosts=3 To learn more, see Connection Options . Restrict network access to your Atlas cluster. Connect to your Atlas cluster over private networking using a Network Peering connection between your Atlas cluster and your Google Cloud function, or,
alternatively, a private endpoint ,
so that you can allow only private IP addresses from your IP access list . If you don't use private networking, consider connecting to your Atlas cluster via a NAT gateway . Otherwise, you must allow all IP addresses (0.0.0.0/0) to access
your Atlas cluster. Warning Adding 0.0.0.0/0 to your IP access list allows cluster access from anywhere in the public internet.
Ensure that you're using strong credentials for all database
users when allowing access from anywhere. Set maxIdleTimeMS to 60000 to automatically close your connections after 1 minute
of idle time. Tuning your maxIdleTimeMS can help reduce the
occurrence of timeout errors from your serverless functions. Configure concurrency. When you create a new Google Cloud function: Select the 2nd gen environment, which can handle
multiple concurrent requests. 2nd gen also reduces the connection load on the server by allowing the function to share a single MongoClient with many concurrent invocations. Increase the concurrency setting to minimize cold starts and
improve latency. Note If you increase the concurrency setting, you may need to
increase the CPU for best performance. To learn more, see Concurrency . Google Cloud Connection Example The following example connects a Node.js Google Cloud function to an Atlas deployment. Replace <YOUR-ATLAS-CONNECTION-STRING> with
your Atlas connection string. const { MongoClient } = require ( 'mongodb' ) ; let client ; async function getConnection ( ) { if ( ! client) { const client = new MongoClient ( '<YOUR-ATLAS-CONNECTION-STRING>' ) ; client. on ( 'connectionCreated' , () => { console . log ( 'New connection created successfully.' ) ; }) ; // Connect to the database in the global scope await client. connect ( ) ; } return client ; } Back Azure Functions Next Troubleshoot
