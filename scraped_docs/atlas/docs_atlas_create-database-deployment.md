# Cluster Types - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Cluster Types On this page Choose a Deployment Type Dedicated Clusters Shared Clusters and Flex Clusters Global Clusters Local Deployments Feature Support and Comparison Take the Next Steps MongoDB Atlas can deploy two types of cloud databases: Clusters, which includes Dedicated clusters for high-throughput
production applications and Shared clusters and Flex clusters for
development purposes and small-scale applications. Serverless instances . You create new cloud databases through the Atlas UI, Atlas Administration API,
or Atlas CLI. You can also create a local Atlas deployment with the
Atlas CLI. Choose a Deployment Type Dedicated Clusters Create a Dedicated cluster if you want to: Choose a specific database configuration based on your workload requirements. Define database scaling behavior . Run high-throughput production workloads. Always have capacity available. You can: Set the cluster tier . Use advanced capabilities such as sharding . Distribute your data to multiple regions and cloud providers . Scale your cluster on-demand. Enable autoscaling . MongoDB bills clusters based on the deployment configuration and cluster tier . Shared Clusters and Flex Clusters Important We are introducing new Flex clusters in a phased approach. Once your
org has the ability to create Flex clusters, you will no longer be
able to create M2 and M5 clusters or Serverless instances in the
Atlas UI. We will also be seamlessly migrating existing M2 and M5 clusters to
Flex clusters in a phased manner. There will be no downtime and
you will not need to make any changes to your configuration during this
migration. Create a Flex cluster if you want
to: Get started quickly with minimal database configuration and low costs. Have your database scale automatically and dynamically to meet your workload. Run infrequent or sparse workloads. Develop or test in a cloud environment. Global Clusters Create a global cluster if you want to support location-aware read and write operations.
Location-aware read and write operations are ideal for globally-distributed
application instances and clients. Global Clusters are a highly-curated implementation
of a sharded cluster that offer: Low-latency read and write operations for globally distributed
clients. Uptime protection during partial or full regional outages. Location-aware data storage in specific geographic regions. Workload isolation based on cluster member types. You can enable Global Writes in Atlas when deploying an M30 or
greater sharded cluster. For replica sets, scale the cluster to at least an M30 tier and enable Global Writes . All shard nodes deploy with the
selected cluster. Important You can't disable Global Writes for a cluster once it is deployed. Local Deployments Create a local deployment to try Atlas features on a single-node replica set hosted on your local
computer. Feature Support and Comparison The following table indicates whether Dedicated clusters or
Flex clusters support the listed configuration or capability in MongoDB Atlas . Note MongoDB plans to add support for more configurations and
capabilities on Atlas Flex over time. To see
the current Atlas Flex limitations and learn
about planned support, see Atlas Flex Limitations . For the latest product updates, see the Atlas Changelog . Configurations Configuration Dedicated Clusters Flex Clusters Rapid releases AWS regions Select regions only Google Cloud regions Select regions only Microsoft Azure regions Select regions only Multi-region deployments Multi-cloud deployments Sharded deployments Global clusters IP access list Network peering Private endpoints Advanced enterprise security features (including LDAP and database auditing ) Capabilities Capability Dedicated Clusters Flex Clusters Use the Atlas API Monitor metrics Configure alerts on available metrics or billing Configure backups Snapshots Perform point-in-time or automated restores from backup snapshots Use the Atlas UI (Find, Indexes, Schema
Advisor and Aggregation Pipeline Builder) Get on-demand index and schema
suggestions Load sample data Use triggers Use Atlas Search Use Online Archive Run federated queries Use BI Connector Use MongoDB Charts Take the Next Steps Once you select a cluster type, you can Create a cluster . Back Create & Connect to Clusters Next Create a Cluster
