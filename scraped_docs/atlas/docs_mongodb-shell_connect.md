# Connect to a Deployment - MongoDB Shell


Docs Home / MongoDB Shell Connect to a Deployment On this page Prerequisites Supported MongoDB Versions Install mongosh Connect to a MongoDB Atlas Deployment Get your Atlas Connection String Set Your Database Credentials Connect to MongoDB Atlas with mongosh Connect to a Local Deployment on the Default Port Connect to a Local Deployment on a Non-Default Port Connect to a Deployment on a Remote Host Specify Connection Options Connect With Authentication Connect with OpenID Connect Connect with LDAP Connect to a Replica Set Connect Using TLS Connect to a Specific Database Proxy Settings Connect to a Different Deployment Verify Current Connection Disconnect from a Deployment Non-genuine Deployments Limitations This page shows how to use the MongoDB Shell to connect to a MongoDB
deployment. You can connect to a MongoDB Atlas cloud-hosted deployment ,
connect to a local deployment, or connect to another remote host with MongoDB Shell . Prerequisites To use the MongoDB Shell , you must have a MongoDB deployment to connect
to. For a free cloud-hosted deployment, you can use MongoDB Atlas . To learn how to run a local MongoDB deployment, see Install MongoDB . Supported MongoDB Versions You can use the MongoDB Shell to connect to MongoDB version 4.2 or
greater. Install mongosh These procedures assume you have already installed mongosh . For more
information about installing mongosh , refer to Install mongosh . Connect to a MongoDB Atlas Deployment You can connect to your MongoDB Atlas deployment directly from your shell. 1 Get your Atlas Connection String You need an Atlas connection string to connect from MongoDB Shell .
You can get the Atlas connection string in the Atlas UI. Refer to the Find Your MongoDB Atlas Connection String guide for details. 2 Set Your Database Credentials If you haven't already created a database user ,
you must set a username and password. To connect to Atlas, pass your username with
the Atlas connection string. After you issue the connect command, the
shell prompts for your password. 3 Connect to MongoDB Atlas with mongosh To establish your connection, run the mongosh command with your
connection string and options to establish the connection. The connection string includes the following elements: Your cluster name A hash A flag for the API version A flag for the username you want to use to connect It resembles the following string: mongosh "mongodb+srv://YOUR_CLUSTER_NAME.YOUR_HASH.mongodb.net/" --apiVersion YOUR_API_VERSION --username YOUR_USERNAME Note Learn More You can use other connection security options to connect to Atlas via mongosh . For information on connecting with a private
IP for peering or a Private Endpoint connection, refer to the Atlas Connect via mongosh documentation. Connect to a Local Deployment on the Default Port To connect to a MongoDB deployment running on localhost with default port 27017, run mongosh without any options: mongosh This is equivalent to the following command: mongosh "mongodb://localhost:27017" Connect to a Local Deployment on a Non-Default Port To specify a port to connect to on localhost, you can use either: A connection string with the
chosen port The --port command-line option For example, the following commands connect to a deployment running on
localhost port 28015: mongosh "mongodb://localhost:28015" mongosh --port 28015 Connect to a Deployment on a Remote Host To specify a remote host and port, you can use either: A connection string with the
chosen host and port. The --host and --port command-line options. If you omit the --port option, mongosh uses the default port 27017. For example, the following commands connect to a MongoDB deployment
running on host mongodb0.example.com and port 28015: mongosh "mongodb://mongodb0.example.com:28015" mongosh --host mongodb0.example.com --port 28015 Note Connect to MongoDB Atlas If your remote host is an Atlas cluster, you can copy your
connection string from the Atlas UI. To learn more, see Connect to a Cluster in the Atlas documentation. Specify Connection Options Specify different connection options to connect to different types of
deployments. Connect With Authentication To connect to a MongoDB deployment that requires authentication, use the --username and --authenticationDatabase options. mongosh prompts you for a
password, which it hides as you type. For example, to authenticate as user alice on the admin database, run the following command: mongosh "mongodb://mongodb0.example.com:28015" --username alice --authenticationDatabase admin To provide a password as part of the connection command instead of using
the prompt, use the --password option. Use this
option for programmatic usage of mongosh , like a driver . Tip See also: To enforce authentication on a deployment, see Enable Access Control . To provision access to a MongoDB deployment, see Database
Users . Connect with OpenID Connect To connect to a deployment using OpenID Connect ,
use the --authenticationMechanism option and set it to MONGODB-OIDC . mongosh redirects you to a browser where you enter your identity provider's
log-in information. For example, the following connects to a local deployment using MONGODB-OIDC : mongosh "mongodb://localhost/" --authenticationMechanism MONGODB-OIDC Connect with LDAP To connect to a deployment using LDAP : Set --username to a username that
respects the security.ldap.authz.queryTemplate , or any
configured security.ldap.userToDNMapping template. Set --password to the appropriate
password. If you do not specify the password to the --password command-line option, mongosh prompts you for
the password. Set --authenticationDatabase to $external .
The $external argument must be placed in single quotes, not
double quotes, to prevent the shell from interpreting $external as a variable. Set --authenticationMechanism to PLAIN . Warning When you use one-time passwords with LDAP authentication, adding
the connection string options maxPoolSize=1&srvMaxHosts=1 to your connection string is
recommended to reduce the potential for connection failures. Include the --host and --port of the MongoDB deployment, along with
any other options relevant to your deployment. For example, the following operation authenticates to a MongoDB
deployment running with LDAP authentication and authorization: mongosh --username alice@dba.example.com --password  --authenticationDatabase '$external' --authenticationMechanism "PLAIN" --host "mongodb.example.com" --port 27017 Connect to a Replica Set To connect to a replica set, you can either: Use the DNS Seedlist Connection Format . Explicitly specify the replica set name and members in the connection
string. Option 1: DNS Seedlist Format To use the DNS seedlist connection format, include the +srv modifier
in your connection string. For example, to connect to a replica set on server.example.com , run
the following command: mongosh "mongodb+srv://server.example.com/" Note +srv TLS Behavior When you use the +srv connection string modifier, MongoDB
automatically sets the --tls connection option to true . To override this behavior, set --tls to false . Option 2: Specify Members in Connection String You can specify individual replica set members in the connection string . For example, to connect to a three-member replica set named replA ,
run the following command: mongosh "mongodb://mongodb0.example.com.local:27017,mongodb1.example.com.local:27017,mongodb2.example.com.local:27017/?replicaSet=replA" Note directConnection Parameter Added Automatically When you specify individual replica set members in the connection
string, mongosh automatically adds the directConnection=true parameter, unless at least one of the following is true: The replicaSet query parameter is present in the connection string. The connection string uses the mongodb+srv:// connection string
format. The connection string contains a seed list with multiple hosts. The connection string already contains a directConnection parameter. When directConnection=true , all operations are run on the host
specified in the connection URI. Connect Using TLS To connect to a deployment using TLS, you can either: Use the DNS Seedlist Connection Format . The +srv connection string modifier automatically sets the tls option to true for the connection. For example, to connect to a DNS seedlist-defined replica set with tls enabled, run the following command: mongosh "mongodb+srv://server.example.com/" Set the --tls option to true in the connection
string. For example, to enable tls with a connection string option, run
the following command: mongosh "mongodb://mongodb0.example.com:28015/?tls=true" Specify the --tls command-line option. For example, to connect to a remote host with tls enabled, run the
following command: mongosh "mongodb://mongodb0.example.com:28015" --tls Connect to a Specific Database To connect to a specific database, specify a database in your connection string URI path . If
you do not specify a database in your URI path, you connect to the test database. For example, to connect to a database called qa on localhost, run the
following command: mongosh "mongodb://localhost:27017/qa" Proxy Settings To establish a connection with proxy configurations, you can use the
following environment variables: Variable Description Example MONGODB_PROXY Proxy connections to mongodb:// and mongodb+srv:// URLs, such
as database clusters. The following example sets the MONGODB_PROXY environment variable to
proxy all MongoDB connections through a CONNECT proxy located at example.com:8080 with TLS enabled. export MONGODB_PROXY=https://example.com:8080 HTTP_PROXY Proxy connections to http:// URLs. HTTP connections are mostly
used for OIDC authentication. If you also set HTTPS_PROXY , the value of HTTPS_PROXY takes
precedence for all requests. The following example sets the HTTP_PROXY environment variable to
proxy HTTP connections through a CONNECT proxy located at example.com:8080 : export HTTP_PROXY=http://example.com:8080 HTTPS_PROXY Proxy connections to https:// URLs. HTTPS connections are mostly
used for OIDC authentication. If you also set HTTP_PROXY , the value of HTTPS_PROXY takes
precedence for all requests. The following example sets the HTTPS_PROXY environment variable to
proxy all HTTPS connections through a CONNECT proxy located at localhost:8080 without TLS: export HTTPS_PROXY=http://localhost:8080 ALL_PROXY Proxy all connections to the specified URL. The following example sets the ALL_PROXY environment variable to
proxy all outbound network connections through a Socks5 proxy located at example.com:1234 with credentials included in the URL: export ALL_PROXY=socks5://username:password@example.com:1234 NO_PROXY Comma-separated list of hostnames that should be excluded from
proxying. The following example sets the NO_PROXY environment variable to
bypass the proxy for connections to localhost and internal-db.example.com . export NO_PROXY=localhost,internal-db.example.com Note mongosh supports the following proxy types: Socks5 proxies HTTP proxies CONNECT proxies PAC URLs that resolve to one of the previously
listed proxies Connect to a Different Deployment If you are already connected to a deployment in the MongoDB Shell , you can
use the Mongo() or connect() method to connect to a different
deployment from within the MongoDB Shell . To learn how to connect to a different deployment using these methods,
see Open a New Connection . Verify Current Connection To verify your current database connection, use the db.getMongo() method. The method returns the connection string URI for your current connection. Disconnect from a Deployment To disconnect from a deployment and exit mongosh , perform one of the
following actions: Type .exit , exit , or exit() . Type quit or quit() . Press Ctrl + D . Press Ctrl + C twice. Non-genuine Deployments The shell displays a warning message when you connect to non-genuine
MongoDB instances. Non-genuine instances may behave differently from the
official MongoDB instances due to missing, inconsistent, or incomplete
features. Limitations Kerberos authentication does not allow authMechanismProperties=CANONICALIZE_HOST_NAME:true|false in the
connection string. Instead, use either: authMechanismProperties=CANONICALIZE_HOST_NAME:forward authMechanismProperties=CANONICALIZE_HOST_NAME:forwardAndReverse authMechanismProperties=CANONICALIZE_HOST_NAME:none mongosh currently only supports the zlib compressor . The following
compressors are not supported: zstd snappy Starting in mongosh 2.0.0: For boolean values in connection strings , you: must use true or false . cannot use 1 , y , yes , or t instead of true . cannot use -1 , 0 , n , no , or f instead of false . Back Verify Windows Packages Next Configure
