# Deploy a Federated Database Instance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / Azure Blob Storage Deploy a Federated Database Instance On this page Prerequisites Procedure This page describes how to deploy a federated database instance for
accessing data in your Azure Blob Storage containers. Prerequisites Before you begin, complete the following prerequisites: Create a MongoDB Atlas account, if you don't have one already. Install Azure PowerShell or Azure
CLI . To learn more
about these tools, see Choose the right Azure command-line tool . Configure Azure PowerShell or Azure CLI . Optional. Set Up Azure Service Principal Access . Procedure Atlas CLI Atlas UI To create a new Data Federation database using the
Atlas CLI, run the following command: atlas dataFederation create <name> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dataFederation create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI 1 Log in to MongoDB Atlas. 2 Select the Data Federation option on the left-hand navigation. 3 Create a federated database instance. Click the Create New Federated Database dropdown. Select Manual Setup . 4 Select the cloud provider where Atlas Data Federation will process your queries against your federated database instance. You can select AWS , Azure , or Google Cloud. Once your federated database instance is created, you
can't change the cloud provider where Atlas Data Federation processes your queries. If you are configuring a federated database instance for data in an Azure Blob Storage container, you can't choose a cloud provider that is different from the cloud provider that is hosting your data. That is, you must choose Azure . 5 Type a name for your federated database instance in the Federated Database Instance Name field and click Continue . Defaults to FederatedDatabaseInstance[n] . Once your federated database instance is
created, you can't change its name. 6 Select the configuration method. For a guided experience, click Visual Editor . To edit the raw JSON , click JSON Editor . 7 Specify your Azure Blob Storage data store and configure federated database instance and virtual collections that map to your data store. Visual Editor JSON Editor Select the dataset for your federated database instance from the Data Sources section. Click Add Data Sources to select your data store. Specify your data store. Choose Azure to configure a federated database instance for data in Azure Blob Storage
containers. Corresponds to stores.[n].provider JSON configuration setting. Select an Azure Service Principal for Atlas . You can select an existing Azure Service Principal that Atlas is
authorized for from the Service Principal dropdown or choose Authorize an Azure Service Principal to authorize a new
service principal. If you selected an existing service principal that Atlas is
authorized for, proceed to the next step. If you are authorizing Atlas for an existing service principal or
are creating a new service principal, complete the following steps
before proceeding to the next step: Select Authorize an Azure Service Principal to
authorize a new or existing service principal and click Continue . Use the Azure Service Principal AppId in the Add
Atlas to your Azure Service Principal section to grant Atlas access through an existing or new Azure Service Principal. Follow the steps in the PowerShell or AzureCLI tab in the Atlas UI to create a new
service prinicpal or modify an existing service principal. Enter the tenant ID and Service Principal ID in the respective
fields after completing the steps in the Atlas UI. Click Validate and Finish to proceed to the next step. Configure access to your Azure Blob Storage. In the Configure Azure Blob Storage page, you must
configure Azure Storage Account credential delegation and Storage
Container access. To do these: Enter your Storage Account Resource ID in the Storage
Account Credential Delegation field. To learn more, see Get the resource ID for a storage account . Copy and run the command from the Storage Account
Credential Delegation step in your Azure PowerShell
to set up the credentials delegation. Specify whether the storage container allows Read only or Read and write operations. Atlas can only query Read-only containers; if you
wish to query and save query results to your Azure Blob Storage container,
choose Read and write . Atlas Data Federation doesn't support writes to your Azure Blob Storage container using $out . Enter your Storage Container name. Copy and run the command shown from the Storage
Container Access step in your Azure PowerShell to set up blob
container access. Click Continue . Define the path structure for your files in the Azure Blob Storage container
and click Next . Enter the storage path to your Azure Blob Storage container. For example: https://<storage-account>.blob.core.windows.net/<container>/<file-name> To add additional paths to data on your Azure Blob Storage container, click Add Data Source and enter the path. To learn more about
paths, see Define Path for S3 Data . Corresponds to databases.[n].collections.[n].dataSources.[n].path JSON configuration setting. Optional . Specify the partition fields that Data Federation should use
when searching the files in the Azure Blob Storage container and the field
value type. If omitted, Data Federation does a recursive search for all files from the
root of the Azure Blob Storage container. If you don't select a specific field
value type, Data Federation adds any value in that path in all queries. Corresponds to stores.[n].prefix and databases.[n].collections.[n].dataSources.[n].path JSON configuration settings. Create the virtual databases, collections, and views and map the
databases, collections, and views to your data store. (Optional) Click the for the: Database to edit the database name. Defaults to VirtualDatabase[n] . Corresponds to databases.[n].name JSON configuration
setting. Collection to edit the collection name. Defaults to VirtualCollection[n] . Corresponds to databases.[n].collections.[n].name JSON configuration setting. View to edit the view name. You can click: Add Database to add databases and collections. associated with the database to add collections
to the database. associated with the collection to add views on the collection. To create a
view, you must specify: The name of the view. The pipeline to apply to the view. The view definition pipeline cannot include the $out or
the $merge stage. If the view definition includes
nested pipeline stages such as $lookup or $facet ,
this restriction applies to those nested pipelines as well. To learn more about views, see: Views db.createView associated with the database, collection, or
view to remove it. Select Azure Blob Storage from the dropdown in the Data Sources section. Drag and drop the data store to map with the collection. Corresponds to databases.[n].collections.[n].dataSources JSON configuration setting. Your configuration for Azure Blob Storage data store should look
similar to the following: { "stores" : [ { "name" : "<string>" , "provider" : "<string>" , "region" : "<string>" , "serviceURL" : "<string>" , "containerName" : "<string>" , "delimiter" : "<string>" , "prefix" : "<string>" , "public" : <boolean> } ] , "databases" : [ { "name" : "<string>" , "collections" : [ { "name" : "<string>" , "dataSources" : [ { "storeName" : "<string>" , "path" : "<string>" , "defaultFormat" : "<string>" , "provenanceFieldName" : "<string>" , "omitAttributes" : <boolean> } ] } ] , "maxWildcardCollections" : <integer> , "views" : [ { "name" : "<string>" , "source" : "<string>" , "pipeline" : "<string>" } ] } ] } For more information on the configuration settings, see Define Data Stores for a Federated Database Instance . Define your Azure Blob Storage data store. Edit the JSON configuration settings shown in the UI for stores . Your stores cofiguration setting should resemble the
following: "stores" : [ { "name" : "<string>" , "provider" : "<string>" , "region" : "<string>" , "serviceURL" : "<string>" , "containerName" : "<string>" , "delimiter" : "<string" , "prefix" : "<string>" , "public" : <boolean> } ] To learn more about these configuration settings, see stores . Define your federated database instance virtual databases, collections, and views. Edit the JSON configuration settings shown in the UI for databases . Your databases cofiguration setting should
resemble the following: "databases" : [ { "name" : "<string>" , "collections" : [ { "name" : "<string>" , "dataSources" : [ { "storeName" : "<string>" , "defaultFormat" : "<string>" , "path" : "<string>" , "provenanceFieldName" : "<string>" , "omitAttributes" : <boolean> } ] } ] , "maxWildcardCollections" : <integer> , "views" : [ { "name" : "<string>" , "source" : "<string>" , "pipeline" : "<string>" } ] } ] To learn more about these configuration settings, see databases . 8 Optional: Repeat steps in the Visual Editor or JSON Editor tab above to define additional Azure Blob Storage data stores. To add other data stores for federated queries, see: Create Atlas Data Store From the UI Create HTTP or HTTPS Data Store From the
UI Create Atlas Online Archive Data Store From the UI Note You can't create an AWS data store for running federated
queries across different cloud providers. 9 Click Save to create the federated database instance. Back Azure Blob Storage Next Google Cloud Storage
