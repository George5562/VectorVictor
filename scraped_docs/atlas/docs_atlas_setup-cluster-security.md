# Configure Security Features for Clusters - MongoDB Atlas


Docs Home / MongoDB Atlas Configure Security Features for Clusters On this page Preconfigured Security Features Encryption in Transit Virtual Private Cloud Encryption at Rest Required Security Features Network and Firewall Requirements IP Access List User Authentication or Authorization Optional Security Features Network Peering Connection Private Endpoints Unified AWS Access Cluster Authentication and Authorization Encryption at Rest using your Key Management Client-Side Field Level Encryption Database Auditing Access Tracking Multi-Factor Authentication for Atlas UI Access Allow Access to or from the Atlas Control Plane Allow Access to Data Federation OCSP Certificate Revocation Check You can use Atlas securely out of the box. Atlas comes
preconfigured with secure default settings. You can fine-tune
the security features for your clusters to meet your
unique security needs and preferences. Review the following security
features and considerations for clusters. Important As a security best practice, don't include sensitive information in
namespaces and field names. Atlas doesn't obfuscate this
information. Preconfigured Security Features The following security features are part of the Atlas product: Encryption in Transit Atlas requires TLS / SSL to encrypt the connections to your
databases. TLS / SSL certificates are: Valid for 90 days from the day Atlas issues the certificate. Rotated 42 days before the certificate's expiration date. To learn more about TLS encryption, see the Atlas Security White Paper . To configure SSL or TLS OCSP certificate revocation checking, see OCSP Certificate Revocation Check . Virtual Private Cloud All Atlas projects with one or more M10+ dedicated clusters
receive their own dedicated VPC (or VNet if you use Azure ). Atlas deploys all dedicated clusters inside this VPC or VNet. Encryption at Rest By default, Atlas encrypts all data stored on your Atlas clusters. Atlas also supports Encryption at Rest using your Key Management . Required Security Features You must configure the following security features: Network and Firewall Requirements Make sure your application can reach your MongoDB Atlas environment. To add the inbound network access from your application environment to Atlas , do one of the following: Add the public IP addresses to your IP access list Use VPC / VNet peering to add private IP
addresses. Add private endpoints . Tip See also: IP Access List If your firewall blocks outbound network connections, you must also
open outbound access from your application environment to Atlas .
You must configure your firewall to allow your applications to make
outbound connections to ports 27015 to 27017 to TCP traffic on Atlas hosts. This grants your applications access to databases
stored on Atlas . Note By default, MongoDB Atlas clusters do not need to be able to
initiate connections to your application environments. If you wish
to enable Atlas clusters with LDAP authentication and authorization ,
you must allow network access from Atlas clusters directly to
your secure LDAP . You can allow access to your LDAP by using
public or private IPs as long as a public DNS hostname points to
an IP that the Atlas clusters can access. If you are not using VPC / VNet peering and plan
to connect to Atlas using public IP addresses, see the following
pages for additional information: Can I specify my own VPC for my MongoDB Atlas project? Do Atlas cluster's public IPs ever change? IP Access List Atlas only allows client connections to the cluster from entries in
the project's IP access list. To connect, you must add an entry to the
IP access list. To set up the IP access list for the project, see Configure IP Access List Entries . For Atlas clusters deployed on Google Cloud Platform (GCP) or Microsoft Azure , add the IP addresses of your Google Cloud or Azure services to Atlas project IP access list to grant
those services access to the cluster. User Authentication or Authorization Atlas requires clients to authenticate to connect to the database.
You must create database users to access the database. To set up
database users to your clusters, see Configure Database Users . Atlas offers many
security features for cluster authentication and authorization . To access clusters in a project, users must belong to
that project. Users can belong to multiple projects. Tip See also: Configure Access to the Atlas UI . Optional Security Features You may configure the following security features: Network Peering Connection Atlas supports peering connections with other AWS , Azure , or Google Cloud network peering connections. To learn more, see Set Up a Network Peering Connection . Important If this is the first M10+ dedicated paid cluster for the
selected region or regions and you plan on creating one or more VPC peering connections , please review the documentation
on VPC peering connections before continuing. Private Endpoints Atlas supports private endpoints on: AWS using the AWS PrivateLink feature Azure using the Azure Private Link feature Google Cloud using the GCP Private Service Connect feature To use private endpoints, see Learn About Private Endpoints in Atlas . Unified AWS Access Some Atlas features, including Data Federation and Encryption at Rest using Customer Key Management , use AWS IAM roles for authentication. To set up an AWS IAM role for Atlas to use, see Set Up Unified AWS Access . Cluster Authentication and Authorization Atlas offers the following security features for
cluster authentication and authorization. Database User Authentication or Authorization Atlas requires clients to authenticate to access
clusters. You must create database users to access the
database. To set up database users for your clusters,
see Configure Database Users . Custom Roles for Database Authorization Atlas supports creating custom roles for database authorization in cases where the built-in Atlas roles don't grant your desired set of
privileges. Authentication with AWS IAM You can set up authentication and authorization for your AWS IAM roles. To learn more, see Set Up Authentication with AWS IAM . User Authentication or Authorization with LDAP Atlas supports performing user authentication and authorization
with LDAP . To use LDAP , see Set Up User Authentication and Authorization with LDAP . User Authentication with X.509 X.509 client certificates provide database users access to the
clusters in your project. Options for X.509
authentication include Atlas -managed X.509 authentication and
self-managed X.509 authentication. To learn more
about self-managed X.509 authentication, see Set Up Self-Managed X.509 Authentication . Restrict MongoDB Support Access to Atlas Backend Infrastructure Organization owners can restrict MongoDB Production Support Employees
from accessing Atlas backend infrastructure for any Atlas cluster in their organization. Organization owners may
grant a 24 hour bypass to the access restriction at the Atlas cluster level. Important Blocking infrastructure access from MongoDB Support
may increase support issue response and resolution
time and negatively impact your cluster's availability. To enable this option, see Configure MongoDB Support Access to Atlas Backend Infrastructure . Encryption at Rest using your Key Management Atlas supports using AWS KMS , Azure Key Vault, and Google Cloud to
encrypt storage engines and cloud provider backups. To use encryption
at rest, see Encryption at Rest using Customer Key Management . Client-Side Field Level Encryption Atlas supports client-side field level encryption , including automatic encryption of fields. All Atlas users are entitled to use MongoDB's
automatic client-side field level encryption features. To learn more, see Client-Side Field Level Encryption Requirements . Note MongoDB Compass , the Atlas UI , and the MongoDB Shell ( mongosh ) do not support decrypting client-side field
level-encrypted fields. Tip See also: Client-Side Field Level Encryption Use-Case Guide for Client-Side Field Level Encryption Database Auditing Atlas supports auditing all system event actions. To use database
auditing, see Set up Database Auditing . Access Tracking Atlas surfaces authentication logs directly in the Atlas UI so
that you can easily review successful and unsuccesful authentication
attempts made against your clusters. To view your
database access history, see View Database Access History . Multi-Factor Authentication for Atlas UI Access Atlas supports MFA to help you control access to your Atlas accounts. To set up MFA , see Manage Your Multi-Factor Authentication Options . Allow Access to or from the Atlas Control Plane If you use any of the following Atlas features, you might have to
add Atlas IP addresses to your network's IP access list: Alert Webhooks Encryption at Rest using Customer Key Management Note If you enable the Encryption at Rest feature, you must allow access from public IPs for all your hosts
in your deployment, including CSRS (Config Server Replica
Sets) if you are using sharded
clusters . Fetch Atlas Control Plane IP Addresses Send a GET request to the controlPlaneIPAddresses endpoint
to fetch the current Atlas control plane IP addresses. The API endpoint returns a list of inbound and outbound Atlas control plane IP
addresses in CIDR notation categorized by cloud provider and region,
similar to the following: { "controlPlane" : { "inbound" : { "aws" : { // cloud provider "us-east-1" : [ // region "3.92.113.229/32" , "3.208.110.31/32" , "107.22.44.69/32" ... , ] , ... } } , "outbound" : { "aws" : { // cloud provider "us-east-1" : [ // region "3.92.113.229/32" , "3.208.110.31/32" , "107.22.44.69/32" ... , ] , ... } } } , "data_federation" : { "inbound" : { } , "outbound" { } } , "app_services" : { "inbound" : { } , "outbound" { } } , ... } To add the returned IP addresses to your cloud provider's KMS IP access list,
see the prerequisites for managing customer keys with AWS , Azure , and GCP . Required Outbound Access Outbound access is traffic coming from the Atlas control plane. We
recommend that you use the Atlas Admin API to fetch the current outbound Atlas control plane IP addresses. Required Inbound Access Inbound access is traffic coming into the Atlas control plane. If
your network allows outbound HTTP requests only to specific IP
addresses, you must allow access from the inbound IP addresses so that Atlas can communicate with your webhooks and KMS . We recommend
that you use the Atlas Admin API to fetch the current inbound Atlas control plane IP addresses. Allow Access to Data Federation If your network allows outbound requests to specific IP addresses only,
you must allow access to the following IP addresses on TCP port 27017
so that your requests can reach the federated database instance: 108.129.35.102 13.54.14.65 18.138.155.47 18.140.240.47 18.196.201.253 18.200.7.156 18.204.47.197 18.231.94.191 3.122.67.212 3.6.3.105 3.8.218.156 3.9.125.156 3.9.90.17 3.98.247.136 3.99.32.43 3.130.39.53 3.132.189.43 35.206.65.216 35.209.197.46 35.210.31.154 35.210.66.17 20.23.173.153 20.23.171.79 20.96.56.124 20.190.207.191 20.197.103.232 20.197.103.246 34.217.220.13 34.237.78.67 35.158.226.227 52.192.130.90 52.193.61.21 52.64.205.136 54.203.115.97 54.69.142.129 54.91.120.155 54.94.3.214 65.1.222.250 99.81.123.21 OCSP Certificate Revocation Check If your network allows outbound requests to specific IP addresses only,
to allow SSL or TLS OCSP certificate revocation checking, you must allow access to Atlas ' CA (Certificate Authority) OCSP Responder servers that can be found in the OCSP URL of the SSL or TLS certificate. To disable OCSP certificate revocation checking, refer to the documentation
for the MongoDB driver version that your application uses. Back Troubleshoot Next Cluster Access Quickstart
