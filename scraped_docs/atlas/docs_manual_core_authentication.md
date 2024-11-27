# Authentication on Self-Managed Deployments - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Self-Managed Deployments / Security Authentication on Self-Managed Deployments On this page Getting Started Authentication Mechanisms SCRAM Authentication x.509 Certificate Authentication Kerberos Authentication LDAP Proxy Authentication OpenID Connect Authentication Internal / Membership Authentication Note Starting in MongoDB 8.0, LDAP authentication and authorization is
deprecated. LDAP is available and will continue to operate without
changes throughout the lifetime of MongoDB 8. LDAP will be removed in a
future major release. For details, see LDAP Deprecation . Authentication is the process of verifying the identity of a client.
When access control ( authorization ) is
enabled, MongoDB requires all clients to authenticate themselves in
order to determine their access. Although authentication and authorization are closely connected, authentication is distinct from authorization: Authentication verifies the identity of a user . Authorization determines the verified user's access to resources
and operations. You can configure authentication through the UI for deployments hosted in MongoDB Atlas . Getting Started To get started using access control, follow these tutorials: Enable Access Control on Self-Managed Deployments Create a User on Self-Managed Deployments Authenticate a User with Self-Managed Deployments Authentication Mechanisms SCRAM Authentication Salted Challenge Response Authentication Mechanism (SCRAM) is the default authentication mechanism for
MongoDB. For more information on SCRAM and MongoDB, see: SCRAM Authentication Use SCRAM to Authenticate Clients on Self-Managed Deployments x.509 Certificate Authentication MongoDB supports x.509 certificate authentication for client authentication and internal
authentication of the members of replica sets and sharded clusters.
x.509 certificate authentication requires a secure TLS/SSL
connection . To use MongoDB with x.509, you must use valid certificates generated and
signed by a certificate authority. The client x.509 certificates
must meet the client certificate requirements . For more information on x.509 and MongoDB, see: x.509 Certificate Authentication Use x.509 Certificates to Authenticate Clients on Self-Managed Deployments Kerberos Authentication MongoDB Enterprise supports Kerberos Authentication . Kerberos is
an industry standard authentication protocol for large client/server
systems that provides authentication using short-lived tokens that are
called tickets. To use MongoDB with Kerberos, you must have a properly configured
Kerberos deployment, configured Kerberos service principals for MongoDB, and a Kerberos user
principal added to MongoDB. For more information on Kerberos and MongoDB, see: Kerberos Authentication Configure Self-Managed MongoDB with Kerberos Authentication on Linux Configure Self-Managed MongoDB with Kerberos Authentication on Windows LDAP Proxy Authentication MongoDB Enterprise and MongoDB Atlas support LDAP Proxy Authentication proxy
authentication through a Lightweight Directory Access Protocol (LDAP)
service. For more information on Kerberos and MongoDB, see: LDAP Proxy Authentication Authenticate Using Self-Managed SASL and LDAP with ActiveDirectory Authenticate Using Self-Managed SASL and LDAP with OpenLDAP Authenticate and Authorize Users Using Self-Managed Active Directory with Native LDAP These mechanisms allow MongoDB to integrate into your
existing authentication system. OpenID Connect Authentication MongoDB Enterprise supports OpenID Connect authentication. OpenID
Connect is an authentication layer built on top of OAuth2. You can use OpenID
Connect to configure single sign-on between your MongoDB database and a third-party
identity provider. For more information on OpenID Connect and MongoDB, see: OpenID Connect Authentication Configure MongoDB with OpenID Connect OpenID Connect Internal / Membership Authentication In addition to verifying the identity of a client, MongoDB can require
members of replica sets and sharded clusters to authenticate
their membership to their respective
replica set or sharded cluster. See Self-Managed Internal/Membership Authentication for more information. Back Enable Access Control Next Kerberos
