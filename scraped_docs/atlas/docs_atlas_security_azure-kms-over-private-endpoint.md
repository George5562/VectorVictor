# Manage Customer Keys with Azure Key Vault Over Private Endpoints - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Encryption at Rest / Azure Key Vault Manage Customer Keys with Azure Key Vault Over Private Endpoints On this page Considerations Use Case Benefits Limitations Prerequisites Procedures Enable Customer-Managed Keys for a Project Enable and Set up Private Endpoint Connections for a Project Enable Customer Key Management for an Atlas Cluster Disable Customer-Managed Keys for a Project Disable Private Endpoint Connections for a Project Reject or Remove Private Endpoint Connection Revoke Access to an Encryption Key Rotate your Azure Key Identifier Related Topics The Encryption at Rest using Azure Key Vault over Private Endpoints feature is available by request. To request this functionality for your Atlas deployments, contact your Account Manager. Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . You can use a customer-managed key (CMK) from Azure Key Vault (AKV)
to further encrypt your data at rest in Atlas . You can also
configure all traffic to your AKV to use Azure Private Link. This page describes how to use the Atlas Administration API to automatically
set up Azure Private Link in your AKV to ensure that all traffic between Atlas and AKV take place over Azure 's private network
interfaces. Considerations Before you enable Encryption at Rest using AKV over private endpoints,
review the following use cases, benefits, limitations, and prerequisites. Use Case Suppose your Atlas deployment is on a single cloud service provider.
You now have a requirement that all access to your AKV occur over your
cloud provider's private networking infrastructure. This page walks you
through the steps to enable private endpoint connections for your Atlas project. Benefits You can use the Atlas Administration API to allow Atlas to configure
Encryption At Rest with AKV using Private Endpoints. This allows all
traffic to AKV to pass through a set of private endpoints and avoid
exposing AKV to the public internet or public IP addresses. It
eliminates the need to maintain allowed IP addresses while enhancing
data security by keeping all AKV traffic within Azure 's private
network. Limitations Atlas doesn't support Encryption at Rest using CMK over
Private Endpoints for multi-cloud deployments. If you enable encryption
at rest using CMK over Azure Private Link in an existing project with
multi-cloud clusters, Atlas disables the multi-cloud
clusters in your project. Atlas doesn't support Encryption at Rest using CMK over
Private Endpoints for projects in INACTIVE state. Atlas doesn't support AKV access over private networking for AWS or Google Cloud clusters. Prerequisites To enable customer-managed keys with AKV for a MongoDB project, you
must: Use an M10 or larger cluster. Use Cloud Backups to encrypt your backup snapshots. Legacy Backups are not supported. Have the Azure account and Key Vault credentials, and the key
identifier for the encryption key in your AKV . For the account, you must have the client ID, tenant ID, and secret. For the Key Vault, you must have the subscription ID, Resource Group
Name, and Key Vault name. To learn how to configure these Azure components, see the Azure Documentation . Atlas uses these resources when enabling encryption at rest
for a cluster in the Atlas project. Note You must register Microsoft.Network under your Azure subscription resource providers. To learn more, see Azure
documentation . Procedures Enable Customer-Managed Keys for a Project You must enable CMK for a project before you can enable it on a
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
interfaces. To learn more, see Enable and Set up Private Endpoint Connections for a Project . Enable and Set up Private Endpoint Connections for a Project You can enable and set up private endpoint only by using the
Atlas Administration API. To enable private networking and set up a private
endpoint in your AKV , you must do the following: 1 Enable private networking. Send a PATCH request to the endpoint and set the requirePrivateNetworking flag value to true . Example curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request PATCH "https://cloud.mongodb.com/api/atlas/v2/groups/{groupId}/encryptionAtRest/" \ --data ' { "azureKeyVault" : { "azureEnvironment" : "AZURE" , "clientID" : "5e4ea010-a908-45a1-a70b-ebd2e4feb055" , "enabled" : true , "keyIdentifier" : "https://EXAMPLEKeyVault.vault.azure.net/keys/EXAMPLEKey/d891821e3d364e9eb88fbd3d11807b86" , "keyVaultName" : "string" , "requirePrivateNetworking" : true , "resourceGroupName" : "string" , "secret" : "string" , "subscriptionID" : "d0dd68eb-7e97-448c-b361-f7a7213dc7e2" , "tenantID" : "f95ac700-4c8f-4a38-a8d1-1582733edd5b" } } ' 2 Create a private endpoint. Use the Atlas Administration API to create a private endpoint to
communicate with your AKV . Send a POST request to the endpoint with the Azure region in which you want Atlas to create the private
endpoint. You must send a separate request for each region
in which you want Atlas to create a private endpoint. Example curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request POST "https://cloud.mongodb.com/api/atlas/v2/groups/{groupId}/encryptionAtRest/AZURE/privateEndpoints" \ --data ' { "regionName" : "US_CENTRAL" } ' After you approve the private endpoint, the following restrictions
apply: Atlas creates all new clusters only in the regions with
approved private endpoints. Atlas deploys additional nodes for existing clusters only
in the regions with approved private endpoints. 3 Approve the private endpoint connections to your AKV . You can use the Azure UI , CLI , or
Terraform to approve the private endpoint connections. After you approve, Atlas automatically migrates all
clusters for which you enabled customer managed keys , including
existing clusters that allow connections using public
internet, to use only the private endpoint connection. You can
optionally disable public internet access to your AKV after
migrating your clusters to use the private endpoint
connection. All new Atlas clusters on Azure will by
default use only the active private endpoint connection. 4 Check the status of your request. To check the status of the private endpoint, send a GET request to the encryptionAtRest endpoint . Example curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request GET "https://cloud.mongodb.com/api/atlas/v2/groups/{groupId}/encryptionAtRest/AZURE/privateEndpoints" HIDE OUTPUT { "links": [ { "href": "https://cloud.mongodb.com/api/atlas", "rel": "self" } ], "results": [ { "cloudProvider": "AZURE", "errorMessage": "string", "id": "24-hexadecimal-digit-string", "regionName": "string", "status": "INITIATING", "privateEndpointConnectionName": "string" } ], "totalCount": 0 } After you approve the private endpoint, it can take Atlas up
to three minutes to reflect the current status of your private
endpoint. The private endpoint can have one of the following
statuses: INITATING Indicates that Atlas is in the process of creating the
private endpoint. PENDING_ACCEPTANCE Indicates that the private endpoint hasn't yet been approved. You
must accept the private endpoint to allow Atlas to use it. ACTIVE Indicates that the private endpoint is approved and Atlas can
or is using it. PENDING_RECREATION Indicates that the private endpoint was either rejected or removed
and Atlas is in the process of creating a new private
endpoint in the same region. FAILED Indicates that the private endpoint creation failed. DELETING Indicates that Atlas is in the process of deleting the
private endpoint. After you enable Encryption at Rest Using CMK (Over Private
Networking) for your project, you can enable Encryption at Rest using CMK for
each Atlas cluster in your project. Enable Customer Key Management for an Atlas Cluster After you Enable Customer-Managed Keys for a Project , you must enable customer key
management for each Atlas cluster that contains data that you want
to encrypt. If you configured private endpoint connections for your Atlas project, Atlas automatically migrates all clusters for
which you already enabled customer managed keys , including
existing clusters that allow connections using public internet, to
use only the private endpoint connection. Note You must have the Project Owner role to
enable customer key management for clusters in that project. For new clusters, toggle the Manage your own encryption keys setting to Yes , if it
isn't already enabled, when you create the cluster. For existing clusters: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Modify the cluster's configuration. For the cluster that contains data that you want to encrypt, click the , then select Edit Configuration . 3 Enable cluster encryption. Expand the Additional Settings panel. Toggle the Manage your own encryption keys setting to Yes . Verify the status of the Require Private Networking setting for your cluster. If you configured Encryption at Rest Using CMK (Over Private
Networking) for Atlas at the project level, the status is Active . If you haven't configured any private
endpoint connection for your project, the status is Inactive . 4 Review and apply your changes. Click Review Changes . Review your changes, then click Apply Changes to update
your cluster. Disable Customer-Managed Keys for a Project To disable CMK for a project, you must first remove all private endpoints, regardless of
their state, associated with the project. Atlas displays an error if
you attempt to disable CMK for a project that is associated with
active private endpoints. After removing all private endpoints for a project, you must disable
customer key management on each cluster in the project before you
disable the feature for the project. Warning Do not disable or delete any AKV keys that any cluster in your Atlas project uses before you have disabled customer key
management within the Atlas project. If Atlas can't access
an AKV key, any data that the key encrypted becomes inaccessible. Disable Private Endpoint Connections for a Project To disable private endpoint connections for a project, you must first remove all private endpoints,
regardless of their state, associated with the project. Atlas doesn't disable private endpoint connections for a project if the
project is associated with active private endpoints. After removing all private endpoints for a project, you can disable
private endpoint connections for the project by using the
Atlas Administration API. To disable a private endpoint connection, send a PATCH request to the endpoint with the requirePrivateNetworking boolean
flag value set to false . Example { "azureKeyVault": { "azureEnvironment": "AZURE", "clientID": "5e4ea010-a908-45a1-a70b-ebd2e4feb055", "enabled": true, "keyIdentifier": "https://EXAMPLEKeyVault.vault.azure.net/keys/EXAMPLEKey/d891821e3d364e9eb88fbd3d11807b86", "keyVaultName": "string", "requirePrivateNetworking": false, "resourceGroupName": "string", "secret": "string", "subscriptionID": "d0dd68eb-7e97-448c-b361-f7a7213dc7e2", "tenantID": "f95ac700-4c8f-4a38-a8d1-1582733edd5b" } } Reject or Remove Private Endpoint Connection To successfully remove a private endpoint, send a DELETE request to
the Atlas Administration API endpoint and specify the ID of
the project and of the private endpoint that you want to delete. Example curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request DELETE "https://cloud.mongodb.com/api/atlas/v2/groups/{groupId}/encryptionAtRest/AZURE/privateEndpoints/{endpointId}" \ --data ' { "cloudProvider" : "AZURE" , "regions" : [ "string" ] } ' When you delete a private endpoint by using the Atlas Administration API, the
private endpoint transitions to the DELETING status while Atlas deletes the private endpoint. If you remove or reject an active private endpoint from the Azure UI, Atlas automatically attempts to recreate a new private endpoint in
the same region. You can check the status of the private endpoint by
sending a GET request to the Atlas Administration API encryptionAtRest get all endpoint or get one endpoint, for which you must specify the ID of the private endpoint
in the path. Example Return All Private Endpoints for One Project curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \ --header "Accept: application/json" \ --header "Content-Type: application/json" \ --include \ --request GET "https://cloud.mongodb.com/api/atlas/v2/groups/{groupId}/encryptionAtRest/AZURE/privateEndpoints/" While Atlas attempts to create a new private endpoint, the status of
the private endpoint that you rejected or removed transitions to PENDING_RECREATION and the new endpoint that Atlas attempts to
create is in INITIATING state. You must approve the new private
endpoint after it is created. Revoke Access to an Encryption Key You can revoke Atlas 's access to an encryption key from within AKV to freeze your data. Atlas automatically pauses your
clusters when you revoke access to the encryption key. Rotate your Azure Key Identifier Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Before you begin, learn About Rotating Your Azure Key Identifier . You must create a new key in the AKV associated with your Atlas project. The following procedure documents how to rotate your Atlas project Key Identifier by specifying a new key identifier in Atlas . 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
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
the MongoDB server documentation. To learn more about Encryption at Rest with Cloud Backups, see Storage Engine and Cloud Backup Encryption . Back Configure Access Over Public Network Next Google Cloud KMS
