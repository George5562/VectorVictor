# Client-Side Field Level Encryption - MongoDB Shell


Docs Home / MongoDB Shell Client-Side Field Level Encryption On this page Create a Data Encryption Key When working with a MongoDB Enterprise or MongoDB Atlas cluster, you can use mongosh to configure Client-Side Field Level Encryption and connect with encryption
support. Client-side field level encryption uses data encryption keys
for supporting encryption and decryption of field values, and stores
this encryption key material in a Key Management Service (KMS). mongosh supports the following KMS providers for use with
client-side field level encryption: Amazon Web Services KMS Azure Key Vault Google Cloud Platform KMS Locally Managed Keyfile Create a Data Encryption Key The following procedure uses mongosh to create a data encryption key
for use with client-side field level encryption and decryption. Use the tabs below to select the KMS appropriate for your deployment: Amazon Web Services KMS Azure Key Vault Google Cloud KMS Local Keyfile 1 Launch the mongosh Shell. Create a mongosh session without connecting to a running database
by using the --nodb option: mongosh - - nodb 2 Create the Encryption Configuration. Configuring client-side field level encryption for the AWS KMS
requires an AWS Access Key ID and its associated Secret Access Key.
The AWS Access Key must correspond to an IAM user with all List and Read permissions for the KMS service. In mongosh , create a new AutoEncryptionOpts variable for storing the
client-side field level encryption configuration, which contains these
credentials: var autoEncryptionOpts = { "keyVaultNamespace" : "encryption.__dataKeys" , "kmsProviders" : { "aws" : { "accessKeyId" : "YOUR_AWS_ACCESS_KEY_ID" , "secretAccessKey" : "YOUR_AWS_SECRET_ACCESS_KEY" } } } Fill in the values for YOUR_AWS_ACCESS_KEY_ID and YOUR_AWS_SECRET_ACCESS_KEY as appropriate. 3 Connect with Encryption Support. In mongosh , use the Mongo() constructor to
establish a database connection to the target cluster. Specify the AutoEncryptionOpts document as the second
parameter to the Mongo() constructor to configure
the connection for client-side field level encryption: csfleDatabaseConnection = Mongo ( "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster" , autoEncryptionOpts ) Replace the replaceMe.example.net URI with
the connection string for the target cluster. 4 Create the Key Vault Object. Create the keyVault object using the getKeyVault() shell method: keyVault = csfleDatabaseConnection. getKeyVault ( ) ; 5 Create the Encryption Key. Create the data encryption key using the createKey() shell method: keyVault. createKey ( "aws" , { region : "regionname" , key : "awsarn" } , [ "keyAlternateName" ] ) Where: The first parameter must be "aws" to specify the configured
Amazon Web Services KMS. The second parameter must be a document containing the following: the AWS region you are connecting to, such as us-west-2 the Amazon Resource Name (ARN) to the AWS customer master key (CMK). The third parameter may be an array of one or more keyAltNames for the data encryption key. Each key alternate
name must be unique. getKeyVault() creates a unique index on keyAltNames to
enforce uniqueness on the field if one does not already exist. Key
alternate names facilitate data encryption key findability. If successful, createKey() returns
the UUID of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either: Use getKey() to retrieve the created
key by its UUID , or Use getKeyByAltName() to
retrieve the key by its alternate name, if specified. 1 Launch the mongosh Shell. Create a mongosh session without connecting to a running database
by using the --nodb option: mongosh - - nodb 2 Create the Encryption Configuration. Configuring client-side field level encryption for Azure Key Vault
requires a valid Tenant ID, Client ID, and Client Secret. In mongosh , create a new AutoEncryptionOpts variable for storing the
client-side field level encryption configuration, which contains these
credentials: var autoEncryptionOpts = { "keyVaultNamespace" : "encryption.__dataKeys" , "kmsProviders" : { "azure" : { "tenantId" : "YOUR_TENANT_ID" , "clientId" : "YOUR_CLIENT_ID" , "clientSecret" : "YOUR_CLIENT_SECRET" } } } Fill in the values for YOUR_TENANT_ID , YOUR_CLIENT_ID , and YOUR_CLIENT_SECRET as appropriate. 3 Connect with Encryption Support. In mongosh , use the Mongo() constructor to
establish a database connection to the target cluster. Specify the AutoEncryptionOpts document as the second
parameter to the Mongo() constructor to configure
the connection for client-side field level encryption: csfleDatabaseConnection = Mongo ( "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster" , autoEncryptionOpts ) Replace the replaceMe.example.net URI with
the connection string for the target cluster. 4 Create the Key Vault Object. Create the keyVault object using the getKeyVault() shell method: keyVault = csfleDatabaseConnection. getKeyVault ( ) ; 5 Create the Encryption Key. Create the data encryption key using the createKey() shell method: keyVault. createKey ( "azure" , { keyName : "keyvaultname" , keyVaultEndpoint : "endpointname" } , [ "keyAlternateName" ] ) Where: The first parameter must be "azure" to specify the configured
Azure Key Vault. The second parameter must be a document containing: the name of your Azure Key Vault the DNS name of the Azure Key Vault to use (e.g. my-key-vault.vault.azure.net ) The third parameter may be an array of one or more keyAltNames for the data encryption key. Each key alternate
name must be unique. getKeyVault() creates a unique index on keyAltNames to
enforce uniqueness on the field if one does not already exist. Key
alternate names facilitate data encryption key findability. If successful, createKey() returns
the UUID of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either: Use getKey() to retrieve the created
key by its UUID , or Use getKeyByAltName() to
retrieve the key by its alternate name, if specified. 1 Launch the mongosh Shell. Create a mongosh session without connecting to a running database
by using the --nodb option: mongosh - - nodb 2 Create the Encryption Configuration. Configuring client-side field level encryption for the GCP KMS
requires your GCP Email and its associated Private Key. In mongosh , create a new AutoEncryptionOpts variable for storing the
client-side field level encryption configuration, which contains these
credentials: var autoEncryptionOpts = { "keyVaultNamespace" : "encryption.__dataKeys" , "kmsProviders" : { "gcp" : { "email" : "YOUR_GCP_EMAIL" , "privateKey" : "YOUR_GCP_PRIVATEKEY" } } } Fill in the values for YOUR_GCP_EMAIL and YOUR_GCP_PRIVATEKEY as appropriate. 3 Connect with Encryption Support. In mongosh , use the Mongo() constructor to
establish a database connection to the target cluster. Specify the AutoEncryptionOpts document as the second
parameter to the Mongo() constructor to configure
the connection for client-side field level encryption: csfleDatabaseConnection = Mongo ( "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster" , autoEncryptionOpts ) Replace the replaceMe.example.net URI with
the connection string for the target cluster. 4 Create the Key Vault Object. Create the keyVault object using the getKeyVault() shell method: keyVault = csfleDatabaseConnection. getKeyVault ( ) ; 5 Create the Encryption Key. Create the data encryption key using the createKey() shell method: keyVault. createKey ( "gcp" , { projectId : "projectid" , location : "locationname" , keyRing : "keyringname" , keyName : "keyname" } , [ "keyAlternateName" ] ) Where: The first parameter must be "gcp" to specify the configured
Google Cloud KMS. The second parameter must be a document containing projectid is the name of your GCP project, such as my-project locationname is the location of the KMS keyring, such as global keyringname is the name of the KMS keyring, such as my-keyring keyname is the name of your key. The third parameter may be an array of one or more keyAltNames for the data encryption key. Each key alternate
name must be unique. getKeyVault() creates a unique index on keyAltNames to
enforce uniqueness on the field if one does not already exist. Key
alternate names facilitate data encryption key findability. If successful, createKey() returns
the UUID of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either: Use getKey() to retrieve the created
key by its UUID , or Use getKeyByAltName() to
retrieve the key by its alternate name, if specified. 1 Launch the mongosh Shell. Create a mongosh session without connecting to a running database
by using the --nodb option: mongosh - - nodb 2 Generate an Encryption Key. To configure client-side field level encryption for a locally managed
key, you must specify a base64-encoded 96-byte string with no line
breaks. Run the following command in mongosh to generate a key
matching these requirements: crypto. randomBytes ( 96 ). toString ( 'base64' ) You will need this key in the next step. 3 Create the Encryption Configuration. In mongosh , create a new AutoEncryptionOpts variable for storing the
client-side field level encryption configuration, replacing MY_LOCAL_KEY with the key generated in step 1: var autoEncryptionOpts = { "keyVaultNamespace" : "encryption.__dataKeys" , "kmsProviders" : { "local" : { "key" : BinData ( 0 , "MY_LOCAL_KEY" ) } } } 4 Connect with Encryption Support. In mongosh , use the Mongo() constructor to
establish a database connection to the target cluster. Specify the AutoEncryptionOpts document as the second
parameter to the Mongo() constructor to configure
the connection for client-side field level encryption: csfleDatabaseConnection = Mongo ( "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster" , autoEncryptionOpts ) 5 Create the Key Vault Object. Create the keyVault object using the getKeyVault() shell method: keyVault = csfleDatabaseConnection. getKeyVault ( ) ; 6 Create the Encryption Key. Create the data encryption key using the createKey() shell method: keyVault. createKey ( "local" , [ "keyAlternateName" ] ) Where: The first parameter must be local to specify the configured
Locally Managed Key. The second parameter may be an array of one or more keyAltNames for the data encryption key. Each key alternate
name must be unique. getKeyVault() creates a unique
index on keyAltNames to enforce uniqueness on the field if
one does not already exist. Key alternate names facilitate data
encryption key findability. If successful, createKey() returns
the UUID of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either: Use getKey() to retrieve the created
key by its UUID , or Use getKeyByAltName() to
retrieve the key by its alternate name, if specified. Tip See also: List of field level encryption shell methods Client-side field level encryption reference Back Run Aggregation Pipelines Next Write Scripts
