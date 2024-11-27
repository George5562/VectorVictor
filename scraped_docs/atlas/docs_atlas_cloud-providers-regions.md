# Cloud Providers and Regions - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Cloud Providers and Regions On this page Cloud Providers and Regions for Dedicated Search Nodes The choice of cloud provider and region affects network latency for clients
accessing your cluster and the cost of running the cluster . For clusters,
this choice also affects the configuration options for the available cluster
tiers. The region refers to the physical location of your MongoDB
cluster. Atlas supports deploying Atlas Flex on a subset of each cloud provider's
regions. For a list of supported regions, see: Amazon Web Services (AWS) Google Cloud Platform (GCP) Microsoft Azure In the Create New Cluster page: Regions marked as â are Recommended regions that
provide higher availability compared to other regions. Regions marked as under Shared tier
are not available for shared tier clusters and therefore appear
grayed-out. These regions are available for dedicated clusters only. For more information, see: AWS Recommended Regions GCP Recommended Regions Azure Recommended Regions Tip See also: For more information on multi-region configurations for increased
availability, see Configure High Availability and Workload Isolation . Cloud Providers and Regions for Dedicated Search Nodes Atlas supports deploying separate Search Nodes for M10 and higher
clusters on AWS , Google Cloud , or Azure . Atlas supports deploying
Search Nodes in any Google Cloud or Azure regions but only a subset of AWS regions. For more information, see: AWS Dedicated Search Nodes GCP Dedicated Search Nodes Azure Dedicated Search Nodes Back Create a Global Cluster Next Connection Methods
