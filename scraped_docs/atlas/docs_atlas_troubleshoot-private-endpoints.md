# Troubleshoot Private Endpoint Connection Issues - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Private Endpoints Troubleshoot Private Endpoint Connection Issues On this page Dedicated Clusters This page outlines common private endpoint connection issues and possible resolutions. Dedicated Clusters AWS PrivateLink Azure Private Link GCP Private Service Connect 1 Check the status of your AWS PrivateLink connections. To view the status of each private endpoint: In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. Click the Private Endpoint tab. Review the statuses. The Atlas Endpoint Service Status and Endpoint Status fields show the status of each
private endpoint. Refer to the following statuses to help you determine the state of
your private endpoint connections: Atlas Endpoint Service Status Status Description Creating private link Atlas is creating the network load balancer and VPC resources. Failed A system failure has occurred. Available The Atlas network load balancer and VPC endpoint service
are created and ready to receive connection requests. Deleting Atlas is deleting the private endpoint service. Endpoint Status Status Description Not configured Atlas created the network load balancer and VPC endpoint
service, but AWS hasn't yet created the interface endpoint . Click Edit and complete
the wizard to create the interface endpoint. Pending acceptance AWS has received the connection request from your interface endpoint to the Atlas VPC endpoint
service. Pending AWS is establishing the connection between your interface endpoint and the Atlas VPC endpoint
service. Failed AWS failed to establish a connection between Atlas VPC resources and the interface endpoint in your VPC . Click Edit , verify that the information you
provided is correct, and then create the private endpoint
again. IMPORTANT: If your Interface Endpoint fails, you might see
the following message: No dns entries found for endpoint vpce-<guid>, your endpoint must be provisioned in at least one subnet. Click "Edit" to fix the problem. This message indicates that you didn't specify
a subnet when you created the AWS PrivateLink
connection. To resolve this error: Click Edit . Click Back . Specify at least one subnet. Follow the remaining instructions to create
the AWS PrivateLink connection. Available Atlas VPC resources are connected to the interface endpoint in your VPC . You can connect to Atlas clusters in this
region using AWS PrivateLink. Deleting Atlas is removing the interface endpoint from the private
endpoint service. 2 Make sure that your security groups are configured properly. For each resource that needs to connect to your Atlas clusters
using AWS PrivateLink, the resource's security group must allow
outbound traffic to the interface endpoint's private IP addresses on all ports. See Adding Rules to a Security Group for more information. Your interface endpoint security group must allow inbound
traffic on all ports from each resource that needs to connect to
your Atlas clusters using AWS PrivateLink. Whitelist instance IP addresses or security groups to allow traffic from them to reach the interface endpoint security group. To view the status of each private endpoint: 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab. 3 Review the statuses. The Atlas Endpoint Service Status and Endpoint Status fields show the status of each
private endpoint. Refer to the following statuses to help you determine the state of
your private endpoint connections: Atlas Endpoint Service Status Status Description Creating private link Atlas is creating the load balancer and VNet
resources. Failed A system failure has occurred. Available Atlas created the load balancer and Azure Private Link
Service.
The Azure Private Link Service is ready to receive connection
requests. Deleting Atlas is deleting the Azure Private Link Service. Endpoint Status Status Description Not configured Atlas created the load balancer and Azure Private Link
Service, but you haven't created a private endpoint
yet. Click Edit and complete the wizard
to create the private endpoint. Initiating Atlas has not yet accepted the connection to your
private endpoint. Failed Azure failed to establish a connection between Atlas VNet resources and the private endpoint in
your VNet. Click Edit , verify that the
information you provided is correct, and then create
the private endpoint again. Available Atlas VNet resources are connected to the private
endpoint in your VNet. You can connect to Atlas clusters in this region using Azure Private Link. Deleting Atlas is removing the private endpoint
connection from the Azure Private Link Service. To view the status of each private endpoint: 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab. 3 Review the statuses. The Atlas Endpoint Service Status and Endpoint Status fields show the status of each
private endpoint. Refer to the following statuses to help you determine the state of
your private endpoint connections: Atlas Endpoint Service Status Status Description Creating private link Atlas is creating the network load balancer and VPC resources. Failed A system failure has occurred. Available Atlas created the network load balancer and VPC endpoint
service.
The private endpoint service is ready to receive connection requests. Deleting Atlas is deleting the private endpoint service. Endpoint Status Status Description Initiating Atlas is not yet connected to your private endpoint and
has not yet accepted the endpoints. Waiting for User VPC resources on Atlas are ready for use. You must
set up the endpoints within your VPC by running the shell
script. Verified Atlas verified the endpoints within your VPC but has not
yet accepted the private endpoint
in your Google Cloud VPC . It might take several minutes for the Endpoint Status to become Available . Available The Atlas VPC resources are connected to the private endpoint
in your Google Cloud VPC . Atlas has accepted the endpoints.
You can connect to Atlas clusters in this region using GCP Private Service Connect. Active Atlas is ready to use VPC resources. Atlas has accepted the
endpoints. A VM is assigned to the private service
connection. Failed Google Cloud failed to establish a connection between Atlas VPC resources and the private endpoint in your Google Cloud VPC .
Click Edit , verify that the information you
provided is correct, and then create the private endpoint
again. Deleted You manually deleted the private endpoint from a region in Atlas . You must also delete the private endpoint in Google Cloud to delete resources. Pending deletion of the region group. Back Manage and Connect Next Cloud Provider Access
