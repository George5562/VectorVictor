# Set Up User Authentication and Authorization with LDAP - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication Set Up User Authentication and Authorization with LDAP On this page Required Access Prerequisites Recommendation Considerations Conflicts between LDAP Authorization and X.509 Users Usernames Connection String Rolling Restart on Configuration Change Using Public IP Addresses Limitations Procedures Configure Authentication with LDAP Configure Authorization Add an LDAP Database User or Group View LDAP Configuration Disable LDAP Configuration Tutorials for Third-Party LDAP Providers Note Starting with MongoDB 8.0, LDAP authentication and authorization is
deprecated. The feature is available and will continue to operate
without changes throughout the lifetime of MongoDB 8. LDAP will be
removed in a future major release. For details, see LDAP Deprecation . Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Atlas provides the ability to manage user authentication and
authorization from all MongoDB clients using your own Lightweight
Directory Access Protocol ( LDAP ) server over TLS . A single LDAPS ( LDAP over TLS ) configuration applies to all clusters in a project. If you enable user authorization with LDAP , you can create LDAP groups on the admin database by mapping LDAP groups to MongoDB
roles on your Atlas databases. To use LDAP groups effectively, create additional projects within Atlas to control access to specific deployments in your
organization, such as creating separate Atlas projects for
development and production environments. You can then map an LDAP group to a role in the Atlas project to provide access to the
desired deployment. Note When you enable user authorization and an LDAP user doesn't belong
to any LDAP group, Atlas doesn't assign any database roles to
the user. When you enable user authentication and you disable user
authorization, Atlas assigns MongoDB database roles to the LDAP user. If you have multiple departments with their own billing needs, alert
settings, and project members, consider creating a new set of projects or a new organization for each department or business unit. Note An explanation of LDAP is out of scope for the MongoDB
documentation. Please review RFC 4515 and RFC 4516 or refer to your preferred LDAP documentation. Required Access To manage LDAP users or groups, you must have Organization Owner or Project Owner access to Atlas . Prerequisites You must meet the following prerequisites to manage user authentication
and authorization using LDAP in Atlas : Atlas cluster using MongoDB 4.0 or later. LDAP server using TLS that your Atlas clusters can access
over the network using either VPC or
VNet peering connection or the cluster nodes' public IP addresses. LDAP group memberships embedded as an attribute for each user in
the LDAP entry for user authorization only. Recommendation For your LDAPS service to access Atlas clusters, MongoDB
recommends one of two configurations: Using a VPC or VNet: Run your LDAP server in a VPC or VNet. Establish a peering connection to your Atlas project. Use a public FQDN that resolves to the private IP address
of your LDAP server. Using your data center: Run your LDAP server with a public FQDN that resolves to a
public IP address. Configure the LDAP server to allow inbound access from the Atlas cluster nodes' public IP addresses. Considerations Conflicts between LDAP Authorization and X.509 Users If you enable LDAP authorization, you can't connect to your
clusters with users that authenticate with an Atlas -managed X.509 certificate. After you enable LDAP authorization, you can connect to your
clusters with users that authenticate with an self-managed X.509 certificate . However,
the user's Common Name in their X.509 certificate must match the
Distinguished Name of a user who is authorized to access your
database with LDAP. Usernames Atlas uses the full Distinguished Name (DN) of users in your LDAP server as the Atlas username. For example, an example LDAP user
named ralph has the following username in Atlas : cn=ralph,cn=Users,dc=aws-atlas-ldap-01,dc=myteam,dc=com Connection String If the administrator enables user authentication or both user
authentication and authorization with LDAP , database users must
override the following parameters in the connection string for their
clients. authSource must be $external authenticationMechanism must be PLAIN Example The following connection string for mongosh authenticates an LDAP user named rob : mongosh "mongodb+srv://cluster0-tijis.mongodb.net/test?authSource=%24external" \ --authenticationMechanism PLAIN \ --username cn=rob,cn=Users,dc=ldaps-01,dc=myteam,dc=com To copy the connection string: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Locate the connection string. Click Connect . 3 Edit the connection string. Edit the string with your User DN and password. Note If your passwords, database names, or connection strings contain
reserved URI characters, you must escape the characters. For example,
if your password is @bc123 , you must escape the @ character when specifying the password in the connection
string, such as %40bc123 . To learn more, see Special Characters in Connection String Password . Rolling Restart on Configuration Change If you change your LDAP configuration, Atlas performs a rolling
restart of your cluster. This restart allows Atlas to use the
correct settings to authenticate users. Using Public IP Addresses You can use public IP addresses that refer to other internal or private
IP addresses using Network Address Translation to allow Atlas traffic to your LDAP server. If you do this, be aware that certain activities trigger a change
in the Atlas cluster's public IP addresses. If you allowed LDAP server access based on public IP addresses,
changes to the Atlas cluster's public IP address prevent LDAP access. To restore LDAP access, add the new Atlas cluster public
IP addresses to the LDAP access list. Limitations You cannot use both LDAP and SCRAM authentication for the same
database user. Procedures Configure Authentication with LDAP Atlas CLI Atlas UI Note You can use the same Atlas CLI command to configure LDAP authentication and LDAP authorization. To save one LDAP configuration for the project you specify using the
Atlas CLI, run the following command: atlas security ldap save [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas security ldap save . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Use the following procedure to configure user authentication with LDAP for all clusters in a project. 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authentication to On . Note You might incur additional costs when you enable this feature.
See Advanced Security . 3 Enter the server details and bind credentials for all of your LDAP servers in the Configure Your LDAP Server panel. You may list multiple servers separated by commas. You cannot use different ports. 4 Enter certificates issued from a Certificate Authority (CA) for your LDAP servers, separated by commas, in the CA Root Certificate field. You may provide self-signed certificates. 5 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
servers using the configuration details that you provided. Configure Authorization Atlas CLI Atlas UI Note You can use the same Atlas CLI command to configure LDAP authentication and LDAP authorization. To save one LDAP configuration for the project you specify using the
Atlas CLI, run the following command: atlas security ldap save [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas security ldap save . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Use the following procedure to configure user authorization with LDAP for all clusters in a project. Important You must enable authentication with LDAP before enabling
authorization. When you enable and configure LDAP authorization, database users
who are only configured for LDAP authentication will no longer
be able to access databases. 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authorization to On . 3 Enter the server details and bind credentials for your LDAP server in the Configure Your LDAP Server panel. 4 Enter a query template in Query Template . When a user attempts to perform an action, Atlas executes the LDAP query template to obtain the LDAP groups to which the authenticated user belongs. Atlas permits the action if the query returns at least one group
that is authorized to perform the action. Atlas does not permit
the action if the query returns no groups that are authorized to
perform the action. Atlas substitutes the authenticated username in the {USER} placeholder when it runs the query. The query is relative to the host
specified in Server Hostname . The formatting for the query must conform to RFC4515 . If you do not provide a query template, Atlas applies the default
value: {USER}?memberOf?base . 5 Click Verify and Save . Wait for Atlas to deploy your changes. Atlas verifies that
your clusters can connect to, authenticate with, and query your LDAP
server using the configuration details that you provide. Add an LDAP Database User or Group Atlas CLI Atlas UI To create a database user for your project using the
Atlas CLI, run the following command: atlas dbusers create [builtInRole]... [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dbusers create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI After you configure authorization with LDAP , follow these steps to create an LDAP
database user or group: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add New Database User dialog box. If it isn't already displayed, click the Database Users tab. Click Add New Database User . 3 Select LDAP . In the Authentication Method section of the Add
New Database User modal window, select the box labeled LDAP . Note If you don't see an LDAP option, you must configure authorization with LDAP . 4 Select the LDAP type. Under LDAP Type , select LDAP User for a single
user or LDAP Group for an LDAP group. 5 Enter LDAP authentication string. Enter the authentication string for the LDAP user or LDAP group. Example For the LDAP user named myUser in the project named projectName,
enter the following: cn=myUser,ou=projectName,dc=com If you enable LDAP authorization, you can create LDAP users, but they
can't access your clusters. Add an LDAP group to access
clusters with LDAP authorization enabled. 6 Assign privileges. Select the database user privileges. You can assign privileges to the new user
in one or more of the following ways: Select a built-in role from the Built-in Role dropdown menu. You can select one
built-in role per database user within the Atlas UI. If you delete the
default option, you can click Add Built-in Role to select a new built-in role. If you have any custom roles defined, you can expand
the Custom Roles section and select
one or more roles from the Custom Roles dropdown menu. Click Add Custom Role to add more custom roles. You can also
click the Custom Roles link to see the custom
roles for your project. Expand the Specific Privileges section and select one or more privileges from the Specific Privileges dropdown menu. Click Add Specific Privilege to add more privileges. This assigns the
user specific privileges on individual databases and collections. Atlas can apply a built-in role, multiple custom roles, and multiple specific
privileges to a single database user. To remove an applied role or privilege, click Delete next to the role or privilege you wish to delete. Note Atlas doesn't display the Delete icon
next to your Built-in Role , Custom Role , or Specific Privilege selection if you selected only one option. You
can delete the selected role or privilege once you apply another role or privilege. For more information on authorization, see Role-Based
Access Control and Built-in
Roles in the MongoDB manual. 7 Specify the resources in the project that the user can access. By default, users can access all the clusters and federated database instances in the
project. You can restrict access to specific clusters and federated database instances
by doing the following: Toggle Restrict Access to Specific Clusters/Federated
Database Instances to ON . Select the clusters and federated database instances to grant the user access to
from the Grant Access To list. 8 Save as a temporary user or temporary group. Toggle Temporary User or Temporary Group to On . Choose a time after which Atlas can delete the
user or group from the Temporary User Duration or Temporary Group Duration dropdown. You can select one
of the following time periods for the user or group to exist: 6 hours 1 day 1 week In the Database Users tab, temporary users and groups
display the time remaining until Atlas will delete the user or
group. Once Atlas deletes the user or group, any client or
application that uses the temporary user's or group's credentials
loses access to the cluster. 9 Click Add User or Add Group . View LDAP Configuration Atlas CLI Atlas UI To return the details for one LDAP configuration using the
Atlas CLI, run the following command: atlas security ldap get [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas security ldap get . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view your current LDAP settings using the Atlas UI: 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authentication to On . Atlas displays your LDAP authentication settings. To view your LDAP authorization settings, toggle the button next to LDAP Authorization to On . Atlas displays your LDAP authorization settings. Disable LDAP Configuration Atlas CLI Atlas UI Note You can use the same Atlas CLI command to disable LDAP authentication settings and LDAP authorization settings. To delete one LDAP configuration using the
Atlas CLI, run the following command: atlas security ldap delete [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas security ldap delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To disable your current LDAP settings using the Atlas UI: 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to LDAP Authentication to OFF . Atlas disables your LDAP authentication settings and your LDAP authorization settings. To disable LDAP authorization only, toggle the button next to LDAP Authorization to OFF . Atlas disables your LDAP authorization settings. Tutorials for Third-Party LDAP Providers Use the following tutorials to configure Atlas to authenticate and
authorize users from third-party LDAP providers: Configure User Authentication and Authorization with Microsoft Entra ID Domain Services Configure User Authentication and Authorization with Okta LDAP Interface Configure User Authentication and Authorization with OneLogin VLDAP Back AWS IAM Next Microsoft Entra ID DS
