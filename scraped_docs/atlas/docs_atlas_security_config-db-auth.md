# Configure Cluster Authentication and Authorization - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features Configure Cluster Authentication and Authorization On this page Database User Authentication or Authorization Custom Database Roles Authentication with AWS IAM User Authentication or Authorization with LDAP User Authentication with OIDC User Authentication with X.509 Atlas offers the following security features for
cluster authentication and authorization. Database User Authentication or Authorization Atlas requires clients to authenticate to access
clusters. You must create database users to access the
database. To set up database users for your clusters,
see Configure Database Users . Custom Database Roles When the built-in Atlas database user privileges don't
meet your desired set of privileges, you can create custom roles . Authentication with AWS IAM You can authenticate applications running on AWS services to Atlas clusters with AWS IAM roles. You can set up a database user to
use an AWS IAM role ARN for authentication and connect to your
database using mongosh and drivers that authenticate using your AWS IAM role ARN. Using AWS IAM role reduces the number of
authentication mechanisms and number of secrets to manage. To learn more, see Set Up Authentication with AWS IAM . User Authentication or Authorization with LDAP Atlas supports performing user authentication and authorization
with LDAP . To use LDAP , see Set up User Authentication and Authorization with LDAP . User Authentication with OIDC Atlas supports performing user authentication and authorization
with OIDC . To use OIDC , see Authentication and Authorization with OIDC/OAuth 2.0 . User Authentication with X.509 X.509 client certificates provide database users access to the
clusters in your project. Options for X.509
authentication include Atlas -managed X.509 authentication and
self-managed X.509 authentication. To learn more
about self-managed X.509 authentication, see Set Up Self-Managed X.509 Authentication . Back GCP Service Account Next Database Users
