# Set Up a Network Peering Connection - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features Set Up a Network Peering Connection On this page Required Access Configure Network Containers Configure an Atlas Network Peering Connection View Atlas Network Peering Connections Remove an Atlas Network Peering Connection Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Atlas supports network peering
connections for dedicated clusters hosted on AWS , Google Cloud , and Azure , and on multi-cloud sharded clusters. Network peering establishes a private
connection between your Atlas VPC and your cloud provider's VPC . The connection isolates traffic from public networks for added
security. Warning Atlas does not support Network Peering between clusters
deployed in a single region on different cloud providers.
For example, you cannot set up Network Peering between
an Atlas cluster hosted in a single region on AWS and an
application hosted in a single region on GCP. Required Access To set up a Network Peering connection, you must have Organization Owner or Project Owner access to
the project. Configure Network Containers Create a Network Container To configure the Atlas CIDR without configuring Network Peering,
see Create a New Network Peering Container .
You must use the API to create the container without
Network Peering. View Network Containers Atlas CLI Atlas Administration API To list all network peering containers for your project using the
Atlas CLI, run the following command: atlas networking containers list [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas networking containers list . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view your network containers, see Return All Network Peering Containers for One Project . Delete Network Containers Atlas CLI Atlas Administration API To delete the network peering container you specify using the
Atlas CLI, run the following command: atlas networking containers delete <containerId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas networking containers delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To delete a network container, see Remove One Network Peering Container . Configure an Atlas Network Peering Connection To configure Atlas Network Peering for a cluster, perform the
procedure on the tab corresponding to your cluster's cloud provider.
You also configure the Atlas VPC CIDR during this procedure. AWS Azure GCP Considerations DNS Configuration DNS resolves the cluster's hostnames to their public IP address rather than their internal IP address if: DNS hostnames are disabled, DNS resolution is disabled, and The user accesses the Atlas cluster from outside a peered VPC . To learn more about how to enable these options, see Updating DNS Support for Your VPC . If the applications deployed within AWS use custom DNS services and VPC peering with Atlas ,
see the FAQ to learn how to
connect using private connection strings. Deployments in Multiple Regions Atlas deployments in multiple regions must have a peering
connection for each Atlas region. For example: If you have a VPC in Sydney and Atlas deployments in Sydney and Singapore, create two peering
connections. AWS VPC Peering Prerequisites Create the following network traffic rule on your AWS security group
attached to your resources that connect to Atlas : Permission Direction Port Target Allow outbound 27015-27017 inclusive to your Atlas CIDR Configure Network Peering for an AWS-backed Cluster To configure Atlas VPC Peering for an AWS -backed
cluster: 1 In AWS , enable DNS hostnames and DNS resolution . Log in to your AWS account. Go to the VPC dashboard . Open your list of VPC resources. Select the VPC you want to peer with. Enable DNS hostnames and DNS resolution . These settings ensure that when your application connects to the
cluster within the VPC it uses private IP
addresses. 2 Add a new Network Peering connection for your project. Note You can skip this step if you are using the Atlas CLI to add a network peering connection. In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. In the Peering tab, click Add Peering Connection . 3 In Atlas , configure your network peering connection. Atlas CLI Atlas UI To create a network peering connection with AWS using the Atlas CLI, run the following command: atlas networking peering create aws [options] To watch for a peering connection to become available using the Atlas CLI, run the following command: atlas networking peering watch <peerId> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas networking peering create aws and atlas networking peering watch . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI In the Peering Connection modal, select AWS and click Next . Atlas displays
the Peering Connection modal. Important Atlas does not support adding AWS security groups of
cross-region peered VPC s to IP access lists. Instead,
use the CIDR block of the peer VPC. To learn more about
this limitation, see the AWS documentation . To learn more about CIDR blocks, see RFC 4632 . Fill out the fields in the Your Application VPC section. Field Description Account ID Unique number that identifies the AWS Account ID of the
owner of the peer VPC . To find your AWS Account ID , click Learn More . VPC ID Unique string that starts with vpc- that identifies the
peer VPC . To find your VPC ID , click Learn More . VPC CIDR AWS VPC CIDR block or subset of the network in which
your application runs. This range cannot overlap with your Atlas CIDR Block or any other Network Peering
connection VPC CIDR . The CIDR block must be in one of the following private networks : Lower Bound Upper Bound Prefix 10.0.0.0 10.255.255.255 10/8 172.16.0.0 172.31.255.255 172.16/12 192.168.0.0 192.168.255.255 192.168/16 To include this VPC CIDR block in your IP access list,
click Add this CIDR block to my IP whitelist .
You can choose to add the Security Group associated with the AWS VPC . To learn more about CIDR blocks, see RFC 4632 . Application VPC Region AWS region where the AWS VPC resides. Fill out the fields in the Your Atlas VPC section. Field Description Atlas VPC Region AWS region where the Atlas VPC resides. Atlas creates a VPC for the Atlas project in your chosen
region if that region has no M10 or greater clusters or VPC peering connections. Clear Same as application VPC region to select
a region different from where your application's VPC resides. VPC CIDR Atlas uses this Atlas CIDR block for all other Network Peering
connections created in the project. The Atlas CIDR block must be
at least a /24 and at most a /21 in one of the following private networks . Lower Bound Upper Bound Prefix 10.0.0.0 10.255.255.255 10/8 172.16.0.0 172.31.255.255 172.16/12 192.168.0.0 192.168.255.255 192.168/16 Atlas locks this value for a given region if an M10 or greater
cluster or a Network Peering connection already exists in that region. To modify the CIDR block, the target project cannot have: Any M10 or greater clusters with nodes in the target region Any cloud backup snapshots stored in the target region Any other VPC peering connections to the target region You can also create a new project then create a Network Peering Connection to set the desired Atlas VPC CIDR block for that project. IMPORTANT: Atlas limits the number of MongoDB nodes per Network Peering
connection based on the CIDR block and the region selected for the project: For example, a project in an AWS region supporting 3 availability
zones and a Atlas CIDR VPC block of /24 is
limited to the equivalent of 27 three-node replica sets. Contact MongoDB Support for any questions on Atlas limits of MongoDB nodes per VPC . Click Initiate Peering . Wait for approval of peering connection request. The owner of the peer VPC must approve the VPC peering
connection request. Ensure that the owner approves the request. Atlas provides instructions for approving the connection
request. Important Requests expire after 7 days. 4 In AWS , update your VPC's route table. In the VPC Dashboard , click Route Tables . Select the Route Table for your VPC or subnets. Click the Routes tab. Click Edit Routes . Click Add route . Add the Atlas VPC 's CIDR block to the Destination column. Add the AWS Peering Connection ID to the Target column. This value uses a prefix of pcx- . Click Save . Note Each Atlas project may have a maximum of 50 peering connections
in total. This total includes a maximum of 25 pending
peering connections. Once set up, you can edit or terminate VPC peering
connection from the Peering table. Before your new VPC peer can connect to your Atlas cluster,
you must: Locate the VPC CIDR block addresses (or subset), or the
Security Groups, associated with the VPC configured
in your project. Add at least one of these CIDR blocks to the access list . Tip See also: CIDR Subnet Selection for MongoDB Atlas FAQ on changes to AWS network peering . Note Effective March 31, 2020, Atlas has removed the Peering-Only Mode limitations for all existing and new
Azure clusters. To learn how to use these new features, see
the FAQ on changes to Azure network peering Azure Roles Required to Configure a Network Peering Connection To learn the Azure roles that you need to create a Network
Peering connection, see the Azure documentation . Configure Network Peering for an Azure-backed Cluster To configure Network Peering for an Azure -backed cluster: 1 Add a new Network Peering connection for your project. Note You can skip this step if you are using the Atlas CLI to add a network peering connection. In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. In the Peering tab, click Add Peering Connection . 2 In Atlas , configure your network peering connection. Important For multi-region Azure clusters, you must create a peering connection for
each Atlas region from your application's regional VNET. For example, if you have an application VNET in Sydney, another application
VNET in Singapore, and Atlas nodes deployed in both regions, with the
primary node deployed in Sydney, you need to cross peer the application
VNET in Singapore to the Atlas VNET in Sydney, in addition to
the Atlas VNET in Singapore, in order to establish a successful
connection between the application in Singapore and the primary node. To configure the Atlas region, fill in the Atlas Vnet Region field in the Peering Connection modal. Atlas CLI Atlas UI To create a network peering connection with Azure using the Atlas CLI, run the following command: atlas networking peering create azure [options] To watch for a peering connection to become available using the Atlas CLI, run the following command: atlas networking peering watch <peerId> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas networking peering create azure and atlas networking peering watch . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI In the Peering Connection modal, select Azure and click Next . To create the Network Peering connection, fill in the
requested information: Field Description Subscription ID Unique identifier for your Azure subscription. You
can find this information on the Overview tab of your
Azure Virtual networks dashboard. Directory ID Unique identifier of your Azure directory. You
can find this information on the Properties tab of your Microsoft Entra ID dashboard. Resource Group Name Unique identifier of the Azure resource group to
which the virtual network belongs. You can find this
information on the Overview tab of your
Azure virtual network. VNet Name Name of your Azure virtual network. You can find
this information on the Virtual networks dashboard. Atlas CIDR CIDR block for your Atlas cluster. Atlas uses the specified CIDR block for all other Network Peering
connections created in the project. You can't create peering connection
if a peer with an overlapping CIDR block already exists. The Atlas CIDR block must be at least /24 and at most /21 in
one of the following private networks . Lower Bound Upper Bound Prefix 10.0.0.0 10.255.255.255 10/8 172.16.0.0 172.31.255.255 172.16/12 192.168.0.0 192.168.255.255 192.168/16 Atlas locks this value for a given region if an M10 or greater
cluster or a Network Peering connection already exists in that region. To modify the CIDR block, the target project cannot have: Any M10 or greater clusters with nodes in the target region Any cloud backup snapshots stored in the target region Any other VPC peering connections to the target region Alternatively, create a new project and create a Network Peering Connection to set the desired Atlas Network Peering CIDR block for that project. IMPORTANT: Atlas limits the number of MongoDB nodes per Network Peering
connection based on the CIDR block and the region selected for the project.
Contact MongoDB Support for any questions on Atlas limits of MongoDB nodes per VPC . Atlas VNet Region Azure region in which your Atlas cluster
resides. Click Next . 3 In Azure , create the peering request. You must grant Atlas the
following permissions on the virtual network. You can revoke
these permissions after the VNet peering has been
established. Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read Microsoft.Network/virtualNetworks/virtualNetworkPeerings/write Microsoft.Network/virtualNetworks/virtualNetworkPeerings/delete Microsoft.Network/virtualNetworks/peer/action To grant Atlas permission to create a peering
connection with your Azure virtual network: Launch the Azure console. Run the commands from the Peering Connection modal to create a service principal, create a new custom
role, and assign the custom role to the service
principal. Note Run the first command to create a service principal
only once for all Azure VNets from the same Azure
subscription. Click Validate . Click Initiate Peering . You must add the CIDR block address (or subset)
associated with the peer VNet to the whitelist before your network peer
can connect to your Atlas cluster. When connecting to your
cluster, you must use the new private connection string to utilize the peering. Considerations VPC peering connections Atlas have the following limitations: Google Kubernetes Engine (GKE) supports two network modes: routes-based and VPC-native. While VPC-native GKE clusters
can connect to Atlas clusters, route-based GKE clusters can't connect to Atlas clusters via peering because Atlas doesn't accept custom routes when VPC peering connections are created. Consider using Public IP allow lists for
route-based GKE clusters. Google App Engine (Standard), Cloud Functions, and Cloud Run can't connect to Atlas clusters over VPC peering connections. To connect over VPC peering, these services require a serverless VPC Access connector. Clients can't connect to Atlas clusters with Google Cloud VPN (Virtual Private Network) or Interconnect because Atlas doesn't accept custom routes when VPC peering connections are created. Consider creating private
endpoints . Configure VPC Peering for a GCP-backed Cluster To configure Atlas VPC Peering for a Google Cloud -backed
cluster: 1 Add a new Network Peering connection for your project. Note You can skip this step if you are using the Atlas CLI to add a network peering connection. In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. In the Peering tab, click Add Peering Connection . 2 In Atlas , configure your network peering connection. Note Since Google Cloud uses global VPCs, you need to create only one peering connection. Atlas CLI Atlas UI To create a network peering connection with Google Cloud using the Atlas CLI, run the following command: atlas networking peering create gcp [options] To watch for a peering connection to become available using the Atlas CLI, run the following command: atlas networking peering watch <peerId> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas networking peering create gcp and atlas networking peering watch . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI In the Peering Connection modal, select Google Cloud Platform and click Next . To create the VPC Peering connection, fill in the
requested information in the Peering Connection modal: Field Description Project ID Google Cloud Project ID of the peer VPC . Refer to the
dialog box for instructions on finding your GCP Project ID . VPC Name Name of the peer VPC . Refer to the dialog box for
instructions on finding your VPC Name . Atlas CIDR CIDR block for your Atlas cluster. Atlas uses the specified CIDR block for all other Network Peering
connections created in the project. By default, the Atlas CIDR block must be at least an /18 in one of the following private networks . Lower Bound Upper Bound Prefix 10.0.0.0 10.255.255.255 10/8 172.16.0.0 172.31.255.255 172.16/12 192.168.0.0 192.168.255.255 192.168/16 If your application requires Atlas to use a smaller CIDR block,
use the Atlas API to create an Atlas network
peering container with a CIDR block of /21 to /24 . When you choose a smaller CIDR block, the IP address space of the CIDR block you choose is distributed evenly across the Google Cloud regions
to which you deploy the network peering container. Atlas requires a CIDR block of /24 for each region. Refer to the following table to
learn the number of regions to which you can deploy a network peering
container based on the CIDR block you choose. CIDR Block Number of Google Cloud Regions /21 1 - 8 /22 1 - 4 /23 1 - 2 /24 1 IMPORTANT: You can't use the Atlas user interface to specify an Atlas CIDR block smaller than /18 . You must use the Atlas API and
specify the regions (up to eight, based on the CIDR block you
choose) to which to deploy the network peering container. You can
deploy Atlas clusters only to these regions in this project. Atlas locks this value for all regions if an M10 or greater
cluster or a Network Peering connection already exists in that project. To modify the CIDR block, the target project cannot have: Any M10 or greater clusters Any other VPC peering connections Alternatively, create a new project and create a Network Peering Connection to set the desired Atlas Network Peering CIDR block for that project. IMPORTANT: Atlas limits the number of MongoDB nodes per Network Peering
connection based on the CIDR block and the region selected for the project. For example, a project with an Atlas VPC CIDR block of /18 is limited to approximately 80 three-node
replica sets per Google Cloud region. Contact MongoDB Support for any questions on Atlas limits of MongoDB nodes per Network Peering connection. Click Initiate Peering . 3 In Google Cloud , create the peering connection. In the Google Cloud Console , click VPC network peering . Click Create Connection . Click Continue . In Name , enter a name for your peering
connection. In Your VPC Network , enter the name of your Google Cloud VPC network. In Peered VPC network , select In another project . In Project ID , enter your Atlas Project ID. To find this name in the VPC Peering view in Atlas . In
the Security section of the left navigation: In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. Click the Peering tab. In VPC network name , enter your Atlas VPC Name. To find this name in the VPC Peering view in Atlas : In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. Click the Peering tab. Note Each Atlas project may have a maximum of 50 peering connections
in total. This total includes a maximum of 25 pending
peering connections. You must add your VPC CIDR block address (or subset)
associated with the peer VPC to the IP access list before your new VPC peer
can connect to your Atlas cluster. When connecting to your
cluster, you must use the new private connection strings to utilize the peering. Tip See also: Auto mode IP ranges . Rolling Back a Google Cloud Container with a Restricted Set of Regions After a Google Cloud container with a restricted set of regions is generated,
that project is locked into that set of regions. Any attempts to use other
regions will generate an error message similar to what you find below: There are no more regions supported with your existing configuration. Try changing to a different cluster tier or changing your region configuration. To resolve this error, follow this general process: Remove all clusters from the Google Cloud container . Delete the Google Cloud container using the Atlas Administration API. See Remove One
Network Peering Container . Create a new Google Cloud container without restricted regions with an Atlas CIDR block of
at least /18 using the Atlas Administration API. See Create a New Network
Peering Container . View Atlas Network Peering Connections Atlas CLI Atlas UI To return the details for all network peering connections in the project you specify using the
Atlas CLI, run the following command: atlas networking peering list [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas networking peering list . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view your network peering connections using the Atlas UI: 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Peering tab. Atlas displays your network peering connections. Remove an Atlas Network Peering Connection Atlas CLI Atlas UI To delete the network peering connection you specify using the
Atlas CLI, run the following command: atlas networking peering delete <peerId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas networking peering delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To remove your network peering connection using the Atlas UI: 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Peering tab. Atlas displays your network peering connections. 3 Remove the network peering connection. Click TERMINATE next to the network peering
connection that you want to remove. Click Yes, Terminate to confirm the removal. Back IP Access List Next Private Endpoints
