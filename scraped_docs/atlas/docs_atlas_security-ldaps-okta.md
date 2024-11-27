# Configure User Authentication and Authorization with Okta LDAP Interface - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication / LDAP Configure User Authentication and Authorization with Okta LDAP Interface On this page Limitations Required Access Procedures Configure Okta for LDAP Authentication Configure Atlas for LDAP Authentication Configure Okta for LDAP Authorization Configure Atlas for LDAP Authorization Connect to your Cluster Using mongosh In Atlas , go to the Clusters page for your project. Connect to your cluster with the user credentials that you added to Atlas . After connecting to your cluster, run commands to verify the user has the read or write privileges you assigned them. Troubleshoot LDAP Connection Issues Note Starting with MongoDB 8.0, LDAP authentication and authorization is
deprecated. The feature is available and will continue to operate
without changes throughout the lifetime of MongoDB 8. LDAP will be
removed in a future major release. For details, see LDAP Deprecation . Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . This guide shows you how to enable Atlas to authenticate and
authorize database users (not Atlas users) from Okta , a third-party LDAP provider. You can enable LDAP authentication only or you can enable both LDAP authentication and authorization: If you enable LDAP authentication only, you add individual users to Atlas and assign database access
privileges to each user you add. If you enable LDAP authentication
and authorization, you add user groups to Atlas and assign
database access privileges to each group. Users inherit the database
access privileges from the LDAP group they belong to. Atlas supports: Authenticating database users from Okta Active Directory
synchronization. Authenticating database users from Okta. Authorizing database users in Okta groups. Limitations You must deploy M10 or larger Atlas clusters to enable LDAP integration. LDAP integration is an Atlas Enterprise feature. Atlas does not support authorizing database users in Okta Active
Directory synchronization groups. Atlas does not support single sign-on integration for database
users. To learn about single-sign on integration for the Atlas administrative web interface, see Configure Federated Authentication . Required Access To manage LDAP users or groups, you must have Organization Owner or Project Owner access to Atlas . Procedures Configure Okta for LDAP Authentication The following procedure configures Okta for authentication
with Atlas : 1 Set up the Okta LDAP interface. To learn more about setting up the Okta LDAP interface,   see the Okta documentation . Note your <okta-instance-id> . You must provide it
in several places during the configuration process. The instance name is located in the URL you use to sign in to your
Okta account: https://<okta-instance-id>.admin.okta.com 2 Create a bind user. Create a new Okta user to use as the Atlas bind user. The bind user is an Okta
user that you use to query the account and to authenticate
database users' credentials when they connect to an Atlas database. Important Don't use your own user account for the bind user. Use the following template to determine the full Distinguished Name
(DN) of your bind user: uid=<bind-user-email>,dc=<okta-instance-id>,dc=okta,dc=com For example, if your <bind-user-email> is bind@example.com and your <okta-instance-id> is mdb-example , your bind user's DN is: uid=bind@example.com,ou=users,dc=mdb-example,dc=okta,dc=com 3 Create database users in Okta. If they don't exist already, create users in Okta that you want to
grant database access to: Navigate to your Okta People page. Click Add Person . Enter the user's details. Use email addresses for usernames. Note Avoid entering email addresses with plus symbols ( + ). The Atlas LDAP integration may encounter issues with email
addresses containing plus symbols. Click Save . Configure Atlas for LDAP Authentication The following procedure enables Atlas to authenticate database users from Okta LDAP : 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authentication to On . Note You might incur additional costs when you enable this feature.
See Advanced Security . 3 Enter the server details and bind credentials for all of your LDAP servers in the Configure Your LDAP Server panel. You may list multiple servers separated by commas. You cannot use different ports. 4 Add a User to DN Mapping. Add a User to DN mapping similar to the following example to allow
clients to provide their email addresses instead of full DNs when they
connect to Atlas databases: [ { "match": "(.+)", "substitution": "uid={0},ou=users,dc=<okta_instance_id>,dc=okta,dc=com" } ] 5 Enter certificates issued from a Certificate Authority (CA) for your LDAP servers, separated by commas, in the CA Root Certificate field. You may provide self-signed certificates. 6 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
servers using the configuration details that you provided. 7 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 8 Add LDAP users to Atlas . Note Skip this step if you want to enable
LDAP authorization. Add users managed in the Okta LDAP to Atlas . Click Add New Database User . Click LDAP User . Perform one of the following: If you have not entered a User to DN Mapping , enter
the full DN of the LDAP user. Follow this template: uid=<user-name>,ou=users,dc=<okta-instance-id>,dc=okta,dc=com For example, if your <user-name> is jane@example.com and
your <okta-instance-id> is mdb-example , your user's
DN is: uid=jane@example.com,ou=users,dc=mdb-example,dc=okta,dc=com If you entered a User to DN Mapping ,
enter the username or email address that your mapping requires. Select the database access level to grant to the user. Click Add User . Configure Okta for LDAP Authorization Note Skip this section if you don't want to
enable LDAP authorization. The following procedure configures Atlas to authorize users who
belong to Okta LDAP database access groups. Important You must enable authentication with LDAP before enabling
authorization. When you enable and configure LDAP authorization, database users
who are only configured for LDAP authentication will no longer
be able to access databases. 1 Create Okta database access groups. Atlas LDAP authorization uses LDAP groups to determine if users
are authorized to perform database actions. Create separate Okta groups for each level of access that you want
to grant to users. For example,
you create one group for read access to one database, another for read
and write access, and so on. Navigate to your Okta Groups page by clicking Directory , then Groups . Click Add Group . Enter a group name, for example db-read . Click Add Group . 2 Add Okta users to database access groups. Assign users to groups based on the level of access
each user requires. Click the group you want to add users to. Click Manage People . Add users to the group, and then click Save . 3 Assign privileges to the bind user. The bind user must have Read Only Administrator privileges to
authorize users against specific Okta groups and to perform LDAP
searches. To assign the bind user Read Only Administrator privileges: Navigate to your Okta Administrators page by clicking Security , then Administrators . Click Add Administrator . Search for your bind user, then select the Read Only Administrator role. Click Add Administrator . Configure Atlas for LDAP Authorization Note Skip this section if you don't want to
enable LDAP authorization. The following procedure adds the Okta database access
groups to Atlas and enables database user authorization in Atlas : 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Add the database access LDAP groups to Atlas . Add each of the Okta database groups you created to Atlas .
Members of groups that you add are authorized to perform database actions
granted to the group. Click Add New Database User . Click LDAP Group , and then enter the full DN of the
group containing your database users, even if you enabled User to DN Mapping . Follow this template: cn=<group-name>,ou=groups,dc=<okta-instance-id>,dc=okta,dc=com For example, if your <group-name> is db-read and your <okta-instance-id> is mdb-example , your bind user's DN is: cn=db-read,ou=groups,dc=mdb-example,dc=okta,dc=com Select the database access level to grant to users in this group. Click Add User . 3 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 4 Toggle the button next to LDAP Authorization to On . 5 Verify the server details and bind credentials for your LDAP server are correct in the Configure Your LDAP Server panel. 6 Enter a query template in Query Template . When a user attempts to perform an action, Atlas executes the LDAP query template to obtain the LDAP groups to which the authenticated user belongs. Atlas permits the action if the query returns at least one group
that is authorized to perform the action. Atlas does not permit
the action if the query returns no groups that are authorized to
perform the action. Atlas substitutes the authenticated username in the {USER} placeholder when it runs the query. The query is relative to the host
specified in Server Hostname . The formatting for the query must conform to RFC4515 . If you want to identify what group a user is a member of, you can use
the following Query Template : ou=groups,dc=<okta-instance-id>,dc=okta,dc=com?dn?sub?(&(objectClass=groupofUniqueNames)(uniqueMember={USER})) Note Other query templates may also work. Using the default template of {USER}?memberOf?base may result in longer search times. 7 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
server using the configuration details that you provide. Connect to your Cluster Using mongosh The following procedure verifies that LDAP authentication (and LDAP authorization, if enabled) is configured correctly: Note When LDAP authentication is enabled, database users must override
the following parameters in the connection string for their
clients: authSource must be $external authenticationMechanism must be PLAIN 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Connect to your cluster with the user credentials that you added to Atlas . Use mongosh to connect to your cluster. To copy the connection string: Click Connect . Click LDAP , and then click Copy . Paste and edit the string with your User DN and password. Note Connect to your cluster with a user's full DN if User to DN
Mapping is not enabled. 3 After connecting to your cluster, run commands to verify the user has the read or write privileges you assigned them. Troubleshoot LDAP Connection Issues Note In Okta, the bind user must have Read Only Administrator privileges to perform LDAP searches. Make sure that your bind
user has these privileges before running ldapsearch . Use ldapsearch to determine if the query template you
configured Atlas to use returns user DNs the way you expect. The
query template may not be returning the correct user DNs if LDAP authentication works but LDAP authorization doesn't. Use the following ldapsearch template: ldapsearch -H 'ldaps://<okta-instance-id>.ldap.okta.com' -D "<bind-user-dn>" -w "<bind-user-pwd>" -b 'ou=groups,dc=<okta-instance-id>,dc=okta,dc=com' '(&(objectClass=groupofUniqueNames)(uniqueMember=<bind-user-dn or group-dn>)) For example, if your bind-user-dn is uid=jane@example.com,ou=users,dc=mdb-example,dc=okta,dc=com and your <okta-instance-id> is mdb-example , use the
following command: ldapsearch -H 'ldaps://mdb-example.ldap.okta.com' -D "uid=jane@example.com,dc=mdb-example,dc=okta,dc=com" -w "REDACTED" -b 'ou=groups,dc=mdb-example,dc=okta,dc=com' '(&(objectClass=groupofUniqueNames)(uniqueMember=uid=jane@example.com,ou=users,dc=mdb-example,dc=okta,dc=com))' Note Other query templates may also work. Using the default template of {USER}?memberOf?base may result in longer search times. Back Microsoft Entra ID DS Next OneLogin
