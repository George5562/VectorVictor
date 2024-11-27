# Live Migrate (Push) a MongoDB 6.0.17+ or 7.0.13+ Cluster Monitored by Cloud Manager into Atlas - MongoDB Atlas


Docs Home / MongoDB Atlas / Migrate or Import Data / Live Migrate a 6.0.17+ or a 7.0.13+ Cluster Live Migrate (Push) a MongoDB 6.0.17+ or 7.0.13+ Cluster Monitored by Cloud Manager into Atlas On this page Restrictions Migration Path and Supported Platforms Supported Source and Destination Cluster Configuration Pairs Required Access Prerequisites Considerations Migrate Your Cluster Push Live Migration APIs Push Live Migration CLI Commands Migration Support If both the source and destination clusters are running MongoDB 6.0.17+
or 7.0.13+, and Cloud Manager monitors the source cluster, Atlas can push a source cluster to an Atlas cluster using the procedure
described in this section. This process uses mongosync as the underlying data migration tool,
enabling faster live migrations with less downtime: Atlas syncs data from the source to the destination cluster until
you cut your applications over to the destination Atlas replica set. Once you reach the cutover step in the following procedure: Stop writes to the source cluster. Stop your application instances, point them to the Atlas cluster,
and restart them. Restrictions The Cluster-to-Cluster Sync Limitations apply to this live migration. Live migration doesn't support migrating Atlas Search indexes from a source cluster to the destination cluster. Support for VPC Peering and Private Endpoints The following table lists the current support status for VPC peering and private endpoints for source and destination
clusters that you live migrate to Atlas .
Select the tab for replica sets or sharded clusters. Replica Sets Sharded Clusters Cloud Provider VPC Peering Private Endpoints Azure AWS Google Cloud Cloud Provider VPC Peering Private Endpoints Azure AWS Google Cloud Migration Path and Supported Platforms Live Migration from Cloud Manager to Atlas is supported for all platforms on
which you can provision a host for mongosync . For a full list of supported
platforms on which you can provision a host for mongosync , see mongosync platforms . Atlas live migration (push) supports the following migration paths: Source Cluster MongoDB Version Destination Atlas Cluster MongoDB Version 6.0.17 6.0.17 7.0.13 7.0.13 Supported Source and Destination Cluster Configuration Pairs For this type of live migration, Atlas supports the following source
and destination cluster configuration pairs: Source Cluster Configuration Destination Cluster Configuration Live Migration Support Notes Standalone Any type of cluster Before migrating a standalone source cluster using this
migration procedure, convert the standalone to a replica set . Replica Set Replica Set Replica Set Sharded Cluster When you run this type of migration, you may specify sharding parameters.
To learn more, see the live migration procedure in this section
and this sharding example . Sharded Cluster Sharded Cluster The number of shards in source and destination clusters might differ.
The source sharded cluster must use CSRS (Config Server Replica Sets).
To learn more, see Replica Set Config Servers . Sharded Cluster Replica Set Required Access To live migrate your data, you must have Project Owner access
to Atlas . Users with Organization Owner access must add themselves to the
project as a Project Owner . Prerequisites Before you begin the push live migration from a cluster running
MongoDB 6.0.17 or later, or 7.0.13 or later monitored
in Cloud Manager to Atlas : Upgrade the source cluster to MongoDB 6.0.17 or later. Create an Atlas Account . Create an Atlas organization and
then create a project in this organization. Deploy your cluster in this project. Connect to your cluster from all client servers where your applications run. Consider configuring a VPC peering connection or
a private endpoint between each migration host
and the destination Atlas cluster on the same cloud provider
and in the same region as the destination cluster. Note If you choose not to use VPC peering or private endpoints when
migrating replica sets, the live migration process runs over
public IP addresses that you add to the Atlas project's IP access list as part of the live migration
procedure in this section. On your source cluster in Cloud Manager , provision a migration host in Cloud Manager . The username and password used to connect to the source cluster. If you aren't using a private endpoint between the migration host and the destination Atlas cluster,
obtain the external IP addresses or CIDR blocks of the provisioned
migration hosts in Cloud Manager from your Cloud Manager administrator. If the source cluster uses TLS / SSL with a Custom Root Certificate Authority ,
to ensure the hosts can read the certificate, add the source
cluster's CA file to the
migration hosts. During the live migration process, Atlas validates that it can collect
MongoDB database statistics using dbStats .
Before you live migrate to an Atlas cluster, review the project settings for the source cluster in Cloud Manager and ensure that the option Collect Database Specific Statistics is enabled. This option
is enabled by default in Cloud Manager , and it should remain enabled so that the
migration process passes validation. If the cluster runs with authentication, meet the following prerequisites: For replica sets, grant the backup and readAnyDatabase roles on the admin database to the user that will run the migration process. For sharded clusters, grant the backup , readAnyDatabase ,
and clusterMonitor roles on the admin database to the user
that will run the migration process. Ensure the specified user exists
on every shard and the config server replica set.
The user must have permissions that allow the following actions: Stop or start the sharded cluster balancer. Read all databases and collections on the host. Read the oplog on the host. Ensure that this user is authenticated using both SCRAM-SHA-1 and SCRAM-SHA-256 .
To learn more, see Source Cluster Security . Important Source Cluster Readiness To help ensure a smooth data migration, your source cluster should
meet all production cluster recommendations. Check the Operations
Checklist and Production Notes before
beginning the Live Migration process. Live Migration Workflow This section outlines the workflow. For detailed steps,
see the procedure for migrating a cluster from Cloud Manager to Atlas . The stages in the live migration workflow are: Stage 1: Link with Atlas . Perform this step in Atlas ,
after you have created your Atlas account, organization, and
project; deployed your dedicated cluster in this project; and can
connect to it. In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page
displays. Click Live Migration in the sidebar. The Live Migration to Atlas page
displays. Select Migrate from Cloud Manager and
start the live migration wizard. Stage 2: Provision Migration Host . provision a migration host in Cloud Manager . A migration host runs a dedicated MongoDB Agent
that orchestrates the live migration process from Cloud Manager to Atlas . Note If you are migrating a source MongoDB deployment that hasn't used Cloud Manager before, add existing MongoDB processes to Cloud Manager . In the Live Migration: Connect to Atlas section of your Cloud Manager organization's Settings page, select Connect to Atlas and paste the link-token
that you created in Atlas . To learn more, see Connect to Atlas for Live Migration in Cloud Manager . Stage 3: Start the Migration . In Atlas , follow the
steps in the wizard to start the live migration process. External IP Address of the Migration Host in Cloud Manager Before you begin the live migration procedure, add the IP addresses or CIDR blocks of your migration hosts to the project IP access list . Atlas allows connections to the
destination cluster only from hosts with entries in the project's
access list. Pre-Migration Validation Before starting the live migration procedure, Atlas runs validation
checks on the source and destination clusters. The source and destination cluster's MongoDB version is at least
6.0.17+ and is matching, or at least 7.0.13+
and is matching. The source cluster's database user has the correct permissions as
described in Source Cluster Security . The destination Atlas cluster doesn't have BI Connector for Atlas enabled. The source cluster enables collecting database statistics for its
project in Cloud Manager . This allows Atlas to collect MongoDB
database statistics during the live migration process. To confirm that
the option Collect Database Specific Statistics is enabled, review the project settings for the source cluster in Cloud Manager . Source Cluster Security Various built-in roles provide sufficient privileges. For example: For source replica set clusters, a MongoDB user must have the readAnyDatabase and backup roles. For source sharded clusters a MongoDB user must have the readAnyDatabase , backup , and clusterMonitor roles. To verify that the database user who will run the live migration process
has these roles, run the db.getUser() command on the admin database. For example, for a replica set, run: use admin db. getUser ( "admin" ) { "_id" : "admin.admin" , "user" : "admin" , "db" : "admin" , "roles" : [ { "role" : "backup" , "db" : "admin" } , { "role" : "readAnyDatabase" , "db" : "admin" } ] } ... Specify the username and password to Atlas when prompted by
the walk-through screen of the live migration procedure. Atlas only supports SCRAM for
connecting to source clusters that enforce authentication. Security Requirements for the Migration Host For push-type live migrations, you're responsible for provisioning, securing,
and running the migration host. The migration host only encrypts outbound
communication with Atlas clusters. To learn more about Atlas security, see the Atlas Security whitepaper. Considerations Network Encryption During push live migrations, if the source cluster does not use TLS encryption
for its data, the traffic from the source cluster to the migration host
is not encrypted, but the traffic from the migration host to Atlas is
encrypted. Determine if this is acceptable before you start a push live
migration procedure. Database Users and Roles If the source cluster doesn't use authentication, you must create a
user in Atlas because Atlas doesn't support running without authentication. Atlas doesn't migrate any user or role data to the destination cluster. If the source cluster enforced authentication, before you migrate you
must re-create the appropriate authentication mechanism used by your
applications on the destination Atlas cluster. The following
table lists authentication mechanisms and how to configure them in Atlas . Authentication Mechanism Configuration Method SCRAM Create database users with SCRAM for password authentication . LDAP Set up LDAP . AWS KMS, Azure Key Vault, Google Cloud KMS Set up KMS encryption . Source and Destination Cluster Balancers To avoid any impact on write performance during migration, Atlas stops the sharded cluster balancers on the source and destination
clusters at the start of the procedure, and starts the balancers
at the end of the procedure. If you cancel live migration, Atlas restarts the balancers on the
source and destination clusters. If Atlas can't restart the load balancer on the source or
destination clusters at the end of a successful live migration,
a warning banner indicates that you must manually restart the source or destination cluster balancer. Destination Cluster Configuration For the destination cluster, the following considerations apply: The source and destination clusters are either both replica sets, or
they are both sharded clusters. The number of shards may differ
between the source and the destination cluster. You can't select an M0 (Free Tier) or M2/M5 shared-tier
cluster as the destination for live migration. The destination cluster in Atlas must match or exceed the source
deployment in terms of RAM, CPU, and storage. Provision a destination
cluster of an adequate size so that it can accommodate both the
migration process and the expected workload, or scale up the destination cluster to a tier with more processing power, bandwidth or disk IO. To maximize migration performance, use at least an M40 cluster for the
destination cluster. When migrating large data sets, use an M80
cluster with 6000 IOPS disks or higher. You can also choose to temporarily increase the destination Atlas cluster's size for the duration of the migration process. After you migrate your application's workload to a cluster in Atlas , contact support for assistance with further
performance tuning and sizing of your destination cluster to minimize costs. To avoid unexpected sizing changes, disable auto-scaling on the destination
cluster. To learn more, see Manage Clusters . To prevent unbounded oplog collection growth, and to ensure that
the live migration's lag window stays within the bounds of the oplog
replication lag window, set an oplog size to a large enough fixed value for the duration of the live migration process. To learn more, see: Scale a Cluster Atlas Configuration Options oplog Sizing in the Cluster-to-Cluster Sync documentation. If you are observing performance issues even after you've followed these
recommendations, contact support . Do not change the featureCompatibilityVersion flag while Atlas live migration is running. Avoid Workloads on the Destination Cluster Avoid running any workloads, including those that might be running on
namespaces that don't overlap with the live migration process, on the
destination cluster. This action avoids potential locking conflicts and
performance degradation during the live migration process. Don't run multiple migrations to the same destination cluster at the
same time. Don't start the cutover process for your applications to the destination
cluster while the live migration process is syncing. Avoid Cloud Backups Atlas stops taking on-demand cloud backup snapshots of the target cluster during live migration.
Once you complete the cutover step in the live migration procedure on
this page, Atlas resumes taking cloud backup snapshots based on
your backup policy . Avoid Namespace Changes Don't make any namespace changes during the migration
process, such as using the renameCollection command
or executing an aggregation pipeline that includes the $out aggregation stage. Avoid Elections The live migration process makes a best attempt to continue a migration
during temporary network interruptions and elections on the source or
destination clusters. However, these events might cause the live migration
process to fail. If the live migration process can't recover automatically,
restart it from the beginning. Staging and Production Environments Consider running the following  procedure twice. Perform a partial migration
that stops at the Perform the Cutover step first . This creates
an up-to-date Atlas -backed staging cluster to test application behavior
and performance using the latest driver version that supports the MongoDB version of the Atlas cluster. After you test your application, run the full migration procedure
using a separate Atlas cluster to create your Atlas -backed
production environment. Migrate Your Cluster Important Avoid making changes to the source cluster configuration while the
live migration procedure runs, such as removing replica set members
or modifying mongod runtime settings, such as featureCompatibilityVersion . Procedure 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Go to the Live Migration to Atlas page. Click Live Migration in the sidebar. The Live Migration to Atlas page
displays. 3 Start the migration process. Click Migrate from Ops Manager or Cloud Manager . Note The UI label mentions Ops Manager , however, for this procedure, you
can only migrate to Atlas MongoDB deployments 6.0.17 or later
that Cloud Manager monitors. Click I'm Ready to Start . Atlas displays a Live Migration wizard with instructions on how
to proceed with the process. The process pushes the data from your
source cluster to the new destination cluster. After you complete
the wizard steps, you can point your application to the new cluster. 4 Link with Atlas. Click Generate Link-Token . Atlas displays the
page for generating a link-token . Click Next to see a page that contains the generated link-token. Copy the link-token and store it in a secure location. Atlas never displays the contents of the link-token. Atlas also does
not display the link-token after generating it. Do not
share it publicly. Note Use one unique link-token for live migrating all
projects in one Cloud Manager organization to Atlas . Click Done . 5 Paste the link-token into Cloud Manager. Access the organization in Cloud Manager : Open Cloud Manager , and navigate to the organization
whose project's cluster you are live migrating to Atlas . Click Settings in the left navigation panel. In the Live Migration: Connect to Atlas section, click Connect to Atlas . The Connect to Atlas dialog box opens. Paste the link-token you generated in the previous step of the
Live Migration wizard and click Connect to Atlas . Cloud Manager establishes the connection to Atlas . Use the Refresh button to send an update to Atlas , if
needed. 6 Create the destination Atlas cluster. If you haven't already, create a destination cluster in Atlas .
See Required Access . 7 Initiate the migration from the destination cluster. Click Select Target Cluster from Projects . Go to your destination Atlas cluster's project and find your
destination cluster. Click and select Migrate Data to this Cluster from the dropdown list to start the migration.
The Migrate Data to This Cluster page opens. Click Migrate from Ops Manager or Cloud Manager . Note The UI label mentions Ops Manager , however, for this procedure, you
can only migrate to Atlas MongoDB deployments 6.0.17 or later
that Cloud Manager monitors. Fill in the fields as follows: Select the source project in Cloud Manager , if it's not already selected. Select the source cluster from the dropdown. If you are migrating a replica set to a sharded cluster: If you'd like to shard collections, click the checkmark in Include sharding parameters and paste your sharding configuration
JSON into the text box using the sharding example .
Save this configuration in a file externally, in case you would like to
refer to it later. The sharding configuration JSON defines the shardingEntries array,
which specifies the collections to shard, and the keys to use for sharding.
MongoDB shards only those collections that you include into this array.
To learn more, see Sharding . If you omit specifying the sharding configuration, you can shard collections
on the destination cluster after you migrate your cluster to Atlas . In addition to the sharding configuration, a compatible index for the
specified sharding keys must exist on the destination cluster in service. Click the checkmark in Create supporting indexes so that
MongoDB automatically creates supporting shard key indexes on the
destination cluster in Atlas . Select a migration host for handling the migration. If you aren't using a private endpoint, review the
IP address access list and check that the migration host's
external IP address is included in this list. If it's not added,
add it now: Click Set Network Access for Host Click + Add IP Address Return to the Live Migration wizard. Select the source
cluster from the dropdown and choose Migrate data to this cluster under . Select the source cluster from the drop-down. If the source cluster enforces authentication, enter a username and
password into the provided text boxes. See Source Cluster Security for guidance on the
user permissions required by Atlas live migration. If you suspend the source cluster from automation in Cloud Manager , but
continue to monitor the source cluster with the Monitoring Agent,
the Username and Password display. If
your deployment requires user authentication, provide the user
name and password in these fields. The database user whose
credentials you provide must have at least the backup role on
the admin database and must be authenticated using both SCRAM-SHA-1 and SCRAM-SHA-256 . If the source cluster uses TLS / SSL , toggle the Is encryption in transit enabled? button. If the source cluster uses TLS / SSL with a custom Root
Certificate Authority (CA), copy the path to the CA file from your migration host
and paste this path into the provided text box. The file must be
present on the migration host to ensure the migration host can
read the certificate. Atlas checks that the certificate is
present and readable. If your destination cluster has data that you want to preserve,
keep the Clear any existing data on your destination cluster option unchecked. The live migration service checks a sample of documents
during validation and warns you if it finds duplicate namespaces.
If you want to delete the existing data, check this option and
then enter the name of the destination cluster. Choose a connection to connect to the cluster. The Standard connection always shows as available in
the UI. However, other connection options are enabled only if
you have previously configured a VPC peering connection or a
private endpoint for your clusters. If Atlas detects that
you don't have VPC connections or private endpoints configured,
these options are grayed out. If you aren't using VPC peering or a private endpoint, click Standard connection and proceed to the Validation stage of this step. If you configured a VPC peering connection between the migration host and the Atlas replica set, the VPC Peering option is active. Click VPC Peering to connect using VPC peering for live
migration. If the VPC Peering option is grayed out, configure a VPC peering connection before
starting this procedure. To learn more, see Support for VPC Peering and Private Endpoints . If you configured a private endpoint between the migration host and the Atlas cluster, the Private Endpoint option is active. Click Private Endpoint to connect with a private endpoint , and then select
a previously-configured private endpoint from the dropdown.
Only private endpoints that are in AVAILABLE state are valid.
If the Private Endpoint option is grayed out, configure a private endpoint before starting this procedure. To learn more, see Support for VPC Peering and Private Endpoints . Note For push live migrations where the source and destination clusters are
running MongoDB 6.0.17 or later, private endpoints are supported
only for clusters deployed within a single cloud provider and single
region. Click Validate . The validation process verifies that
your migration host is reachable, and performs the following
validation checks to ensure that you can start live migration
to Atlas . To take advantage of the following validation checks, upgrade the MongoDB Agent in Cloud Manager to
the latest version.
The following validation checks run during the live migration: The migration host can connect to the destination cluster. If the source cluster uses TLS / SSL with a custom Root
Certificate Authority (CA), the migration host can access
the source cluster using TLS / SSL . The database user credentials are valid. This validation check
runs only if you suspend the source cluster from automation in Cloud Manager , but continue to monitor the source cluster with the
Monitoring Agent. The migration process validates that the destination cluster
has enough disk space based on the storage size of the compressed
data. To learn more about data and storage sizes, see dbStats . If validation fails, check the migration host, the validity of
your external IP addresses or CIDR block, and the link-token.
Also check the database user credentials, your TLS / SSL certificates, and the amount of disk storage size on the destination
cluster. If validation succeeds, click Next . 8 Start the migration. Review the report listing your source organization, project and
cluster, and the migration host that the live migration process
will use. Click Start the Migration . Once the migration process begins, Atlas UI displays the Migrating Data walk-through screen for the destination Atlas cluster. The walk-through screen updates as the
destination cluster proceeds through the migration process.
The migration process includes: Applying new writes to the source cluster data to the destination
cluster data. Copying data from the source cluster to the destination cluster. Finalizing the migration on the destination cluster. A lag time value displays during the final phase of the migration process
that represents the current lag between the source and destination clusters. When the lag timer is close to zero and the migration process is caught up, Atlas activates the Cutover to your destination cluster button
and indicates that your source and destination clusters are in sync.
Proceed to the next step. 9 Perform the cutover. Cutover is a three-step process of directing your application's reads and writes
away from your source cluster and to your destination cluster. When Atlas detects that the source and destination clusters are
nearly in sync, it starts an extendable 120 hour (5 day) timer to begin
the cutover stage of the live migration procedure. After the 120 hour
period passes, Atlas stops synchronizing with the source cluster. At this stage in the migration process, you can proceed to cutover or
extend the syncing period and then proceed to cutover. If you click I'm ready to cutover , Atlas starts the cutover process. If you click Extend Sync , and if the extended sync completes successfully, Atlas confirms that source and destination clusters are in sync. Proceed
with the cutover process. If the sync time expires, you can retry the migration. If your migration is about to expire, Atlas sends you an email similar
to the following example: A migration to your Atlas cluster will expire in <number> hours! Navigate to your destination cluster to start the cutover process. If you don't take any action within <number> hours, the migration will be cancelled and you will need to start again. You can also extend the migration process if you need more time. Click I'm ready to cutover . Proceed with the three-step cutover
process quickly to ensure minimal downtime to your application. Click Proceed to cutover . The three-step cutover process begins: Stop writes to your source cluster. Click I confirm that I've stopped writes to my source cluster .
Click Finalize migration to proceed. Wait a few minutes while Atlas finalizes the migration. Atlas performs these actions to complete the process: Removes the MongoDB live migration server subnets from the IP access
list on the destination cluster. Removes the database user that live migration used to import data
to the destination cluster. If the cutover process has been in progress for at least 12 hours, Atlas sends you an email that suggests you check on the migration
process or contact support. If the migration succeeds, the You have successfully migrated to Atlas page displays. Atlas shows the status of the synced changes,
the application downtime, the duration of the migration process,
the amount of initial data copied, and the number of copied collections. Verify that your data is transferred to the destination cluster
by comparing document counts and running hash comparisons.
To learn more, see Cluster-to-Cluster Sync Verification of Data Transfer . Click Connect to your new cluster . Atlas redirects you
to the Connect to Atlas page, where you can choose a connection method. After you connect to your cluster, resume writes to the destination cluster. Push Live Migration APIs To run tasks associated with the live migration procedure, see Push Live Migration API . Note The Live Migration APIs mention Cloud Manager or Ops Manager , however, the type of live migration
described in this section only supports migrating source clusters
monitored in Cloud Manager to destination clusters in Atlas . Push Live Migration CLI Commands To migrate a cluster using the Atlas CLI, you can perform the following steps: Create or delete a link-token Create or view a validation job Create or view a migration job Perform the cutover For other steps in the live migration procedure , you must use the Cloud Manager UI or the Atlas UI. To learn more, see the live migration workflow . Before you migrate a cluster using the Atlas CLI, complete the pre-migration validation . Note Before you run any Atlas CLI commands, you must: Install the Atlas CLI Connect to the Atlas CLI Create or Delete a Link-Token To create a new link-token using the Atlas CLI, run the following command: atlas liveMigrations link create [options] To delete the link-token you specify using the Atlas CLI, run the following command: atlas liveMigrations link delete [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas liveMigrations link create and atlas liveMigrations link delete . If you are migrating from Ops Manager, request an external IP address
and specify it in the link-token. To learn more, see Request an External IP Address in the
Ops Manager documentation. Create and View a Validation Job To create a new validation request using the Atlas CLI, run the following command: atlas liveMigrations validation create [options] To return the details for the validation request you specify using the Atlas CLI, run the following command: atlas liveMigrations validation describe [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas liveMigrations validation create and atlas liveMigrations validation describe . To learn what Atlas validates, see the Validate bullet
in the Migrate Your Cluster section on this page. Create and View a Migration Job To create one new migration job using the Atlas CLI, run the following command: atlas liveMigrations create [options] To return the details of the migration job you specify using the Atlas CLI, run the following command: atlas liveMigrations describe [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas liveMigrations create and atlas liveMigrations describe . Perform the Cutover To start the cutover for live migration using the
Atlas CLI, run the following command: atlas liveMigrations cutover [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas liveMigrations cutover . When the cutover completes, Atlas completes the live migration process and stops synchronizing with the source cluster. To learn
more, see the Migrate Your Cluster section on this page. Note The Live Migration CLI commands might mention Cloud Manager or Ops Manager , however, the
type of live migration described in this section only supports
migrating source clusters monitored in Cloud Manager to destination
clusters in Atlas . Migration Support If your migration fails at any stage of the live migration process, Atlas notifies you via email with a link to explore the migration results. If you have any questions regarding migration support beyond what is
covered in this documentation, or if you encounter an error during
migration, please request support through the
Atlas UI. To file a support ticket: 1 In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. 2 Request support. Click Request Support . For Issue Category , select Help with live migration . For Priority , select the appropriate priority. For
questions, please select Medium Priority . If there was a
failure in migration, please select High Priority . For Request Summary , please include Live Migration in your summary. For More details , please include any other relevant
details to your question or migration error. Click the Request Support button to submit the
form. Back Pull into Atlas Next Sharding Example
