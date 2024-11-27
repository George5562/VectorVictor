# Configure User Authentication and Authorization with Microsoft Entra ID Domain Services - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication / LDAP Configure User Authentication and Authorization with Microsoft Entra ID Domain Services On this page Limitations Required Access Prerequisites Procedures Configure Microsoft Entra ID Domain Services for Your Domain Configure Atlas for LDAP Authentication Add the Database Access LDAP Groups to Atlas Configure Atlas for LDAP Authorization Connect to your Cluster Using mongosh In Atlas , go to the Clusters page for your project. Use to connect to your cluster with user credentials that you added to Atlas . After connecting to your cluster, run commands to verify the user has the read or write privileges you assigned them. Troubleshoot LDAP Connection Issues Note Starting with MongoDB 8.0, LDAP authentication and authorization is
deprecated. The feature is available and will continue to operate
without changes throughout the lifetime of MongoDB 8. LDAP will be
removed in a future major release. For details, see LDAP Deprecation . Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . This guide shows you how to enable Atlas to authenticate and
authorize database users (not Atlas users) from Microsoft Entra ID Domain Services , a third-party LDAP provider. You can enable LDAP authentication only or you can enable both LDAP authentication and authorization: If you enable LDAP authentication only, you add individual users to Atlas and assign database access
privileges to each user you add. If you enable LDAP authentication
and authorization, you add user groups to Atlas and assign
database access privileges to each group. Users inherit the database
access privileges from the LDAP group they belong to. Atlas supports authenticating and authorizing database users from Microsoft Entra ID Domain Services . Limitations You must deploy M10 or larger Atlas clusters to enable LDAP integration. LDAP integration is an Atlas Enterprise feature. Atlas does not support single sign-on integration for database
users. To learn about single-sign on integration for the Atlas administrative web interface, see Configure Federated Authentication . Required Access To manage LDAP users or groups, you must have Organization Owner or Project Owner access to Atlas . Prerequisites To integrate Microsoft Entra ID Domain Services LDAP with Atlas , you must have: An Azure subscription. To obtain a subscription, visit the Microsoft Azure portal . Contributor privileges or greater for your Azure subscription to
create the resources the LDAP integration requires. An Microsoft Entra ID tenant associated with
your subscription. For information about setting up an Microsoft Entra ID tenant, see the Microsoft Entra ID Documentation . Global Administrator privileges in your Microsoft Entra ID tenant to enable Microsoft Entra ID Domain Services . A custom, routable domain name. Procedures Configure Microsoft Entra ID Domain Services for Your Domain 1 Configure Microsoft Entra ID Domain Services for your domain. To configure Microsoft Entra ID Domain Services , follow the Create an advanced managed domain tutorial in the Azure Documentation using the Custom domain names DNS name option. When you configure your managed domain, make sure that you note the
value you enter in the DNS domain name field. This value
is your <managed-domain> . You must provide it in several places in
this tutorial. Example aadds.example.com 2 Obtain an SSL certificate for secure LDAP. Microsoft Entra ID Domain Services uses SSL certificates to secure LDAP. Your certificate
must adhere to the requirements outlined in the Azure Documentation . To obtain a certificate, either: Get one from the public or enterprise certificate authority (CA) your
organization uses. You must obtain a wildcard certificate to ensure secure LDAP works
properly with Microsoft Entra ID Domain Services . The certificate's subject name must match the <managed-domain> you used when you configured Microsoft Entra ID Domain Services . Example *.aadds.example.com Generate a self-signed certificate. Self-signed certificates are not
recommended for production. To generate a self-signed certificate on MacOS or Linux systems for
testing purposes : Note If you are on macOS Catalina, install the latest version of openssl . Run the following command to install using Homebrew: brew install openssl Generate a private key with openssl . The following command
generates a private key file named <your-key-name>.key : openssl genrsa -out <your-key-name>.key 2048 Edit the following configuration file template. Update the
attributes in the [dn-param] section with values that relate
to your organization. Make sure the subject name ( CN ) matches
the following template: *.<managed-domain> Example *.aadds.example.com # openssl x509 extfile params extensions = extend [req] # openssl req params prompt = no distinguished_name = dn-param [dn-param] # DN fields C = US ST = NY L  = New York O = MongoDB OU = Atlas CN = *.aadds.example.com [extend] # openssl extensions subjectKeyIdentifier = hash authorityKeyIdentifier = keyid:always keyUsage = digitalSignature,keyEncipherment,keyCertSign extendedKeyUsage=serverAuth,clientAuth Save the file as <your-config-name>.cfg . Generate a certificate signing request using the key and
configuration files you created. The following command generates a
certificate signing request named <your-csr-name>.csr : openssl req -new -key <your-key-name>.key \ -out <your-csr-name>.csr -config <your-config-name>.cfg \ -extensions extend Generate a self-signed certificate using key, configuration, and
certificate signing request files you created. The following
command generates a self-signed certificate file named <your-cert-name>.crt : openssl x509 -req -sha256 -days 365 -in <your-csr-name>.csr \ -signkey <your-key-name>.key -out <your-cert-name>.crt \ -extfile <your-config-name>.cfg To generate a self-signed certificate on a Windows system for testing
purposes , see the Azure documentation . 3 Obtain an SSL certificate that includes your private key. Microsoft Entra ID Domain Services uses private keys to decrypt secure LDAP traffic.
Certificates that include private keys use the PKCS#12 format and
use the .pfx file format. You must upload a certificate of this
format to Microsoft Entra ID Domain Services to decrypt secure LDAP traffic sent over
the public internet. To generate a .pfx certificate on MacOS or Linux systems: Save your public key and SSL certificate to your local machine. Note Your certificate must use the PEM format. If your certificate does not contain your private key, you can save
your private key to a .key format file. Generate a .pfx certificate using your private key and your
certificate with openssl . The following command generates a .pfx certificate file named <your-cert-name>.pfx : openssl pkcs12 -export -out <your-cert-name>.pfx \ -inkey <your-key-name>.key -in <your-cert-name>.crt When prompted, enter and verify a password to encrypt the file. You
will enter this password to decrypt your private key when you
upload the .pfx certificate to Microsoft Entra ID Domain Services . To generate a .pfx certificate on a Windows system,
see the Azure documentation . 4 Enable secure LDAP on Microsoft Entra ID Domain Services . To enable secure LDAP on Microsoft Entra ID Domain Services , see the Azure documentation . 5 Configure your DNS provider. You must configure your DNS provider so that Atlas and the
database nodes can connect to the LDAP server in the custom domain
that Microsoft Entra ID Domain Services manages. Create a host record for LDAP traffic that resolves a subdomain of
your <managed-domain> to the external IP address that the Microsoft Entra ID Domain Services LDAP service uses: LDAP IP Address Subdomain for LDAP Traffic 203.0.113.77 ldap.aadds.example.com To find the external IP address the Microsoft Entra ID Domain Services LDAP service uses,
see the Azure documentation . 6 Add your custom domain to Microsoft Entra ID . Add your custom domain name to Microsoft Entra ID to create users that belong
to your domain. After you add your domain, you must also add the Microsoft Entra ID DNS information in a TXT record with your DNS provider and verify the configuration. To add your custom domain to Microsoft Entra ID , see the Azure documentation . 7 Configure Microsoft Entra ID Domain Services for inbound LDAP traffic. You must allow all traffic over all ports from the public internet to
port 636 to use Microsoft Entra ID Domain Services as an LDAP provider with Atlas . To add an inbound security rule to allow inbound LDAP traffic on port 636 , see the Azure documentation . 8 Create a bind user. Create a bind user. The bind user is an Microsoft Entra ID user that you use to query
the account and to authenticate database users' credentials when they
connect to an Atlas database. The bind user must belong to the
custom domain you added to Microsoft Entra ID . To create Microsoft Entra ID users, see the Azure documentation . 9 Enable the bind user account for Microsoft Entra ID Domain Services . You must generate a password hash for the bind user for Kerberos
and NTLM authentication before the bind user can use Microsoft Entra ID Domain Services .
The steps differ based on the type of Microsoft Entra ID user account. To learn how to generate password hashes for your users, see the Azure documentation . 10 Assign the Directory Readers role to the bind user account. To query Microsoft Entra ID , the bind user
must have the permissions granted by the Directory Readers role. To assign the Directory Readers role to the bind user, see the Azure documentation . 11 Create Microsoft Entra ID Users. If they don't exist already, create users in Microsoft Entra ID Domain Services that you
want to grant database access to. Users must belong to the custom
domain you added to Microsoft Entra ID . To create Microsoft Entra ID users, see the Azure documentation . Configure Atlas for LDAP Authentication The following procedure enables Atlas to authenticate database users from Microsoft Entra ID Domain Services LDAP : 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authentication to On . Note You might incur additional costs when you enable this feature.
See Advanced Security . 3 Enter the server details and bind credentials for all of your LDAP servers in the Configure Your LDAP Server panel. You may list multiple servers separated by commas. You cannot use different ports. 4 Add a User to DN Mapping. Add a User to DN mapping similar to the following example to allow
clients to provide their username instead of full DNs when they
connect to Atlas databases: [ { "match":"(.+)", "substitution":"CN={0},OU=AADDC Users,DC=<managed-domain>,DC=com" } ] Note For Microsoft Entra ID Domain Services , the attributes in distinguished names must be
upper case. If your <managed-domain> consists of one or more subdomains,
you must add a DC (domainComponent) attribute to the
distinguished name for each. Example If your <managed-domain> is aadds.example.com , the domain
components are: DC=aadds,DC=example,DC=com 5 Enter certificates issued from a Certificate Authority (CA) for your LDAP servers, separated by commas, in the CA Root Certificate field. You may provide self-signed certificates. 6 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
servers using the configuration details that you provided. 7 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 8 Add LDAP users to Atlas . Note Skip this step if you want to enable
LDAP authorization. Add users managed in the Azure AD to Atlas . Click Add New Database User . Click LDAP User . Perform one of the following: If you have not entered a User to DN Mapping , enter
the full DN of the LDAP user. Follow this template: CN=<user-name>,OU=AADDC Users,DC=<managed>,DC=<domain>,DC=com For example, if your <user-name> is Jane Doe and
your <managed-domain> is aadds.example.com , your user's
DN is: CN=Jane Doe,ou=AADDC Users,DC=aadds,DC=example,DC=com If you entered a User to DN Mapping ,
enter the username that your mapping requires. Select the database access level to grant to the user. Click Add User . Add the Database Access LDAP Groups to Atlas Note Skip this section if you don't want to
enable LDAP authorization. Important You must enable authentication with LDAP before enabling
authorization. When you enable and configure LDAP authorization, database users
who are only configured for LDAP authentication will no longer
be able to access databases. Atlas LDAP authorization uses LDAP groups to determine if
users are authorized to perform database actions. Create separate Microsoft Entra ID groups for
each level of access that you want to grant to users. For example,
you create one group for read access to one database, another for read
and write access, and so on. Assign users to groups based on the level
of access each user requires. To create Microsoft Entra ID database access
groups and assign users, see the Azure documentation . Configure Atlas for LDAP Authorization Note Skip this section if you don't want to
enable LDAP authorization. The following procedure adds the Microsoft Entra ID Domain Services database access
groups to Atlas and enables database user authorization in Atlas : 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Add the database access LDAP groups to Atlas . Add each of the Azure database groups you created to Atlas .
Members of groups that you add are authorized to perform database actions
granted to the group. Click Add New Database User . Click LDAP Group , and then enter the full DN of the
group containing your database users, even if you enabled User to DN Mapping . Follow this template: CN=<group-name>,OU=AADDC Users,DC=<managed-domain>,DC=com Note For Microsoft Entra ID Domain Services , the attributes in distinguished names must be
upper case. If your <managed-domain> consists of one or more subdomains,
you must add a DC (domainComponent) attribute to the
distinguished name for each. Example If your <managed-domain> is aadds.example.com , the domain
components are: DC=aadds,DC=example,DC=com For example, if your <group-name> is Atlas read only and
your <managed-domain> is aadds.example.com , your user's
DN is: CN=Atlas read only,OU=AADDC Users,DC=aadds,DC=example,DC=com Select the database access level to grant to users in this group. Click Add User . 3 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 4 Toggle the button next to LDAP Authorization to On . 5 Verify the server details and bind credentials for your LDAP server are correct in the Configure Your LDAP Server panel. 6 Enter a query template in Query Template . When a user attempts to perform an action, Atlas executes the LDAP query template to obtain the LDAP groups to which the authenticated user belongs. Atlas permits the action if the query returns at least one group
that is authorized to perform the action. Atlas does not permit
the action if the query returns no groups that are authorized to
perform the action. Atlas substitutes the authenticated username in the {USER} placeholder when it runs the query. The query is relative to the host
specified in Server Hostname . The formatting for the query must conform to RFC4515 . If you want to identify what group a user is a member of, you can use
the default Query Template : {USER}?memberOf?base Note Other query templates may also work. 7 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
server using the configuration details that you provide. Connect to your Cluster Using mongosh The following procedure verifies that LDAP authentication (and LDAP authorization, if enabled) is configured correctly: Note When LDAP authentication is enabled, database users must override
the following parameters in the connection string for their
clients: authSource must be $external authenticationMechanism must be PLAIN 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Use mongosh to connect to your cluster with user credentials that you added to Atlas . To copy the connection string: Click Connect . Click LDAP , and then click Copy . Paste and edit the string with your User DN and password. Note Connect to your cluster with a user's full DN if User to DN
Mapping is not enabled. Note For Microsoft Entra ID Domain Services , the attributes in distinguished names must be
upper case. If your <managed-domain> consists of one or more subdomains,
you must add a DC (domainComponent) attribute to the
distinguished name for each. Example If your <managed-domain> is aadds.example.com , the domain
components are: DC=aadds,DC=example,DC=com Escape spaces in user or group names in the user's full DN: --username CN=Jane\ Doe,OU=AADDC\ Users,DC=aadds,DC=example,DC=com Note If you're using a user's full DN, include only the AADDC Users OU (Organizational Unit). Don't include other Microsoft Entra ID groups the user is a
member of. 3 After connecting to your cluster, run commands to verify the user has the read or write privileges you assigned them. Troubleshoot LDAP Connection Issues Note In Microsoft Entra ID Domain Services , the bind user must be a member of the Microsoft Entra ID DC Administrators group
to perform LDAP searches. Make sure that your bind user has these privileges before running ldapsearch . Use ldapsearch to determine if the query template you
configured Atlas to use returns user DNs the way you expect. The
query template may not be returning the correct user DNs if LDAP authentication works but LDAP authorization doesn't. Use the following ldapsearch template: ldapsearch -H 'ldaps://ldap.<managed-domain>.com' -b 'DC=<managed>,DC=<domain>,DC=com' -s sub -D 'CN=<bind-user-dn>,OU=AADDC Users,DC=<managed>,DC=<domain>,DC=com' -w '<REDACTED>' '(&(objectCategory=user)(memberOf=CN=<group-name>,OU=AADDC Users,DC=<managed-domain>,DC=com))' Note For Microsoft Entra ID Domain Services , the attributes in distinguished names must be
upper case. If your <managed-domain> consists of one or more subdomains,
you must add a DC (domainComponent) attribute to the
distinguished name for each. Example If your <managed-domain> is aadds.example.com , the domain
components are: DC=aadds,DC=example,DC=com For example, if your bind-user-dn is CN=LDAP Bind User,OU=AADDC Users,DC=aadds,DC=example,DC=com ,
your <managed-domain> is aadds.example.com , and your group-name is Atlas read only , use the following command: ldapsearch -H 'ldaps://ldap.aadds.example.com' -b 'DC=aadds,DC=example,DC=com' -s sub -D 'CN=LDAP Bind User,OU=AADDC Users,DC=aadds,DC=example,DC=com' -w '<REDACTED>' '(&(objectCategory=user)(memberOf=CN=Atlas read only,OU=AADDC Users,DC=aadds,DC=example,DC=com))' Note Other query templates may also work. Back LDAP Next Okta
