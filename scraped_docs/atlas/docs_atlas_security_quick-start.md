# Configure Cluster Access with the Quickstart Wizard - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features Configure Cluster Access with the Quickstart Wizard On this page Procedure The Atlas UI includes a Quickstart page to configure
access to your cluster. To configure access to your cluster, you must
do the following: Configure Database Users Configure IP Access List Entries Procedure To configure access to your cluster from the Quickstart page: 1 Go to the Quickstart page. In the Security section of the left navigation, click Quickstart . If Quickstart isn't available in
your UI left navigation, add Quickstart to your UI: In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. Toggle Atlas Security Quickstart to On . 2 Specify how you would like to authenticate the connection to your Atlas cluster. In the How would you like to authenticate your
connection? section of the Quickstart page, you can
configure one of the following options for your cluster. Username and Password Certificate Click Username and Password . Set the new user's Username and Password . Note If you use special characters in your password, you must
escape them in the connection string that you use to
connect to your cluster. To learn more,
see Special Characters in Connection String Password . You can't change a username after you create the user. You
can click the Edit button to edit the password. Click Create User . Click Certificate . MongoDB uses X.509
certificates for passwordless authentication. Specify the Common Name (CN) for the new user. Optional . Toggle the Download certificate
when user is added to On to download the
certificate after creating the user. If you choose to download the certificate, you must also
specify certificate expiration. To specify the duration,
choose the duration for the certificate from
the dropdown. You can set the certificate expiration to 3 , 6 , 12 , or 24 months. Click Add User . The new user is granted Project Data Access Read/Write role by default. Tip See also: Configure Database Users Set Up Self-Managed X.509 Authentication 3 Specify from where you would like to connect to your Atlas cluster. You can enable access for any network that needs to read and write
data to your cluster. To enable access, you can configure access from
your local environment or the cloud environment for your cluster. Local Environment Cloud Environment Choose My Local Environment to add network IP
addresses to the project IP Access List. Atlas allows
only client connections to the cluster from
entries in the project's IP access list. You can modify the
IP addresses in the access list at any time. Enter the IP address and a description to associate with the
IP address in the IP Address and Description fields respectively, or click Add My Current IP Address . You can specify either a single IP address or a CIDR-notated
range of addresses. Click Add Entry . Note Network Peering and Private Endpoint are available only for M10 or higher cluster. Choose Cloud Environment to configure network
access between Atlas and your cloud or on-premise
environment. Enter the IP address and a description to associate with the
IP address in the IP Address and Description fields respectively, or click Add My Current IP Address . You can specify either a single IP address or a CIDR-notated
range of addresses. Click Add Entry . Optional . For M10 and higher clusters, you can set up VPC peering and private endpoint by clicking the
corresponding Configure in New Tab button. To learn more about setting up: VPC Peering connection, see Set Up a Network Peering Connection . Private endpoint, see Configure Private Endpoints . Tip See also: Configure IP Access List Entries Set Up a Network Peering Connection Configure Private Endpoints 4 Click Finish and Close . Once you have completed setting up database and network access for
the first cluster in your project, Atlas disables access to Quickstart . You can enable it to revisit these
configurations from a consolidated page. A dialog box displays prompting you to specify whether you wish to see
the Quickstart page in your navigation. You can select
or deselect the Hide Quickstart guide in the navigation checkbox to hide or add Quickstart to your navigation. Alternatively, you can use the following steps to hide or add Quickstart to your navigation: In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. Toggle Atlas Security Quickstart to Off or On respectively. 5 Click Go to Database to view your database deployments.
