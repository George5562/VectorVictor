# Authentication and Authorization with OIDC/OAuth 2.0 - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication Authentication and Authorization with OIDC/OAuth 2.0 You can authenticate and authorize access to Atlas clusters for both human users
and applications with your own identity provider that supports OIDC or OAuth 2.0. You can use your existing identity provider to configure single-sign-on for
human user access to Atlas clusters with
Workforce Identity Federation. You can similarly use your existing cloud provider application users,
such as Azure Service Principals, Azure Managed Identities, or GCP Service
Accounts, for application access to Atlas clusters with Workload Identity Federation. You can manage authentication all in one place, either using your OIDC provider for human user access, or your OAuth 2.0 provider for application
access. The following table compares the OIDC and OAuth 2.0 access options. Note If you already use other authentication mechanisms, such as SCRAM, X.509
or AWS-IAM, you can continue to use them for database access. Authentication method User type Supported protocols Workforce Identity Federation Human users OIDC Workload Identity Federation Programmatic users OAuth 2.0 Select the authentication method to learn more: Workforce Identity Federation (Humans) Workload Identity Federation (Applications) Back OneLogin Next Workforce (Humans)
