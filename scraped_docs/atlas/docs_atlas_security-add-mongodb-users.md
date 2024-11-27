# Configure Database Users - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication Configure Database Users On this page In Atlas , go to the Project Activity Feed page. Database User Authentication Required Access Add Database Users View Database Users and Certificates Modify Database Users Delete Database Users Create database users to provide clients access to the clusters in your
project. A database user's access is determined by the roles assigned
to the user. When you create a database user, any of the built-in roles add the user to all clusters in your Atlas project. You can remove the
default built-in role and set specific privileges and custom roles to add the user to specific clusters. Database users are separate from Atlas users. Database users have
access to MongoDB databases, while Atlas users have access to the Atlas application itself. Atlas supports creating temporary
database users that automatically expire within a user-configurable
7-day period. Atlas audits the creation, deletion, and updates of database users
in the project's Activity Feed. Atlas audits actions pertaining to
both temporary and non-temporary database users. To view the project's Activity Feed: 1 In Atlas , go to the Project Activity Feed page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Click the Project Activity Feed icon in the right
side of the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Activity Feed in the sidebar. The Project Activity Feed page displays. For more information on the project Activity Feed, see View All Activity . Atlas supports a maximum of 100 database users per Atlas project by default. If you require more than 100 database users on a
project, you can use the Atlas Administration API to increase the limit. For assistance, contact Atlas support . Important You must use the Atlas CLI , Atlas Administration API ,
Atlas UI, or a supported integration to add, modify, or delete database users on Atlas clusters. Otherwise, Atlas rolls back
any user modifications. Database User Authentication Atlas offers the following forms of authentication for database users: Password X.509 Certificates AWS IAM LDAP OIDC SCRAM is MongoDB's
default authentication method. SCRAM requires a password for
each user. The authentication database for
SCRAM-authenticated users is the admin database. Note By default, Atlas supports SCRAM-SHA-256 authentication.
If you have any database users created before the release of
MongoDB 4.0, update their passwords to generate SCRAM-SHA-256
credentials. You may reuse existing passwords. X.509 Certificates , also known
as mutual TLS or mTLS, allow passwordless authentication by using
a trusted certificate. The authentication database for
X.509-authenticated users is the $external database. If you enable LDAP authorization , you can't connect to your
clusters with users that authenticate with an Atlas -managed X.509 certificate. To enable LDAP and
connecting to your clusters with X.509 users, see Set Up Self-Managed X.509 Authentication . You can create a database user which uses an AWS IAM User or Role ARN for authentication. The authentication database for
AWS IAM-authenticated users is the $external database. AWS IAM authentication is available only on clusters which use MongoDB
version 5.0 and higher. Note Starting with MongoDB 8.0, LDAP authentication and authorization is
deprecated. The feature is available and will continue to operate
without changes throughout the lifetime of MongoDB 8. LDAP will be
removed in a future major release. For details, see LDAP Deprecation . You can create a database user that uses LDAP for authentication. The authentication database for LDAP -authenticated users is the $external database. If you enable LDAP authorization , you
can't connect to your clusters with users that authenticate with an Atlas -managed X.509 certificate. To enable LDAP and
connecting to your clusters with X.509 users, see Set Up Self-Managed X.509 Authentication . You can create a database user that uses OIDC for authentication. The authentication database for OIDC -authenticated users is the $external database. OIDC authentication is available only on clusters that use MongoDB
version 7.0 and higher. Required Access To add database users, you must have Organization Owner or Project Owner access to Atlas . Add Database Users A project can have users with different authentication methods. You cannot change a user's authentication method after creating that
user. To use an alternative authentication method, you must create a
new user. Atlas CLI Atlas Administration API Atlas UI The Atlas CLI uses the following commands to create new database users and X.509 certificates. The options you specify determine the authentication method. To create a database user for your project using the Atlas CLI, run the following command: atlas dbusers create [builtInRole]... [options] To create a new Atlas-managed X.509 certificate for the specified database user using the Atlas CLI, run the following command: atlas dbusers certs create [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas dbusers create and atlas dbusers certs create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI You can add database users through the Atlas Administration API. The
options you specify determine the authentication method. To learn
more, see Create One Database User . Select an authentication mechanism and follow the steps to create
a new database user using the Atlas UI. Password Authentication X.509 Certificates AWS IAM OIDC LDAP 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add New Database User dialog box. If it isn't already displayed, click the Database Users tab. Click Add New Database User . 3 Select Password . In the Authentication Method section of the Add
New Database User modal window, select the box labeled Password . 4 Enter user information. Under Password Authentication , there are two text fields. Enter a username for the new user in the top text field. Enter a password for the new user in the lower text field. To use a password auto-generated by Atlas ,
click the Autogenerate Secure Password button. 5 Assign privileges. Select the database user privileges. You can assign privileges to the new user
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
Roles in the MongoDB manual. 6 Specify the resources in the project that the user can access. By default, users can access all the clusters and federated database instances in the
project. You can restrict access to specific clusters and federated database instances
by doing the following: Toggle Restrict Access to Specific Clusters/Federated
Database Instances to ON . Select the clusters and federated database instances to grant the user access to
from the Grant Access To list. 7 Save as temporary user. Toggle Temporary User to On and choose
a time after which Atlas can delete the user from the Temporary User Duration dropdown. You can select one of the
following time periods for the user to exist: 6 hours 1 day 1 week In the Database Users tab, temporary users display
the time remaining until Atlas will delete the user. Once Atlas deletes the user, any client or application that uses
the temporary user's credentials loses access to the cluster. 8 Click Add User . 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add New Database User dialog box. If it isn't already displayed, click the Database Users tab. Click Add New Database User . 3 Select Certificate . In the Authentication Method section of the Add
New Database User modal window, select the box marked Certificate . 4 Enter user information. Enter a username for the new user in the Common Name text
field. (Optional) If you would like to download an Atlas-managed certificate
after the new user is created, toggle the Download certificate
when user is added switch to On . Note To download the certificate upon saving, you must provide a
certificate expiration date. (Optional) Select a certificate expiration period. X.509 certificates expire and are invalid after the
certificate expiration date you set. A user cannot
log in with an expired X.509 certificate and must be issued
a new certificate. To help manage this, Atlas automatically creates a
project-level alert when you create a new user with X.509
authentication enabled. This alert sends a notification 30 days
before that user's latest certificate expires, repeating every
24 hours. You can view and edit this alert from Atlas 's Alert Settings page. For more information on
configuring alerts, see Configure Alert Settings . Important If a user loses their certificate, they will need a new
certificate before they can log in again. Important You cannot revoke X.509 certificates. To revoke an X.509
certificate-authenticated user's access to your project,
you must delete that user. If you prefer to manage your own X.509 certificates, you
can upload a PEM-encoded certificate authority through Self-Managed X.509 Certificates . 5 Assign privileges. Select the database user privileges. You can assign privileges to the new user
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
Roles in the MongoDB manual. 6 Specify the resources in the project that the user can access.
By default, users can access all the clusters and federated database instances in the
project. You can restrict access to specific clusters and federated database instances
by doing the following: Toggle Restrict Access to Specific Clusters/Federated
Database Instances to ON . Select the clusters and federated database instances to grant the user access to
from the Grant Access To list. 7 Click Add User . Note AWS IAM authentication is available only on clusters which use
MongoDB version 5.0 and higher. 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add New Database User dialog box. If it isn't already displayed, click the Database Users tab. Click Add New Database User . 3 Select AWS IAM . In the Authentication Method section of the Add
New Database User modal window, select the box marked AWS IAM . 4 Enter user information. Select a user type from the AWS IAM Type dropdown menu. Enter an AWS user ARN . Click the See instruction below link for help with finding your ARN. 5 Assign privileges. Select the database user privileges. You can assign privileges to the new user
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
Roles in the MongoDB manual. 6 Specify the resources in the project that the user can access. By default, users can access all the clusters and federated database instances in the
project. You can restrict access to specific clusters and federated database instances
by doing the following: Toggle Restrict Access to Specific Clusters/Federated
Database Instances to ON . Select the clusters and federated database instances to grant the user access to
from the Grant Access To list. 7 Save as temporary user. Toggle Temporary User to On and choose
a time after which Atlas can delete the user from the Temporary User Duration dropdown. You can select one of the
following time periods for the user to exist: 6 hours 1 day 1 week In the Database Users tab, temporary users display
the time remaining until Atlas will delete the user. Once Atlas deletes the user, any client or application that uses
the temporary user's credentials loses access to the cluster. 8 Click Add User . AWS IAM Connection String Example Connecting to Atlas using AWS IAM authentication with the mongosh requires shell version v0.9.0 or higher. Use your AWS IAM credentials ,
using your access key ID as your username and your secret key as your
password. The authSource query parameter is $external , URL-encoded as %24external . The authMechanism query parameter is MONGODB-AWS . Example mongosh "mongodb+srv://<atlas-host-name>/test?authSource=%24external&authMechanism=MONGODB-AWS" --username <access-key-id> --password <secret-key> 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add New Database User or Group dialog box. Click Add New Database User or Group . Note Until you apply your Workforce IdP to Atlas , this button says Add New Database User . 3 Select Federated Auth . In the Authentication Method section, select Federated Auth . Note Until you enable Workforce IdP for your organization ,
you can't select this box. 4 Select Identity Provider and Identifier a. In the Select Identity Provider section, select a configured OIDC Identity Provider . Specify either the user identifier or group identifier associated with
your configured Workforce Identity Provider . Note For Azure Entra ID users, this value maps to the Object Id of your
Azure user group rather than user group name. 5 Assign user or group privileges. To assign privileges to the new user or group, do one or more of the
following tasks: Select a built-in role from the Built-in Role dropdown menu. You can select one built-in role per database group in the Atlas UI. If you delete the default option, you can click Add Built-in Role to select a new built-in role. Select or add custom roles . If you have any custom roles defined, you can expand
the Custom Roles section and select
one or more roles from the Custom Roles dropdown menu. Click Add Custom Role to add more custom roles. Click the Custom Roles link to see the custom
roles for your project. Add privileges . Expand the Specific Privileges section and select one or more
privileges from the Specific Privileges dropdown menu. Click Add Specific Privilege to add more privileges. This assigns
the group specific privileges on individual databases and collections. Remove an applied role or privilege. Click Delete next to the role or privilege to delete. Note Atlas doesn't display the Delete icon
next to your Built-in Role , Custom Role , or Specific Privilege selection if you selected only one option. You
can delete the selected role or privilege once you apply another role or privilege. Atlas can apply a built-in role, multiple custom roles, and multiple specific
privileges to a database group. To learn more about authorization, see Role-Based
Access Control and Built-in
Roles in the MongoDB manual. 6 Specify the resources in the project that the user or group can access. By default, groups can access all the clusters and federated database instances in the
project. To restrict access to specific clusters and federated database instances: Toggle Restrict Access to Specific Clusters/Federated
Database Instances to On . Select the clusters and federated database instances to grant the group access to
from the Grant Access To list. 7 Save as a temporary user or group. Toggle Temporary User or Temporary Group to On and choose a time after which Atlas can delete the user
or group from the Temporary User Duration or Temporary Group Duration dropdown. You can select one of the
following time periods for the group to exist: 6 hours 1 day 1 week In the Database Users tab, temporary users or groups display
the time remaining until Atlas deletes the users or group. After Atlas deletes the user or group, any client or application that uses
the temporary user's or group's credentials loses access to the cluster. 8 Add the new database user or group. Do one of the following steps: If you added a user, click the Add User button. If you added a group, click the Add Group button. Note Starting with MongoDB 8.0, LDAP authentication and authorization is
deprecated. The feature is available and will continue to operate
without changes throughout the lifetime of MongoDB 8. LDAP will be
removed in a future major release. For details, see LDAP Deprecation . Follow the steps to Configure Authentication with LDAP , then follow the
steps to Add an LDAP Database User or Group . View Database Users and Certificates Atlas CLI Atlas Administration API Atlas UI View Database Users To list all Atlas database users for your project using the Atlas CLI, run the following command: atlas dbusers list [options] To return the details for a single Atlas database user in the project you specify using the Atlas CLI, run the following command: atlas dbusers describe <username> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas dbusers list and atlas dbusers describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI View X.509 Certificates for a Database User To list all Atlas-managed, unexpired certificates for a database user using the
Atlas CLI, run the following command: atlas dbusers certs list <username> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dbusers certs list . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view Atlas database users using the
Atlas Administration API, see Get All . To view Atlas database users and X.509 certificates in the
Atlas UI: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 View Atlas database users. If it's not already displayed, click the Database Users tab. Click Edit for the user
to view their privileges, authentication details, and
X.509 certificates. Modify Database Users Atlas CLI Atlas Administration API Atlas UI To update a database user from your project using the
Atlas CLI, run the following command: atlas dbusers update <username> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dbusers update . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI You can update database users through the Atlas Administration API. To
learn more, see Update One . To modify existing users for an Atlas project: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Modify an existing user. If it's not already displayed, click the Database Users tab. Click Edit for the user you
want to modify. You can modify the privileges and authentication details
assigned to the user. You cannot modify the authentication
method. The following table describes what you can do for each user: User Type Action SCRAM authenticated users Edit a user's password. X.509 certificate authenticated users Download a new certificate. AWS IAM users Modify database access privileges. Temporary users Modify the time period the user exists or make the
user a permanent user, provided the user's expiration
date has not already passed. Note You cannot change a permanent user into a temporary user.
If you change a temporary user into a permanent user, you
cannot make it temporary again. Click Update User to save the changes. Delete Database Users Atlas CLI Atlas Administration API Atlas UI To delete a database user from your project using the
Atlas CLI, run the following command: atlas dbusers delete <username> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas dbusers delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI You can delete database users through the Atlas Administration API. To
learn more, see Delete One . To delete existing users for an Atlas project using the
Atlas UI: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Delete an existing user. If it's not already displayed, click the Database Users tab. Click Delete next to
the user you want to delete. Click Delete again to confirm. Back Authentication Next Built-In Roles and Privileges
