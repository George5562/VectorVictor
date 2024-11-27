# Generate Wildcard Collections - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / Atlas Cluster Generate Wildcard Collections You can dynamically generate collection names that map to data in your Atlas cluster. To dynamically generate collection names, specify
the wildcard, * , as the value for the collection name setting in
your federated database instance storage configuration. You can use the storageSetConfig command to configure the settings for generating wildcard ( * )
collections. For the Atlas data store, you can generate the following wildcard
collections and databases in your federated database instance storage configuration: Wildcard collections for a specific database Wildcard databases with one wildcard collection You can also dynamically generate collection names that match a regex
pattern. Wildcard Collections Wildcard Databases To generate wildcard collections in your federated database instance storage
configuration that map to data in your Atlas cluster,
configure the following settings in your federated database instance storage
configuration: Specify * as the value for the databases.[n].collections.[n].name field. Omit the databases.[n].collections.[n].dataSources.[n].collection field. Optional . Use the databases.[n].collections.[n].dataSources.[n].collectionRegex field to generate wildcard collection names that match a regex
pattern. Example "databases" : [ { "name" : "<db-name>" , "collections" : [ { "name" : "*" , "dataSources" : [ { "storeName" : "<atlas-store-name>" , "database" : "<atlas-db-name>" , "collectionRegex" : "<regex-pattern>" } ] } ] } ] You can also use the create administration command and the federated database instance User Interface to
configure the settings for generating wildcard collections. To dynamically generate databases with one wildcard collection in
your federated database instance storage configuration, configure the following
settings in your federated database instance storage configuration: Specify * as the value for the databases.[n].name field. Specify * as the value for the databases.[n].collections.[n].name field. Omit the databases.[n].collections.[n].dataSources.[n].database and databases.[n].collections.[n].dataSources.[n].collection fields. Optional . Use the databases.[n].collections.[n].dataSources.[n].collectionRegex field to generate wildcard collection names that match a regex
pattern. Example "databases" : [ { "name" : "*" , "collections" : [ { "name" : "*" , "dataSources" : [ { "storeName" : "<atlas-store-name>" , "collectionRegex" : "<regex-pattern>" } ] } ] } ] You can use the create administration command also to configure the settings for
generating wildcard collection for wildcard databases. You
can't use the federated database instance User Interface to configure the settings
for generating wildcard collection for wildcard databases. Dynamically generated databases: Can exist alongside explicitly defined databases. However,
Atlas Data Federation won't include dynamically generated databases with
names that conflict with databases that are explicitly
defined in the storage configuration. Can only be from a single Atlas cluster. Atlas Data Federation won't
dynamically generate databases from multiple Atlas clusters or other data stores. Back Deploy Next HTTP URL
