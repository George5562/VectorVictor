# Connect to a Cluster using Command Line Tools - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods Connect to a Cluster using Command Line Tools On this page Access the Command Line Tools Tab In Atlas , go to the Clusters page for your project. Choose Command Line Tools for your desired cluster. Connect with mongorestore Connect with mongodump Connect with mongoimport Connect with mongoexport Connect with mongostat Connect with mongotop Troubleshooting Atlas provides instructions for connecting to an Atlas cluster
using select MongoDB command line tools in the Command Line Tools tab. For Serverless instances, use MongoDB Tools version
100.10.0 or later. To learn more, see Minimum MongoDB Tools Version for serverless instances . Note The Required Access sections in the MongoDB Database Tools documentation reference
MongoDB roles and privileges that correspond to Atlas roles , privileges , and privilege actions. Access the Command Line Tools Tab To access the Atlas Command Line Tools tab: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Choose Command Line Tools for your desired cluster. From the menu for the cluster, click Command Line Tools . Connect with mongorestore Note Since Atlas doesn't offer an individual restore role,
privilege, or privilege action, you must have the Atlas admin role to use mongorestore . The Binary Import and Export Tools section of the Command Line Tools tab
displays a copyable template with the minimum required options for
connecting mongorestore to your Atlas cluster.
For instructions on finding the Command Line Tools tab,
see Access the Command Line Tools Tab . The template includes placeholder values for certain options.
You must replace these placeholders with the appropriate values for
your Atlas cluster: <PASSWORD> - replace this with the password for the user
specified in --username . The template includes a database user
for the project as the --username . If you want to authenticate
as a different user, replace the value of --username and
specify the password for that user in --password . If your password contains special characters, surround it in double
or single quotes. For example, if your password is @bc123 , you
must surround it in quotes, such as "@bc123" . Include any other mongorestore command line options as required
before copying and pasting the command into your system terminal and
executing the full command. See mongorestore for complete
documentation on the available command line options and how to use
them. Note Connecting to an Atlas cluster from Microsoft Windows For users on Windows , specify mongorestore.exe You may need to provide the full file
path to the mongorestore.exe . Connect with mongodump The Binary Import and Export section of the Command Line Tools tab
displays a copyable template with the minimum required options for
connecting mongodump to your Atlas cluster.
For instructions on finding the Command Line Tools tab,
see Access the Command Line Tools Tab . The template includes placeholder values for certain options.
You must replace these placeholders with the appropriate values for
your Atlas cluster: <PASSWORD> - replace this with the password for the user
specified in --username . The template includes a database user
for the project as the --username . If you want to authenticate
as a different user, replace the value of --username and
specify the password for that user in --password . If your password contains special characters, surround it in double
or single quotes. For example, if your password is @bc123 , you
must surround it in quotes, such as "@bc123" . <DATABASE> - replace this with the name of the database you want to export data from Include any other mongodump command line options as required
before copying and pasting the command into your system terminal and
executing the full command. See mongodump for complete
documentation on the available command line options and how to use
them. Note Connecting to an Atlas cluster from Microsoft Windows For users on Windows , specify mongodump.exe You may need to provide the full file
path to the mongodump.exe . Connect with mongoimport The Data Import and Export Tools section of the Command Line Tools tab
displays a copyable template with the minimum required options for
connecting mongoimport to your Atlas cluster.
For instructions on finding the Command Line Tools tab,
see Access the Command Line Tools Tab . The template includes placeholder values for certain options.
You must replace these placeholders with the appropriate values for
your Atlas cluster: <PASSWORD> - replace this with the password for the user
specified in --username . The template includes a database user
for the project as the --username . If you want to authenticate
as a different user, replace the value of --username and
specify the password for that user in --password . If your password contains special characters, surround it in double
or single quotes. For example, if your password is @bc123 , you
must surround it in quotes, such as "@bc123" . <DATABASE> - the name of the database you want to import data into. <COLLECTION> - the name of the collection you want to import data into. <FILETYPE> - the file type of the data source you are importing data from. See --type for more information. <FILENAME> - the name of the data source you are importing data from. See --file for more information. Include any other mongoimport command line options as required
before copying and pasting the command into your system terminal and
executing the full command. See mongoimport for complete
documentation on the available command line options and how to use
them. Note Connecting to an Atlas cluster from Microsoft Windows For users on Windows , specify mongoimport.exe You may need to provide the full file
path to the mongoimport.exe . Connect with mongoexport The Data Import and Export Tools section of the Command Line Tools tab
displays a copyable template with the minimum required options for
connecting mongoexport to your Atlas cluster.
For instructions on finding the Command Line Tools tab,
see Access the Command Line Tools Tab . The template includes placeholder values for certain options.
You must replace these placeholders with the appropriate values for
your Atlas cluster: <PASSWORD> - replace this with the password for the user
specified in --username . The template includes a database user
for the project as the --username . If you want to authenticate
as a different user, replace the value of --username and
specify the password for that user in --password . If your password contains special characters, surround it in double
or single quotes. For example, if your password is @bc123 , you
must surround it in quotes, such as "@bc123" . <DATABASE> - the name of the database you want to export data from. <COLLECTION> - the name of the collection you want to export data from. <FILETYPE> - the file type of the data source you are exporting data to. See --type for more information. <FILENAME> - the name of the data source you are exporting data to. See --file for more information. Include any other mongoexport command line options as required
before copying and pasting the command into your system terminal and
executing the full command. See mongoexport for complete
documentation on the available command line options and how to use
them. Note Connecting to an Atlas cluster from Microsoft Windows For users on Windows , specify mongoexport.exe You may need to provide the full file
path to the mongoexport.exe . Connect with mongostat The Set Up Diagnostics section of the Command Line Tools tab
displays a copyable template with the minimum required options for
connecting mongostat to your Atlas cluster.
For instructions on finding the Command Line Tools tab,
see Access the Command Line Tools Tab . The template includes placeholder values for certain options.
You must replace these placeholders with the appropriate values for
your Atlas cluster: <PASSWORD> - replace this with the password for the user
specified in --username . The template includes a database user
for the project as the --username . If you want to authenticate
as a different user, replace the value of --username and
specify the password for that user in --password . If your password contains special characters, surround it in double
or single quotes. For example, if your password is @bc123 , you
must surround it in quotes, such as "@bc123" . Include any other mongostat command line options as required
before copying and pasting the command into your system terminal and
executing the full command. See mongostat for complete
documentation on the available command line options and how to use
them. Note Connecting to an Atlas cluster from Microsoft Windows For users on Windows , specify mongostat.exe You may need to provide the full file
path to the mongostat.exe . Connect with mongotop The Set Up Diagnostics section of the Command Line Tools tab
displays a copyable template with the minimum required options for
connecting mongotop to your Atlas cluster.
For instructions on finding the Command Line Tools tab,
see Access the Command Line Tools Tab . The template includes placeholder values for certain options.
You must replace these placeholders with the appropriate values for
your Atlas cluster: <PASSWORD> - replace this with the password for the user
specified in --username . The template includes a database user
for the project as the --username . If you want to authenticate
as a different user, replace the value of --username and
specify the password for that user in --password . If your password contains special characters, surround it in double
or single quotes. For example, if your password is @bc123 , you
must surround it in quotes, such as "@bc123" . Include any other mongotop command line options as required
before copying and pasting the command into your system terminal and
executing the full command. See mongotop for complete
documentation on the available command line options and how to use
them. Note Connecting to an Atlas cluster from Microsoft Windows For users on Windows , specify mongotop.exe You may need to provide the full file
path to the mongotop.exe . Troubleshooting If you are experiencing issues connecting to your cluster, see Troubleshoot Connection Issues . Back Power BI Desktop Next VS Code
