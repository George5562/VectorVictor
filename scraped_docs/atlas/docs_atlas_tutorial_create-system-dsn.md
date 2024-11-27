# Create a System DSN - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods / BI Connector Create a System DSN On this page Prerequisites Procedure Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . The following steps describe how to create a system Data Source
Name (DSN) for the BI Connector for Atlas . A DSN is a saved
configuration which describes a database connection to be
used by an ODBC driver.
Once the DSN is created, you can configure a wide
range of SQL clients and BI tools to use the DSN and import
data from MongoDB. Windows macOS Prerequisites Before creating a DSN , you should: Windows macOS Download and install Visual C++ Redistributable for Visual Studio 2015 Download and install the MongoDB ODBC Driver for BI Connector for your platform. Procedure Windows macOS 1 Start the Microsoft ODBC Data Sources program. Choose the program version (64-bit or 32-bit) which is
appropriate for your system and ODBC driver version. 2 Select System DSN , then click Add . 3 Select a MongoDB ODBC driver from the list of available drivers. Select either the MongoDB ODBC ANSI Driver or the MongoDB ODBC Unicode Driver , then click OK . Note ANSI ODBC/Connectors offer better performance but have a limited
character set. Unicode ODBC/Connectors support a wider character
set but may be less performant. 4 Fill in the necessary form fields. Click the Details button to expose the lower half of the form. The following form fields are required: Field Name Description Data Source Name A name of your choice. TCP/IP Server The hostname specified in the Atlas connect dialog box. Port The IANA port number specified in the Atlas connect dialog box. The default is 27015 . Database The name of the database to which you want to connect. User Enter either the user specified in the Atlas connect dialog box
or another database user with access to the database. The user is specified in the following format: <username>?source=<database-name> where the <database-name> is the authentication database
for the user. If admin is the authentication database,
you can omit ?source=<database-name> . If you are using Username and Password ( SCRAM-SHA-256 )
authentication, the expected authenticating database is admin . If you are using LDAP ( PLAIN ) authentication, the
expected authenticating database is $external . For example: myTestUser?source=$external Password The password that corresponds to the specified User . 5 Click Test to validate the ODBC connection. If the connection is successful, click OK to add the DSN . If the connection fails,
check to make sure your database user is correctly authenticated for
the database named in the connection. 1 Launch ODBC Manager. Note ODBC Manager is included with the MongoDB ODBC driver. 2 Click System DSN , then click Add . 3 Select a MongoDB ODBC driver from the list of available drivers. Select either the MongoDB ANSI ODBC driver or the MongoDB Unicode ODBC driver, then click OK . Note ANSI ODBC/Connectors offer better performance but have a limited
character set. Unicode ODBC/Connectors support a wider character
set but may be less performant. 4 Enter a Data Source Name (DSN) . Optionally enter a Description . Note Do not close the setup window. Proceed to the next step. 5 Add the necessary keywords. Click Add to add a keyword value pair. Modify the Keyword by double-clicking on it, entering
the desired keyword, then pressing enter. Modify the Value by double-clicking on it, entering the
desired keyword, then pressing enter. Using the procedure above, add the following keywords: Keyword Value SERVER The hostname specified in the Atlas connect dialog box. PORT The IANA port number specified in the Atlas connect dialog box. The default is 27015 . DATABASE The database to use after connecting. This is required when connecting with Microsoft Excel. UID The username for the user that can access the active Atlas database. For example, if the user myTestUser is authenticated
against the admin database, use the following value: ``myTestUser?source=admin`` If you are using Username and Password ( SCRAM-SHA-256 )
authentication, the expected authenticating database is admin . If you are using LDAP ( PLAIN ) authentication, the
expected authenticating database is $external . For example: myTestUser?source=$external PWD The password associated with the UID . For the complete list of ODBC parameters, see Connector/ODBC Connection Parameters . Note Do not close the setup window. Proceed to the next step. 6 Click OK to finish creating the DSN.
