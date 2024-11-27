# Connect from the MongoDB Shell - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL / Connect Connect from the MongoDB Shell On this page Prerequisites Procedure Aggregation Syntax and Short-form Syntax This page describes how to connect to a federated database instance through the MongoDB Shell ( mongosh ). Prerequisites A federated database instance that is mapped to one or more data stores. Note If some or all of your data comes from an Atlas cluster, you must
use MongoDB version 5.0 or greater for that cluster to
take advantage of Atlas SQL. Procedure 1 In Atlas , go to your federated database instance for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Data Federation under
the Services heading. The Data Federation page displays. 2 Click Connect to open the federated database instance connection modal. 3 Select Shell . 4 Install the MongoDB Shell if you haven't already. If you do not have the MongoDB Shell installed: Select I do not have the MongoDB Shell installed inside the connection modal. Select your operating system from the modal dropdown menu. Follow the installation instructions for your operating system provided in the modal. (Optional) Confirm that your mongosh installation was successful. To check that your installation was successful, in your
terminal, run: mongosh --version If the installation was successful, mongosh displays a version. If you already have the MongoDB Shell installed: Select I have the MongoDB Shell installed inside the connection modal. Select mongosh from the modal dropdown menu. Note The MongoDB Shell, or mongosh , is separate from
the mongo versions in the modal dropdown menu. If you want to ensure that you have mongosh installed,
in your terminal, run: mongosh --version If mongosh is installed, it displays a version. 5 Select your authentication method. Your authentication method depends on how your
database access is configured. To learn more about
database access, see Configure Database Users . You can choose: Password (SCRAM) , or X.509 . Atlas Data Federation provides a connection string for your authentication
method. 6 Copy and run your connection string. If you selected the Password (SCRAM) authentication
method, you are prompted for a password for the connecting user. 7 (Optional) Confirm the connection to your federated database instance. To confirm that you are connected to your federated database instance, using mongosh , run: show dbs If you successfully connected to your federated database instance that is
mapped to a data store, mongosh displays the names of your
virtual databases. Aggregation Syntax and Short-form Syntax Atlas SQL supports an aggregation pipeline stage syntax and a short-form syntax for constructing the SQL queries.
You can use either of these syntaxes to write queries in the MongoDB Shell. Aggregation Pipeline Stage Syntax You can use the $sql aggregation pipeline stage to
write Atlas SQL queries. See $sql for a list of
properties you must provide to $sql . The following example uses $sql syntax to execute the Atlas SQL statement select * from Users limit 2 : db.aggregate( [ { $sql: { statement: "SELECT * FROM users LIMIT 2", format: "jdbc", dialect: "mongosql" } } ] ) Note Atlas SQL uses the dialect mongosql . Short-form Syntax You can use a short-form syntax, db.sql , to supply an
Atlas SQL statement directly. Important Short-form syntax is not stable and may change in the future. db.sql(` SELECT * FROM users LIMIT 2 `); Back Connect Next JDBC Driver
