# Set Up a Private Endpoint for a Federated Database Instance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Administration / Manage Private Endpoints Set Up a Private Endpoint for a Federated Database Instance On this page Required Access Prerequisites Procedure MongoDB supports AWS private endpoints using the AWS PrivateLink feature for your federated database instance. You
can set up the private endpoints from the Atlas CLI, Atlas User Interface,
and API . Required Access To set up a private endpoint, you must have Project Owner access to the project.
Users with Organization Owner access must add themselves as a Project Owner to the project before setting up a private endpoint. Prerequisites Have an AWS user account with an IAM user policy that grants
permissions to create, modify, describe, and delete endpoints. To
learn more about controlling the use of interface endpoints, see
the AWS Documentation . Install the AWS CLI . If you have not already done so, create your VPC and EC2 instances
in AWS . To learn more, see the AWS documentation for guidance. Note You can't use your Atlas cluster private endpoint ID for Atlas Data Federation. The Atlas Data Federation endpoint ID must be
different from your Atlas cluster endpoint ID, if you have one. Procedure Atlas CLI Atlas Administration API Atlas UI To create a new Data Federation private endpoint using the
Atlas CLI, run the following command: atlas dataFederation privateEndpoints create <endpointId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dataFederation privateEndpoints create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To configure a private endpoint from the API, send a POST request
with the private endpoint ID to the privateNetworkSettings endpoint. If the endpoint ID already exists and there is no change to
the comment associated with the endpoint, Atlas makes no change
to the endpoint ID list. If the endpoint ID already exists and there is a change to the
associated comment, Atlas updates the comment value only in
the endpoint ID list. If the endpoint ID doesn't exist, Atlas appends the new endpoint
to the list of endpoints in the endpoint ID list. To learn more about the syntax and options, see API . You can create a new private endpoint or add an existing private
endpoint through your Atlas User Interface. To set up the private
endpoint: Create New Endpoint Add Existing Endpoint 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab and then the following tab for the resource. Data Federation / Online Archive to manage the
private endpoint for your federated database instance or online archive. 3 Click the following button to set up the private endpoint. Click Create new endpoint button. 4 Choose an AWS region. From the AWS Region list, select the region where you
want to create the private endpoint. You can select one of the following regions: Data Federation Regions AWS Regions Virginia, USA us-east-1 Oregon, USA us-west-2 Sao Paulo, Brazil sa-east-1 Ireland eu-west-1 London, England eu-west-2 Frankfurt, Germany eu-central-1 Tokyo, Japan ap-northeast-1 Mumbai, India ap-south-1 Singapore ap-southeast-1 Sydney, Australia ap-southeast-2 Montreal, Canada ca-central-1 The following table shows the service names for the various
endpoints in each region: Region Service Name us-east-1 com.amazonaws.vpce.us-east-1.vpce-svc-00e311695874992b4 us-west-2 com.amazonaws.vpce.us-west-2.vpce-svc-09d86b19e59d1b4bb eu-west-1 com.amazonaws.vpce.eu-west-1.vpce-svc-0824460b72e1a420e eu-west-2 com.amazonaws.vpce.eu-west-2.vpce-svc-052f1840aa0c4f1f9 eu-central-1 com.amazonaws.vpce.eu-central-1.vpce-svc-0ac8ce91871138c0d sa-east-1 com.amazonaws.vpce.sa-east-1.vpce-svc-0b56e75e8cdf50044 ap-southeast-2 com.amazonaws.vpce.ap-southeast-2.vpce-svc-036f1de74d761706e ap-south-1 com.amazonaws.vpce.ap-south-1.vpce-svc-03eb8a541f96d356d ca-central-1 com.amazonaws.vpce.ca-central-1.vpce-svc-08564bb8ccae8ba64 ap-northeast-1 com.amazonaws.vpce.ap-northeast-1.vpce-svc-0b63834ecd618a332 ap-southeast-1 com.amazonaws.vpce.ap-southeast-1.vpce-svc-07728d2dfd2860efb To learn more, see Atlas Data Federation Regions . Click Next . 5 Configure your private endpoint. Enter the following details about your AWS VPC : Tip You can click Show instruction for the following
settings to display a screenshot of the AWS console where you
can find the value for the setting. Your VPC ID Unique 22-character alphanumeric string that identifies
the peer AWS VPC . Find this value on the VPC dashboard in your AWS account. Your Subnet IDs Unique strings that identify the subnets that your AWS VPC uses. Find these values on the Subnet dashboard in your AWS account. IMPORTANT: You must specify at least one subnet. If you don't, AWS won't provision an interface endpoint in
your VPC . An interface endpoint is required for
clients in your VPC to send traffic to the private
endpoint. Copy the command the dialog box displays and run it using the AWS CLI. Note You can't copy the command until Atlas finishes creating VPC resources in the background. See Creating an Interface Endpoint to perform this task using the AWS CLI. Enter the 22-character alphanumeric string that identifies your
private endpoint in the VPC Endpoint ID field. Find
this value on the AWS VPC Dashboard under Endpoints > VPC ID . Enter the alpha-numeric DNS hostname associated with your private
endpoint on AWS in the Your VPC Endpoint DNS Name field. If you have multiple DNS names for your private endpoint, copy and
paste the first name from your list. To learn more, see Manage DNS names for VPC endpoint services . 6 Run the command to create your VPC interface endpoint. Copy the command the dialog box displays and run it using the AWS CLI. 7 Modify the private DNS name to ensure that the hostname resolves to an address on your network. To ensure that the hostname resolves to an address on your network: Copy the command the dialog box displays and run it using the AWS CLI. Optional . Add a comment to associate with this endpoint. 8 Click Finish endpoint creation . 9 Configure your resources' security groups to send traffic to and receive traffic from the interface endpoint . For each resource that needs to connect to your federated database instance using
AWS PrivateLink, the resource's security group must allow outbound
traffic to the interface endpoint's private IP addresses on all ports. See Adding Rules to a Security Group for more information. 10 Create a security group for your interface endpoint to allow resources to access it. This security group must allow inbound traffic on all ports from each
resource that needs to connect to your federated database instance using AWS PrivateLink: In the AWS console, navigate to the VPC Dashboard . Click Security Groups , then click Create security group . Use the wizard to create a security group. Make sure you select
your VPC from the VPC list. Select the security group you just created, then click the Inbound Rules tab. Click Edit Rules . Add rules to allow all inbound traffic from each resource in your
VPC that you want to connect to your federated database instance. Click Save Rules . Click Endpoints , then click the endpoint for your
VPC. Click the Security Groups tab, then click Edit Security Groups . Add the security group you just created, then click Save . To learn more about VPC security groups , see the AWS documentation. 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab and then the following tab for the resource. Data Federation / Online Archive to manage the
private endpoint for your federated database instance or online archive. 3 Click the following button to set up the private endpoint. Click Add existing endpoint button. 4 Enter your VPC endpoint ID and DNS name. Enter the 22-character alphanumeric string that identifies your
private endpoint in the Your VPC Endpoint ID field. Enter the alpha-numeric DNS hostname associated with your private
endpoint on AWS in the Your VPC Endpoint DNS Name field. If you have multiple DNS names for your private endpoint, copy and
paste the first name from your list. To learn more, see Manage DNS names for VPC endpoint services . Tip Click and expand Show more instructions in the dialog box
for a visual clue as to where you can find the necessary
information in the AWS console. 5 Add a comment to associate with this endpoint.
You can enter your subnet ID, VPC ID, AWS region, and other
information to associate with this endpoint here. 6 Click Confirm to add the existing private endpoint. To verify whether the private endpoint setup is successful: 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab. 3 Click the Federated Database Instance / Online Archive sub-tab. 4 Review the details. Review the VPC Endpoint ID , Region , and VPC Endpoint DNS Name . Back IP Access Lists Next Database Users
