# Manage Customer Keys with AWS KMS - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Encryption at Rest Manage Customer Keys with AWS KMS On this page Required Access Enable Customer-Managed Keys with AWS KMS Example Prerequisites Enable Role-Based Access to Your Encryption Key for a Project Switch to Role-Based Access to Your Encryption Key for a Project Enable Customer Key Management for an Atlas Cluster Rotate your AWS Customer Master Key MongoDB Master Key - MongoDB Responsibility Your AWS CMK - Your Responsibility Procedure Reconfigure AWS KMS Region During an Outage Procedure Related Topics Note Starting with the 26 January 2021 Release , you must use AWS IAM roles instead of IAM users to manage access to your AWS KMS encryption keys for customer key management. When you move from AWS IAM users to roles, ensure that your new role
has access to your old AWS customer master key. Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . You can configure your Atlas project to use an AWS IAM role for accessing your AWS KMS keys for encryption at rest. You can
either use an existing role or create a new role when you enable
encryption at rest for your project. This page covers configuring customer key management on your Atlas project for role-based access. If you have not yet enabled encryption at rest for your new or existing Atlas project, follow the Enable Role-Based Access to Your Encryption Key for a Project procedure
to enable encryption at rest for your Atlas project. If you have an Atlas project for which you have already enabled encryption at rest
and configured credentials-based access to your encryption keys, follow
the Switch to Role-Based Access to Your Encryption Key for a Project procedure to switch to role-based
access to your encryption keys. You must configure customer key management for the Atlas project
before enabling it on clusters in that project. Tip See also: Set Up Unified AWS Access Required Access To configure customer key management, you must have Project Owner access to the project. Users with Organization Owner access must add themselves to the
project as a Project Owner . Enable Customer-Managed Keys with AWS KMS Customer key management in Atlas follows a process called envelope encryption .
This process creates multiple layers of encryption by encrypting one key with another
key. To enable customer key management, Atlas uses the following encryption keys: Customer-Managed Key (CMK) Customer-managed keys are encryption keys that you create, own,
and manage in AWS KMS . You create the CMK in AWS KMS and
connect it to Atlas at the Project level.
To learn more about the CMK s used in AWS KMS , see the AWS KMS Documentation . Atlas uses this key only to encrypt the MongoDB Master Keys. MongoDB Master Key Each node in your Atlas cluster creates a MongoDB Master Key.
MongoDB Master Keys are encryption keys that a MongoDB Server uses to
encrypt the per-database encryption keys. Atlas saves an encrypted
copy of the key locally. This key is encrypted with the CMK and encrypts the per-database
encryption keys. Per-Database Encryption Key Each node in your Atlas cluster also creates an encryption key
per database in your cluster. Atlas uses these keys to
read and write data via WiredTiger, which also encrypts and stores these
keys. This key is encrypted with the MongoDB Master Key. Example Consider the following encryption hierarchy for a three-node replica set. Atlas uses the CMK from AWS KMS to encrypt a unique
MongoDB Master Key for each node in the cluster. Each node also contains
three databases, each of which is encrypted with a unique
per-database encryption key. When the cluster starts up, Atlas decrypts the MongoDB Master Key by using the CMK from AWS KMS and supplies this to the MongoDB Server. Note If you revoke Atlas 's access to the CMK , Atlas shuts down the
nodes in your cluster and you can't access your data until
you restore access to the CMK . click to enlarge Prerequisites To enable customer-managed keys with AWS KMS for a MongoDB
project, you must: Use an M10 or larger cluster. Use Cloud Backups to encrypt your backup snapshots. Legacy Backups are not supported. Have a symmetric AWS KMS key .
To learn how to create a key, see Creating Keys in the AWS documentation. Note To ensure resilience in the event of a regional outage,
configure your KMS key to be a multi-Region key . To learn more, see Reconfigure AWS KMS Region During an Outage . Have an AWS IAM role with sufficient privileges. Atlas must
have permission to perform the following actions with your key: DescribeKey Encrypt Decrypt Note If you wish to use the AWS KMS key with an AWS IAM role from a
different AWS account instead of that of the IAM role which
created the AWS KMS key , ensure you have sufficient privileges: Add a key policy statement under the AWS KMS key  to include the
external AWS account. Add an IAM inline policy for the IAM role in the external AWS
account. For a comprehensive discussion of IAM roles and customer master
keys, see the AWS documentation . After confirming the above privileges, you can follow the usual
steps to configure the KMS settings in Atlas , with the
following exception: You must provide the full ARN for
the AWS KMS key  (e.g. arn:aws:kms:eu-west-2:111122223333:key/12345678-1234-1234-1234-12345678 )
instead of the master key ID (e.g. 12345678-1234-1234-1234-12345678 )
in the AWS KMS key ID field. To learn how to create an IAM role, see IAM Roles in the AWS documentation. Atlas uses the same IAM role and AWS KMS key settings for
all clusters in a project for which Encryption at Rest is enabled. If your AWS KMS configuration requires it, allow
access from Atlas IP addresses and the public IP addresses or DNS hostnames of your cluster nodes so that Atlas can communicate with your KMS . You must include the IP addresses in your managed IAM role policy by
configuring IP address condition operators in your policy document.
If the node IP addresses change , you must update your
configuration to avoid connectivity interruptions. Enable Role-Based Access to Your Encryption Key for a Project UI API 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to Encryption at Rest using your Key Management to On . 3 Click the Authorize a new IAM role link to authorize an AWS IAM role to Atlas to access your AWS KMS keys for encryption at rest. To create a new AWS IAM role for accessing your AWS KMS keys for
encryption at rest, follow the Create New Role with the
AWS CLI procedure. If you have an existing AWS IAM role that you want to authorize, follow the Add
Trust Relationships to an Existing Role procedure. 4 Add an access policy to your AWS IAM role via the AWS console or CLI. See Managing IAM policies for more information. Note This policy statement allows MongoDB's AWS Principal to use the
customer's KMS key for encryption and decryption operations. The Atlas Principal is not secret and is used across all Atlas customers. This is a highly-restricted, purpose-limited AWS account, with no resources in it other than the IAM user. The ExternalId in the policy statement is unique for each Atlas project, but it is not secret. The ExternalId is used to
mitigate the possibility of cross-context (confused deputy)
vulnerabilities. Atlas 's use of a common principal to access all
customers' keys is an access pattern recommended by Amazon, as
described here . The access policy for encryption at rest looks similar to the following: { "Version" : "2012-10-17" , "Statement" : [ { "Effect" : "Allow" , "Action" : [ "kms:Decrypt" , "kms:Encrypt" , "kms:DescribeKey" ] , "Resource" : [ "arn:aws:kms:us-east-1:123456789012:key/12x345y6-7z89-0a12-3456-xyz123456789" ] } ] } 5 Repeat steps 1 and 2 to assign the role you authorized in step 3 to your project for accessing your encryption key. 6 Specify the following for accessing your encryption key and click Save . Select the role to assign from the AWS IAM role dropdown
list. Specify your encryption key in the Customer Master Key ID field. Select the AWS region for your encryption key. 1 Send a POST request to the cloudProviderAccess endpoint. Use the API endpoint to
create a new AWS IAM role. Atlas will use this role for
authentication with your AWS account. Keep the returned field values atlasAWSAccountArn and atlasAssumedRoleExternalId handy for use in the next step. 2 Modify your AWS IAM role trust policy. Log in to your AWS Management Console. Navigate to the Identity and Access Management (IAM) service. Select Roles from the left-side navigation. Click on the existing IAM role you wish to use for Atlas access
from the list of roles. Select the Trust Relationships tab. Click the Edit trust relationship button. Edit the Policy Document . Add a new Statement object
with the following content. Note This policy statement allows MongoDB's AWS Principal to use the
customer's KMS key for encryption and decryption operations. The Atlas Principal is not secret and is used across all Atlas customers. This is a highly-restricted, purpose-limited AWS account, with no resources in it other than the IAM user. The ExternalId in the policy statement is unique for each Atlas project, but it is not secret. The ExternalId is used to
mitigate the possibility of cross-context (confused deputy)
vulnerabilities. Atlas 's use of a common principal to access all
customers' keys is an access pattern recommended by Amazon, as
described here . Note Replace the highlighted lines with values returned from the API
call in step 1. { "Version" : "2020-03-17" , "Statement" : [ { "Effect" : "Allow" , "Principal" : { "AWS" : "<atlasAWSAccountArn>" } , "Action:" "sts:AssumeRole" , "Condition" : { "StringEquals" : { "sts:ExternalId" : "<atlasAssumedRoleExternalId>" } } } ] } Click the Update Trust Policy button. 3 Authorize the newly created IAM role. Use the API endpoint to authorize and configure the new IAM Assumed Role ARN .
If the API call is successful, you can use the roleId value when
configuring Atlas services that use AWS . 4 Enable AWS KMS with Role Authorization on the Project Send a PATCH request to the encryptionAtRest API endpoint
to update the awsKms.roleId field with your authorized AWS IAM
role ID. Example curl --user "{public key}:{private key}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request PATCH \ "https://cloud.mongodb.com/api/atlas/v1.0/groups/{groupId}/encryptionAtRest?pretty=true&envelope=true" \ --data ' { "awsKms": { "enabled": true, "roleId": "<roleId>", "customerMasterKeyID": "<master-key-id>", "region": "<aws-region>" } }' Switch to Role-Based Access to Your Encryption Key for a Project Important If you switch your encryption keys to role-based access, you can't
undo the role-based access configuration and revert to
credentials-based access for encryption keys on that project. UI API 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 For the Encryption at Rest using your Key Management section, click Edit . 3 Read the information in the Grant Access to Keys with an AWS IAM Role section and click Configure . 4 Authorize and assign an AWS IAM role to Atlas to access your AWS KMS keys for encryption at rest. To create a new AWS IAM role for accessing your AWS KMS keys for
encryption at rest, follow the Create New Role with the
AWS CLI procedure. If you have an existing AWS IAM role that you want to authorize, follow the Add
Trust Relationships to an Existing Role procedure. To update your encryption key management with the
Atlas Administration API, use the same steps outlined in the above procedure . Enable Customer Key Management for an Atlas Cluster After you Enable Role-Based Access to Your Encryption Key for a Project , you must enable customer key
management for each Atlas cluster that contains data that you want
to encrypt. Note You must have the Project Owner role to
enable customer key management for clusters in that project. For new clusters, toggle the Manage your own encryption keys setting to Yes when you create the cluster. For existing clusters: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Modify the cluster's configuration. For the cluster that contains data that you want to encrypt, click the , then select Edit Configuration . 3 Enable cluster encryption. Expand the Additional Settings panel. Toggle the Manage your own encryption keys setting to Yes . Verify the status of the Require Private Networking setting for your cluster. If you configured Encryption at Rest Using CMK (Over Private
Networking) for Atlas at the project level, the status is Active . If you haven't configured any private
endpoint connection for your project, the status is Inactive . 4 Review and apply your changes. Click Review Changes . Review your changes, then click Apply Changes to update
your cluster. Rotate your AWS Customer Master Key Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . MongoDB Master Key - MongoDB Responsibility When you use your own cloud provider KMS , Atlas automatically rotates
MongoDB Master Keys at least every 90 days. Your key rotation will begin
during a maintenance window ,
if you have one configured. Deferring maintenance (either manually or automatically)
may cause the key to be rotated past the 90-day mark.
Keys are rotated on a
rolling basis and the process does not require the data to be rewritten. Your AWS CMK - Your Responsibility Atlas does not automatically rotate the AWS CMK used for AWS -provided Encryption at Rest. As a best practice, Atlas creates an alert to remind you
to rotate your AWS CMK every 90 days by default when you enable Encryption at Rest for an Atlas project. You can configure the time period of this alert. You can rotate your AWS CMK yourself or configure your AWS KMS instance to automatically rotate your CMK . If
you configure automatic AWS CMK rotation, the default time period
for rotation is approximately 365 days. If you have already set up an automatic CMK rotation in AWS and
don't want to receive the Atlas alert to rotate your CMK every 90
days, you can modify the default alert period
to be greater than 365 days or disable the alert. This page explains how to create a new key and update the CMK ID in Atlas to rotate your Atlas project CMK . This method of key
rotation supports more granular control of the rotation period compared
to AWS KMS automatic CMK rotation. Important Cloud Backups with Encryption at Rest For clusters using Encryption at Rest and Back Up Your Cluster , Atlas uses the project's CMK and AWS IAM user credentials at the time of the snapshot to
automatically encrypt the snapshot data files. This is an additional
layer of encryption on the existing encryption applied to all Atlas storage and snapshot volumes. Atlas does not re-encrypt snapshots with the new CMK after
rotation. Do not delete the old CMK until you check every backup-enabled cluster in the project for any snapshots still using
that CMK . Atlas deletes backups in accordance to the Backup Scheduling, Retention, and On-Demand Snapshots . After Atlas deletes all
snapshots depending on a given CMK , you can delete that CMK safely. Procedure 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 For the Encryption at Rest using your Key Management section, click Edit . 3 Update the AWS CMK details. Enter the following information: Field Action AWS IAM role Select an existing AWS IAM role that already has access
to your KMS keys, or authorize a new role and grant this
role access to your KMS keys with the following
permissions: DescribeKey Encrypt Decrypt To learn more, see Role-Based Access to Your Encryption Key for a Project . Customer Master Key ID Enter your AWS customer master key ID. Customer Master Key Region Select the AWS region in which you created your AWS CMK . Atlas lists only AWS regions that support AWS KMS . Click Save . Atlas displays a banner in the Atlas console during the CMK rotation process. Do not delete or disable the CMK until
your changes have deployed. Reconfigure AWS KMS Region During an Outage During a regional outage, your AWS KMS region might
become unavailable. If you've enabled Encryption at Rest using Customer Key Management ,
you can perform encrypt and decrypt operations while at least one node
is still available. However, if all nodes become unavailable,
you can't perform cryptographic operations. A node becomes unavailable
if it restarts during the outage. To get the unavailable nodes to a healthy state, you
can reconfigure your current AWS KMS region to an available region.
To change your KMS region, your AWS KMS key must be a multi-Region key .
To create a multi-Region Key, see the AWS documentation . Note You can't convert a single-Region key to a multi-Region Key. Procedure To reconfigure your AWS KMS region, complete the following steps
in Atlas : 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 For the Encryption at Rest using your Key Management section, click Edit . 3 Verify your AWS CMK credentials. To ensure that Atlas doesn't re-encrypt your data, verify that the AWS IAM role and Customer Master Key ID reflect
your existing credentials. 4 Update the Customer Master Key Region . Select another AWS region for which you have configured
your multi-Region key. 5 Click Save . Related Topics To learn more about MongoDB Encryption at Rest, see Encryption at Rest in
the MongoDB server documentation. To learn more about Encryption at Rest with Cloud Backups, see Storage Engine and Cloud Backup Encryption . Back Encryption at Rest Next Azure Key Vault
