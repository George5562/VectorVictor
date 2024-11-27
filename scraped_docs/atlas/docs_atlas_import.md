# Migrate or Import Data - MongoDB Atlas


Docs Home / MongoDB Atlas Migrate or Import Data On this page MongoDB 6.0.17 and Later: Live Migrate to Atlas Earlier MongoDB Versions: Live Migrate to Atlas Additional Reference You can bring data from existing MongoDB deployments, JSON , or CSV files into deployments in Atlas using either: live migration where Atlas assists you, or tools for a self-guided migration of data from your existing deployments
into Atlas . MongoDB 6.0.17 and Later: Live Migrate to Atlas If both the source and destination clusters are running MongoDB 6.0.17+,
you can migrate your data from a source cluster into an Atlas MongoDB
cluster using one of the following types of guided live migration
in the Atlas UI: Live migration (pull). For instructions, see Live Migrate (Pull) a MongoDB 6.0.17+ or 7.0.13+ Cluster into Atlas . Live migration (push). For instructions, see Live Migrate (Push) a MongoDB 6.0.17+ or 7.0.13+ Cluster Monitored by Cloud Manager into Atlas . Earlier MongoDB Versions: Live Migrate to Atlas If you are migrating source deployments with MongoDB versions earlier than 6.0.17,
use one of the following migration methods, depending on your deployment's requirements
and configuration. Source Cluster Configuration Import Strategy A replica set running MongoDB earlier than 6.0.17 that isn't
monitored by Cloud Manager or Ops Manager . Use live migration (pull) where Atlas pulls data from the source deployment and requires access to
the source deployment through the deployment's firewall. A sharded cluster running MongoDB version earlier than 6.0.17 that isn't
monitored by Cloud Manager or Ops Manager . To live migrate a source sharded cluster that runs a MongoDB version 6.0.17 or earlier, upgrade the cluster to 6.0.17+ or 7.0.13+ and then live
migrate it to Atlas using this live migration procedure . A replica set running MongoDB earlier than 6.0.17 that is
monitored by Cloud Manager or Ops Manager . Use live migration (push) where Cloud Manager or Ops Manager pushes data to Atlas using a secure link-token without
requiring access to the source cluster through the cluster's firewall. A sharded cluster running MongoDB earlier than 6.0.17 that is
monitored by Cloud Manager or Ops Manager . To live migrate a source sharded cluster that runs a MongoDB version 6.0.17 or earlier, upgrade the cluster to 6.0.17+ or 7.0.13+ and then live
migrate it to Atlas using this live migration procedure . A shared multi-tenant cluster, or a cluster where you have no
access to the oplog, or a cluster that runs a MongoDB version
that is no longer supported. Use mongorestore . A replica set in AWS . Migrate a MongoDB Replica Set from AWS to MongoDB Atlas . Additional Reference To move data to a Serverless instance, use Compass to export and import data , or migrate data with self-managed tools .
To learn more, see Serverless Instance Limitations . To load data into a new cluster in Atlas , see Load Sample Data . To make a copy of your cluster for testing purposes, see MongoDB Backup Methods . If the application that you want to migrate requires a near-continuous
uptime, contact MongoDB Support and share your
uptime requirements and cluster configuration. Back Configure MongoDB Support Access to Atlas Backend Infrastructure Next Monitor Migrations
