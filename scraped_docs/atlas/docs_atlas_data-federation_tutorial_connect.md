# Connect to Your Federated Database Instance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Get Started Connect to Your Federated Database Instance On this page Prerequisites Procedure Next Steps Estimated completion time: 15 minutes This part of the tutorial will walk you through connecting to your
federated database instance using the MongoDB Shell, mongosh . Prerequisites To complete this part of the tutorial, you will need to have completed
the following: Part 1: Deploy a Federated Database Instance Part 2: Configure Connection for Your Federated Database Instance Procedure 1 In Atlas , go to your federated database instance for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Data Federation under
the Services heading. The Data Federation page displays. 2 Click the Connect button for the federated database instance that you want to connect to. 3 Choose the type of connection. You can choose one of the following: Private Endpoint if you already configured endpoints
and want to use the connection string for your endpoint. Note If you don't have a configured private endpoint to select in
the Connect modal dropdown, the dropdown displays
the standard connection string. Standard Connection if you want to use your
deployment's standard connection string. 4 For Private Endpoint connection type, select the configured endpoint to connect to from the dropdown. 5 Add a connection IP address and create a database user if you haven't already done so and click Next . 6 Choose your connection method. You can connect using any of the following: MongoDB Drivers Compass mongosh VS Code Atlas SQL Note To run the sample queries , choose mongosh . 7 Connect to your federated database instance. To learn more about connecting to your federated database instance using your selected
connection method, see: Connect via Drivers Connect via Compass Connect via mongosh Connect via VS Code Connect Using the Atlas SQL Interface Note Only one user can authenticate on a connection to a federated database instance at any
given time. If a user authenticates and then runs the db.auth() command, Data Federation replaces the previous user's permissions with the new
user's permissions. The connectionStatus command shows only the newly authenticated user in the authenticatedUsers output field. Next Steps Now that you're connected to your federated database instance using mongosh , proceed to Run Queries Against Your federated database instance .
