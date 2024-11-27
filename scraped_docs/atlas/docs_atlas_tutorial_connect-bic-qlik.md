# Connect from Qlik Sense - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods / BI Connector Connect from Qlik Sense Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . Important Atlas BI Connector is approaching end-of-life.
It will be deprecated and no longer supported in June 2025. MongoDB is transitioning away from the BI Connector for Atlas to Atlas SQL .
To learn about transitioning to the new interface, see Transition from Atlas BI Connector to Atlas SQL . For M10+ clusters that have enabled the BI Connector for Atlas , the Connect dialog box provides the details to connect via the BI Connector for Atlas . To connect to the BI Connector for Atlas : 1 Click the Connect button for your cluster. 2 Select Standard Connection and
click Choose a connection method . 3 Click Connect Your Business Intelligence Tool and use the provided connection information to connect with
your BI tool. For more information on connecting to the BI Connector for Atlas , see Connection Tutorials . Prerequisites Atlas cluster with BI Connector for Atlas enabled Create a system Data Source Name (DSN) Qlik Sense Desktop Procedure 1 Start Qlik Sense Desktop. Start the Qlik Sense desktop application. 2 Create a Data Connection to the BI Connector for Atlas . Click Create a New App . Enter a name for the app and Create .  If created
successfully, Open app . Click Add data from files and other sources . Select ODBC from the list of data sources. In the Create New Connection window, in the System DSN , select the DSN that you created earlier. Leave the Username and Password fields
blank as the application uses the username and password specified
in the DSN during the ODBC set up. Click Create . Additional Reference For more information on the MongoDB Connector for Business
Intelligence, see MongoDB Connector for BI Manual . Back Tableau Desktop Next MySQL Workbench
