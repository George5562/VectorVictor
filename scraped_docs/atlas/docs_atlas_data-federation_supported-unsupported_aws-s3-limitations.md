# Data Federation AWS S3 Limitations - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket Data Federation AWS S3 Limitations Atlas Data Federation supports the following Amazon S3 storage classes only: Standard Intelligent Tiering Standard-Infrequent Access Data Federation supports files in the Standard storage
class by default. To enable support for files in the Intelligent Tiering and Standard-Infrequent Access storage classes, see stores.[n].additionalStorageClasses . Data Federation does not support creating a federated database instance with S3 buckets from more
than one AWS account. Back CSV and TSV Next Azure Blob Storage
