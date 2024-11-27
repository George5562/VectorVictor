# Connect Using the Atlas SQL Interface - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL Connect Using the Atlas SQL Interface On this page Get Your Connection Information Connect with a BI Tool Get Your Connection Information After you configure your federated database instance, you can connect to it from various BI tools or from the MongoDB Shell. To find the information you need to connect, select Connect using the Atlas SQL interface in the
federated database instance connection modal. Connect with a BI Tool Note To connect to your federated database instance with the MongoDB Shell,
see Connect from the MongoDB Shell . To connect to your federated database instance with a BI tool, you can use a custom connector with
its associated and officially supported BI tool, or a standalone driver to
integrate with a BI tool of your choice. Custom Connectors MongoDB supports and regularly updates the following custom Atlas SQL
connectors. To ensure a successful connection and support for the
full range of Atlas SQL capabilities, use one of the following custom connectors
with its associated BI tool: Tableau Power BI Standalone Drivers Important If you use a standalone driver with a BI tool that MongoDB doesn't officially
support, you must test the features of Atlas SQL that you want to use in order
to confirm they are supported by that tool. MongoDB can't guarantee that all BI tools are fully supported. MongoDB provides the Atlas SQL standalone JDBC and ODBC drivers for
experimentation and custom integration with SQL-92 dialect-based
third-party BI tools that support a generic ODBC or JDBC driver connection.
Use the type of driver that your BI tool specifies: JDBC driver ODBC driver Supported Authentication Mechanisms You can authenticate with SCRAM-SHA-1, SCRAM-SHA-256 , MONGODB-X509 , and MongoDB Passwordless Authentication with AWS . Back Advanced Configuration Next MongoDB Shell
