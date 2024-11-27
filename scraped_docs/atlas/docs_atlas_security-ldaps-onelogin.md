# Configure User Authentication and Authorization with OneLogin VLDAP - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication / LDAP Configure User Authentication and Authorization with OneLogin VLDAP On this page Limitations Required Access Procedures Configure OneLogin for LDAP Authentication Configure Atlas for LDAP Authentication Configure OneLogin for LDAP Authorization Configure Atlas for LDAP Authorization Connect to your Cluster Using mongosh In Atlas , go to the Clusters page for your project. Connect to your cluster with the user credentials that you added to Atlas . After connecting to your cluster, run commands to verify the user has the read or write privileges you assigned them. Troubleshoot LDAP Connection Issues Note Starting with MongoDB 8.0, LDAP authentication and authorization is
deprecated. The feature is available and will continue to operate
without changes throughout the lifetime of MongoDB 8. LDAP will be
removed in a future major release. For details, see LDAP Deprecation . Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . This guide shows you how to enable Atlas to authenticate and
authorize database users (not Atlas users) from OneLogin , a third-party LDAP provider. You can enable LDAP authentication only or you can enable both LDAP authentication and authorization: If you enable LDAP authentication only, you add individual users to Atlas and assign database access
privileges to each user you add. If you enable LDAP authentication
and authorization, you add user groups to Atlas and assign
database access privileges to each group. Users inherit the database
access privileges from the LDAP group they belong to. Atlas supports authenticating and authorizing database users from
OneLogin. Limitations You must deploy M10 or larger Atlas clusters to enable LDAP integration. LDAP integration is an Atlas Enterprise feature. Atlas does not support authenticating and authorizing users
synchronized from existing LDAP directories. Atlas does not support single sign-on integration for database
users. To learn about single-sign on integration for the Atlas administrative web interface, see Configure Federated Authentication . Required Access To manage LDAP users or groups, you must have Organization Owner or Project Owner access to Atlas . Procedures Configure OneLogin for LDAP Authentication The following procedure configures OneLogin for authentication
with Atlas : 1 Set up OneLogin LDAP service. To learn more about setting up the OneLogin LDAP service, see the OneLogin documentation . Important You may need to contact OneLogin support to enable
the VLDAP service for your account. Note your <onelogin-instance-id> . You must provide it
in several places during the configuration process. The instance name is located in the URL you use to sign in to your OneLogin
account: https://<onelogin-instance-id>.onelogin.com 2 Add IP addresses to the IP access list. In OneLogin, click Authentication , then click VLDAP . Add the following to the Allow access by IP address field to add them to the
IP access list: The IP address of each node in your Atlas cluster. Use nslookup to get the IP address of each host in your cluster,
using hostnames that Atlas generates: nslookup cluster0-shard-00-00-example.mongodb.net Note If the IP addresses of any of your nodes change , you must update the IP access list
with the new IP addresses. ( Optional ) The IP address of a machine you can run ldapsearch commands from to troubleshoot LDAP connection issues . 3 Create a bind user. Create a new OneLogin user to use as the Atlas bind user. The bind user is a OneLogin
user that you use to query the account and to authenticate database
users' credentials when they connect to an Atlas database. The Email and Username fields are required
when you create the bind user. You should enter the same email
address in both of these fields. Important Don't use your own user account for the bind user. Use the following template to determine the full Distinguished Name
(DN) of your bind user: cn=<bind-user-email>,ou=users,dc=<onelogin-instance-id>,dc=onelogin,dc=com For example, if your <bind-user-email> is bind@example.com and
your <onelogin-instance-id> is mdb-example , your bind
user's DN is: cn=bind@example.com,ou=users,dc=mdb-example,dc=onelogin,dc=com 4 Assign privileges to the bind user. In OneLogin , assign the bind user the Manage users , Manage group , or Super user privilege. Note If you grant the bind user the Manage group privilege, you must
select a group. Atlas can only authenticate and authorize LDAP users who belong to this group. Navigate to your OneLogin Users page. Click the bind user. Click Add Privilege . Select the privilege  you want to grant the user, then click Continue . Click Save User . 5 Set the bind user's password in OneLogin . If you have not done so already, set a password for the bind user in OneLogin : Click More Actions , then click Change Password . Enter a password, then click Update . 6 Create database users in OneLogin . If they don't exist already, create users in OneLogin that you want to
grant database access to: Navigate to your OneLogin users page. Click New User . Enter the user's details. The Email and Username fields are required
when you create database users. Enter the same email address in
both of these fields. Note Avoid entering email addresses with plus symbols ( + ). The Atlas LDAP integration may encounter issues with email
addresses containing plus symbols. Click Save User . 7 Set the database users' passwords in OneLogin . If you have not done so already, set a password for each database user
in OneLogin : Navigate to your OneLogin users page. Click the user you want to set a password for. Click More Actions , then click Change Password . Enter a password, then click Update . Configure Atlas for LDAP Authentication The following procedure enables Atlas to authenticate database
users from OneLogin LDAP : 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authentication to On . Note You might incur additional costs when you enable this feature.
See Advanced Security . 3 Enter the server details and bind credentials for all of your LDAP servers in the Configure Your LDAP Server panel. You may list multiple servers separated by commas. You cannot use different ports. 4 Add a User to DN Mapping. Add a User to DN mapping similar to the following example to allow
clients to provide their email addresses instead of full DNs when they
connect to Atlas databases: [ { "match": "(.+)", "substitution": "cn={0},ou=users,dc=<onelogin_instance_id>,dc=onelogin,dc=com" } ] 5 Enter certificates issued from a Certificate Authority (CA) for your LDAP servers, separated by commas, in the CA Root Certificate field. You may provide self-signed certificates. 6 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
servers using the configuration details that you provided. 7 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 8 Add LDAP users to Atlas Note Skip this step if you want to
enable LDAP authorization. Add users managed in the OneLogin LDAP to Atlas . Click Add New Database User . Click LDAP User . Perform one of the following: If you have not entered a User to DN Mapping , enter
the full DN of the LDAP user. Follow this template: cn=<user-name>,ou=users,dc=<onelogin-instance-id>,dc=onelogin,dc=com For example, if your <user-name> is jane@example.com and
your <onelogin-instance-id> is mdb-example , your bind user's
DN is: cn=jane@example.com,ou=users,dc=mdb-example,dc=onelogin,dc=com If you entered a User to DN Mapping ,
enter the username or email address that your mapping requires. Select the database access level to grant to the user. Click Add User . Configure OneLogin for LDAP Authorization Note Skip this section if you don't want to
enable LDAP authorization. The following procedure configures Atlas to authorize users who
belong to OneLogin LDAP database access groups. Important You must enable authentication with LDAP before enabling
authorization. When you enable and configure LDAP authorization, database users
who are only configured for LDAP authentication will no longer
be able to access databases. 1 Create OneLogin database access groups. Atlas LDAP authorization uses LDAP groups to determine if users
are authorized to perform database actions. Create separate OneLogin groups for each level of access that you want
to grant to users. For example,
you create one group for read access to one database, another for read
and write access, and so on. Navigate to your OneLogin groups page. Click New Group . Enter a group name, for example db-read . Click Save . 2 Add OneLogin Users to database access groups. Assign users to groups based on the level of access
each user requires. Navigate to your OneLogin Users page. Click the user you want to add to a group. Click the Authentication tab. Select the group you want to add the user to. Click Save User . Configure Atlas for LDAP Authorization Note Skip this section if you don't want to
enable LDAP authorization. The following procedure adds the OneLogin database access
groups to Atlas and enables database user authorization in Atlas : 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Add the database access LDAP groups to Atlas . Add each of the OneLogin database groups you created to Atlas .
Members of groups that you add are authorized to perform database actions
granted to the group. Click Add New Database User . Click LDAP Group , and then enter the full DN of the
group containing your database users, even if you enabled User to DN Mapping . Follow this template: cn=<group-name>,ou=groups,dc=<onelogin-instance-id>,dc=onelogin,dc=com For example, if your <group-name> is db-read and your <onelogin-instance-id> is mdb-example , your bind user's DN is: cn=db-read,ou=groups,dc=mdb-example,dc=onelogin,dc=com Select the database access level to grant to users in this group. Click Add User . 3 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 4 Toggle the button next to LDAP Authorization to On . 5 Verify the server details and bind credentials for your LDAP server are correct in the Configure Your LDAP Server panel. 6 Enter a query template in Query Template . When a user attempts to perform an action, Atlas executes the LDAP query template to obtain the LDAP groups to which the authenticated user belongs. Atlas permits the action if the query returns at least one group
that is authorized to perform the action. Atlas does not permit
the action if the query returns no groups that are authorized to
perform the action. Atlas substitutes the authenticated username in the {USER} placeholder when it runs the query. The query is relative to the host
specified in Server Hostname . The formatting for the query must conform to RFC4515 and RFC 4516 . Enter the following Query Template : {USER}?memberOf?base Note Other query templates may also work. 7 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
server using the configuration details that you provide. Connect to your Cluster Using mongosh The following procedure verifies that LDAP authentication (and LDAP authorization, if enabled) is configured correctly: Note When LDAP authentication is enabled, database users must override
the following parameters in the connection string for their
clients: authSource must be $external authenticationMechanism must be PLAIN 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Connect to your cluster with the user credentials that you added to Atlas . Use mongosh to connect to your cluster. To copy the connection string: Click Connect . Click LDAP , and then click Copy . Paste and edit the string with your User DN and password. Note Connect to your cluster with a user's full DN if User to DN
Mapping is not enabled. 3 After connecting to your cluster, run commands to verify the user has the read or write privileges you assigned them. Troubleshoot LDAP Connection Issues Note add the host from which you're
running ldapsearch to your IP access list before you
troubleshoot OneLogin connection issues. Use ldapsearch to determine if the query template you
configured Atlas to use returns user DNs the way you expect. The
query template may not be returning the correct user DNs if LDAP authentication works but LDAP authorization doesn't. Use the following ldapsearch template: ldapsearch -H 'ldaps://ldap.us.onelogin.com:636' -D '<bind_user_dn>' -w '<bind_user_pwd>' -b 'dc=<onelogin_instance_id>,dc=onelogin,dc=com' -s sub For example, if your bind-user-dn is cn=jane@example.com,ou=users,dc=mdb-example,dc=onelogin,dc=com and your <onelogin-instance-id> is mdb-example , use the
following command: ldapsearch -H 'ldaps://ldap.us.onelogin.com:636' -D 'cn=jane@example.com,ou=users,dc=mdb-example,dc=onelogin,dc=com' -w '<REDACTED>' -b 'dc=mdb-example,dc=onelogin,dc=com' -s sub Note Other query templates may also work. Back Okta Next OIDC/OAuth2.0
