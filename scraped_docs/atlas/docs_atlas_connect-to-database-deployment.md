# Connect to a Cluster - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Connect to a Cluster On this page Considerations Prerequisites Connect to Your Cloud Cluster Connect to a Local Deployment with the Atlas CLI Troubleshooting Considerations Atlas does not guarantee that host names remain consistent with
respect to node types during topology changes. Example If you have a cluster named foo123 containing an analytics
node foo123-shard-00-03-a1b2c.mongodb.net:27017 , Atlas does
not guarantee that specific host name will continue to refer to an
analytics node after a topology change, such as scaling a cluster to modify its
number of nodes or regions. Improve Connection Performance for Sharded Clusters Behind a Private Endpoint Atlas can generate an optimized SRV connection string for sharded
clusters using the load balancers from your private endpoint
service. When you use an optimized connection string, Atlas limits
the number of connections per mongos between your application and
your sharded cluster. The limited connections per mongos improve performance during spikes in connection counts. Note Atlas doesn't support optimized connection strings for
clusters that run on Google Cloud or Azure . To use an optimized connection string, you must meet all of the following criteria: Configure a sharded cluster . Ensure that the sharded cluster runs on AWS . Ensure that the sharded cluster runs MongoDB version 5.0 or
later. If your cluster currently runs an earlier version of
MongoDB, upgrade your cluster's MongoDB version to version 5.0 or later to use an
optimized SRV connection string. Set up a private endpoint for your
cluster. Use either: A single-region cluster or A multi-region cluster with regionalized private endpoints enabled. Only the AWS regions in a
multi-region cluster support an optimized SRV connection string. Atlas doesn't support
optimized connections to multi-region clusters using a single SRV record. Connect using one of the following methods: Connect using a driver that meets or exceeds the minimum driver version for optimized connections . Connect using Compass . Connect using mongosh . Note If your cluster meets the criteria for optimized SRV strings, Atlas generates an Optimized SRV Connection string for you. If your cluster ever had legacy connection strings, Atlas maintains those strings indefinitely and includes a Legacy SRV Connection string when you select the Private Endpoint connection type. Consider switching to
the Optimized SRV Connection for optimal performance and
update your connection string wherever you use it. If you create the cluster and enable private endpoints after Atlas released this feature, Atlas displays the optimized
connection string by default when you select the Private Endpoint connection type. You can identify an
optimized connection string by the addition of lb to the
connection string as shown in the following example: mongodb+SRV://User1:P@ssword@cluster0-pl-0-lb.oq123.mongodb-dev.net/ To disable optimized connection strings for clusters that don't
have the Legacy SRV Connection option, contact support . Use Optimized Connection Strings with a Driver To learn how to connect using a driver and an optimized connection
string, select the Private Endpoint Connection tab in the Connect Your Application procedure . Use Optimized Connection Strings with Compass To learn how to connect using Compass and an optimized connection
string, select the Private Endpoint Connection tab in the Connect to your Cluster procedure . Use Optimized Connection Strings with mongosh To learn how to connect using mongosh and an optimized connection
string, select the Private Endpoint Connection tab in the Connect to your Cluster procedure . Prerequisites IP Access List To access a cluster, you must connect from an IP address on the Atlas project's IP access list. If you need to add an IP address to
the IP access list, you can do so in the Connect dialog box.
You can also add the IP address from the Network Access tab . Database User To access a cluster, you must create a database user with access to the
desired databases on your Atlas cluster. Database users are
separate from Atlas users. Database users have access to MongoDB
databases, while Atlas users have access to the Atlas application itself. You can create a database user to access your Atlas cluster in
the Connect dialog box. You can also add the database user from
the Cluster view . Open Ports 27015 to 27017 to Access Atlas Databases Make sure your application can reach your MongoDB Atlas environment. To add the inbound network access from your application environment to Atlas , do one of the following: Add the public IP addresses to your IP access list Use VPC / VNet peering to add private IP
addresses. Add private endpoints . Tip See also: IP Access List If your firewall blocks outbound network connections, you must also
open outbound access from your application environment to Atlas .
You must configure your firewall to allow your applications to make
outbound connections to ports 27015 to 27017 to TCP traffic on Atlas hosts. This grants your applications access to databases
stored on Atlas . Note By default, MongoDB Atlas clusters do not need to be able to
initiate connections to your application environments. If you wish
to enable Atlas clusters with LDAP authentication and authorization ,
you must allow network access from Atlas clusters directly to
your secure LDAP . You can allow access to your LDAP by using
public or private IPs as long as a public DNS hostname points to
an IP that the Atlas clusters can access. If you are not using VPC / VNet peering and plan
to connect to Atlas using public IP addresses, see the following
pages for additional information: Can I specify my own VPC for my MongoDB Atlas project? Do Atlas cluster's public IPs ever change? Connect to Your Cloud Cluster In order to connect to your cluster, you must get your
deployment's connection string .
Once you have the connection string, you can connect to your deployment
by using the following connection methods: Connect via Drivers Connect via Compass Connect via mongosh Connect via VS Code Note To connect using mongodump or mongorestore ,
use the Command Line Tools tab. The tab
creates an auto-generated template for connecting to your Atlas cluster with your preferred tool. To get your deployment's connection string, you can
use the Atlas CLI or Atlas UI: Atlas CLI Atlas UI You can use the Atlas CLI to get your deployment's standard connection string. To return the SRV connection strings for your Atlas cluster using the
Atlas CLI, run the following command: atlas clusters connectionStrings describe <clusterName> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas clusters connectionStrings describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI For example, if the Atlas CLI returns the following connection string: mongodb+srv://mycluster.abcd1.mongodb.net You can connect to your deployment using mongosh by including the connection string
in the mongosh command: mongosh "mongodb+srv://mycluster.abcd1.mongodb.net/myFirstDatabase" --apiVersion 1 --username <username> Note To successfully connect to Atlas , you must add your username and database name
to the connection string. In some cases, such as when you're using mongosh from the terminal, Atlas prompts you to enter the password for the database user. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Click Connect . Click Connect for the cluster to
which you want to connect. 3 Choose how you want to limit connections to your cluster. Standard Connection Private IP for Peering Private Endpoint Connection Add a Connection IP Address Important Skip this step if Atlas indicates in the Setup connection security step that you have
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
endpoint you want to use. 4 Create a Database User. Important Skip this step if Atlas indicates in the Setup connection security step that you have at least
one database user configured in your project. To manage existing
database users, see Configure Database Users . To access the cluster, you need a MongoDB user with access to the
desired database or databases on the cluster in your project. If your
project has no MongoDB users, Atlas prompts you to create a new
user with the Atlas Admin role. Enter the new user's Username . Enter a Password for this new user or click Autogenerate Secure Password . Click Create Database User to save the user. Use this user to connect to your cluster in the following step. Once you have added an IP address to your IP access list and added a
database user, click Choose Your Connection Method . 5 Click Choose a connection method . Connect to a Local Deployment with the Atlas CLI To connect to an Atlas deployment using the
Atlas CLI, run the following command: atlas deployments connect [deploymentName] [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas deployments connect . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Troubleshooting If you are experiencing issues connecting to your cluster, see Troubleshoot Connection Issues . Tip See also: Connect via Drivers Connect via Compass Connect via mongosh Connect via BI Connector for Atlas Browse Data via the Atlas UI Test Primary Failover Manage Connections with AWS Lambda Connection Limits and Cluster Tier Connect via VS Code Back Cloud Providers and Regions Next Drivers
