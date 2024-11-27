# Create a Cluster - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Create a Cluster This tutorial takes you through the steps to create a new Atlas cluster. To learn how to modify an existing Atlas cluster, see Modify a Cluster . Clusters can be either a replica set or a sharded cluster . This tutorial walks you through creating a replica set. Required Access To create a cluster, you must have Organization Owner or Project Owner access to
the project. Considerations To minimize network latency and data transfer costs, and
to increase overall stability and security, use the
same cloud provider and region to host
your application and cluster when possible. Clusters can span regions and cloud service providers. The total number
of nodes in clusters spanning across regions has a specific constraint
on a per-project basis. Atlas limits the total number of nodes in other regions in one
project to a total of 40, not including: Google Cloud regions communicating with each other Free clusters Flex clusters Sharded clusters include additional nodes. The electable nodes on
the dedicated Config Server Replica Set (CSRS) count towards the
total number of allowable nodes. Each sharded cluster has an
additional electable node per region as part of the dedicated CSRS. To
learn more, see Replica Set Config Servers . The total number of nodes between any two regions must meet this
constraint. Example If an Atlas project has nodes in clusters spread across three
regions: 30 nodes in Region A 10 nodes in Region B 5 nodes in Region C You can only add 5 more nodes to Region C because: If you exclude Region C, Region A + Region B = 40. If you exclude Region B, Region A + Region C = 35, <= 40. If you exclude Region A, Region B + Region C = 15, <= 40. Each combination of regions with the added 5 nodes still meets
the per-project constraint: Region A + B = 40 Region A + C = 40 Region B + C = 20 You can't create a multi-region cluster in a project if it has one or
more clusters spanning 40 or more nodes in other regions. Contact Atlas support for questions
or assistance with raising this limit. M30 and higher clusters are recommended for production environments.
Clusters with sustained loads on M10 and M20 tiers may experience
degraded performance over time. Each Atlas project supports up to 25 clusters.
Please contact Atlas support for questions or assistance regarding
the cluster limit. To contact support: 1 In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. 2 Request support. If your Atlas project contains a custom role that uses actions introduced
in a specific MongoDB version, you must delete that role before
creating clusters with an earlier MongoDB version. Atlas clusters created after July 2020 use TLS version 1.2 by
default. When you create a cluster, Atlas creates a network container in the project for the cloud
provider to which you deploy the cluster if one does not already
exist. If you have a Backup Compliance Policy enabled , all
new and existing clusters have Cloud Backup automatically
enabled and use the project-level Backup Compliance Policy. Atlas augments any
preexisting cluster-level policies to meet the minimum
requirements of the Backup Compliance Policy. All new clusters use the Backup Compliance Policy
unless the mininum requirements of the cluster-level backup policy expand beyond the mininum requirements of the Backup Compliance Policy. Procedure Atlas CLI Atlas UI To create one cluster in the specified project using the Atlas CLI, run the following command: atlas clusters create [name] [options] To watch for a specific cluster to become available using the Atlas CLI, run the following command: atlas clusters watch <clusterName> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas clusters create and atlas clusters watch . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI View Available Regions To list available regions that Atlas supports for new deployments using the
Atlas CLI, run the following command: atlas clusters availableRegions list [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas clusters availableRegions list . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI When you create your first Atlas cluster using the
Atlas UI, you can either: Use a template with preset advanced configuration
options. Specify advanced configuration options. Whether you use a template or specify advanced configuration, you can modify all configuration options after you create
the cluster. Note The procedure for creating a new Atlas cluster in the
Atlas UI differs depending on whether you already have one or
more clusters in your project. The following steps
apply to both, but you may see slightly different options in the UI. Use a Template Use Advanced Settings 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Open the Create a New Cluster Page. If you already have one or more clusters, click Build a Cluster to display the Deploy your Cluster page. If this is your first cluster: Click Build a Database . Click advanced configuration options at the top of
the screen to display the Create New Cluster dialog box. 3 Select a cluster type. You can deploy the following clusters from this page: M10 The M10 tier is suitable for development environments
and low-traffic applications, while higher tiers can handle large
datasets and high-traffic applications. Dedicated clusters can be
deployed into a single geographical region or multiple geographical
regions. Note To create Dedicated cluster tiers higher than M10, select Go to Advanced Configuration at the bottom of the page. Flex Clusters Flex clusters are low-cost cluster types suitable for teams
who are learning MongoDB or developing small proof-of-concept applications.
You can begin your project with an Atlas Flex cluster and upgrade to
a production-ready Dedicated cluster tier at a future time. Important We are introducing new Flex clusters in a phased approach. Once your
org has the ability to create Flex clusters, you will no longer be
able to create M2 and M5 clusters or Serverless instances in the
Atlas UI. We will also be seamlessly migrating existing M2 and M5 clusters to
Flex clusters in a phased manner. There will be no downtime and
you will not need to make any changes to your configuration during this
migration. Important If you see "Serverless" as an option instead of Atlas Flex,
refer to Create a Serverless Instance .
Note that all Serverless instances will be automatically migrated in the
near future, based on current usage, to Free clusters, Flex clusters,
or Dedicated clusters. The All Clusters page in the Atlas UI will show which tiers your instances will be migrated to. Free clusters A Free cluster provides a free sandbox replica set. You can deploy
one M0 cluster per Atlas project. Free clusters are more
limited than Atlas Flex and Dedicated clusters. For information on
these limitations, refer to Configuration Limits . 4 Select your preferred Cloud Provider & Region . The choice of cloud provider and region affects the configuration
options for the available cluster tiers, network latency for clients
accessing your cluster, the geographic location of the nodes in your
cluster, and the cost of running the cluster . To learn more, see Cloud Providers and Regions . Note To deploy your cluster across multiple regions, or to
deploy separate Search Nodes for workload isolation, select Go to Advanced Configuration at the bottom of the page. 5 Specify a name for the cluster in the Name box. This label identifies the cluster in Atlas . Note Atlas creates your hostname based on your cluster name. You can't change the cluster name after Atlas deploys the
cluster. Cluster names can't exceed 64 characters in length. Important Atlas truncates the cluster name to 23 characters in
its internal interactions. In practice, this means: Cluster names shorter than 23 characters can't end with
hyphen or dash ( - ). Cluster names 23 characters or longer can't use a hyphen or
dash ( - ) as its 23rd character. The first 23 characters in a cluster name must be unique
within a project. Don't include sensitive information in your
cluster name. 6 Specify a tag key and value to apply to the cluster. To learn more, see Apply a cluster Tag to a New Cluster from a Template . Important Don't include sensitive information such as Personally Identifiable
Information (PII) or Protected Health Information (PHI) in your
resource tags. Other MongoDB services, such as Billing, can access
resource tags. Resource tags are not intended for private and
sensitive data. To learn more, see Sensitive Information . 7 Deploy your cluster. Click Create . Important Each Atlas project supports up to 25 clusters.
Please contact Atlas support for questions or assistance regarding
the cluster limit. To contact support: In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. Request support. 8 Update your Billing Address details as needed. Field Necessity Action Billing Email Address Optional Type the email address to which Atlas should send billing alerts . By default, Atlas sends billing alerts to the Organization Owners
and Billing Admins. If you leave the Billing Email Address blank, Atlas sends billing alerts to the Organization Owners and Billing Admins. If you specify a billing email address and uncheck Only
send invoice emails to the Billing Email
Address , Atlas sends billing alerts to the billing
email address, Organization Owners, and Billing Admins. If you specify a billing email address and check the box for Only
send invoice emails to the Billing Email
Address , Atlas send billing alerts to the billing email address only. Company Name Optional Type the name of the company for your billing address. Country Required Select the country for your billing address. You can also
start typing the name of the country and then select it from
the filtered list of countries. Street Address Required Type the street address for your billing address. Apt/Suite/Floor Optional Type an the apartment, suite, or floor for your
billing address. City Required Type the name of the city for your billing address. State/Province/Region Required Type or select the political subdivision in which your billing
address exists. The label and field change depending on what
you selected as your Country : If you select United States as your Country , this
label changes to State . The field changes to a dropdown
menu of U.S. states. You can also start typing the name of
the state and then select it from the filtered list of
states. If you select Canada as your Country , this label
changes to Province . The field changes to a dropdown
menu of Canadian provinces. You can also start typing the
name of the province and then select it from the filtered
list of provinces. If you select any other country as your Country , this
label changes to State/Province/Region . The field
changes to a text box. Type the name of your province,
state, or region in this box. ZIP or Postal Code Required Type the ZIP (U.S.) or Postal Code (other countries) for your
billing address. VAT Number Conditional Atlas displays the VAT ID field if you
select a country other than the United States. To learn more about VAT, see VAT ID . If your company's billing address is in a country other than
the United States (USA), Atlas typically charges VAT if you do
not enter a valid VAT ID Number on your billing profile . IMPORTANT: If your billing address is in Ireland or certain
Canadian provinces, Atlas always charges VAT , even with a valid VAT ID Number . To learn more about VAT by region, see International Usage and Taxation . 9 Update your Payment Method details as needed. Click the radio button for Credit Card or Paypal . If you selected Credit Card , type values for the
following fields: Field Necessity Action Name on Card Required Type the name that appears on your credit card. Card Number Required Type the 16-digit number that appears on your
credit card. American Express uses a 15-digit number. Expiration Date Required Type the expiration date for your credit card in the
two-digit month and two-digit year format. CVC Required Type the three-digit number on the back of your credit
card. American Express uses a 4-digit number found on
the front of the credit card. If you selected PayPal : Click Pay with PayPal . Complete the actions on the PayPal website. Note All projects within your organization share the same billing
settings, including payment method. 10 Review project's cost. Under the Cart section, review the following: Field Description Cluster Tier Displays cost for your selected cluster tier and configuration
details. To learn more, see Cloud Service Provider and Region and Cluster Tier . Included Features Displays features included with your selected cluster
configuration. Additional Settings Displays additional settings that you enabled, such as cloud
backups, sharding, BI Connector , and more. To learn more, see Cloud Backups . 11 Deploy your cluster. Click Confirm and Deploy Cluster . Important Each Atlas project supports up to 25 clusters.
Please contact Atlas support for questions or assistance regarding
the cluster limit. To contact support: In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. Request support. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Open the Create New Cluster Dialog. If you already have one or more clusters, click Create to display the Create New Cluster dialog box. If this is your first cluster: Click Build a Database . Click advanced configuration options at the top of
the screen to display the Create New Cluster dialog box. 3 Open Advanced Configuration. Navigate to the bottom of the page and click Go to Advanced Configuration . 4 Select a cluster type. You can deploy the following clusters from this page: Flex Clusters Flex clusters are low-cost cluster types suitable for teams
who are learning MongoDB or developing small proof-of-concept applications.
You can begin your project with an Atlas Flex cluster and upgrade to
a production-ready Dedicated cluster tier at a future time. Flex clusters
are more limited than Dedicated clusters. For information on these limitations,
refer to Configuration Limits . Important We are introducing new Flex clusters in a phased approach. Once your
org has the ability to create Flex clusters, you will no longer be
able to create M2 and M5 clusters or Serverless instances in the
Atlas UI. We will also be seamlessly migrating existing M2 and M5 clusters to
Flex clusters in a phased manner. There will be no downtime and
you will not need to make any changes to your configuration during this
migration. Important If you see "Serverless" as an option instead of Atlas Flex,
refer to Create a Serverless Instance .
Note that all Serverless instances will be automatically migrated in the
near future, based on current usage, to Free clusters, Flex clusters,
or Dedicated clusters. The All Clusters page in the Atlas UI will show which tiers your instances will be migrated to. Dedicated clusters Dedicated clusters include M10 and higher tiers. The
M10 and M20 tiers are suitable for development environments
and low-traffic applications, while higher tiers can handle large
datasets and high-traffic applications. Dedicated clusters can be
deployed into a single geographical region or multiple geographical
regions. Note If you choose to create a Dedicated cluster, you also have the option
to Create a Global Cluster. For more information, refer to Manage Global Clusters . Free clusters A Free cluster provides a free sandbox replica set. You can deploy
one M0 cluster per Atlas project. Free clusters are more
limited than Atlas Flex and Dedicated clusters. For information on
these limitations, refer to Configuration Limits . 5 Select your preferred Cloud Provider & Region . The choice of cloud provider and region affects the configuration
options for the available cluster tiers, network latency for clients
accessing your cluster, the geographic location of the nodes in your
cluster, and the cost of running the cluster . To learn more about selecting a provider and region, refer to Cloud Providers and Regions . From the Cloud Provider & Region section, you can also
choose Multi-Cloud, Multi-Region & Workload Isolation . Multi-region
clusters can better withstand data center outages and may contain
dedicated geographic regions for localized reads, thereby improving
performance. To learn how to deploy a multi-region cluster, see Configure High Availability and Workload Isolation . If you choose Multi-Cloud, Multi-Region & Workload Isolation ,
you can also choose to configure: Electable nodes Read-only nodes Analytics nodes Search nodes For information on these settings, see Configure High Availability and Workload Isolation . 6 Select the Cluster Tier . The selected tier dictates the memory, storage, vCPUs, and IOPS specification for each data-bearing server [ 1 ] in the
cluster. Dedicated clusters support Cluster Auto-Scaling . Cluster tier Auto-scaling is enabled by default
when you create new clusters in the user interface. It is disabled by
defaut if you create new clusters in the API. With auto-scaling enabled, Atlas automatically scales your cluster tier, storage capacity, or
both in response to cluster usage. Auto-scaling allows your cluster to
adapt to your current workload and reduce the need to make manual
optimizations. Cluster storage scaling automatically increases your cluster storage capacity when 90% of disk
capacity is used. This setting is enabled by default to help ensure that
your cluster can always support sudden influxes of data. To opt out of
cluster storage scaling, un-check the Storage Scaling checkbox in the Auto-scale section. Cluster tier scaling automatically scales your cluster tier up or down in response to
various cluster metrics. To opt out of cluster tier auto-scaling,
un-check the Cluster Tier Scaling checkbox in the Auto-scale section. To control how Atlas should auto-scale your cluster, you set: The maximum cluster tier to which your cluster can automatically
scale up. By default, this setting is set to the next cluster tier
compared to your current cluster tier. The minimum cluster tier to which your cluster can scale down.
By default, this setting is set to the current cluster tier. For more information on how to select an appropriate cluster tier and
storage settings for your workload, see Select Cluster Tier and Customize Cluster Storage . You can select a cluster tier appropriately
sized for your analytics workload. To learn more, see Analytics Nodes for Workload Isolation . You can also select a different tier for your Search Nodes. To learn more
about the available tiers for your Search Nodes, see Search Tier . 7 Select any Additional Settings . From the Additional Settings section, you can: Select the MongoDB Version of the Cluster Configure Backup Options for the Cluster Termination Protection Deploy a Sharded Cluster Configure the Number of Shards Enable BI Connector for Atlas Manage Your Own Encryption Keys Configure Additional Options 8 Specify the Cluster Details . From the Cluster Details section, you can: Specify the Cluster Name . This label identifies the cluster in Atlas . Note Atlas creates your hostname based on your cluster name. You can't change the cluster name after Atlas deploys the
cluster. Cluster names can't exceed 64 characters in
length. Important Atlas truncates the cluster name to 23 characters in
its internal interactions. In practice, this means: Cluster names shorter than 23 characters can't end with
hyphen or dash ( - ). Cluster names 23 characters or longer can't use a hyphen or
dash ( - ) as its 23rd character. The first 23 characters in a cluster name must be unique
within a project. Don't include sensitive information in your
cluster name. Apply tags to the cluster . Important Don't include sensitive information such as Personally Identifiable
Information (PII) or Protected Health Information (PHI) in your
resource tags. Other MongoDB services, such as Billing, can access
resource tags. Resource tags are not intended for private and
sensitive data. To learn more, see Sensitive Information . 9 Proceed to checkout. Click Create Cluster below the form and complete the
billing information only if it doesn't already exist. If your
organization already has the billing information, Atlas deploys
your cluster. 10 Update your Billing Address details as needed. Field Necessity Action Billing Email Address Optional Type the email address to which Atlas should send billing alerts . By default, Atlas sends billing alerts to the Organization Owners
and Billing Admins. If you leave the Billing Email Address blank, Atlas sends billing alerts to the Organization Owners and Billing Admins. If you specify a billing email address and uncheck Only
send invoice emails to the Billing Email
Address , Atlas sends billing alerts to the billing
email address, Organization Owners, and Billing Admins. If you specify a billing email address and check the box for Only
send invoice emails to the Billing Email
Address , Atlas send billing alerts to the billing email address only. Company Name Optional Type the name of the company for your billing address. Country Required Select the country for your billing address. You can also
start typing the name of the country and then select it from
the filtered list of countries. Street Address Required Type the street address for your billing address. Apt/Suite/Floor Optional Type an the apartment, suite, or floor for your
billing address. City Required Type the name of the city for your billing address. State/Province/Region Required Type or select the political subdivision in which your billing
address exists. The label and field change depending on what
you selected as your Country : If you select United States as your Country , this
label changes to State . The field changes to a dropdown
menu of U.S. states. You can also start typing the name of
the state and then select it from the filtered list of
states. If you select Canada as your Country , this label
changes to Province . The field changes to a dropdown
menu of Canadian provinces. You can also start typing the
name of the province and then select it from the filtered
list of provinces. If you select any other country as your Country , this
label changes to State/Province/Region . The field
changes to a text box. Type the name of your province,
state, or region in this box. ZIP or Postal Code Required Type the ZIP (U.S.) or Postal Code (other countries) for your
billing address. VAT Number Conditional Atlas displays the VAT ID field if you
select a country other than the United States. To learn more about VAT, see VAT ID . If your company's billing address is in a country other than
the United States (USA), Atlas typically charges VAT if you do
not enter a valid VAT ID Number on your billing profile . IMPORTANT: If your billing address is in Ireland or certain
Canadian provinces, Atlas always charges VAT , even with a valid VAT ID Number . To learn more about VAT by region, see International Usage and Taxation . 11 Update your Payment Method details as needed. Click the radio button for Credit Card or Paypal . If you selected Credit Card , type values for the
following fields: Field Necessity Action Name on Card Required Type the name that appears on your credit card. Card Number Required Type the 16-digit number that appears on your
credit card. American Express uses a 15-digit number. Expiration Date Required Type the expiration date for your credit card in the
two-digit month and two-digit year format. CVC Required Type the three-digit number on the back of your credit
card. American Express uses a 4-digit number found on
the front of the credit card. If you selected PayPal : Click Pay with PayPal . Complete the actions on the PayPal website. Note All projects within your organization share the same billing
settings, including payment method. 12 Review project's cost. Under the Cart section, review the following: Field Description Cluster Tier Displays cost for your selected cluster tier and configuration
details. To learn more, see Cloud Service Provider and Region and Cluster Tier . Included Features Displays features included with your selected cluster
configuration. Additional Settings Displays additional settings that you enabled, such as cloud
backups, sharding, BI Connector , and more. To learn more, see Cloud Backups . 13 Deploy your cluster.
Click Confirm and Deploy Cluster . Important Each Atlas project supports up to 25 clusters.
Please contact Atlas support for questions or assistance regarding
the cluster limit. To contact support: In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. Request support. [ 1 ] For replica sets, the data-bearing servers are the servers hosting the
replica set nodes. For sharded clusters, the data-bearing servers are the
servers hosting the shards. For sharded clusters, Atlas also deploys
servers for the config servers ; these are
charged at a rate separate from the cluster costs. Back Cluster Types Next Create a Global Cluster
