# Create a Global Cluster - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Create a Global Cluster On this page Required Access Considerations Procedure This section covers enabling Global Writes on an Atlas cluster. Required Access To create to a Global Cluster , you must have Organization Owner or Project Owner access to
the project. Considerations Before creating a Global Cluster , review Global Clusters Overview and Global Clusters Sharding Reference . You can enable Global Writes in Atlas when you create an M30 or greater sharded cluster. After you deploy the cluster, you can't convert a Global Cluster to a standard sharded cluster. Due to sharding requirements ,
you can't load sample data onto a Global Cluster . If this is the first dedicated paid cluster for the selected region or
regions and you plan on creating one or more VPC peering connections , review VPC Peering Connections before continuing. Procedure 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Open the Create New Cluster Dialog. If you already have one or more clusters, click Create to display the Create New Cluster dialog box. If this is your first cluster: Click Build a Database . Click advanced configuration options at the top of
the screen to display the Create New Cluster dialog box. 3 Enable Global Writes for your cluster. In the Create New Cluster dialog box, select
the Dedicated cluster type. For more information,
see Create a Cluster . Click Global Cluster Configuration to expand the
section. Toggle Enable Global Writes (M30 and Up) to On to display the Global Cluster configuration. 4 Select your sharding configuration. By default, global clusters enable Atlas-Managed Sharding to automatically configure the shard keys and zones for the cluster.
For each shard, Atlas creates a location field in the shard key
associated with the corresponding zone so that Atlas can distribute data to shards based on geographic location.
This option is recommended for most workloads. If you're an advanced user and the default configuration is too restrictive
for your workload, select Self-Managed Sharding .
If you select this option, you must manually configure the sharding
strategy by using mongosh or a supported MongoDB Driver .
To learn more about zone sharding, see Zones . To learn how to add shards to a zone,
see Manage Zones . Important You can't change between Atlas-Managed Sharding and Self-Managed Sharding after you deploy the cluster. 5 Select your preferred cloud provider. Note Each cloud provider has a selection of global regions to which Atlas can deploy a zone. The choice of cloud provider may
support or constrict your ability to deploy a zone to specific
geographic locations. The configuration options available and
the cost for running the cluster may also vary depending on
cloud provider selection. 6 Configure your Global Cluster Zones. Atlas provides three options for configuring your Global Cluster zones: Configure Global Writes Zones Using a Template Configure a Global Writes Single Region Zone Configure a Global Writes Multi Region Zone Select the appropriate tab based on how you would like to configure
your Global Cluster zones. Use a Template Single Region Zone Multi-Region Zone Atlas provides two templates for configuring Global Writes zones for the cluster, each with a description of the purpose
of its underlying configuration. Click on a template to view
the Zone Map for that template. The Zone Map provides a visual
description of the cluster zone configuration, including
estimates of geographic latency and coverage. Click Zone configuration summary below the zone map
to view a summary of each zone in the Global Cluster . Atlas provides the following validations for each zone: Validation Guidance Low latency reads and writes in <geography> Indicates the geographic locale for which the zone
supports low latency reads and writes. The exact
geographic locale specified depends on the preferred Region for that zone. You can modify the
zone's preferred region in the Zone
Configuration section. Local reads in all other zones Indicates whether data in this zone is replicated to
every other zone for local secondary reads by clients
in those zones. Click the Configure Local Reads in All
Zones button in the Zone configuration
summary to automatically configure every zone in the
cluster for local reads. (Not) Available during partial region outage Indicates whether the zone supports high availability,
such that a majority of electable nodes remain healthy
and reachable in the event of a partial region outage. Regions marked as Recommended in the Atlas UI support high availability during
partial regional outages. To learn more, see the following pages: Amazon Availability Zones . GCP Zones . Azure Availability Zones . (Not) Available during full region outage Indicates whether the zone supports high availability,
such that a majority of electable nodes remain healthy
and reachable in the event of a complete regional
outage. By default, each template deploys a series of single-region
zones and builds a map of country and subdivision locations
geographically near each zone. MongoDB uses this location-zone
map to route read and write operations which contain location data to the shard
or shards in the corresponding zone. If you enabled Atlas-Managed Sharding ,
click Configure Location Mappings in the Zone
Map to view the list of location-zone mappings. To customize
the location-zone mapping, click the Zone dropdown
for a given Location Name and select a new zone.
Click the Reset button to reset a custom mapping
for any given location. Click the Reset All Zone
mappings button to reset all custom mappings for the cluster. You can make additional configuration changes to each zone
after selecting a zone template. For instructions, see the Single Region Zone tab. You can also create Multi-region zones. For instructions, see
the Multi-Region Zone tab. Clicking Configure Local Reads in All Zones converts all
zones to multi-region. Click View Zone Templates in the Zone Map to return
to the template selection. The Zone Configuration section allows you to
configure each zone in your cluster. Atlas displays a
drop-down box directly above the Zone Configuration that indicates the currently selected zone. Click the + Add a Zone button to add additional zones to the Global Cluster , up to a maximum of nine (9) zones. If
you require more than nine zones, contact Atlas support . The Zone Map updates as you modify each zone. If the Zone Map
currently displays the template selection menu, click Configure Zones Myself to view the Zone map. In the Zone Configuration section,
click the Select the preferred region for your zone drop-down box and select a region as the Highest
Priority region for each shard assigned to the zone. Atlas builds a map of countries and subdivisions that are
geographically near the selected region. MongoDB uses this
location-zone map to route read and write operations which
contain location data to the
shard or shards in the corresponding zone. If you enabled Atlas-Managed Sharding ,
click Configure Location Mappings in the Zone Map
to view the list of location-zone mappings. To customize the
location-zone mapping, click the Zone dropdown for
a given Location Name and select a new zone. Click
the Reset button to reset a custom mapping for any
given location. Click the Reset All Zone mappings button to reset all custom mappings for the cluster. For each shard in the zone, Atlas distributes the shard
nodes with respect to the Zone Configuration . You
can add additional shards to the zone by clicking Additional Options in the Zone
Configuration section and selecting the total number of shards
in the zone from the drop-down box. By default, Atlas deploys one shard per zone. Atlas recommends creating
additional zones to support heavy write load in a geographic
region instead of adding multiple shards to a single zone. Atlas supports no more than 100 shards per Global Cluster . Important Selecting a zone template resets any
configuration changes made in the Zone
Configuration section to the default for the selected
template. The Zone Configuration section allows you to
configure each zone in your cluster. Atlas displays a
drop-down box directly above the Zone Configuration that indicates the currently selected zone. Click the + Add a Zone button to add additional zones to the Global Cluster , up to a maximum of nine (9) zones. If
you require more than nine zones, contact Atlas support . The Zone Map updates as you modify each zone. If the Zone Map
currently displays the template selection menu, click Configure Zones Myself to view the Zone map. Click the Select Multi-Region, Workload Isolation and Replication Options button to display the multi-region configuration controls.
Zones for which you toggled the Configure Local Reads in All Zones in the Zone configuration summary display the multi-region
zone controls by default. Electable nodes for high availability Configure the Highest Priority and Electable nodes in the zone. Tip See also: Global Write Zones and Zone Mapping . If you add regions with electable nodes, you: increase data availability and reduce the impact of data center outages. You may set different regions from one cloud provider or choose
different cloud providers. Atlas sets the node in the first row of the Electable nodes table as the Highest Priority region. Atlas prioritizes nodes in this region for primary eligibility.
Other nodes rank in the order that they appear. For more information,
see Member Priority . Click Add a region to add a new row for region
selection and select the region from the dropdown. Specify
the desired number of Nodes for the region. The
total number of electable nodes across all regions in the
zone must be 3, 5, or 7. Atlas builds a map of countries and subdivisions
geographically near the selected region for the Highest Priority node. MongoDB uses this
location-zone map to route read and write operations which
contain location data to
the shard or shards in the corresponding zone. If you enabled Atlas-Managed Sharding ,
click Configure Location Mappings in the Zone
Map to view the list of location-zone mappings. To customize
the location-zone mapping, click the Zone dropdown for a given Location Name and select a
new zone. Click the Reset button to reset a
custom mapping for any given location. Click the Reset All Zone mappings button to reset all
custom mappings for the cluster. Read-only nodes for optimal local reads Configure the Read-only nodes in the zone. Each
row represents one Region where Atlas deploys
the configured Number of Nodes of the Read-only Node Type . Click Add a region to add additional Read-only rows. Consider
adding Read-only nodes in each region where you
want to facilitate local secondary read operations. Analytics nodes for workload isolation Use analytics nodes to isolate
queries which you do not wish to contend with your operational
workload. Analytics nodes help handle data analysis operations, such as
reporting queries from BI Connector for Atlas . Analytics nodes have distinct replica set tags which allow you
to direct queries to desired regions. Click Add a region to select a region in which to
deploy analytics nodes. Specify the desired number of Nodes for the region. For each shard in the zone, Atlas distributes the shard
nodes with respect to the Zone Configuration . You
can add additional shards to the zone by clicking Additional Options in the Zone
Configuration section and selecting the total number of shards
in the zone from the drop-down box. By default, Atlas deploys one shard per zone. Atlas recommends creating
additional zones to support heavy write load in a geographic
region instead of adding multiple shards to a single zone. Atlas supports no more than 100 shards per Global Cluster . Important Selecting a zone template resets any configuration changes made in the Zone Configuration section to the default for the
selected template. Note Removing Zones from an Existing Global Cluster If you are using the standard connection string format rather than the DNS seedlist format,
removing an entire zone from an existing global cluster may result
in a new connection string. To verify the correct connection string after deploying the changes: In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. Verify the connection string. Click Connect . 7 Select the Cluster Tier . To use Global Clusters , you must select a cluster tier
that is M30 or larger. The selected tier dictates the memory, storage, vCPUs, and IOPS specification for each data-bearing server in the
cluster. For more information on how to select an appropriate cluster tier and
storage settings for your workload, see Select Cluster Tier and Customize Cluster Storage . 8 Select any Additional Settings . From the Additional Settings section
for Global Clusters , you can: Select the MongoDB Version of the Cluster Configure Backup Options for the Cluster Enable BI Connector for Atlas Manage Your Own Encryption Keys Configure Additional Options 9 Specify the Cluster Name . This is the cluster name as it appears in Atlas . You can't
change the cluster name once Atlas deploys the cluster. Cluster names can't exceed 64 characters in length. Important Atlas truncates the cluster name to 23 characters in
its internal interactions. In practice, this means: Cluster names shorter than 23 characters can't end with
hyphen or dash ( - ). Cluster names 23 characters or longer can't use a hyphen or
dash ( - ) as its 23rd character. The first 23 characters in a cluster name must be unique
within a project. Don't include sensitive information in your
cluster name. 10 Proceed to checkout.
Click Create Cluster below the form and complete the
billing information only if it doesn't already exist. If your
organization already has the billing information, Atlas deploys
your cluster. 11 Update your Billing Address details as needed. Field Necessity Action Billing Email Address Optional Type the email address to which Atlas should send billing alerts . By default, Atlas sends billing alerts to the Organization Owners
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
Canadian provinces, Atlas always charges VAT , even with a valid VAT ID Number . To learn more about VAT by region, see International Usage and Taxation . 12 Update your Payment Method details as needed. Click the radio button for Credit Card or Paypal . If you selected Credit Card , type values for the
following fields: Field Necessity Action Name on Card Required Type the name that appears on your credit card. Card Number Required Type the 16-digit number that appears on your
credit card. American Express uses a 15-digit number. Expiration Date Required Type the expiration date for your credit card in the
two-digit month and two-digit year format. CVC Required Type the three-digit number on the back of your credit
card. American Express uses a 4-digit number found on
the front of the credit card. If you selected PayPal : Click Pay with PayPal . Complete the actions on the PayPal website. All projects within your organization share the same billing
settings, including payment method. 13 Review project's cost. Under the Cart section, review the following: Field Description Cluster Tier Displays cost for your selected cluster tier and configuration
details. To learn more, see Cloud Service Provider and Region and Cluster Tier . Included Features Displays features included with your selected cluster
configuration. Additional Settings Displays additional settings that you enabled, such as cloud
backups, sharding, BI Connector , and more. To learn more, see Cloud Backups . 14 Deploy your cluster.
Click Confirm and Deploy Cluster below the form to deploy your
cluster. Important Each Atlas project supports up to 25 clusters.
Please contact Atlas support for questions or assistance regarding
the cluster limit. To contact support: In Atlas , go to the Project Support page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Support . The Project Support page displays. Request support. 15 Shard a global collection. If you selected Atlas-Managed Sharding , you can
use the Atlas UI to shard a collection for global writes.
To learn more, see Shard a Global Collection . If you selected Self-Managed Sharding , you must manually
configure the shard key and shard the global collection. To learn more,
see Shard Keys and Shard a Collection . Tip See also: Manage Global Clusters Back Create a Cluster Next Cloud Providers and Regions
