# Connect via Compass - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods Connect via Compass On this page Prerequisites Connect to Your Cluster Troubleshooting The Connect dialog box for a cluster provides the details to
connect to a cluster using Compass . Prerequisites TLS Use MongoDB Compass 1.5 or later to connect to Atlas clusters. These
versions support the required SNI TLS extension. MongoDB Compass To complete this procedure, do one of the following: Install MongoDB Compass . See Compass Installation . Upgrade to the latest version of MongoDB Compass by downloading MongoDB Compass from links in the Atlas Connect dialog box. To access these
links, click Connect for the cluster you
wish to connect to, then click Compass . IP Access List To access a cluster, you must connect from an IP address on the Atlas project's IP access list. If you need to add an IP address to
the IP access list, you can do so in the Connect dialog box.
You can also add the IP address from the Network Access tab . Database User To access a cluster, you must create a database user with access to the
desired databases on your Atlas cluster. Database users are
separate from Atlas users. Database users have access to MongoDB
databases, while Atlas users have access to the Atlas application itself. You can create a database user to access your Atlas cluster in
the Connect dialog box. You can also add the database user from
the Cluster view . Connect to Your Cluster Compass 1.8 and later Compass 1.7 or earlier Use the following procedure to connect MongoDB Compass 1.8 or later
versions to your Atlas cluster. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Click Connect Click Connect for the cluster to
which you want to connect. 3 Choose your Connection Security. Choose Connection Type from the set of available buttons. Note Options Display if Feature Enabled Atlas displays the connection type options after you enable Private IP for Peering , Private Endpoint , or
both. If you haven't enabled either feature, no buttons display
and Connection Type defaults to Standard . Standard Connection Private IP for Peering Private Endpoint Connection Use this connection type for allowed public IP addresses. Use this connection type if you enabled peering: For Google Cloud or Azure and are connecting with Compass
from a peered network, or For AWS and are connecting with Compass from a
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
endpoint if you are connecting with Compass over a
Private Endpoint connection either because Compass: Runs inside your cloud provider network, or Has transitive network access to your cloud provider network. You want to use an optimized connection string . If none of these apply, add your IP address to your IP
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
database user, click Choose Your Connection Method . 6 Get the Connection String for MongoDB Compass from Atlas . Click I have MongoDB Compass . Choose your version of MongoDB Compass in the dropdown. To check
the version of MongoDB Compass that you have installed on your system,
click About MongoDB Compass in the application. Copy the connection string presented in the Atlas Connect dialog box. 7 Open MongoDB Compass and Connect to Atlas . Paste Connection String Fill in Connection Fields Individually Use the copied connection string for connecting to MongoDB Compass if
your deployment uses a single cloud provider or doesn't use any
of the following: SSL, authentication certificates, or an SSH tunnel. Click New Connection and paste the connection
string into the Paste your connection string field. ( Optional ) To save this connection for future use, click Create Favorite and add a name for this connection.
You can find saved favorite connections under Favorites in the left pane of the MongoDB Compass Connect window. Click Connect . Fill in connection fields individually if your deployment spans
more than one cloud provider or if it uses one of the following:
SSL, authentication certificates, or an SSH tunnel. Click Fill in Connection Fields Individually . Under the hostname tab, enter the hostname and port,
and choose your authentication mechanism from the dropdown. Under the More options tab, configure the following: If your deployment uses SSL or an SSH tunnel, specify
SSL or SSH tunnel options. If your deployment spans more than one cloud provider,
specify read preference options . If your deployment uses X.509 certificates, add a self-managed X.509 certificate or an auto-generated X.509 certificate managed by Atlas . To learn more, see Connect to MongoDB in the MongoDB Compass documentation. ( Optional ) To save this connection for future use, click Create Favorite and add a name for this connection.
You can find saved favorite connections under Favorites in the left pane of the MongoDB Compass Connect window. Click Connect . For MongoDB Compass 1.7 or earlier versions, you can manually
create a new connection in Compass . To set up a New Connection from MongoDB Compass to your Atlas cluster, enter the following information in MongoDB Compass and click Connect : Field Name Description Hostname Hostname of primary for a replica set or the hostname
for the mongos for a sharded cluster. To locate the hostname of the replica set primary in
the Atlas UI: In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. Click the cluster to which you want to connect. Click the replica set member marked as PRIMARY . Copy the hostname of the replica set. To locate the hostname for a sharded cluster in the Atlas user interface: Click Connect for the cluster. Click Drivers . Extract the mongos hostname from the URI connection string . Make note of the port number of the primary or mongos . Use that port to fill in the Port field in MongoDB Compass . Port Port of the primary for a replica set or the port of
the mongos for a sharded cluster. Authentication Select Username / Password . Username MongoDB user. The Atlas connection string
displays the MongoDB administration user set up for
the cluster. You can connect with a different MongoDB
user. Password Password associated with the specified MongoDB user. Authentication Database Specify "admin" . Replica Set Name Name of the Atlas cluster's replica set. To retrieve the replica set name: Click the Connect button for the
cluster. Select Connect Your Application . Extract the replica set name from the URI connection string's replicaSet value. Read Preference Specify how MongoDB Compass directs read operations. Options
are Primary , Primary Preferred , Secondary , Secondary Preferred , and Nearest . See /core/read-preference . SSL Select "Use System CA / Atlas Deployment" SSH Tunnel Select "Off" Favorite Name Enter a name for the connection if you want to save it
as a favorite. Troubleshooting If you are experiencing issues connecting to your cluster, see Troubleshoot Connection Issues . Back Drivers Next mongosh
