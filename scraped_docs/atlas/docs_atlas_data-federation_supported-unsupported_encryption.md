# Configure S3 Encryption - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket Configure S3 Encryption Atlas Data Federation can query and analyze unencrypted data in your AWS S3 buckets without additional configuration. However, to read encrypted
data or write data to your S3 buckets using $out ,
Data Federation might require additional permissions depending on your S3 encryption settings. The following table describes the required configuration for your
federated database instance to read encrypted data and to use $out to
write data to S3 for each type of AWS S3 encryption. AWS S3 Encryption Types Required Data Federation Configuration AES-256 Atlas Data Federation supports both reads and writes of data encrypted in S3 buckets using AES-256 AWS Managed Keys by default. No additional
configuration is required. SSE with Amazon S3-Managed Atlas Data Federation supports both reads and writes of data encrypted in the S3 buckets using SSE with Amazon S3 Managed Keys by default. No
additional configuration is required. Customer Managed Symmetric Customer Master Keys Atlas Data Federation can't access data encrypted in the S3 buckets using SSE
Customer Managed Symmetric Customer Master Keys by default. For
reads and writes, you must add permissions similar to the following
to the policy assigned to your IAM role: { "Effect" : "Allow" , "Action" : [ "kms:GenerateDataKey" , "kms:decrypt" ] , "Resource" : [ "arn:aws:kms:<aws-region>:<role-ID>:key/<master-key>" ] } To modify the your AWS IAM role trust policy: Log in to your AWS Management Console and navigate to the Identity and Access Management (IAM) service
page. Select Roles from the left-side navigation and
click on the IAM role to modify. Select the Trust Relationships tab. Click the Edit trust relationship button and edit
the Policy Document . Back Optimize Queries Next Data Formats
