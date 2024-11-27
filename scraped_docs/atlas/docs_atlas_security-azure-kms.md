# Manage Customer Keys with Azure Key Vault - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Encryption at Rest Manage Customer Keys with Azure Key Vault On this page About Customer-Managed Keys with Azure Key Vault Example What You Need to Know About Rotating Your Azure Key Identifier About Azure Key Vault Failover During an Outage Next Steps Required Access Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . You can use a customer-managed key (CMK) from Azure Key Vault (AKV)
to further encrypt your data at rest in Atlas . You can also
configure all traffic to your AKV to use Azure Private Link. Atlas uses your Azure Key Vault CMK to encrypt and decrypt
your MongoDB Master Keys. These MongoDB Master Keys are used to
encrypt cluster database files and cloud providers snapshots . To learn more about how Atlas uses CMK s
for encryption, see About Customer-Managed Keys with Azure Key Vault . When you use your own cloud provider KMS , Atlas automatically rotates
MongoDB Master Keys at least every 90 days. Your key rotation will begin
during a maintenance window ,
if you have one configured. Deferring maintenance (either manually or automatically)
may cause the key to be rotated past the 90-day mark.
Keys are rotated on a
rolling basis and the process does not require the data to be rewritten. Important Azure limits Client Secret lifetime for CMK s to two years. Atlas can't access a CMK once the Client Secret expires.
Therefore, rotate your Client Secrets before its expiration to
prevent loss of cluster availability. This page covers configuring customer key management using AKV on
your Atlas project. You can also use the Atlas Administration API to
automatically set up Azure Private Link in your AKV to ensure that all traffic
between Atlas and AKV take place over Azure s private network
interfaces. You must configure customer key management for the Atlas project
before enabling it on clusters in that project. About Customer-Managed Keys with Azure Key Vault Customer key management in Atlas follows a process called envelope encryption .
This process creates multiple layers of encryption by encrypting one key with another
key. To enable customer key management, Atlas uses the following encryption keys: Customer-Managed Key (CMK) Customer-managed keys are encryption keys that you create, own,
and manage in Azure Key Vault . You create the CMK in Azure Key Vault and
connect it to Atlas at the Project level.
To learn more about the CMK s used in Azure Key Vault , see the Azure Documentation . Atlas uses this key only to encrypt the MongoDB Master Keys. MongoDB Master Key Each node in your Atlas cluster creates a MongoDB Master Key.
MongoDB Master Keys are encryption keys that a MongoDB Server uses to
encrypt the per-database encryption keys. Atlas saves an encrypted
copy of the key locally. This key is encrypted with the CMK and encrypts the per-database
encryption keys. Per-Database Encryption Key Each node in your Atlas cluster also creates an encryption key
per database in your cluster. Atlas uses these keys to
read and write data via WiredTiger, which also encrypts and stores these
keys. This key is encrypted with the MongoDB Master Key. Example Consider the following encryption hierarchy for a three-node replica set. Atlas uses the CMK from Azure Key Vault to encrypt a unique
MongoDB Master Key for each node in the cluster. Each node also contains
three databases, each of which is encrypted with a unique
per-database encryption key. When the cluster starts up, Atlas decrypts the MongoDB Master Key by using the CMK from Azure Key Vault and supplies this to the MongoDB Server. Note If you revoke Atlas 's access to the CMK , Atlas shuts down the
nodes in your cluster and you can't access your data until
you restore access to the CMK . click to enlarge What You Need to Know After configuring Atlas to use your AKV CMK , learn more About Azure Key Vault Failover During an Outage and About Azure Key Vault Failover During an Outage . About Rotating Your Azure Key Identifier Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . MongoDB Master Key - MongoDB Responsibility When you use your own cloud provider KMS , Atlas automatically rotates
MongoDB Master Keys at least every 90 days. Your key rotation will begin
during a maintenance window ,
if you have one configured. Deferring maintenance (either manually or automatically)
may cause the key to be rotated past the 90-day mark.
Keys are rotated on a
rolling basis and the process does not require the data to be rewritten. Rotate your Azure Key ID - Your Responsibility Atlas does not automatically rotate the Key Identifier used for
Azure Key Vault. Atlas automatically creates an encryption key rotation alert to remind you to rotate your Azure Key Identifier every 90 days by
default when you enable Encryption at Rest for an Atlas project. You can rotate CMK stored in Azure Key Vault yourself or configure
your Azure Key Vault to automatically rotate your keys. If you
configure automatic rotation in Azure Key Vault, the default time period for rotation is
approximately 365 days. If you have already set up an automatic rotation in Azure Key Vault and
don't want to receive the Atlas alert to rotate your Azure Key
Identifier every 90 days, you can modify the
default alert period to be greater than 365 days. About Azure Key Vault Failover During an Outage During a regional outage, your AKV region might become unavailable. If
this happens, Azure automatically routes incoming Key Vault requests
to a pre-assigned secondary region. To learn more, see Azure Key
Vault Failover and Regional Pairings . If both regions are down, you can manually migrate your key to a
region outside of the regional pairing. To learn more, see Move a Key Vault across Regions . Note If you've enabled Encryption at Rest using Customer Key Management , you can perform
encrypt and decrypt operations while at least one node is still
available during the outage. Atlas won't shut down your
clusters. For certain regions, Azure doesn't support automatic failover. To
learn more, see Azure documentation . Next Steps You can use a customer-managed key (CMK) from Azure Key Vault (AKV) over
a public network or over Azure Private Endpoints. To learn more, see
the following: Manage Customer Keys with Azure Key Vault Over Private Endpoints Manage Customer Keys with Azure Key Vault Over a Public Network Required Access To configure customer key management, you must have Project Owner access to the project. Users with Organization Owner access must add themselves to the
project as a Project Owner . Note If you've enabled Encryption at Rest using Customer Key Management , you can
perform encrypt and decrypt operations while at least one node
is still available during the outage. Back AWS KMS Next Configure Access Over Public Network
