# Manage Customer Keys with Azure Key Vault Over a Public Network - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Encryption at Rest / Azure Key Vault Manage Customer Keys with Azure Key Vault Over a Public Network On this page Prerequisites Enable Customer-Managed Keys for a Project Enable Customer Key Management for an Atlas Cluster Disable Customer-Managed Keys for a Project Revoke Access to an Encryption Key Rotate your Azure Key Identifier Related Topics Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . You can use a customer-managed key (CMK) from Azure Key Vault (AKV)
to further encrypt your data at rest in Atlas . This page describes
how to configure customer key management using AKV on your Atlas project and on the clusters in that project. Prerequisites To enable customer-managed keys with AKV for a MongoDB project, you
must: Use an M10 or larger cluster. Use Cloud Backups to encrypt your backup snapshots. Legacy Backups are not supported. Have the Azure account and Key Vault credentials, and the key
identifier for the encryption key in your AKV . For the account, you must have the client ID, tenant ID, and secret. For the Key Vault, you must have the subscription ID, Resource Group
Name, and Key Vault name. To learn how to configure these Azure components, see the Azure Documentation . Atlas uses these resources when enabling encryption at rest
for a cluster in the Atlas project. To help users easily create or change a cluster, you
can allow public access to the key. To narrow the scope of the
key and mitigate risks, use controls such as TLS and authentication. For restricted access to defined IP ranges, allow access from Atlas IP addresses and the public IP addresses of your
cluster nodes. Ensure Atlas can communicate with your AKV . To avoid
connectivity interruptions, update your configuration whenever node
IP addresses change . For example, you
might need to update your inbound access rules . If you restrict access to the AKV , you create more complexity when
IP addresses change. For example, when you create or update a
cluster, you must grant access in the AKV to any new IP
addresses. Enable Customer-Managed Keys for a Project You must enable CMK for a project before you can enable it on a
cluster in that project. You can enable CMK for a project from the
Atlas UI and Atlas Administration API. Atlas UI Atlas Admin API 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to Encryption at Rest using your Key Management to On . 3 Select Azure Key Vault . 4 Enter your Account Credentials . Client ID Enter the Client ID (or Application ID ) of the Azure application. The Active Directory Application must have the role
of Azure key Vault Reader assigned to it. Tenant ID Enter the Tenant ID (or Directory ID )
of the Active Directory tenant. Secret Enter one of the application's non-expired Client Secrets
associated with the Active Directory tenant. Azure Environment Select the Azure cloud your Active Directory tenant lives in. 5 Enter the Key Vault Credentials . Subscription ID Enter the Subscription ID of the Key Vault. Resource Group Name Enter the Resource Group name of an Azure Resource Group containing the Key Vault. Key Vault Name Enter the name of the Key Vault. The Key Vault resource
group must match the Resource Group and the Key
Vault must have the following Access Policies: Key Management Operations GET Cryptographic Operations: ENCRYPT DECRYPT Note You can't modify the AKV credentials here after you enable and set up private endpoint connections to your AKV . 6 Enter the Encryption Key . Key Identifier Enter the full URL for the key created in the Key Vault. IMPORTANT: The key identifier must be provided in the full Azure general format : https://{keyvault-name}.vault.azure.net/{object-type}/{object-name}/{object-version} 7 (Optional) Configure private endpoint connections to your AKV . To learn more, see Enable and Set up Private Endpoint Connections for a Project 8 Verify the network settings. If you configured Atlas using the Atlas Administration API to
communicate with AKV using Azure Private Link to ensure that all traffic
between Atlas and Key Vault takes place over Azure 's
private network interfaces, Atlas sets the Require
Private Networking status to Active . If the status is Inactive , you can, optionally, complete the steps to Enable and Set up Private Endpoint Connections for a Project if you want Atlas to use
private endpoint connections for your AKV . Note The Encryption at Rest using AKV over Private Endpoints
feature is available by request. To request this functionality
for you Atlas deployments, contact your Account Manager. 9 Click Save . Atlas displays a banner in the Atlas console during the
encryption process. 1 Send a PATCH request to the encryptionAtRest endpoint . Example curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/vnd.atlas.2024-05-30+json" \ --header "Content-Type: application/vnd.atlas.2024-05-30+json" \ --request PATCH "https://cloud.mongodb.com/api/atlas/v2/groups/66c9e8f1dd6c9960802420e9/encryptionAtRest" \ --data ' { "azureKeyVault" : { "azureEnvironment" : "AZURE" , "clientID" : "f8b64e7a-4a65-413d-a9fa-7230f003a749" , "enabled" : true , "keyIdentifier" : "https://test-tf-export.vault.azure.net/keys/test/78b9134f9bc94fda8027a32b4715bf3f" , "keyVaultName" : "test-tf-export" , "resourceGroupName" : "test-tf-export" , "secret" : "" , "subscriptionID" : "fd01adff-b37e-4693-8497-83ecf183a145" , "tenantID" : "91405384-d71e-47f5-92dd-759e272cdc1c" } } ' Note You can't modify the following settings after you enable
and set up private endpoint connections to your AKV : keyVaultName resourceGroupName subscriptionID 2 Verify the configuration for Encryption at Rest using CMK for your project. To verify your request to enable and configure encryption at rest
using the keys you manage using AKV , send a GET request to
the encryptionAtRest endpoint . Example curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request GET "https://cloud.mongodb.com/api/atlas/v2/groups/{groupId}/encryptionAtRest" HIDE OUTPUT { "azureKeyVault": { "azureEnvironment": "AZURE", "clientID": "5e4ea010-a908-45a1-a70b-ebd2e4feb055", "enabled": true, "keyIdentifier": "https://EXAMPLEKeyVault.vault.azure.net/keys/EXAMPLEKey/d891821e3d364e9eb88fbd3d11807b86", "keyVaultName": "string", "requirePrivateNetworking": false, "resourceGroupName": "string", "subscriptionID": "d0dd68eb-7e97-448c-b361-f7a7213dc7e2", "tenantID": "f95ac700-4c8f-4a38-a8d1-1582733edd5b", "valid": true } } In the response, enabled is true if your project is
successfully enabled for Encryption at Rest using CMK . You can
set up private networking to ensure that all traffic between Atlas and Key Vault takes place over Azure 's private network
interfaces. To learn more, see Enable and Set up Private Endpoint Connections for a Project . Enable Customer Key Management for an Atlas Cluster After you Enable Customer-Managed Keys for a Project , you must enable customer key
management for each Atlas cluster that contains data that you want
to encrypt. Note You must have the Project Owner role to
enable customer key management for clusters in that project. For new clusters, toggle the Manage your own encryption keys setting to Yes when you
create the cluster. For existing clusters: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Modify the cluster's configuration. For the cluster that contains data that you want to encrypt, click the , then select Edit Configuration . 3 Enable cluster encryption. Expand the Additional Settings panel. Toggle the Manage your own encryption keys setting to Yes . Verify the status of the Require Private Networking setting for your cluster. If you configured Encryption at Rest Using CMK (Over Private
Networking) for Atlas at the project level, the status is Active . If you haven't configured any private
endpoint connection for your project, the status is Inactive . 4 Review and apply your changes. Click Review Changes . Review your changes, then click Apply Changes to update
your cluster. Disable Customer-Managed Keys for a Project You must disable customer key management on each cluster in a project
before you can disable the feature for the project. Warning Do not disable or delete any AKV keys that any cluster in your Atlas project uses before you have disabled customer key
management within the Atlas project. If Atlas cannot access
an AKV key, any data that key encrypted becomes inaccessible. Revoke Access to an Encryption Key You can revoke Atlas 's access to an encryption key from within AKV . Atlas automatically pauses your clusters when you revoke access to the
encryption key unless your AKV IP access list restricts the Atlas control plane. To allow automatic pausing of your cluster, you must either: Disable the IP access list for your AKV Allow access to your AKV from the Atlas control plane . Note MongoDB adds new Atlas control plane IP addresses over time. You must keep
the IP access list updated to allow automatic cluster pausing while using an
IP access list for your AKV . If the IP access list for your AKV restricts access from the Atlas control plane when
you revoke access to an encryption key, you must pause
your clusters manually to revoke Atlas 's access. Rotate your Azure Key Identifier Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Before you begin, learn About Rotating Your Azure Key Identifier . You must create a new key in the AKV associated to the Atlas project.  The following procedure documents how to rotate your Atlas project Key Identifier by specifying a new key identifier in Atlas . 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Click Edit . 3 Update the Azure credentials. Click Azure Key Vault if the Azure Key Vault selector is not already active. Click Encryption Key if the Encryption Key selector is not already active. Enter the Azure Key Identifier in the Key Identifier field. Include the full URL to the new encryption key identifier. For
example: https://mykeyvault.vault.azure.net/keys/AtlasKMSKey/a241124e3d364e9eb99fbd3e11124b23 Important The encryption key must belong to the Key Vault configured
for the project. Click the Key Vault section to view
the currently configured Key Vault for the project. Click Update Credentials . Atlas displays a banner in the Atlas UI during the
Key Identifier rotation process. Do not delete or disable the original Key Identifier until your
changes have deployed. If the cluster uses Back Up Your Cluster , do not delete
or disable the original Key Identifier until you
validate that no snapshots used that key for encryption. Related Topics To enable Encryption at Rest using your Key Management when deploying
an Atlas cluster, see Manage Your Own Encryption Keys . To enable Encryption at Rest using your Key Management for an
existing Atlas cluster, see Enable Encryption at Rest . To learn more about Encryption at Rest using your Key Management in Atlas , see Encryption at Rest using Customer Key Management . To learn more about MongoDB Encryption at Rest, see Encryption at Rest in
the MongoDB server documentation. To learn more about Encryption at Rest with Cloud Backups, see Storage Engine and Cloud Backup Encryption . Back Azure Key Vault Next Configure Access Over Private Endpoints
