# Connect from MySQL Workbench - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods / BI Connector Connect from MySQL Workbench Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . Important Atlas BI Connector is approaching end-of-life.
It will be deprecated and no longer supported in June 2025. MongoDB is transitioning away from the BI Connector for Atlas to Atlas SQL .
To learn about transitioning to the new interface, see Transition from Atlas BI Connector to Atlas SQL . For M10+ clusters that have enabled the BI Connector for Atlas , the Connect dialog box provides the details to connect via the BI Connector for Atlas . To connect to the BI Connector for Atlas : 1 Click the Connect button for your cluster. 2 Select Standard Connection and
click Choose a connection method . 3 Click Connect Your Business Intelligence Tool and use the provided connection information to connect with
your BI tool. For more information on connecting to the BI Connector for Atlas , see Connection Tutorials . Prerequisites Atlas cluster with BI Connector for Atlas enabled MySQL Workbench 6.3 or later Note Versions of MySQL Workbench that are compatible with MySQL server
version 5.7 are also compatible with the BI Connector for Atlas . We recommend that you use a MySQL Workbench version between
and including versions 6.3 and 8.0.31 to guarantee compatibility. Procedure The following tutorial outlines the steps to connect using MySQL
Workbench 6.3. Atlas supports both the Community and Commercial
Editions. 1 Start MySQL Workbench. Start the MySQL Workbench 6.3. 2 Create a New MySQL Connection. From the Welcome page, click on the plus sign ( + ): Alternatively, you can create a new connection from the Manage Connections ... screen. Enter the name for your connection. Configure the parameters for the connection.  In the Parameters section, update the following fields: Field Name Description Hostname Enter the Hostname specified in the Atlas connect dialog box. Port Enter the Port specified in the Atlas connect
dialog box. Username Enter either the user specified in the Atlas connect
dialog box or a different database user for the cluster. The user is specified in the format: <username>?source=<database-name> where the <database-name> is the authentication database
for the user. Password Store the password in the keychain. Default Schema Optional. The name of a database in the cluster to connect. Configure the SSL settings for the connection. In the SSL section, update the following field: Field Name Description Use SSL Select If available . Configure the advanced settings for the connection. In the Advanced section, update the following field: Field Name Description Enable Cleartext Authentication Plugin Select. 3 Click the Test Connection to test the connection. If the connection is successful, click OK and Close the Connection setup screen and return to the
Welcome page. If the connection fails, check the settings, including the MongoDB
database user credentials and the IP access list . 4 Connect. From the Welcome page, double-click on the newly created connection
to connect and open the SQL Editor. Additional Reference For more information on the MongoDB Connector for Business
Intelligence, see MongoDB Connector for BI Manual . Back Qlik Sense Next Power BI Desktop
