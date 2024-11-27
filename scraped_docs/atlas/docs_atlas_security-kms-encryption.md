# Encryption at Rest using Customer Key Management - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features Encryption at Rest using Customer Key Management On this page Required Access Configure Atlas with Customer Key Management Allow Access From the Atlas Control Plane Enable Customer Key Management for an Atlas Cluster Add Nodes to an Encrypted Atlas Cluster Validate your KMS Configuration Restore a Deleted Key Encrypted Backups Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . Atlas encrypts all cluster storage and snapshot volumes at rest
by default. You can add another layer of security by using your
cloud provider's KMS together with the MongoDB encrypted storage engine . Configuring Encryption at Rest using your Key Management incurs
additional charges for the Atlas project. To learn more, see Advanced Security . You can use one or more of the following customer key management
providers when configuring Encryption at Rest for the Atlas project: Amazon Web Services Key Management Service Azure Key Vault Google Cloud Platform Key Management Service After configuring at least one key management provider for the Atlas project, you can enable customer key management for each Atlas cluster for which they require encryption. The key management
provider does not have to match the cluster cloud service provider. Note When you enable or disable customer key management, Atlas performs an initial sync to re-encrypt your cluster data. Alternatively, for projects with M10 or higher Atlas clusters deployed on only Azure regions, you can use the
Atlas Administration API to automatically create Azure Private Link in your AKV that
enables Atlas to securely communicate with your AKV over Azure 's
private network interfaces. To learn more, see Manage Customer Keys with Azure Key Vault . Atlas cannot rotate customer-managed encryption keys. Refer to your
key management provider's documentation for guidance on key rotation.
When you set customer key management in a project, Atlas creates a 90-day key rotation alert . If your KMS provider becomes unavailable, this doesn't disable your
cluster while it still runs. If you decide to restart your cluster, the
lack of a KMS provider disables your cluster. Required Access To configure customer key management, you must have Project Owner access to the project. Users with Organization Owner access must add themselves to the
project as a Project Owner . Configure Atlas with Customer Key Management Encryption at Rest using Key Management requires valid key management
provider credentials and an encryption key. To provide these details
and enable Customer Key Management: 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to Encryption at Rest using your Key Management to On . 3 Enter your key management provider account credentials and provide an encryption key. 4 Click Save . 5 Allow access to or from the Atlas control plane. To learn more, see Allow Access From the Atlas Control Plane . Allow Access From the Atlas Control Plane Optional. Depending on your Key Management Service configuration, you might have
to add Atlas control plane IP addresses to enable Encryption at Rest
for your project so that Atlas can communicate with your KMS . To enable communication between Atlas and KMS: 1 Send a GET request to the returnAllControlPlaneIPAddresses endpoint. The API endpoint returns a list of inbound and outbound Atlas control plane IP
addresses in CIDR categorized by cloud provider and region. To learn
more, see the prerequisites for managing  customer keys with AWS , Azure ,
and GCP . 2 Add the returned outbound IP addresses to your cloud provider's IP access list. See the prerequisites for managing customer keys with AWS , Azure ,
and GCP for more information. Enable Customer Key Management for an Atlas Cluster After you Configure Atlas with Customer Key Management , you must enable customer key
management for each Atlas cluster that contains data that you want
to encrypt. Note You must have the Project Owner role to
enable customer key management for clusters in that project. For new clusters: 1 Enable cluster encryption. Toggle the Manage your own encryption keys setting to Yes on the cluster configuration form. 2 Review and apply your changes. Click Review Changes . Review your changes, then click Apply Changes to deploy
your cluster. 3 Optional: Add IP addresses from the new cluster nodes. Depending on your Key Management configuration, you may have to add Atlas cluster node IP
addresses to your cloud provider KMS access list, so that the cluster can communicate with your
KMS. To enable communication between the cluster and KMS: Send a GET request to the ipAddresses endpoint.
The API endpoint returns
a list of IP addresses from the new cluster nodes, similar to the
following: { "groupId" : "xxx" , // ObjectId "services" : { "clusters" : [ { "clusterName" : "Cluster0" , "inbound" : [ "3.92.113.229" , "3.208.110.31" , "107.22.44.69" ] , "outbound" : [ "3.92.113.229" , "3.208.110.31" , "107.22.44.69" ] } ] } } Add the returned IP addresses to your cloud provider's IP access list.
You must modify your IP access list before the provisioning plan rolls
back. The cluster attempts provisioning for up to three days before the
provisioning plan rolls back from IP access restrictions. See the prerequisites for managing customer keys with AWS , Azure , and GCP for more information. Note If you need more time to update the IP access list, you can: Provision the cluster without Encryption at Rest then enable it
after you update the IP access list. Configure a more inclusive IP access list on your cloud provider's
Key Management Service, launch the cluster with Encryption at Rest,
then modify the IP access list. For existing clusters: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Modify the cluster's configuration. For the cluster that contains data that you want to encrypt, click the , then select Edit Configuration . 3 Enable cluster encryption. Expand the Additional Settings panel. Toggle the Manage your own encryption keys setting to Yes . Verify the status of the Require Private Networking setting for your cluster. If you configured Encryption at Rest Using CMK (Over Private
Networking) for Atlas at the project level, the status is Active . If you haven't configured any private
endpoint connection for your project, the status is Inactive . 4 Review and apply your changes. Click Review Changes . Review your changes, then click Apply Changes to update
your cluster. Add Nodes to an Encrypted Atlas Cluster 1 Add nodes or shards to your replica set cluster or sharded cluster. You can add electable nodes to M10+ clusters or increase the number of shards in your sharded cluster. 2 Optional: Add IP addresses from the new cluster nodes or shards. Depending on your Key Management configuration, you may have to add Atlas cluster node IP
addresses to your cloud provider KMS access list, so that the cluster can communicate with your KMS.
To enable communication between the cluster and KMS: Send a GET request to the ipAddresses endpoint. The API endpoint returns
a list of IP addresses from the new cluster nodes or shards, similar
to the following: { "groupId" : "xxx" , // ObjectId "services" : { "clusters" : [ { "clusterName" : "Cluster0" , "inbound" : [ "3.92.113.229" , "3.208.110.31" , "107.22.44.69" ] , // List<String> "outbound" : [ "3.92.113.229" , "3.208.110.31" , "107.22.44.69" ] } ] } } Add the returned IP addresses to your cloud provider's IP access list. You must modify
your IP access list before the provisioning plan rolls back. The cluster attempts
provisioning for up to three days before the provisioning plan rolls back from IP access restrictions. See the prerequisites for managing customer keys with AWS , Azure , and GCP for more information. Validate your KMS Configuration Atlas validates your KMS configuration: When you add or update credentials. Every 15 minutes. On-demand with the Encryption at Rest API endpoint . Atlas shuts down all mongod and mongos processes on the next
scheduled validity check if one of the following conditions exist: your key management provider credentials become invalid someone deletes or disables your encryption key If Atlas can't connect to your key management provider, Atlas doesn't shut down your processes. The Encryption at Rest KMS network access denied alert is enabled by default for all new projects to communicate any KMS network access failures.
You can configure your alert settings . If Atlas shuts down your clusters, the following events occur: Atlas sends an email to the Project Owner listing all
affected clusters. The Clusters page reflects that Atlas disabled your clusters due to invalid Encryption at Rest settings. You can't read or write data on disabled clusters. You can submit
updates to disabled clusters, such as disk and instance size changes. Atlas processes these changes once someone restores your encryption
key. Atlas continues to perform maintenance and apply security
patches. Disabled clusters retain all your data, so billing continues. Note Virtual Machine Power While a cluster is disabled, Atlas doesn't stop the Virtual
Machine (VM) the cluster is running on. Atlas may perform
patches that reboot the server, but VM power is not cycled. To regain access to your data: Update your credentials if they have
changed since configuring Atlas with Customer Key Management. Restore your key if it has
been disabled or deleted. click to enlarge After updating your configuration, click Try Again to
validate it. If you don't, Atlas validates on its next scheduled
check. All mongod and mongos processes restart after Atlas determines your configuration to be valid. Warning If your key was deleted, restore that key to regain access to your
clusters. You cannot change a key or disable Encryption at Rest
using Customer Key Management without a valid key. Restore a Deleted Key To restore a deleted key, see your key management provider's
documentation: AWS KMS: Delete customer master keys Azure Key Vault: Recover deleted key GCP KMS: Destroy and restore key versions Encrypted Backups Atlas encrypts all snapshot volumes. This secures your cluster data on
disk. Using your cloud provider's KMS , you can: Encrypt your snapshot storage volumes where you store your backups. Encrypt the data files in your snapshots. Access encrypted snapshots. To learn more, see Access an Encrypted Snapshot . Restore snapshots with the key that was active at the time the
snapshot was taken. Encrypt PIT restore oplog data. You cannot restore snapshots encrypted with keys that have become
invalid. You can't enable Legacy Backups (Deprecated) on clusters encrypted with
keys that you manage. You can specify a base snapshot schedule that backs up
every 6 hours. To learn more about customer key management and Cloud Backups,
see: Storage Engine and Cloud Backup Encryption Access an Encrypted Snapshot Restore from a Snapshot Using Encryption at Rest . Back X.509 Next AWS KMS
