# Connect from Excel - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods / BI Connector Connect from Excel Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . Important Atlas BI Connector is approaching end-of-life.
It will be deprecated and no longer supported in June 2025. MongoDB is transitioning away from the BI Connector for Atlas to Atlas SQL .
To learn about transitioning to the new interface, see Transition from Atlas BI Connector to Atlas SQL . For M10+ clusters that have enabled the BI Connector for Atlas , the Connect dialog box provides the details to connect via the BI Connector for Atlas . To connect to the BI Connector for Atlas : 1 Click the Connect button for your cluster. 2 Select Standard Connection and
click Choose a connection method . 3 Click Connect Your Business Intelligence Tool and use the provided connection information to connect with
your BI tool. For more information on connecting to the BI Connector for Atlas , see Connection Tutorials . Prerequisites Windows macOS Atlas cluster with BI Connector for Atlas enabled Create a system Data Source Name (DSN) Atlas cluster with BI Connector for Atlas enabled 64-bit version of Excel. Run the following command to
determine whether the 64-bit or 32-bit version of Excel is
installed: file -N /Applications/Microsoft\ Excel.app/Contents/MacOS/Microsoft\ Excel For information on upgrading to the 64-bit version of Excel,
see Microsoft Support . Install iODBC Note Both the 64-bit and 32-bit versions of iODBC are
included with the installer. If you use iODBC to test your
DSN, you must use the 64-bit version of the application. iODBC is not recommended for creating or modifying your Data Source Name (DSN) .
To create or modify your DSN, use the ODBC Manager
application that is included with the MongoDB ODBC driver. Create a system Data Source Name (DSN) Connect from Microsoft Excel Windows macOS 1 Start Microsoft Excel. Start Microsoft Excel and open a blank worksheet. 2 Use the Data Connection Wizard to set up the connection. Click the Data tab. Select From Other Sources > From Data Connection Wizard option. Select ODBC DSN from the list of data source options
and click Next . Select the DSN created for your Atlas cluster and click Next . Select a database and collection from which to import data
and click Next . Save the data connection file and click Finish . If you wish to re-use this connection in the future, you can
select it from the Data > Get External
Data > Existing Connections menu. In the final wizard window,specify a format for your
worksheet. Click OK when finished. 1 Open a spreadsheet in Excel. Start Microsoft Excel and open a blank worksheet. 2 Open the iODBC Data Source Chooser dialog box. Click the Data on the toolbar. On the toolbar, click New Database Query , then click From Database . If the New Database Query button is not displayed,
click Get External Data , then New Database Query . 3 Select Your DSN. Click the System DSN tab. Select the DSN which connects to your
BI Connector for Atlas . Click OK . 4 Enter Credentials. Enter the username and password used to
connect to BI Connector for Atlas and click Ok . Note When specifying a username , include the authentication
database for the user. For example, salesadmin?source=admin . 5 Select a Table. In the left side of the dialog box, click your server name to expand
the list collections in your database. Select the collection from the list from which contains the data
you want to import. To view your data before importing, click Run to run
the generated SQL statement . Your data appears in the
table below the statement. Click Return Data . 6 Import the Data. Select how you would like to import the data into Excel. You can choose to import the data into: An Existing Sheet , specifying in which cell to begin
the table. A New Sheet , automatically beginning the table in
cell A1 . A PivotTable in a new sheet. Click OK to complete the import process. Additional Reference For more information on the MongoDB Connector for Business
Intelligence, see MongoDB Connector for BI Manual . Back System DSN Next Tableau Desktop
