# Learn About Private Endpoints in Atlas - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Private Endpoints Learn About Private Endpoints in Atlas On this page Required Access Considerations Limitations Prerequisites Note This feature is not available for M0 Free clusters, M2 , and M5 clusters. To learn more about which features are unavailable,
see Atlas M0 (Free Cluster), M2, and M5 Limits . MongoDB Atlas supports private endpoints on dedicated clusters. Select
your cluster type to learn which cloud providers Atlas supports: AWS using the AWS PrivateLink feature. Azure using the Azure Private Link feature. Google Cloud using the GCP Private Service Connect feature. You can also set up private endpoints for your Online Archive. To
learn more, see Set Up a Private Endpoint for Online Archives . AWS PrivateLink Azure Private Link GCP Private Service Connect Private Endpoint Concepts When you enable PrivateLink in AWS and private
endpoints in Atlas , AWS and Atlas create the following
resources to support secure connections over VPC s: Resource Creator Description Private endpoint service Atlas A collection of private endpoint resources within
your Atlas VPC that places clusters within a region behind a network load balancer. AWS refers to the endpoint
service as the VPC endpoint service . Interface endpoint AWS AWS VPC endpoint with a private IP address
that sends traffic to the private endpoint service over AWS PrivateLink. AWS refers to the
interface endpoint as the VPC endpoint . Private endpoint AWS and Atlas together A generic term for the private
connection established
between Atlas and your cloud provider. For AWS , that connection is established using PrivateLink. AWS PrivateLink AWS PrivateLink with Direct Connect Connections to Atlas clusters using private
endpoints offer the following advantages over other network
access management options: Connections using private endpoints are one-way. Atlas VPC s can't initiate connections back to your VPC s. This
ensures your perceived network trust boundary is not extended. Connections to private endpoints within your VPC can be made
transitively from: Another VPC peered to the private endpoint-connected VPC . An on-premises data center connected with DirectConnect to the private endpoint-connected VPC . This enables you to
connect to Atlas directly from your on-premises data
center without adding public IP addresses to the Atlas IP access list . Private Endpoint Concepts When you enable this feature, Azure and Atlas create
the following resources to support secure connections over
VNets: Resource Creator Description Private endpoint service Atlas A collection of private endpoint resources within
your Atlas VNet that places
clusters within a region behind a
network load balancer. Private endpoint Azure and Atlas together A generic term for the private
connection established
between Atlas and your cloud provider. For Azure , that connection is established using Private Link. Atlas creates a Private
Link service and places clusters within a region behind a
load balancer in the Atlas VNet. Then you create resources that establish a one-way
connection from your VNet to the Private Link
service in
the Atlas VNet using a private endpoint. The Private
Link service routes traffic to the load balancer that
fronts the clusters in the Atlas VNet. Connections to Atlas clusters using private
endpoints offer the following advantages over other network access
management options: Connections using private endpoints are one-way. Atlas VNets can't initiate connections back to your VNets. This
ensures your perceived network trust boundary is not extended. Connections to private endpoints within your VNet can be
made transitively from: Another VNet peered to the private endpoint-connected VNet. An on-premises data center connected with ExpressRoute to the private endpoint-connected VNet. This enables
you to connect to Atlas directly from your
on-premises data center without adding public IP
addresses to the Atlas IP access list . Private Endpoint Concepts When you enable this feature, Google Cloud and Atlas create
the following resources to support secure connections over VPC s: Resource Creator Description Private endpoint service Atlas A collection of private endpoint resources within
your Atlas VPC that places
clusters within a region behind
network load balancers. Private endpoints Google Cloud and Atlas together A generic term for the private
connections established
between Atlas and your cloud provider. For Google Cloud , those connections are established using
Private Service Connect. When you enable GCP Private Service Connect in Google Cloud , Atlas creates a private endpoint service using service attachments and load balancers. Next, you create resources that establish a one-way
connection from your VPC to the private endpoint service
in Atlas using a private endpoint. The private endpoint
service routes traffic to the load balancers for the
clusters in the Atlas VPC . To ensure the availability of resources for both current
and future clusters, Atlas performs the following
actions when you enable this feature: Creates 50 load balancers and service attachments for that region. Then, Atlas places existing clusters within the region behind load balancers
in the Atlas VPC . GCP Private Service Connect requires a separate load balancer
for each node within every cluster. Reserves any remaining load balancers and service attachments for future
clusters within that region. One Cluster, One Region Multiple Clusters, One Region The following diagram shows how GCP Private Service Connect
establishes connections when you have one cluster
in one region. The following diagram shows how GCP Private Service Connect
establishes connections when you have two
clusters in one region. Connections to Atlas clusters using private endpoints
offer the following advantages over other network access
management options: Connections to private endpoints are one-way. Atlas VPC s can't initiate connections back to your Google Cloud VPC s. This ensures your perceived network trust
boundary is not extended. You can connect to private endpoints within your VPC transitively from an on-premises data center connected
with Google Cloud VPN to the private endpoint-connected VPC . This enables you to connect to Atlas directly
from your on-premises data center without adding public IP
addresses to the Atlas access list. You can also set up private endpoints for your Online Archive. To
learn more, see Set Up a Private Endpoint for Online Archives . AWS PrivateLink Azure Private Link Connections to Atlas clusters using private
endpoints offer the following advantages over other network
access management options: Connections using private endpoints are one-way. Atlas VPC s can't initiate connections back to your VPC s. This
ensures your perceived network trust boundary is not extended. Connections to private endpoints within your VPC can be made
transitively from: Another VPC peered to the private endpoint-connected VPC . An on-premises data center connected with DirectConnect to the private endpoint-connected VPC . This enables you to
connect to Atlas directly from your on-premises data
center without adding public IP addresses to the Atlas IP access list . Connections to Atlas clusters using private
endpoints offer the following advantages over other network access
management options: Connections using private endpoints are one-way. Atlas VNets can't initiate connections back to your VNets. This
ensures your perceived network trust boundary is not extended. Connections to private endpoints within your VNet can be
made transitively from: Another VNet peered to the private endpoint-connected VNet. An on-premises data center connected with ExpressRoute to the private endpoint-connected VNet. This enables
you to connect to Atlas directly from your
on-premises data center without adding public IP
addresses to the Atlas IP access list . Required Access To set up a private endpoint, you must have Organization Owner or Project Owner access to
the project. Considerations High Availability AWS PrivateLink Azure Private Link GCP Private Service Connect To ensure private endpoint connections to Atlas can
withstand an availability zone outage, you should deploy
subnets to multiple availability zones in a region. You don't need to take additional actions to ensure that Azure private endpoint connections to Atlas can
withstand an availability zone outage. You don't need to take additional actions to ensure that Google Cloud private endpoint connections to Atlas can
withstand an availability zone outage. Multi-Region Support GCP Private Service Connect now provides multi-region support for your Atlas clusters. You can configure global access to connect to private endpoints from a different Google Cloud region.
By using global access, you can ensure high availability for
your multi-region clusters, single-region deployments
hosted in a different region than your own, and Google Cloud nodes in your
multi-cloud deployments. To learn more, see Introducing PSC Interconnect and Global Access for MongoDB Atlas . Port Ranges Used for Private Endpoints AWS PrivateLink Azure Private Link GCP Private Service Connect AWS PrivateLink supports 50 addressable targets, Atlas can use port 1024 through port 65535,
but typically starts with port 1024. The ports
can change under specific circumstances, including
(but not limited to) cluster changes. Important MongoDB strongly recommends using the DNS seedlist
private endpoint-aware connection string, so that DNS
automatically updates the ports that AWS PrivateLink uses if
they change. For the same reason, MongoDB also strongly
recommends allow-listing the entire port range, instead
of specific ports. Azure Private Link supports 150 addressable targets. Atlas can use port 1024
through port 2524, but typically starts with port 1024. The ports
can change under specific circumstances, including (but not limited to)
cluster changes. Important MongoDB strongly recommends that you use the DNS seedlist private
endpoint-aware connection string so that DNS automatically updates
the ports that Azure Private Link uses if they change. For the same reason,
MongoDB also strongly recommends allow-listing the entire port
range instead of specific ports. Atlas services are accessed through
GCP Private Service Connect endpoints on ports 27015 through 27017. The
ports can change under specific circumstances, including
(but not limited to) cluster changes. Important MongoDB strongly recommends using the DNS seedlist
private endpoint-aware connection string, so that DNS
automatically updates the ports that GCP Private Service Connect uses if
they change. For the same reason, MongoDB also strongly
recommends allow-listing the entire port range, instead
of specific ports. Private Endpoint-Aware Connection Strings Dedicated Clusters AWS PrivateLink Azure Private Link GCP Private Service Connect Dedicated Clusters Serverless Instances When you configure a private endpoint, Atlas generates DNS
seedlist and standard private endpoint-aware connection strings: DNS seedlist connection mongodb+srv://cluster0-pl-0-k45tj.mongodb.net Standard connection string mongodb://pl-0-us-east-1-k45tj.mongodb.net:1024,pl-0-us-east-1-k45tj.mongodb.net:1025,pl-0-us-east-1-k45tj.mongodb.net:1026/?ssl=true&authSource=admin&replicaSet=Cluster0-shard-0-shard-0 When a client in your VPC connects to an Atlas cluster using one of these private endpoint-aware
connection strings, the client attempts to
establish a connection to the load balancer in the Atlas VPC through one of the interface endpoints .
Your client's DNS resolution mechanism handles which of the interface
endpoints the hostname resolves to. If one interface endpoint is
unavailable the next is used. This is opaque to the driver or other
connection mechanism. The driver is only aware of the hostname in the
SRV record or in the connection string. SRV Record for DNS Seedlist Private Endpoint-Aware Connection
Strings The following example shows the SRV record for an AWS PrivateLink
-enabled single-region cluster, showing three unique ports
defined for pl-0-us-east-1-k45tj.mongodb.net : $ nslookup - type =SRV _mongodb._tcp.cluster0-pl-0-k45tj.mongodb.net Server: 127.0.0.53 Address: 127.0.0.53#53 Non-authoritative answer: _mongodb._tcp.cluster0-pl-0-k45tj.mongodb.net service = 0 0 1026 pl-0-us-east-1-k45tj.mongodb.net. _mongodb._tcp.cluster0-pl-0-k45tj.mongodb.net service = 0 0 1024 pl-0-us-east-1-k45tj.mongodb.net. _mongodb._tcp.cluster0-pl-0-k45tj.mongodb.net service = 0 0 1025 pl-0-us-east-1-k45tj.mongodb.net. In the preceding example: _mongodb._tcp.cluster0-pl-0-k45tj.mongodb.net is the SRV
record that the mongodb+srv://cluster0-pl-0-k45tj.mongodb.net connection string references. pl-0-us-east-1-k45tj.mongodb.net is the hostname for each
node in one Atlas cluster in one region for which
you have configured AWS PrivateLink. 1024 , 1025 , and 1026 are unique ports that Atlas assigns on the load balancer for each Atlas replica set node in the region for which you enabled
AWS PrivateLink. All nodes in an Atlas replica set are
accessible via the same hostname, with the load balancer
resolving individual nodes by their unique port. Hostname DNS Resolution in Private Endpoint-Aware Connection
Strings and SRV Records The hostname in the SRV record and the standard connection string
is a DNS Canonical Name ( CNAME ) record that resolves to the
endpoint-specific regional DNS name that AWS generates for the
interface endpoint. A DNS ALIAS record exists for each
subnet in your VPC that you deployed the interface endpoint to.
Each ALIAS record contains the private IP address of the interface endpoint for that subnet. The following example shows the DNS lookup for the hostname in
the SRV record and in the standard connection string, including
the endpoint-specific regional DNS name for the interface
endpoint and its DNS ALIAS records: $ nslookup pl-0-us-east-1-k45tj.mongodb.net Server: 127.0.0.53 Address: 127.0.0.53#53 Non-authoritative answer: pl-0-us-east-1-k45tj.mongodb.net canonical name = vpce-024f5b57108c8d3ed-ypwbxwll.vpce-svc-02863655456245e5c.us-east-1.vpce.amazonaws.com. Name: vpce-024f5b57108c8d3ed-ypwbxwll.vpce-svc-02863655456245e5c.us-east-1.vpce.amazonaws.com Address: 10.0.30.194 Name: vpce-024f5b57108c8d3ed-ypwbxwll.vpce-svc-02863655456245e5c.us-east-1.vpce.amazonaws.com Address: 10.0.20.54 When you configure a private endpoint, Atlas generates DNS
seedlist connection strings: DNS seedlist connection mongodb+srv://serverlessinstance0-pl-0-k45tj.mongodb.net When a client in your VPC connects to an Atlas cluster using one of these private endpoint-aware
connection strings, the client attempts to
establish a connection to the load balancer in the Atlas VPC through one of the interface endpoints .
Your client's DNS resolution mechanism handles which of the interface
endpoints the hostname resolves to. If one interface endpoint is
unavailable the next is used. This is opaque to the driver or other
connection mechanism. The driver is only aware of the hostname in the
SRV record or in the connection string. SRV Record for DNS Seedlist Private Endpoint-Aware Connection
Strings The following example shows the SRV record for an AWS PrivateLink-enabled
Serverless instance, showing one port defined for serverlessinstance0-pe-1.oqg5v.mongodb.net : $ nslookup - type =SRV _mongodb._tcp.serverlessinstance0-pe-1.oqg5v.mongodb.net Server: 127.0.0.1 Address: 127.0.0.1#53 Non-authoritative answer: _mongodb._tcp.serverlessinstance0-pe-1.oqg5v.mongodb.net service = 0 0 27017 pe-1-serverlessinstance0.oqg5v.mongodb.net. In the preceding example: _mongodb._tcp.serverlessinstance0-pe-1.oqg5v.mongodb.net is the SRV record that the mongodb+srv://serverlessinstance0-pe-1.oqg5v.mongodb.net connection string references. serverlessinstance0-pe-1.oqg5v.mongodb.net is the hostname
for the Atlas Serverless instance for which you have
configured AWS PrivateLink. 27017 is a unique port that Atlas assigns to the load
balancer for the Atlas Serverless instance for which you
enabled AWS PrivateLink. Hostname DNS Resolution in Private Endpoint-Aware Connection
Strings and SRV Records The hostname in the SRV record and the standard connection string
is a DNS Canonical Name ( CNAME ) record that resolves to the
endpoint-specific regional DNS name that AWS generates for the
interface endpoint. A DNS ALIAS record exists for each
subnet in your VPC that you deployed the interface endpoint to.
Each ALIAS record contains the private IP address of the interface endpoint for that subnet. Dedicated Clusters Serverless Instances When you configure a private endpoint, Atlas generates DNS
seedlist and standard private endpoint-aware connection strings: DNS seedlist connection mongodb+srv://cluster0-pl-0.uzgh6.mongodb.net Standard connection string mongodb://pl-0-eastus2.uzgh6.mongodb.net:1024,pl-0-eastus2.uzgh6.mongodb.net:1025,pl-0-eastus2.uzgh6.mongodb.net:1026/?ssl=truereplicaSet=atlas-18bndf-shard-0 When a client in your VNet connects to an Atlas cluster using
one of these private endpoint-aware connection strings, the
client attempts to establish a connection to the Private Link
Service in the Atlas VNet through the private endpoint's
network interface. The Private Link service sends traffic through
an Azure Standard Load Balancer to the Atlas cluster nodes
that you deployed in that region. Your client's DNS resolution
mechanism handles resolving the hostname to the network
interface's private IP address. The driver is only aware of the
hostname in the connection string, listening on one port for each
node in the cluster's replica set. SRV Record for DNS Seedlist Private Endpoint-Aware Connection Strings The following example shows the SRV record for an
Azure Private Link-enabled single-region cluster, showing three unique
ports defined for pl-0-eastus2.uzgh6.mongodb.net : $ nslookup - type =SRV _mongodb._tcp.cluster0-pl-0.uzgh6.mongodb.net Server:  127.0.0.53 Address:  127.0.0.53#53 Non-authoritative answer: _mongodb._tcp.cluster0-pl-0.uzgh6.mongodb.net service = 0 0 1024 pl-0-eastus2.uzgh6.mongodb.net. _mongodb._tcp.cluster0-pl-0.uzgh6.mongodb.net service = 0 0 1025 pl-0-eastus2.uzgh6.mongodb.net. _mongodb._tcp.cluster0-pl-0.uzgh6.mongodb.net service = 0 0 1026 pl-0-eastus2.uzgh6.mongodb.net. In the preceding example: _mongodb._tcp.cluster0-pl-0.uzgh6.mongodb.net is the SRV record that the connection string references. pl-0-eastus2.uzgh6.mongodb.net is the hostname for each node in one Atlas cluster in one region for which
you have configured Azure Private Link. 1024 , 1025 , and 1026 are unique ports that Atlas assigns on the load balancer for each Atlas replica set node in the region for which you enabled
Azure Private Link. All nodes in an Atlas replica set are
accessible via the same hostname, with the load balancer
resolving individual nodes by their unique port. Hostname DNS Resolution in Private Endpoint-Aware Connection Strings and SRV Records The hostname in the SRV record and the standard connection string
is an DNS A record that resolves to the private IP address
of the private endpoint's network interface. The following example shows the DNS lookup for the hostname in
the SRV record and in the standard connection string: $ nslookup pl-0-eastus2.uzgh6.mongodb.net Server:  127.0.0.53 Address:  127.0.0.53#53 Non-authoritative answer: Name:  pl-0-eastus2.uzgh6.mongodb.net Address: 10.0.0.4 When you configure a private endpoint, Atlas generates a DNS
seedlist connection string: DNS seedlist connection mongodb+srv://cluster0-pl-0.uzgh6.mongodb.net When a client in your VNet connects to an Atlas cluster using the private-endpoint-aware
connection string, the client attempts to establish a connection
to the Private Link Service in the Atlas VNet through the
private endpoint's network interface. The Private Link service
sends traffic through an Azure Standard Load Balancer to the Atlas cluster that you deployed in that
region. Your client's DNS resolution mechanism handles
resolving the hostname to the network interface's private IP
address. The driver is only aware of the hostname in the
connection string. SRV Record for DNS Seedlist Private Endpoint-Aware Connection
Strings The following example shows the SRV record for an
Azure Private Link-enabled Serverless instance, showing one port defined for pl-0-eastus2.uzgh6.mongodb.net : $ nslookup - type =SRV _mongodb._tcp.serverlessinstance0-pe-1.oqg5v.mongodb.net Server:  127.0.0.1 Address:  127.0.0.1#53 Non-authoritative answer: _mongodb._tcp.serverlessinstance0-pe-1.oqg5v.mongodb.net service = 0 0 27017 serverlessinstance0-pe-1.oqg5v.mongodb.net. In the preceding example: _mongodb._tcp.serverlessinstance0-pe-1.oqg5v.mongodb.net is the SRV record that the connection string references. serverlessinstance0-pe-1.oqg5v.mongodb.net is the
hostname for the Atlas Serverless instance for which you have
configured Azure Private Link. 27017 is a unique port that Atlas assigns to the load
balancer for the Atlas Serverless instance for which you
enabled Azure Private Link. Hostname DNS Resolution in Private Endpoint-Aware Connection Strings and SRV Records The hostname in the SRV record and the standard connection string
is an DNS A record that resolves to the private IP address
of the private endpoint's network interface. When you configure a private endpoint, Atlas generates DNS
seedlist and standard private endpoint-aware connection strings: DNS seedlist connection mongodb+srv://cluster0-pl-0.uzgh6.mongodb.net Standard connection string mongodb://pl-00-000-eastus2.uzgh6.mongodb.net:27017,pl-00-001-eastus2.uzgh6.mongodb.net:27017,pl-00-002-eastus2.uzgh6.mongodb.net:27017/?ssl=truereplicaSet=atlas-18bndf-shard-0 When a client in your network connects to an Atlas cluster using one
of these private endpoint-aware connection strings, the client attempts to
establish a connection to the service attachments in the Atlas VPC through the private endpoints. The service attachments send traffic through Google Cloud internal load balancers to the Atlas cluster nodes that you deployed
in that region. Your client's DNS resolution mechanism handles resolving the
hostname to the endpoint's private IP address. Tip See also: Connect to Atlas using a Private Endpoint IP Access Lists and Network Peering Connections with Private Endpoints When you enable private endpoints, you can still enable access to
your Atlas clusters using other methods, such
as adding public IPs to IP access lists and network peering . Clients connecting to Atlas clusters using
other methods use standard connection strings. Your clients might
have to identify when to use private endpoint-aware connection
strings and standard connection strings. (Optional) Regionalized Private Endpoints for Multi-Region Sharded Clusters For multi-region and global sharded clusters,
you can deploy multiple private endpoints to a region if you need
to connect to Atlas using a private endpoint from networks
that can't be peered with one another. You can deploy any number of private endpoints to regions that you
deployed your cluster to. Each regional private
endpoint connects to the mongos instances in that region. WARNING: Your connection strings to existing
multi-region and global sharded clusters change when you enable this
setting. You must update your applications to use the new connection strings.
This might cause downtime. You can enable this setting only if your Atlas project contains no non-sharded replica sets. You can't disable this setting if you have: More than one private endpoint in more than one region, or More than one private endpoint in one region and one private
endpoint in one or more regions. You can create only sharded clusters when you enable the regionalized
private endpoint setting. You can't create replica sets. To use this feature, you must enable the regionalized private
endpoint setting. To enable or disable the regionalized private endpoint setting: Atlas CLI Atlas UI Enable Regionalized Private Endpoints To enable the regionalized private endpoint setting for your project using the
Atlas CLI, run the following command: atlas privateEndpoints regionalModes enable [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints regionalModes enable . Disable Regionalized Private Endpoints To disable the regionalized private endpoint setting for your project using the
Atlas CLI, run the following command: atlas privateEndpoints regionalModes disable [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints regionalModes disable . View Regionalized Private Endpoint Settings To return the regionalized private endpoint settings for your project using the
Atlas CLI, run the following command: atlas privateEndpoints regionalModes describe [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints regionalModes describe . Enable Regionalized Private Endpoints 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 Enable the setting. Toggle the Multiple Regionalized Private Endpoints setting
to Yes . Disable Regionalized Private Endpoints 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 Disable the setting. Toggle the Multiple Regionalized Private Endpoints setting
to No . (Optional) Improve Connection Performance for Sharded Clusters Behind a Private Endpoint Atlas can generate an optimized SRV connection string for sharded
clusters using the load balancers from your private endpoint
service. When you use an optimized connection string, Atlas limits
the number of connections per mongos between your application and
your sharded cluster. The limited connections per mongos improve performance during spikes in connection counts. Note Atlas doesn't support optimized connection strings for
clusters that run on Google Cloud or Azure . To learn more about optimized connection strings for sharded
clusters behind a private endpoint, see Improve Connection Performance for Sharded Clusters Behind a Private Endpoint . Connecting to Multi-Region Clusters Without Regionalized Private Endpoints If you use AWS PrivateLink and have applications that connect to multi-region clusters
that have endpoints in different regions but are not using regionalized private endpoints , ensure that those applications can reach endpoints
in the other regions. For example, to do this with AWS ,
you can peer the VPC s that
contains the endpoints on their side. Billing Dedicated Clusters To learn more about billing for private endpoints for
dedicated clusters, see Private Endpoints for Dedicated Clusters . Limitations Dedicated Clusters AWS PrivateLink Azure Private Link GCP Private Service Connect AWS PrivateLink must be active in all regions into which you
deploy a multi-region cluster. You will receive an
error if AWS PrivateLink is active in some, but not all,
targeted regions. If you have a multi-cloud cluster
in AWS or Azure , you must provision an endpoint in
each provider or region and set up site-to-site VPN. You can do only one of the following: Deploy nodes in more than one region, and have one
private endpoint per region. Have multiple private endpoints in one region, and no
other private endpoints. Important This limitation applies across cloud providers. For
example, if you create more than one private endpoint
in a single region in AWS , you can't create
private endpoints in Azure or any other AWS region. See (Optional) Regionalized Private Endpoints for Multi-Region Sharded Clusters for an exception for
multi-region and global sharded clusters. To connect to Atlas clusters using
AWS PrivateLink from regions in which you haven't deployed a private
endpoint connection, you must peer VPC s in those regions to VPC s in a region in which you have deployed a private
endpoint connection. To learn about inter-region VPC peering, see the AWS documentation . You can use AWS PrivateLink in Atlas projects with up to 50
addressable targets per region . If you need more than
50 addressable targets in a region: Contact MongoDB Support , or Use additional projects or regions to connect to
addressable targets beyond this limit. Addressable targets include: Each mongod instance in a replica set deployment
(sharded clusters excluded). Each sharded cluster deployment that use optimized connection strings . Each mongos instance for sharded cluster deployments
that use non- optimized connection strings . Each BI Connector for Atlas instance across all dedicated clusters in the
project. Note To request a one-time increase to use AWS PrivateLink with
up to 100 addressable targets per Atlas project,
contact MongoDB Support . You can use Azure Private Link to connect to Atlas clusters
that run MongoDB version 4.0 or later. Important Some Atlas clusters on Azure created before 10/16/2020 use Azure networking hardware that is incompatible with Azure Private Link. You
can still configure Azure Private Link for Atlas projects with these
clusters to use with supported clusters in the project, but you will
not be able to connect to the incompatible ones through Azure Private Link. All new Atlas clusters are compatible with Azure Private Link. If you must
connect to your cluster using only Azure Private Link, you can create a new
cluster in the same Atlas project and migrate your data . Azure Private Link must be active in all regions into which you
deploy a multi-region cluster. You will receive an error
if Azure Private Link is active in some, but not all, targeted
regions. If you have a multi-cloud cluster in AWS or Azure , you must provision an
endpoint in each provider or region and set up
site-to-site VPN. You can do only one of the following: Deploy nodes in more than one region, and have one
private endpoint per region. Have multiple private endpoints in one region, and no
other private endpoints. Important This limitation applies across cloud providers. For
example, if you create more than one private endpoint
in a single region in Azure , you can't create
private endpoints in AWS or any other Azure region. See (Optional) Regionalized Private Endpoints for Multi-Region Sharded Clusters for an exception for
multi-region and global sharded clusters. To connect to Atlas clusters using Azure Private Link from
regions in which you haven't deployed a private endpoint
connection, you must peer VNets in those regions to VNets
in a region in which you have deployed a private endpoint
connection. To learn about Global VNet peering, see the Azure documentation . You can use Azure Private Link in Atlas projects with up to 150
addressable targets per region . If you need more than
150 addressable targets in a region: Contact MongoDB Support , or Use additional projects or regions to connect to
addressable targets beyond this limit. Addressable targets include: Each mongod instance in a replica set deployment
(sharded clusters excluded). Each mongos instance in a sharded cluster deployment. Each BI Connector for Atlas instance across all dedicated clusters in the
project. Azure Private Link does not allow more than 64k TCP connections
per target, which might be lower than the maximum number of
connections that a cluster can sustain. You can use GCP Private Service Connect to connect to Atlas clusters
that run MongoDB version 4.0 or later. GCP Private Service Connect must be active in all regions into which you
deploy a multi-region cluster. You will receive an error
if GCP Private Service Connect is active in some, but not all, targeted
regions. You can do only one of the following: Deploy nodes in more than one region, and have one
private endpoint per region. Have multiple private endpoints in one region, and no
other private endpoints. Important This limitation applies across cloud providers. For
example, if you create more than one private endpoint
in a single region in Google Cloud , you can't create
private endpoints in AWS or any other Google Cloud region. See (Optional) Regionalized Private Endpoints for Multi-Region Sharded Clusters for an exception for
multi-region and global sharded clusters. Atlas creates 50 service attachments, each with a
subnet mask value of 27. You can change the number of
service attachments and the subnet masks that Atlas creates by setting the following limits with the Set One Project Limit Atlas Administration API endpoint: Set the atlas.project.deployment.privateServiceConnectionsPerRegionGroup limit to
change the number of service attachments. Set the atlas.project.deployment.privateServiceConnectionsSubnetMask limit to change the subnet mask for each service
attachment. To learn more, see Set One Project Limit . You can have up to 50 nodes when you create Atlas projects
that use GCP Private Service Connect in a single region . If you need
to change the number of nodes, perform one of the
following actions: Remove existing private endpoints and then
change the limit using the Set One
Project Limit Atlas Administration API
endpoint. Contact MongoDB Support . Use additional projects or regions to connect to nodes
beyond this limit. Each private endpoint in Google Cloud reserves an IP address
within your Google Cloud VPC and forwards traffic from the
endpoints' IP addresses to the service attachments .
You must create an equal number of private endpoints
to the number of service attachments. The number of
service attachments defaults to 50. Addressable targets include: Each mongod instance in a replica set deployment
(sharded clusters excluded). Each mongos instance in a sharded cluster deployment. Each BI Connector for Atlas instance across all dedicated clusters in the
project. If you configure dedicated Search Nodes for M10+ clusters in any Google Cloud region, Atlas doesn't count
these nodes in the total count of addressable targets. To request a one-time increase to use GCP Private Service Connect with up to 100 nodes per Atlas project, contact MongoDB Support . You can have up to 40 nodes when you create Atlas projects
that use GCP Private Service Connect across multiple regions . This total
excludes the following instances: Google Cloud regions communicating with each other Free clusters or Shared clusters Google Cloud Private Service Connect supports up to 1024 outgoing
connections per virtual machine. As a result, you can't
have more than 1024 connections from a single Google Cloud virtual machine to an Atlas cluster. To learn more, see the Google Cloud cloud NAT documentation . Google Cloud Private Service Connect is region-specific. However, you
can configure global access to access private endpoints from a different region. To learn more, see Multi-Region Support . Note You can't use VPC peering to access private endpoints
from a different region. When you use Private Service Connect to connect to multi-region
clusters, you can connect only to cluster nodes
that are in the same region as the private endpoint. If
the endpoint and the primary node are in different
regions, you must: Set your application's read preference to allow connections from a secondary node. For example, you can set your application's read
preference to secondaryPreferred . Ensure at least one secondary node is in the same
region as the endpoint. Before you can deploy a private endpoint to a region,
you must first resume any paused clusters
in your project with nodes deployed to that region. Prerequisites To enable connections to Atlas using private endpoints, you must: Have a valid payment method already configured for your organization. Dedicated Clusters AWS PrivateLink Azure Private Link GCP Private Service Connect Configure the private endpoint in the same region as the Atlas cluster that you want to connect to. Have either the Project Owner or Organization Owner role in Atlas . Have an AWS user account with an IAM user policy that
grants permissions to create, modify, describe, and delete
endpoints. For more information on controlling the use of
interface endpoints, see the AWS Documentation . (Recommended) : Install the AWS CLI . If you have not already done so, create your VPC and EC2
instances in AWS . See the AWS documentation for guidance. Have either the Project Owner or Organization Owner role in Atlas . Install the Azure CLI . If you have not already done so, create your VNet and
Compute instances in Azure . See the Azure documentation for guidance. Have either the Project Owner or Organization Owner role in Atlas . Have a Google Cloud user account with an IAM user policy and a Compute Network Admin role that grants permissions to create, modify, and delete
networking resources. For more information on managing
private endpoints and connections, see the GCP
documentation . Install gcloud CLI . If you have not already done so, create your VPC and
Compute instances in Google Cloud . See the GCP
documentation for guidance. Make sure egress firewall rules permit traffic to the
internal IP address of the GCP Private Service Connect endpoint. (Optional) If you enforce a security perimeter with VPC service controls (VPC-SC), you must create ingress and
egress rules to establish the connection between the
GCP Private Service Connect endpoint and Atlas clusters. See the GCP documentation for guidance. Enable global access to use Private Service Connect to connect to Atlas clusters in different regions. Back Private Endpoints Next Dedicated Clusters
