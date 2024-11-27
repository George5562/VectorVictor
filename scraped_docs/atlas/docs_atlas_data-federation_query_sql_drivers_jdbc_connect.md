# Connect with JDBC Driver - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL / Connect Connect with JDBC Driver On this page Supported Authentication Mechanisms Prerequisites Procedure This page describes how to install and configure the
MongoDB JDBC Driver for connecting to a federated database instance. Supported Authentication Mechanisms You can authenticate with SCRAM-SHA-1, SCRAM-SHA-256 , MONGODB-X509 , and MongoDB Passwordless Authentication with AWS . Prerequisites A federated database instance mapped to one or more data stores. Note If some or all of your data comes from an Atlas cluster, you must
use MongoDB version 5.0 or greater for that cluster to
take advantage of Atlas SQL. An application or BI tool that you want to connect to your
federated database instance with the JDBC driver. The MongoDB JDBC Driver . Procedure You can use the JDBC driver to connect to SQL-based Java applications that accept
a JDBC API, such as a Maven project. Download and Verify the JDBC Driver 1 Download the latest MongoDB JDBC Driver version. 2 Verify the integrity of the downloaded package: The MongoDB release team digitally signs all software packages to
certify that a particular MongoDB package is a valid and unaltered
MongoDB release. MongoDB signs each release branch with a different
PGP key in .asc format. Run the following command to download the .asc file from the Maven Central Repository . curl -O https://repo1.maven.org/maven2/org/mongodb/mongodb-jdbc/2.1.2/mongodb-jdbc-2.1.2.jar.asc Run the following command to download then import the key file. Replace {server_url} with one of the current GPG key servers supported by Maven: keyserver.ubuntu.com keys.openpgp.org pgp.mit.edu gpg --keyserver {server_url} --recv-keys 91A2157730666110 HIDE OUTPUT gpg: key 91A2157730666110: public key "Huan Li <huan.li@10gen.com>" imported gpg: Total number processed: 1 gpg:               imported: 1 Run the following command to verify the MongoDB JDBC Driver installation file. gpg --verify mongodb-jdbc-2.1.2.jar.asc mongodb-jdbc-2.1.2.jar GPG should return a response similar to the following: gpg: Signature made Wed May 22 13:24:36 2024 MDT gpg:                using RSA key 91A2157730666110 gpg: Good signature from "Huan Li <huan.li@10gen.com>" If the package is properly signed, but you don't yet trust
the signing key in your local trustdb , gpg will also return
the following message: gpg: WARNING: This key is not certified with a trusted signature! gpg:          There is no indication that the signature belongs to the owner. Primary key fingerprint: D2C4 5B7E 66A5 DCA1 8B76  57A8 91A2 1577 3066 6110 If you receive the following error message, confirm that you
imported the correct public key: gpg: Can't check signature: public key not found Integrate into Maven Project 1 Configure the driver for your Maven application. To connect with your Maven application, copy the dependency snippet from the Maven Central Repository .
Edit the version number in the dependency snippet to match your JDBC driver version.
For example: < dependency > < groupId > org.mongodb </ groupId > < artifactId > mongodb-jdbc </ artifactId > < version > 2.1.0 </ version > </ dependency > 2 Add the dependency to your Maven project. In the pom.xml file for your project, paste the snippet into
the dependencies list as follows: < dependencies > < dependency > < groupId > org.mongodb </ groupId > < artifactId > mongodb-jdbc </ artifactId > < version > 2.1.0 </ version > </ dependency > </ dependencies > 3 Connect to your federated database instance. To connect to your federated database instance, create a connection string and
open a connection from your application. The connection string
for the JDBC driver follows the format of the standard MongoDB
connection string, except with the jdbc: prefix: jdbc:mongodb://[username:password]@[host].a.query.mongodb.net/<databaseName>[?option1=value1[&option2=value2]...] You can get the connection string from the Atlas UI. To get the
connection string from the Atlas UI, do the following: In the Atlas UI, go to the Data Federation page
and click Connect for the federated database instance that you want to
connect to. Under Access your data through tools , select Atlas SQL . Under Select your driver , select JDBC
Driver from the dropdown. Under Get Connection String , select the database that
you want to connect to and copy the connection string. The following example demonstrates how to open a connection.
In addition to the connection string, you must also specify
the database to use through a Properties object parameter.
To learn more, see Connection Strings and Connection Properties . java.util. Properties p = new java .util.Properties(); p.setProperty( "database" , "<databaseName>" ); Connection conn = DriverManager.getConnection( "<connectionString>" , p); Note The driver can only connect to Atlas and not to a mongod instance. Any special characters in the connection string
for the JDBC driver must be URL encoded. Back MongoDB Shell Next ODBC
