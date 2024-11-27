# Upgrade to the Latest Self-Managed Patch Release of MongoDB - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Self-Managed Deployments / Administration / Configuration & Maintenance Upgrade to the Latest Self-Managed Patch Release of MongoDB On this page About this Task Before You Begin Backup Compatibility Considerations Maintenance Window Staging Environment Check Steps Upgrade a MongoDB Instance Upgrade Replica Sets Upgrade Sharded Clusters Learn More MongoDB version numbers have the form X.Y.Z where Z refers to
the patch release number. Patch releases provide security patches, bug
fixes, and new or changed features that generally do not contain any
backward breaking changes. Always upgrade to the latest patch release in
your release series. For more information on versioning, see MongoDB Versioning . About this Task This page describes upgrade procedures for the MongoDB
8.0 release series. To upgrade a different release
series, refer to the corresponding version of the manual. Before You Begin Review the following sections to ensure that your deployment is ready to
be upgraded. Backup Ensure you have an up-to-date backup of your data set. See Backup Methods for a Self-Managed Deployment . Compatibility Considerations Consult the following documents for any special considerations or
compatibility issues specific to your MongoDB release: Release notes Driver documentation Maintenance Window If your installation includes replica sets , set
the upgrade to occur during a predefined maintenance window. Staging Environment Check Before you upgrade a production environment, use the procedures in this
document to upgrade a staging environment that reproduces your
production environment. Ensure that your production configuration is
compatible with all changes before upgrading. Steps Upgrade each mongod and mongos binary
separately. Follow this upgrade procedure: For deployments that use authentication, first upgrade all of your
MongoDB Drivers. To upgrade, see the documentation for your driver . Upgrade any standalone instances. See Upgrade a MongoDB Instance . Upgrade any replica sets that are not part of a sharded cluster, as
described in Upgrade Replica Sets . Upgrade sharded clusters, as described in Upgrade Sharded Clusters . Upgrade a MongoDB Instance To upgrade a 8.0 mongod or mongos instance, use one of these approaches: Upgrade the instance using the operating system's package management
tool and the official MongoDB packages. This is the preferred
approach. See Install MongoDB . Upgrade the instance by replacing the existing binaries with new
binaries. See Replace the Existing Binaries . Replace the Existing Binaries This section describes how to upgrade MongoDB by replacing the existing
binaries. The preferred approach to an upgrade is to use the operating
system's package management tool and the official MongoDB packages, as
described in Install MongoDB . To upgrade a mongod or mongos instance by
replacing the existing binaries: Download the binaries for the latest MongoDB patch release from the MongoDB Download Page and store the binaries in a temporary
location. The binaries download as compressed files that uncompress
to the directory structure used by the MongoDB installation. Shutdown the instance. Replace the existing MongoDB binaries with the downloaded binaries. Make any required configuration file changes. Restart the instance. Upgrade Replica Sets To upgrade a 8.0 replica set, upgrade each member
individually, starting with the secondaries and
finishing with the primary . Plan the upgrade during a predefined
maintenance window. Important Before you upgrade or downgrade a replica set, ensure all replica set
members are running. If you do not, the upgrade or downgrade will not
complete until all members are started. Upgrade Secondaries Upgrade each secondary separately as follows: Upgrade the secondary's mongod binary by following the
instructions in Upgrade a MongoDB Instance . After upgrading a secondary, wait for the secondary to recover to
the SECONDARY state before upgrading the next instance. To
check the member's state, issue rs.status() in mongosh . The secondary may briefly go into STARTUP2 or RECOVERING .
This is normal. Make sure to wait for the secondary to fully recover
to SECONDARY before you continue the upgrade. Upgrade the Primary Step down the primary to initiate the normal failover procedure. Using one of the following: The rs.stepDown() helper in mongosh . The replSetStepDown database command. During failover, the set cannot accept writes. Typically this takes
10-20 seconds. Plan the upgrade during a predefined maintenance
window. Note Stepping down the primary is preferable to directly shutting down the primary. Stepping down expedites the
failover procedure. Once the primary has stepped down, call the rs.status() method from mongosh until you see that another
member has assumed the PRIMARY state. Shut down the original primary and upgrade its instance by
following the instructions in Upgrade a MongoDB Instance . Upgrade Sharded Clusters To upgrade a 8.0 sharded cluster: Disable the cluster's balancer as described in Disable the Balancer . Upgrade the config servers . To upgrade the config server replica set, use the procedures in Upgrade Replica Sets . Upgrade each shard. If a shard is a replica set, upgrade the shard using the
procedure titled Upgrade Replica Sets . If a shard is a standalone instance, upgrade the shard using the
procedure titled Upgrade a MongoDB Instance . Once the config servers and the shards have been upgraded, upgrade
each mongos instance by following the instructions in Upgrade a MongoDB Instance . You can upgrade the mongos instances in any order. Re-enable the balancer, as described in Enable the Balancer . Learn More Production Notes for Self-Managed Deployments View Cluster Configuration Replica Set Data Synchronization Back Run-time Database Configuration Next Manage mongod Processes
