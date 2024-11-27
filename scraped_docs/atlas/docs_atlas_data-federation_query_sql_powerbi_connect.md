# Connect to Atlas SQL from Power BI - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL / Connect Connect to Atlas SQL from Power BI On this page Prerequisites Procedure Direct Query This page describes how to connect to a cluster with Atlas SQL and
Power BI using the Power BI Connector. Prerequisites An Atlas cluster running MongoDB version 5.0 or later. Power BI Desktop 64 bit. Microsoft
updates and releases Power BI monthly, and Atlas supports only
the latest version of Power BI Desktop. Windows operating system. To learn the Windows OS versions that
Power BI Desktop supports, see Power BI System Requirements . Procedure Follow these steps to enable Atlas SQL and connect with Power BI. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Enable Atlas SQL. Under Atlas SQL , click Connect . On the lower right side of the cluster card under Atlas SQL , click Connect . If the Introducing the Atlas SQL Interface dialog box displays, click Get Started . Click Quick Start Quick Start configures a federated database instance for your
cluster with the default settings. To set up Advanced Configuration ,
including querying across Atlas data sources or
limiting the namespaces to query, you must Manually Create a Federated Database Instance for Atlas SQL . Under Create an Atlas SQL Connection for this cluster , click Create . Under Select your driver , select Power BI Connector . Under Get Connection String , select a database and copy the URL . The URL is required to connect from Power BI Desktop. 3 Download the MongoDB ODBC Driver. Download the installer for the latest MongoDB ODBC Driver . Note To use Direct Query , you must install MongoDB ODBC Driver version 1.2 or later. 4 Download and install the MongoDB Atlas Power BI Connector. Note The MongoDB Atlas Power BI Connector is included with Power BI Desktop.
If your version of Power BI Desktop already has the MongoDB connector, you can skip this step.
To use a different version than the one bundled with Power BI Desktop, complete this step. Download the connector file . Move the connector file to the following directory path: C:\Users\<user>\Documents\Power BI Desktop\Custom Connectors . Create this folder if it doesn't already exist. 5 Connect from Power BI Desktop. Open Power BI Desktop. Select Get data from the Home menu. Find and select the MongoDB Atlas SQL connector. Type mongo in the search bar to find the new connector. Select MongoDB Atlas SQL . Click Connect . Enter the URI and the database name and click OK . The MongoDB URI is the URL is the from the previous step. You can also enter a SQL query in the Native query field. Power BI uses the SQL
query as the direct source for the data. Enter your Atlas User name and Password and click Connect . By default, a user can access all clusters and federated database instances in projects to which they have access. If you restricted
access to specific clusters and federated database instances, you can grant
access to the new federated database instance in the Edit User menu. To learn more, see Modify Database Users . Direct Query Direct Query is a connection mode available with the
MongoDB Power BI connector version 1.2 and later.
To use Direct Query, you must install MongoDB ODBC Driver version 1.2 or later. Direct Query is alternative to the standard Import Mode. Direct Query allows
you to query your database directly, which guarantees up-to-date data, but may
take longer to return results. Some actions aren't supported by Direct Query. If you
try to perform an unsupported action, Power BI prompts you to
switch to Import Mode. Back Tableau Next Private Endpoint
