# Generate Wildcard Collections - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket Generate Wildcard Collections You can dynamically generate collection names that map to data in your S3 bucket. To dynamically generate collection names, specify the
wildcard, * , as the value for the collection name setting in your
federated database instance storage configuration. You can use the storageSetConfig command to configure the settings for generating wildcard ( * )
collections. To generate wildcard collections in your federated database instance storage configuration
that map to data in your S3 bucket, configure the following settings
in your federated database instance storage configuration: Specify * as the value for the databases.[n].collections.[n].name setting. Specify the collectionName() function as the value for the databases.[n].collections.[n].dataSources.[n].path setting. Optional . Specify the maximum number of collections to include in
the database in the databases.[n].maxWildcardCollections setting. By
default, Atlas Data Federation generates up to 100 wildcard collections in the
database. Example "databases" : [ { "name" : "<db-name>" , "collections" : [ { "name" : "*" , "dataSources" : [ { "storeName" : "<s3-store-name>" , "path" : "{collectionName()}" } ] } ] , "maxWildcardCollections" : <integer> , } ] You can also use the create administration command and the federated database instance User Interface JSON Editor to
configure the settings for generating wildcard collections. You can't
use the federated database instance User Interface Visual Editor to configure the settings
for generating wildcard collections. Back Deploy Next Define Path for S3 Data
