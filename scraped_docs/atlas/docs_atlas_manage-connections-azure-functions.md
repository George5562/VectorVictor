# Manage Connections with Azure Functions - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Manage Connections with Azure Functions On this page Best Practices Connection Example You can use Azure Functions with Atlas . Best Practices Use the following best practices to properly manage connections
between Azure Functions and Atlas : Define the client to the MongoDB server outside the Run method of
your Azure function handler . Don't define a new MongoClient object each time you invoke your
function. Doing so causes the driver to create a new database
connection with each function call. This can be expensive and
can result in your application exceeding database connection limits.
When you define a new MongoClient , you should: Create the MongoClient object once. Store the object so your function can reuse the MongoClient across function invocations. The Connection Example reuses existing database
connections to speed up communication with the database and keep
connection counts to the database at a reasonable level with respect
to application traffic. Restrict network access to your Atlas cluster from your Azure
Functions. Connect to your Atlas cluster over private networking using a Network Peering connection between your Atlas cluster and your Azure Functions, or,
alternatively, a private endpoint ,
so that you can allow only private IP addresses from your IP access list . Note This configuration requires an Azure Functions Premium Plan with a Virtual Network (VNet) Integration configured. If you don't use private networking, consider connecting to your Atlas cluster using a NAT gateway . Review outbound IP address changes and strategies for ensuring static outbound IP addresses . Set maxIdleTimeMS to 60000 to automatically close your connections after 1 minute
of idle time. Tuning your maxIdleTimeMS can help reduce the
occurrence of timeout errors from your serverless functions. Connection Example The Azure Functions Example in the mongodb-developer repository contains example code that shows how
to work with the MongoDB C# driver and Azure Functions using Atlas clusters. To learn more about using Azure Functions with Visual Studio Code, see Quickstart: Create a C# function in Azure using Visual Studio Code To learn more about using Azure Functions with Visual Studio, see Quickstart: Create your first C# function in Azure using Visual Studio . Back AWS Lambda Next Google Cloud
