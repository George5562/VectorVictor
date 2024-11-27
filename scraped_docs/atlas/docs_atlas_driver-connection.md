# Connect via Drivers - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods Connect via Drivers On this page Prerequisites Connect Your Application Driver Examples Troubleshooting The Connect dialog box for a cluster provides the details to
connect to a cluster with an application using a MongoDB driver . Note Serverless instances don't support connecting via certain drivers
or driver versions at this time. To learn more, see Serverless Instance Limitations . â¤ Use the Select your language drop-down menu to set the
language of the example on this page. Prerequisites C C++11 C# Go Java (Sync) Kotlin (Coroutine) Node.js Perl PHP Python Ruby Rust (Async) Rust (Sync) Scala Swift (Async) Swift (Sync) Important Dedicated Cluster Limitation If you run the C# driver with .NET 5.0 on Linux, you cannot
connect to MongoDB 4.0 on dedicated clusters in Atlas .
This issue applies only to Atlas dedicated clusters. This
issue does not impact cluster tiers M0 through M5. If you
run an earlier .NET or .NET Core version and want to
upgrade to .NET 5.0, contact MongoDB Atlas Support. Driver Version Your driver version must be compatible with your version of the MongoDB
server. We recommend choosing the latest driver that is compatible with
your MongoDB server version to use the latest database features and
prepare for future version upgrades. For a list of driver versions that contain the full set of
functionality for your version of the MongoDB server, check the
compatibility matrix for your MongoDB driver . For a list of driver versions that you can use to connect to
Serverless instances, see Minimum Driver Versions for Serverless Instances . Optimized Connection Strings for Sharded Clusters Behind a Private Endpoint To connect to your sharded cluster using a driver and an optimized connection string , you
must use at least one of the following driver versions: Driver Version C 1.19.0 C++ 3.7.0beta1 C# 2.13.0 Go 1.6.0 Java 4.3.0 Kotlin 4.10.0 Motor 2.5.0 Node.js 4.1.0 PHP 1.11.0 (Extension) 1.10.0 (Library) PyMongo 3.12.0 Ruby 2.16.0 Rust 2.1.0 Scala 4.3.0 Swift 1.2.0 TLS Clients must support TLS to connect to an Atlas cluster. Clients must support the SNI TLS extension to
connect to an Atlas M0 Free cluster or M2/M5 Shared cluster.
To verify that your MongoDB driver supports the SNI TLS extension, refer to the Compatibility section of your
driver's documentation. If the driver is compatible with MongoDB 4.2
and later, it supports the SNI TLS extension. IP Access List To access a cluster, you must connect from an IP address on the Atlas project's IP access list. If you need to add an IP address to
the IP access list, you can do so in the Connect dialog box.
You can also add the IP address from the Network Access tab . Database User To access a cluster, you must create a database user with access to the
desired databases on your Atlas cluster. Database users are
separate from Atlas users. Database users have access to MongoDB
databases, while Atlas users have access to the Atlas application itself. You can create a database user to access your Atlas cluster in
the Connect dialog box. You can also add the database user from
the Cluster view . Connect Your Application 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Click Connect . Click Connect for the cluster to
which you want to connect. 3 Choose your Connection Security. Choose Connection Type from the set of available buttons. Note Options Display if Feature Enabled Atlas displays the connection type options after you enable Private IP for Peering , Private Endpoint , or
both. If you haven't enabled either feature, no buttons display
and Connection Type defaults to Standard . Standard Connection Private IP for Peering Private Endpoint Connection Use this connection type for allowed public IP addresses. Use this connection type if you enabled peering: For Google Cloud or Azure and are connecting with your driver
from a peered network, or For AWS and are connecting with your driver from a
peered network which uses a custom DNS service. If neither of these apply, add your IP address to your IP
access list and use the Standard Connection string. If you are
connecting directly to Atlas from an office or home
network, this might be the preferred option. Note Peer must be available You can't select this option unless one of your peers
is marked as AVAILABLE . To check the status of your peers : In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. Note Multi-Cloud Clusters If your application isn't hosted on the same cloud service
provider as your cluster's primary , the application
can only perform secondary reads. With multi-cloud clusters, consider adding the readPreference connection option to your connection string .
Use one of the following values: primaryPreferred secondary secondaryPreferred Use the connection string for the appropriate interface
endpoint if you are connecting with your driver over a
Private Endpoint connection either because your driver: Runs inside your cloud provider network, or Has transitive network access to your cloud provider network. You want to use an optimized connection string . If none of these apply, add your IP address to your IP
access list and use the Standard Connection string. If you are
connecting directly to Atlas from an office or home
network, this might be the preferred option. Note You can't select this option unless your configured
PrivateLink connection is ready to use. To check the status of your AWS PrivateLink : In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 4 Choose how you want to limit connections to your cluster. Standard Connection Private IP for Peering Private Endpoint Connection Add a Connection IP Address Important Skip this step if Atlas indicates in the Setup connection security step that you have
already configured an IP access list entry in your cluster.
To manage the IP access list, see Add Entries to the Access List . Atlas allows standard client connections to the cluster
from entries in the project's IP access list . The project IP access list differs from the API access list , which
restricts API access to specific IP or CIDR addresses. If the IP access list is empty, Atlas prompts you to add an
IP address to the project's IP access list. You can either: Click Add Your Current IP Address to allow
access from your current IP address. Click Add an IP Address to add a single IP
address or a CIDR -notated range of addresses. Provide an optional description for the newly added IP address
or CIDR range. Click Add IP Address to add the
address to the IP access list. Add a Connection IP Address Important Skip this step if Atlas indicates in the Setup connection security step that you have
already configured an IP access list entry in your cluster.
To manage the IP access list, see Add Entries to the
IP access list . Atlas allows standard client connections to the cluster
from entries in the project's IP access list . The project IP access list differs from the API access list , which
restricts API access to specific IP or CIDR addresses. If the IP access list is empty, Atlas prompts you to add an
IP address to the project's IP access list. Click Add a Different IP Address to add a single IP
address or a CIDR -notated range of addresses. Provide an optional description for the newly added IP address
or CIDR range. Click Add IP Address to add the
address to the IP access list. Under Choose Connection Type , select Private Endpoint . If you see the Private Link Type options,
select one of the following options: Optimized SRV Connection for
load-balanced connections. Legacy SRV Connection for
non-load-balanced connections. To learn more, see Improve Connection Performance for Sharded Clusters Behind a Private Endpoint . Under Choose Private Endpoint , select the
endpoint you want to use. 5 Create a Database User. Important Skip this step if Atlas indicates in the Setup connection security step that you have at least
one database user configured in your project. To manage existing
database users, see Configure Database Users . To access the cluster, you need a MongoDB user with access to the
desired database or databases on the cluster in your project. If your
project has no MongoDB users, Atlas prompts you to create a new
user with the Atlas Admin role. Enter the new user's Username . Enter a Password for this new user or click Autogenerate Secure Password . Click Create Database User to save the user. Use this user to connect to your cluster in the following step. Once you have added an IP address to your IP access list and added a
database user, click Choose Your Connection Method . 6 Select Drivers . In the Choose a connection method step, select Drivers . 7 Select Your Driver and Version. Select your driver and version from the dropdown menus.
The code sample containing a connection string displays.
Replace <password> with the password specified when you created
your database user. Note If your passwords, database names, or connection strings contain
reserved URI characters, you must escape the characters. For example,
if your password is @bc123 , you must escape the @ character when specifying the password in the connection
string, such as %40bc123 . To learn more, see Special Characters in Connection String Password . To learn more, see Driver Compatibility . Driver Examples In the following example, you authenticate and connect to an Atlas cluster by using a URI connection string . Replace the placeholders in the example
with your credentials and deployment details. C C++11 C# Go Java (Sync) Kotlin (Coroutine) Node.js Perl PHP Python Ruby Rust (Async) Rust (Sync) Scala Swift (Async) Swift (Sync) Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a C driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
C driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. client = mongoc_client_new ( "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" ) ; db = mongoc_client_get_database (client, "<databaseName>" ) ; MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 1.11 and later Behavior Note The following configuration options only apply if running the C
driver in single-threaded mode . MongoDB drivers automatically attempt server selection following
a cluster election or failover event. By default, the C
driver immediately raises an error if its first attempt to select
a server fails. The following configuration settings may improve
application connectivity to an Atlas cluster at the expense of
spending more time in a server selection loop: Set serverSelectionTryOnce to false to direct the C driver to
perform server selection up to the time limit defined by serverSelectionTimeoutMS . Lower the serverSelectionTimeoutMS to 15000 from the default of 30000 . MongoDB elections
typically take 10 seconds, but can be as fast as 5 seconds on Atlas . Setting this value to 15 seconds
( 15000 milliseconds) covers the upper bound of election plus
additional time for latency. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a C++ driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
C++ driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. # include <mongocxx/client.hpp> # include <mongocxx/instance.hpp> //... mongocxx:: instance inst{}; mongocxx:: client conn{ mongocxx:: uri{ "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" }}; mongocxx:: database db = conn[ "<databaseName>" ]; MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. Note The Legacy C++ driver has reached End-Of-Life, and is no
longer supported. Behavior Note The following configuration options only apply when using the C++
driver's single-threaded mongocxx::client class to connect to the Atlas cluster. MongoDB drivers automatically attempt server selection following
a cluster election or failover event. By default, the C++
driver immediately raises an error if its first attempt to select
a server fails. The following configuration settings may improve
application connectivity to an Atlas cluster at the expense of
spending more time in a server selection loop: Set serverSelectionTryOnce to false to direct the C++ driver to
perform server selection up to the time limit defined by serverSelectionTimeoutMS . Lower the serverSelectionTimeoutMS to 15000 from the default of 30000 . MongoDB elections
typically take 10 seconds, but can be as fast as 5 seconds on Atlas . Setting this value to 15 seconds
( 15000 milliseconds) covers the upper bound of election plus
additional time for latency. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a C#/.Net driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
C#/.Net driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. var client = new MongoClient( "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" ); var database = client.GetDatabase( "<databaseName>" ); MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 2.7 and later Note Microsoft .NET Core library versions 2.1 and later support the SNI TLS extension on Linux and macOS.
Applications using prior versions of .NET Core on these
platforms cannot connect to an Atlas M0 Free cluster or M2/M5 Shared cluster. To learn more this requirement, see this dotnet/corefx issue . Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Go driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Go driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. uri := "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" ctx, cancel := context.WithTimeout(context.Background(), 10 *time.Second) defer cancel() client, err := mongo.Connect(ctx, options.Client().ApplyURI(uri)) if err != nil { panic (err) } defer func () { if err = client.Disconnect(ctx); err != nil { panic (err) } }() // Ping the primary if err := client.Ping(ctx, readpref.Primary()); err != nil { panic (err) } MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 1.0.0 and later Note To connect to an Atlas M0 cluster, you must use
Java version 8 or later and use a Java driver version that
supports MongoDB 4.0 or later. To learn more about compatibility
between the Java driver and MongoDB, see the MongoDB compatibility matrix . MongoClientURI uri = new MongoClientURI ( "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" ); MongoClient mongoClient = MongoClients.create(uri); MongoDatabase database = mongoClient.getDatabase( "<databaseName>" ); MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 3.8 and later Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Kotlin driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Kotlin driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. val uri = "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" // Construct a ServerApi instance using the ServerApi.builder() method val serverApi = ServerApi.builder() .version(ServerApiVersion.V1) .build() val settings = MongoClientSettings.builder() .applyConnectionString(ConnectionString(uri)) .serverApi(serverApi) .build() // Create a new client and connect to the server val mongoClient = MongoClient.create(settings) val database = mongoClient.getDatabase( "<databaseName>" ) try { // Send a ping to confirm a successful connection val command = Document( "ping" , BsonInt64( 1 )) val commandResult = database.runCommand(command) println( "Pinged your deployment. You successfully connected to MongoDB!" ) } catch (me: MongoException) { System.err.println(me) } MongoDB Version Recommended Driver Versions MongoDB 5.0 and later Version 4.10 and later Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Node.js driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Node.js driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. import mongodb from 'mongodb' ; const MongoClient = mongodb. MongoClient ; const uri = "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" ; const client = new MongoClient ( uri , { useNewUrlParser : true }) ; client. connect ( err => { const collection = client. db ( "<databaseName>" ). collection ( "<collectionName>" ) ; // perform actions on the collection object client. close ( ) ; }) ; To connect to a database other than admin but still authenticate
to the admin database, update the database component of the
connection string. mongodb://username:password@host1:port1,...,hostN:portN/database?authSource=admin&... Example The following connection string specifies the cluster0 deployment and test database component, and includes the authSource=admin option. var uriTestDb = "mongodb+srv://<db_username>:<db_password>@cluster0.mongodb.net/test?ssl=true&authSource=admin&w=majority" ; MongoClient . connect ( uriTestDb , function ( err, db ) { db. close ( ) ; }) ; MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 3.1 and later Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Perl driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Perl driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. my $client = MongoDB - > connect ( 'mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority' ) ; my $db = $client - > get_database ( '<databaseName>' ) ; MongoDB Version Recommended Driver Versions MongoDB 4.2 MongoDB no longer maintains a Perl driver; driver version
2.2.2, which supports up to MongoDB 4.2, is available at https://metacpan.org/pod/MongoDB Behavior MongoDB drivers automatically attempt server selection following
a cluster election or failover event. By default, the Perl
driver immediately raises an error if its first attempt to select
a server fails. The following configuration settings may improve
application connectivity to an Atlas cluster at the expense of
spending more time in a server selection loop: Set serverSelectionTryOnce to false to direct the Perl driver to
perform server selection up to the time limit defined by serverSelectionTimeoutMS . Lower the serverSelectionTimeoutMS to 15000 from the default of 30000 . MongoDB elections
typically take 10 seconds, but can be as fast as 5 seconds on Atlas . Setting this value to 15 seconds
( 15000 milliseconds) covers the upper bound of election plus
additional time for latency. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a PHP driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
PHP driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. The following example uses the MongoDB PHP Library which provides a
high-level abstraction around the lower-level PHP driver: $client = new MongoDB\ Client ( 'mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority' ) ; $db = $client -><databaseName>; MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later PHPLIB 1.4 + mongodb-1.5. Behavior MongoDB drivers automatically attempt server selection following
a cluster election or failover event. By default, the
driver immediately raises an error if its first attempt to select
a server fails. The following configuration settings may improve
application connectivity to an Atlas cluster at the expense of
spending more time in a server selection loop: Set serverSelectionTryOnce to false to direct the  driver to
perform server selection up to the time limit defined by serverSelectionTimeoutMS . Lower the serverSelectionTimeoutMS to 15000 from the default of 30000 . MongoDB elections
typically take 10 seconds, but can be as fast as 5 seconds on Atlas . Setting this value to 15 seconds
( 15000 milliseconds) covers the upper bound of election plus
additional time for latency. Note To connect to an Atlas M0 cluster, you must use
Python 2.7.9 or later and use a Python driver version that supports
MongoDB 4.0 or later. To learn more about compatibility between the Python
driver and MongoDB, see the MongoDB compatibility matrix . import pymongo import dns # required for connecting with SRV client = pymongo.MongoClient( "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" ) db = client.<databaseName> MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 3.7 and later Note macOS and Python 3.6 Installers The Python 3.6 installers for macOS from https://www.python.org do not automatically install
any CA certificates. Without installed CA certificates,
connections to Atlas will fail certificate
verification. After you run the installer from https://www.python.org to install Python 3.6, you
must run the following script to install an up-to-date CA
bundle before connecting to Atlas : open "/Applications/Python 3.6/Install Certificates.command" For more information on Python 3.6 installers for macOS
from https://www.python.org , see https://bugs.python.org/issue29065#msg283984 . Earlier
versions of Python as well as Python 3.6 installed by
other means (e.g. Homebrew ), are not affected. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Ruby driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Ruby driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. client = Mongo::Client .new( 'mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority' ) To connect to a database other than admin but still authenticate
to the admin database, update the database component of the
connection string. mongodb://username:password@host1:port1,...,hostN:portN/database?authSource=admin&... Example The following connection string specifies the cluster0 deployment and the test database component, and includes the authSource=admin option. client = Mongo::Client .new( 'mongodb+srv://<db_username>:<db_password>@cluster0.mongodb.net/test?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin&w=majority' ) MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. MongoDB 5.0 and later Version 2.6 and later Mongoid Example production: # Configure available database clients. (required) clients: # Defines the default client. (required) default: # Defines the name of the default database that Mongoid can connect to. # (required). database: 'myDatabaseName' # Provides the hosts the default client can connect to. Must be an array # of host:port pairs. (required) hosts: - mycluster0-shard-00-00.mongodb.net:27017 - mycluster0-shard-00-01.mongodb.net:27017 - mycluster0-shard-00-02.mongodb.net:27017 options: # The name of the user for authentication. user: <username> # The password of the user for authentication. password: <password> # The database or source to authenticate the user against. If the database # specified above is not admin, admin MUST be specified here. auth_source: admin # All Atlas servers use SSL. (default: false) ssl: true MongoDB Version Minimum ODM Version MongoDB 5.0 and later Version 7.0.0 and later The default async runtime used by the driver is tokio . To use a
different runtime, see Configuring the async runtime . Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Rust driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Rust driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. use mongodb:: { options:: ClientOptions, Client}; #[tokio::main] async fn main () -> mongodb:: error:: Result <()> { let client_options = ClientOptions:: parse ( "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" , ) . await ?; let client = Client:: with_options (client_options)?; let _database = client. database ( "<databaseName>" ); // List the names of the databases in that cluster for db_name in client. list_database_names ( None , None )? { println! ( "{}" , db_name); } Ok (()) } MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. Make sure you enabled the sync API. See Enabling the sync API for more details. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Rust driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Rust driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. use mongodb:: { bson:: doc, sync:: Client}; fn main () -> mongodb:: error:: Result <()> { let client_options = ClientOptions:: parse ( "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" , )?; // Ping the server to see if you can connect to the cluster client . database ( "admin" ) . run_command (doc! { "ping" : 1 }, None )?; println! ( "Connected successfully." ); // List the names of the databases in that cluster for db_name in client. list_database_names ( None , None )? { println! ( "{}" , db_name); } Ok (()) } MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Scala driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Scala driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. val uri: String = "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" System .setProperty( "org.mongodb.async.type" , "netty" ) val client: MongoClient = MongoClient (uri) val db: MongoDatabase = client.getDatabase( "<databaseName>" ) MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Swift driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Swift driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. import MongoSwift import NIO let elg = MultiThreadedEventLoopGroup ( numberOfThreads: 4 ) let uri = "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" let client = try MongoClient ( uri, using: elg ) defer { // clean up driver resources try? client.syncClose () cleanupMongoSwift () // shut down EventLoopGroup try? elg.syncShutdownGracefully () } // print a list of database names to confirm connection print ( try client.listDatabaseNames () .wait () ) MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. Note To connect to an Atlas M0 Free cluster or M2/M5 shared
cluster, you must use a Swift driver version that supports
MongoDB 4.0 and later. For complete documentation on compatibility between the
Swift driver and MongoDB, see the MongoDB compatibility matrix . We recommend that you
upgrade to the latest version of the driver. import MongoSwiftSync let uri = "mongodb+srv://<db_username>:<db_password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority" let client = try MongoClient (uri) // print a list of database names to confirm connection print ( try client.listDatabaseNames () ) MongoDB Version Recommended Driver Versions All See the MongoDB compatibility matrix for the
latest recommended driver versions. Troubleshooting If you are experiencing issues connecting to your cluster, see Troubleshoot Connection Issues . Tip See also: Connection Limits and Cluster Tier Back Connection Methods Next Compass
