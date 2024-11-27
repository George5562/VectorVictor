# Set Up Authentication with AWS IAM - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Get Started / Configure a Connection Set Up Authentication with AWS IAM On this page Set Up Authentication with AWS IAM Roles Grant Database Access to AWS IAM Roles Connect to Atlas Cluster Using AWS IAM You can set up a database user to use an AWS IAM User or Role ARN for authentication. You can connect
to your database using mongosh and drivers and authenticate using
your AWS IAM User or Role ARN. Using AWS IAM reduces the number
of authentication mechanisms and number of secrets to manage. The secret
key that you use for authentication is not sent over the wire to Atlas and is not persisted by the driver. Set Up Authentication with AWS IAM Roles Note You can't setup authentication for AWS IAM principals when LDAP authorization is enabled. If you require authentication for an AWS IAM principal, consider
moving the clusters that you want to access with AWS IAM
authentication into another project where LDAP authorization is
disabled. You can set up AWS IAM Roles to authenticate AWS compute types to
your Atlas clusters. For AWS Lambda and HTTP (ECS and EC2), drivers automatically read
from the environment variables .
For AWS EKS, you must manually assign the IAM role. This page
describes how AWS Lambda, AWS ECS , and AWS EKS can
connect using an AWS IAM role. Note You must assign an IAM role to Lambda, EC2, ECS, or EKS in the AWS console. AWS Lambda AWS ECS AWS ECS Fargate AWS EKS AWS Lambda passes information to functions through the following
environment variables if you assign an execution role to the
lambda function. AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN Note You don't need to manually create these environment variables when
you use an execution role in your
function. To learn more about these environment variables, see Using AWS Lambda
environment variables . AWS ECS gets the credentials from
the following URI: http://169.254.170.2 + AWS_CONTAINER_CREDENTIALS_RELATIVE_URI AWS_CONTAINER_CREDENTIALS_RELATIVE_URI is an environment variable.
To learn more, see IAM Roles for Tasks . AWS EC2 gets the credentials from Instance Metadata Service V2 at the
following URL : http://169.254.169.254/latest/meta-data/iam/security-credentials/ To learn more, see Launch an instance with an IAM role . To learn how to configure an AWS IAM role for authentication with AWS ECS Fargate, see the AWS documentation . For AWS EKS , you must first
assign the IAM role to your pod to set up the following environment
variables in that pod: AWS_WEB_IDENTITY_TOKEN_FILE - contains the path to the web
identity token file. AWS_ROLE_ARN - contains the IAM role used to connect to
your cluster. For information on assigning an IAM role to your pod, see the AWS documentation . After you assign the IAM role to your pod, you must manually
assume the IAM role to connect to your cluster. To assume the role manually: Use the AWS SDK to
call AssumeRoleWithWebIdentity . Tip Omit the ProviderID parameter. Find the value of the WebIdentityToken parameter in the file
described in your pod's AWS_WEB_IDENTITY_TOKEN_FILE environment variable. Pass the credentials that you received in the previous step to the
MongoDB driver. See your driver's documentation for
details. Grant Database Access to AWS IAM Roles To grant database access to the AWS IAM role, complete the steps
described in the Configure Database Users section for AWS IAM . For
more information on granting database access using Atlas CLI,
Atlas Administration API, or Atlas UI, see Add Database Users . Connect to Atlas Cluster Using AWS IAM To connect to Atlas with your AWS IAM credentials using mongosh , provide a connection string that specifies the
MONGODB-AWS authentication mechanism . This connection string
format applies to all AWS IAM authentication mechanisms. Important You must configure authentication using one of the
methods described in the Set Up Authentication with AWS IAM Roles before
you can use this connection string format. Connecting to Atlas using AWS IAM authentication with the mongosh requires shell version v0.9.0 or higher. Use your AWS IAM credentials ,
using your access key ID as your username and your secret key as your
password. The authSource query parameter is $external , URL-encoded as %24external . The authMechanism query parameter is MONGODB-AWS . Example mongosh "mongodb+srv://<atlas-host-name>/test?authSource=%24external&authMechanism=MONGODB-AWS" --username <access-key-id> --password <secret-key> Tip See also: IAM roles for service accounts Back Custom Database Roles Next LDAP
