# Connect from Tableau - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL / Connect Connect from Tableau On this page Prerequisites Procedure This page describes how to connect to Atlas Data Federation with Tableau using the
Tableau custom connector. Prerequisites A federated database instance that is mapped to one or more data stores. Note If some or all of your data comes from an Atlas cluster, you must
use MongoDB version 5.0 or greater for that cluster to
take advantage of Atlas SQL. Tableau Desktop or Server. Procedure The following procedure guides you through installing the necessary
tools, finding your federated database instance connection information, and connecting to
your federated database instance with Tableau. Download the JDBC Driver and Tableau Connector 1 Download the MongoDB JDBC Driver. Download the latest MongoDB JDBC Driver version
if you haven't already. Move the downloaded .jar file into the appropriate
directory for your operating system: Operating System Folder Path Windows C:\Program Files\Tableau\Drivers MacOS ~/Library/Tableau/Drivers 2 Download and install the Tableau custom connector. Download the taco file . Move the downloaded taco file into the appropriate
directory for your operating system: Operating System Folder Path Windows C:\Users\<user>\Documents\My Tableau Repository\Connectors MacOS ~/Documents/My Tableau Repository/Connectors Important Updating Your Connector If you download a new version of the
Tableau custom connector, delete the old
Tableau custom connector file from your
Connectors directory to ensure that Tableau uses the latest
version. Get Your Federated Database Instance Connection Information 1 In Atlas , go to your federated database instance for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Data Federation under
the Services heading. The Data Federation page displays. 2 Click Connect to open the federated database instance connection modal. 3 Select Connect using the Atlas SQL Interface . 4 Select Tableau Connector . 5 Copy your connection information. Atlas Data Federation provides a connection string to connect to your
federated database instance. You'll need this in a later step. Connect with Tableau 1 Open Tableau Desktop or Tableau Server. 2 Navigate to the Connect menu. 3 Select MongoDB Atlas by MongoDB . A connection modal displays. 4 Enter the connection information that you copied from Atlas Data Federation. Enter the following information: MongoDB URI Your connection string from step 5 of Get Your Federated Database Instance Connection Information . Database Your virtual database name. Authentication Your preferred method of authentication. You can select one
of the following from the dropdown: Username and Password Certificate / Token 5 Click Sign In . Back ODBC Next Power BI
