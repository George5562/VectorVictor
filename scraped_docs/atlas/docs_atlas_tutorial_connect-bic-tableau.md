# Connect from Tableau Desktop - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods / BI Connector Connect from Tableau Desktop Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . Important Atlas BI Connector is approaching end-of-life.
It will be deprecated and no longer supported in June 2025. MongoDB is transitioning away from the BI Connector for Atlas to Atlas SQL .
To learn about transitioning to the new interface, see Transition from Atlas BI Connector to Atlas SQL . For M10+ clusters that have enabled the BI Connector for Atlas , the Connect dialog box provides the details to connect via the BI Connector for Atlas . To connect to the BI Connector for Atlas : 1 Click the Connect button for your cluster. 2 Select Standard Connection and
click Choose a connection method . 3 Click Connect Your Business Intelligence Tool and use the provided connection information to connect with
your BI tool. For more information on connecting to the BI Connector for Atlas , see Connection Tutorials . The MongoDB Connector for Business Intelligence for Atlas ( BI Connector ) is only available for M10 and
larger clusters. The BI Connector is a powerful tool which provides users
SQL-based access to their MongoDB databases. As a result, the BI Connector performs operations which may be CPU and memory
intensive. Given the limited hardware resources on M10 and M20 cluster tiers, you may experience performance degradation of
the cluster when enabling the BI Connector . If this occurs,
scale up to an M30 or larger cluster or disable the BI Connector . Prerequisites Windows macOS Atlas cluster with BI Connector for Atlas enabled Create a system Data Source Name (DSN) that uses the MongoDB ODBC driver Tableau version 10.3 or later Atlas cluster with BI Connector for Atlas enabled Create a system Data Source Name (DSN) that uses the MongoDB ODBC driver Tableau version 10.4 or later Procedure Windows macOS 1 Start Tableau Desktop. 2 Connect to the BI Connector for Atlas . Select the MongoDB BI Connector as your Data Source for your Tableau
book. From the left-hand navigation, under To a server ,
click More ... and select Other Databases (ODBC) . Select the DSN that you just created from the DSN list. Enter the following fields in the Connection Attributes pane: Field Action Server Enter the Hostname specified in the Atlas connect dialog box. Port Enter the Port specified in the Atlas connect
dialog box. Username Enter either the user specified in the Atlas connect
dialog box or a different database user for the cluster. The user is specified in the format: <username>?source=<database-name> where the <database-name> is the authentication database
for the user. Password Enter the password corresponding to the entered User . Click Sign In . 1 Start Tableau Desktop. 2 Connect using Tableau. In the left-side navigation under To a server , click
on More ... then click Other Databases (ODBC) . From the Other Databases (ODBC) dialog box, select your DSN
from the list and click Connect . Once the connection test completes, click Sign In . Additional Reference For more information on the MongoDB Connector for Business
Intelligence, see MongoDB Connector for BI Manual . Back Excel Next Qlik Sense
