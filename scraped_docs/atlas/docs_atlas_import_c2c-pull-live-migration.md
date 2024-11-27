# Live Migrate (Pull) a MongoDB 6.0.17+ or 7.0.13+ Cluster into Atlas - MongoDB Atlas


Docs Home / MongoDB Atlas / Migrate or Import Data / Live Migrate a 6.0.17+ or a 7.0.13+ Cluster Live Migrate (Pull) a MongoDB 6.0.17+ or 7.0.13+ Cluster into Atlas On this page Restrictions Supported Migration Paths Required Access Supported Source and Destination Cluster Configuration Pairs Prerequisites Considerations Migrate Your Cluster Migration Support Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . If both the source and destination clusters are running MongoDB 6.0.17+
or 7.0.13+, Atlas can pull a source cluster to an Atlas cluster using the procedure described in this section. This process uses mongosync as the underlying data migration tool,
enabling faster live migrations with less downtime: Atlas syncs data from the source to the destination cluster until
you cut your applications over to the destination Atlas cluster. Once you reach the cutover step in the following procedure: Stop writes to the source cluster. Stop your application instances, point them to the Atlas cluster,
and restart them. Restrictions The Cluster-to-Cluster Sync Limitations apply to this live migration. Live migration (pull) doesn't support: MongoDB 8.0 or rapid releases as the source or destination cluster version. VPC peering or private endpoints for either the source or destination cluster. Live migration doesn't support migrating Atlas Search indexes from a source cluster to the destination cluster. Supported Migration Paths Atlas live migration described in this section supports the following
migration paths: Source Cluster MongoDB Version Destination Atlas Cluster MongoDB Version 6.0.17 6.0.17 7.0.13 7.0.13 Required Access To live migrate your data, you must have Project Owner access
to Atlas . Users with Organization Owner access must add themselves to the
project as a Project Owner . Supported Source and Destination Cluster Configuration Pairs For this type of live migration, Atlas supports the following source
and destination cluster configuration pairs: Source Cluster Configuration Destination Cluster Configuration Live Migration Support Notes Standalone Any type of cluster Before migrating a standalone source cluster using this
migration procedure, convert the standalone to a replica set . Replica Set Replica Set Replica Set Sharded Cluster When you run this type of migration, you may specify sharding parameters.
To learn more, see the live migration procedure in this section
and this sharding example . Sharded Cluster Sharded Cluster The number of shards in source and destination clusters might differ.
The source sharded cluster must use CSRS (Config Server Replica Sets).
To learn more, see Replica Set Config Servers . Sharded Cluster Replica Set Prerequisites If the cluster runs with authentication, meet the following prerequisites: For replica sets, grant the backup and readAnyDatabase roles on the admin database to the user that will run the migration process. For sharded clusters, grant the backup , readAnyDatabase ,
and clusterMonitor roles on the admin database to the user
that will run the migration process. Ensure the specified user exists
on every shard and the config server replica set.
The user must have permissions that allow the following actions: Stop or start the sharded cluster balancer. Read all databases and collections on the host. Read the oplog on the host. Ensure that this user is authenticated using both SCRAM-SHA-1 and SCRAM-SHA-256 .
To learn more, see Source Cluster Security . Important Source Cluster Readiness To help ensure a smooth data migration, your source cluster should
meet all production cluster recommendations. Check the Operations
Checklist and Production Notes before
beginning the Live Migration process. Network Access Configure network permissions for the following components: Source Cluster Firewall Allows Traffic from Live Migration Server Any firewalls for the source cluster must grant the MongoDB live migration
server access to the source cluster. The Atlas live migration process streams data through a
MongoDB-controlled live migration server. Atlas provides the IP ranges
of the MongoDB live migration servers during the live migration process.
Grant these IP ranges access to your source cluster. This allows the
MongoDB live migration server to connect to the source clusters. Note If your organization has strict network requirements
and you cannot enable the required network access
to MongoDB live migration servers,
see Live Migrate a Community Deployment to Atlas . Atlas Cluster Allows Traffic from Your Application Servers Atlas allows connections to a cluster from hosts added to the
project IP access list . Add the IP
addresses or CIDR blocks of your application hosts to the project IP
access list. Do this before beginning the migration procedure. Atlas temporarily adds the IP addresses of the MongoDB  migration
servers to the project IP access list. During the migration procedure,
you can't edit or delete this entry. Atlas removes this entry once
the procedure completes. To learn how to add entries to the Atlas IP access list, see Configure IP Access List Entries . Pre-Migration Validation Before starting the following live migration procedure, Atlas runs
validation checks on the source and destination clusters and verifies that: The source and destination cluster's MongoDB version is at least FCV 6.0.17+ and is matching, or at least FCV 7.0.13+ and
is matching. The source cluster's database user has the correct permissions as
described in Source Cluster Security . The destination Atlas cluster must have no data. If the cluster
has any data before you begin, you have the option to clear data on the
destination cluster during the live migration process. Alternatively,
you can manually delete the data on the destination cluster before
starting the migration procedure. Source Cluster Security Various built-in roles provide sufficient privileges. For example: For source replica set clusters, a MongoDB user must have the readAnyDatabase and backup roles. For source sharded clusters a MongoDB user must have the readAnyDatabase , backup , and clusterMonitor roles. To verify that the database user who will run the live migration process
has these roles, run the db.getUser() command on the admin database. For example, for a replica set, run: use admin db. getUser ( "admin" ) { "_id" : "admin.admin" , "user" : "admin" , "db" : "admin" , "roles" : [ { "role" : "backup" , "db" : "admin" } , { "role" : "readAnyDatabase" , "db" : "admin" } ] } ... Specify the username and password to Atlas when prompted by
the walk-through screen of the live migration procedure. Atlas only supports SCRAM for
connecting to source clusters that enforce authentication. How MongoDB Secures its Live Migration Servers In any pull-type live migration to Atlas , Atlas manages the server
that runs the live migration and sends data from the source to the destination
cluster. MongoDB takes the following measures to protect the integrity and confidentiality
of your data in transit to Atlas : MongoDB encrypts data in transit between the Atlas -managed live migration
server and the destination cluster. If you require encryption for data
in transit between the source cluster and the Atlas -managed migration
server, configure TLS on your source cluster. MongoDB protects access to the Atlas -managed migration server instances
as it protects access to any other parts of Atlas . In rare cases where intervention is required to investigate and restore
critical services, MongoDB adheres to the principle of least privilege
and authorizes only a small group of privileged users to access your Atlas clusters for a minimum limited time necessary to repair
the critical issue. MongoDB requires MFA for these users to log in to Atlas clusters and to establish an SSH connection via the bastion
host. Granting this type of privileged user access requires approval by
MongoDB senior management. MongoDB doesn't allow access by any other
MongoDB personnel to your MongoDB Atlas clusters. MongoDB allows use of privileged user accounts for privileged activities
only. To perform non-privileged activities, privileged users must use
a separate account. Privileged user accounts can't use shared credentials.
Privileged user accounts must follow the password requirements
described in Section 4.3.3 of the Atlas Security whitepaper. You can restrict access to your clusters by
all MongoDB personnel, including privileged users, in Atlas . If you
choose to restrict such access and MongoDB determines that access is
necessary to resolve a support issue, MongoDB must first request your
permission and you may then decide whether to temporarily restore privileged
user access for up to 24 hours. You can revoke the temporary 24-hour access
grant at any time. Enabling this restriction may result in increased time
for the response and resolution of support issues and, as a result, may
negatively impact the availability of your Atlas clusters. MongoDB reviews privileged user access authorization on a quarterly basis.
Additionally, MongoDB revokes a privileged user's access when it is no longer
needed, including within 24 hours of that privileged user changing roles
or leaving the company. We also log any access by MongoDB personnel to
your Atlas clusters, retain audit logs for at least six years,
and include a timestamp, actor, action, and output. MongoDB uses a
combination of automated and manual reviews to scan those audit logs. To learn more about Atlas security, see the Atlas Security whitepaper.
In particular, review the section "MongoDB Personnel Access to MongoDB Atlas Clusters". Considerations Network Encryption During pull live migrations, if the source cluster does not use TLS encryption
for its data, the traffic from the source cluster to Atlas is not
encrypted. Determine if this is acceptable before you start a pull live
migration procedure. Database Users and Roles Atlas doesn't migrate any user or role data to the destination cluster. If the source cluster doesn't use authentication, you must create a
user in Atlas because Atlas doesn't support running without authentication. If the source cluster enforces authentication, you must recreate the
credentials that your applications use on the destination Atlas cluster. Atlas uses SCRAM for user authentication.
To learn more, see Configure Database Users . Source and Destination Cluster Balancers To avoid any impact on write performance during migration, Atlas stops the sharded cluster balancers on the source and destination
clusters at the start of the procedure, and starts the balancers
at the end of the procedure. If you cancel live migration, Atlas restarts the balancers on the
source and destination clusters. If Atlas can't restart the load balancer on the source or
destination clusters at the end of a successful live migration,
a warning banner indicates that you must manually restart the source or destination cluster balancer. Destination Cluster Configuration When you configure the destination cluster, consider the following: The destination Atlas cluster must have no data. If the cluster
has any data before you begin, you have the option to clear data on the
destination cluster during the live migration process. Alternatively,
you can manually delete the data on the destination cluster before
starting the migration procedure. The live migration process streams data through a MongoDB-managed
live migration server. Each server runs on infrastructure hosted in the
nearest region to the source cluster. The following regions are
available: Europe Frankfurt Ireland London Americas Eastern US Western US APAC Mumbai Singapore Sydney Tokyo Use the cloud region for the destination cluster in Atlas that
has the lowest network latency relative to the application servers or to your
deployment hosted on the source cluster. Ideally, your application's
servers should be running in the cloud in the same region as the destination Atlas cluster's primary region. To learn more, see Cloud Providers . The destination cluster in Atlas must match or exceed the source
deployment in terms of RAM, CPU, and storage. Provision a destination
cluster of an adequate size so that it can accommodate both the
migration process and the expected workload, or scale up the destination cluster to a tier with more processing power, bandwidth or disk IO. To maximize migration performance, use at least an M40 cluster for the
destination cluster. When migrating large data sets, use an M80
cluster with 6000 IOPS disks or higher. You can also choose to temporarily increase the destination Atlas cluster's size for the duration of the migration process. After you migrate your application's workload to a cluster in Atlas , contact support for assistance with further
performance tuning and sizing of your destination cluster to minimize costs. To avoid unexpected sizing changes, disable auto-scaling on the destination
cluster. To learn more, see Manage Clusters . To prevent unbounded oplog collection growth, and to ensure that
the live migration's lag window stays within the bounds of the oplog
replication lag window, set an oplog size to a large enough fixed value for the duration of the live migration process. To learn more, see: Scale a Cluster Atlas Configuration Options oplog Sizing in the Cluster-to-Cluster Sync documentation. If you are observing performance issues even after you've followed these
recommendations, contact support . You can't select an M0 (Free Tier) or M2/M5 shared-tier
cluster as the destination cluster for live migration. Don't change the featureCompatibilityVersion flag while Atlas live migration is running. Avoid Workloads on the Destination Cluster Avoid running any workloads, including those that might be running on
namespaces that don't overlap with the live migration process, on the
destination cluster. This action avoids potential locking conflicts and
performance degradation during the live migration process. Don't run multiple migrations to the same destination cluster at the
same time. Don't start the cutover process for your applications to the destination
cluster while the live migration process is syncing. Avoid Cloud Backups Atlas stops taking on-demand cloud backup snapshots of the target cluster during live migration.
Once you complete the cutover step in the live migration procedure on
this page, Atlas resumes taking cloud backup snapshots based on
your backup policy . Avoid Elections The live migration process makes a best attempt to continue a migration
during temporary network interruptions and elections on the source or
destination clusters. However, these events might cause the live migration
process to fail. If the live migration process can't recover automatically,
restart it from the beginning. Migrate Your Cluster Note Staging and Production Migrations Consider running this procedure twice. Run a partial migration
that stops at the Perform the Cutover step first . This
creates an up-to-date Atlas -backed staging cluster to test
application behavior and performance using the latest driver version that
supports the MongoDB version of the Atlas cluster. After you test your application, run the full migration
procedure using a separate Atlas cluster to create your Atlas -backed production environment. Pre-Migration Checklist Before starting the live migration procedure: If you don't already have a destination cluster, create a
new Atlas deployment and configure it as needed. For complete
documentation on creating an Atlas cluster, see Create a Cluster . After your Atlas cluster is deployed, ensure that you can connect
to it from all client hardware where your applications run. Testing
your connection string helps ensure that your data migration process
can complete with minimal downtime. Download and install mongosh on a
representative client machine, if you don't already have it. Connect to your destination cluster using the connection string
from the Atlas UI. For more information, see Connect via mongosh . Once you have verified your connectivity to your destination cluster,
start the live migration procedure. Procedure 1 Start the migration process. Select a destination Atlas cluster. Navigate to the destination Atlas cluster and click the ellipsis ... button. On the cluster list, the ellipsis ... button appears beneath the cluster name. When
you view cluster details, the ellipsis ... appears
on the right-hand side of the screen, next to the Connect and Configuration buttons. Click Migrate Data to this Cluster . Atlas displays a walk-through screen with instructions on
how to proceed with the live migration. The process syncs the data
from your source cluster to the new destination cluster. After
you complete the walk-through, you can point your application to the
new cluster. Collect the following details for your source cluster to
facilitate the migration: For replica sets, the hostname and port of the source cluster primary . For example, mongoPrimary.example.net:27017 . Atlas only connects to the
primary member of the source cluster by default. To increase
resiliency and facilitate failover if needed, Atlas obtains
the IP addresses of other source cluster nodes if these nodes
have publicly available DNS records. For sharded clusters, the hostname and port of each mongos on each shard. For example, mongos.example.net:27017 . The database authentication username and password used to connect
to the source cluster. For replica sets, the database user must
have the readAnyDatabase and backup roles.
For sharded clusters, the database user must
have the readAnyDatabase , backup , and clusterMonitor roles. If the source cluster uses TLS/SSL and isn't using a public
Certificate Authority (CA), you will need the source cluster CA file. Prepare the information as stated in the walk-through screen,
then click I'm Ready To Migrate . Atlas displays a walk-through screen that collects information
required to connect to the source cluster. Atlas displays the IP address of the MongoDB live migration server
responsible for your live migration at the top of the walk-through
screen. Configure your source cluster firewall to grant access
to the displayed IP address. For replica sets, enter the hostname and port of the primary member
of the source cluster into the provided text box.
For sharded clusters, enter the hostname and port of each mongos . If you are migrating a replica set to a sharded cluster: If you'd like to shard collections, click the checkmark in Include sharding parameters and paste your sharding configuration
JSON into the text box using the sharding example .
Save this configuration in a file externally, in case you would like to
refer to it later. The sharding configuration JSON defines the shardingEntries array,
which specifies the collections to shard, and the keys to use for sharding.
MongoDB shards only those collections that you include into this array.
To learn more, see Sharding . If you omit specifying the sharding configuration, you can shard collections
on the destination cluster after you migrate your cluster to Atlas . In addition to the sharding configuration, a compatible index for the
specified sharding keys must exist on the destination cluster in service. Click the checkmark in Create supporting indexes so that
MongoDB automatically creates supporting shard key indexes on the
destination cluster in Atlas . If the source cluster enforces authentication, enter a username and
password into the provided text boxes. See Source Cluster Security for guidance on the
user permissions required by Atlas live migration. If the source cluster uses TLS/SSL and isn't using a public
Certificate Authority (CA), toggle the switch Is encryption in transit enabled? and copy the contents
of the source cluster CA file into the provided text box. If your destination cluster has any existing data, check the option
to delete this data: Clear any existing data on your destination cluster ,
and then enter the name of the destination cluster. Atlas deletes the existing data. If you leave this option unchecked and
the destination cluster has any data during the migration
process, the migration fails and issues a validation error. Click Validate to confirm that Atlas can connect to the
source cluster. If validation fails, check that: You have added Atlas to the IP access list on your source cluster. The provided user credentials, if any, exist on the source cluster
and have the required permissions. The Is encryption in transit enabled? toggle is enabled
only if the source cluster requires it. The CA file provided, if any, is valid and correct. Click Start Migration to start the migration process. Once the migration process begins, Atlas UI displays the Migrating Data walk-through screen for the destination Atlas cluster. The walk-through screen updates as the
destination cluster proceeds through the migration process.
The migration process includes: Applying new writes to the source cluster data to the destination
cluster data. Copying data from the source cluster to the destination cluster. Finalizing the migration on the destination cluster. A lag time value displays during the final phase of the migration process
that represents the current lag between the source and destination clusters. You receive an email notification when your expiration window is nearly up. When the lag behind source is close to zero and the migration process is caught up, Atlas activates the Cutover to your destination cluster button
and indicates that your source and destination clusters are in sync.
Proceed to the next step. 2 Perform the cutover. Cutover is a three-step process of directing your application's reads and writes
away from your source cluster and to your destination cluster. When Atlas detects that the source and destination clusters are
nearly in sync, it starts an extendable 120 hour (5 day) timer to begin
the cutover stage of the live migration procedure. After the 120 hour
period passes, Atlas stops synchronizing with the source cluster. At this stage in the migration process, you can proceed to cutover or
extend the syncing period and then proceed to cutover. If you click I'm ready to cutover , Atlas starts the cutover process. If you click Extend Sync , and if the extended sync completes successfully, Atlas confirms that source and destination clusters are in sync.
Proceed with the cutover process. If the sync time expires, you can retry the migration. If your migration is about to expire, Atlas sends you an email similar
to the following example: A migration to your Atlas cluster will expire in <number> hours! Navigate to your destination cluster to start the cutover process. If you don't take any action within <number> hours, the migration will be cancelled and you will need to start again. You can also extend the migration process if you need more time. Click I'm ready to cutover . Proceed with the three-step cutover
process quickly to ensure minimal downtime to your application. Click Proceed to cutover . The three-step cutover process begins: Stop writes to your source cluster. Click I confirm that I've stopped writes to my source cluster .
Click Finalize migration to proceed. Wait a few minutes while Atlas finalizes the migration. Atlas performs these actions to complete the process: Removes the MongoDB live migration server subnets from the IP access
list on the destination cluster. Removes the database user that live migration used to import data
to the destination cluster. If the cutover process has been in progress for at least 12 hours, Atlas sends you an email that suggests you check on the migration
process or contact support. If the migration succeeds, the You have successfully migrated to Atlas page displays. Atlas shows the status of the synced changes, the application downtime,
the duration of the migration process, the amount of initial data copied,
and the number of copied collections. Verify that your data is transferred to the destination cluster
by comparing document counts and running hash comparisons.
To learn more, see Cluster-to-Cluster Sync Verification of Data Transfer . Click Connect to your new cluster . Atlas redirects you
to the Connect to Atlas page, where you can choose a connection method. After you connect to your cluster, resume writes to the destination cluster. Migration Support If your migration fails at any stage of the live migration process, Atlas notifies you via email with a link to explore the migration results. If you have any questions regarding migration support beyond what is
covered in this documentation, or if you encounter an error during
migration, please request support through the
Atlas UI. To file a support ticket: 1 In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. 2 Request support. Click Request Support . For Issue Category , select Help with live migration . For Priority , select the appropriate priority. For
questions, please select Medium Priority . If there was a
failure in migration, please select High Priority . For Request Summary , please include Live Migration in your summary. For More details , please include any other relevant
details to your question or migration error. Click the Request Support button to submit the
form. Back Live Migrate a 6.0.17+ or a 7.0.13+ Cluster Next Push from Cloud Manager
