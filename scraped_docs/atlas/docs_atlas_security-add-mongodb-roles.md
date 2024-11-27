# Configure Custom Database Roles - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication Configure Custom Database Roles On this page Considerations Required Access Add Custom Roles View Custom Roles Modify Custom Roles Delete Custom Roles Assign Custom Roles You can create custom roles in Atlas when the built-in roles don't include your
desired set of privileges. Atlas applies each database user's custom
roles together with: Any built-in roles you
assign when you add a database user or modify a database user . Any specific privileges you
assign when you add a database user or modify a database user . You can assign multiple custom roles to each database user. Note Free Cluster, Shared Cluster, and Serverless Instance Limitation Changes to custom roles might take up to 30 seconds to deploy in M0 Free clusters, M2/M5 Shared clusters, and Serverless instances. The privilege actions available for custom roles and the custom roles API represent a subset of the privilege actions available for built-in roles . To review the list of custom role privileges, see the API reference . Considerations Important You must use the Atlas CLI , Atlas Administration API ,
Atlas UI,
or a supported integration to add, modify, or delete database roles on Atlas clusters. Otherwise, Atlas rolls back any role
modifications. You can assign up to 20 custom roles to a single database user and can create up to 100 custom roles per project. If you require more custom
roles per database user or per project,
contact Atlas support . Atlas audits the creation, deletion, and updates of custom MongoDB
roles in the project's Activity Feed . If you assign multiple roles to a user and those roles grant
conflicting permissions for an object, Atlas honors the highest
permissions within any role. Example You create two custom roles and assign both to User A: The first custom role grants only read privileges on your database.
It also grants bypassDocumentValidation on your database. The second role grants dbAdmin privileges on your database. It
doesn't grant bypassDocumentValidation ,
which is an implicit denial of bypass permissions. User A would have all of the dbAdmin privileges for your database,
since dbAdmin is the higher database access permission. User A would
also have bypassDocumentValidation ,
since bypassDocumentValidation is the higher bypass permission. Required Access To configure custom database roles, you must have Organization Owner or Project Owner access to Atlas . Add Custom Roles Atlas CLI Atlas Administration API Atlas UI To create a custom database role for your project using the
Atlas CLI, run the following command: atlas customDbRoles create <roleName> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas customDbRoles create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To create custom roles through the Atlas Administration API,
see Create One . Follow these steps to create a custom role through the
Atlas UI: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add Custom Role dialog box. Click the Custom Roles tab. Click Add New Custom Role . 3 Enter role information. Field Description Custom Role Name Name of your custom role. IMPORTANT: The specified role name can only contain letters,
numbers, underscores or hyphens. Additionally, you cannot specify a role
name that meets any of the following criteria: Is a name already used by an existing custom role in the
project Is a name of any of the built-in roles Is atlasAdmin Starts with xgen- Action or Role Privileges granted by the role. Click the dropdown to view the
list of available privilege actions and roles . Atlas groups the actions and roles into the following
categories: Collection Actions , Database Actions and Roles , Global Actions and Roles , Custom Roles (if any) Select the action or role from a single category. Once you
select an action or role, Atlas disables the other categories
with the following exception. If you select an action/role
from the Global Actions and Roles , you can still
select actions/roles from Custom Roles . To grant actions and roles from a different category, click Add an action or role to add a new row. Atlas disables actions not available to any cluster
version in your project. Custom roles are defined at the
project level, and must be compatible with each MongoDB
version used by your project's clusters. Database Database on which the selected actions and roles
are granted, if applicable. This field is required for all roles and actions under the Collection Actions and Database Actions and Roles categories. Collection Collection within the specified database on which
the actions and roles are granted, if applicable. This field is required for all roles and actions under Collection Actions . To grant the same set of privileges on multiple databases and
collections, click Add a database or collection . 4 Click Add Custom Role . View Custom Roles Atlas CLI Atlas Administration API Atlas UI To list all custom database roles for your project using the Atlas CLI, run the following command: atlas customDbRoles list [options] To return the details for a single custom database role in the project you specify using the Atlas CLI, run the following command: atlas customDbRoles describe <roleName> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas customDbRoles list and atlas customDbRoles describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view custom roles through the Atlas Administration API,
see Get All . To view your custom roles through the
Atlas UI: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Click the Custom Roles tab. Modify Custom Roles Atlas CLI Atlas Administration API Atlas UI To update a custom database role for your project using the
Atlas CLI, run the following command: atlas customDbRoles update <roleName> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas customDbRoles update . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To modify custom roles through the Atlas Administration API,
see Update One . Follow these steps to modify a custom role through the
Atlas UI: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Modify the custom role. Click the Custom Roles tab. Click Edit next to
the role you want to modify. You can modify the
following components of the role: The actions or roles the custom role inherits. The databases and collections on which those privileges
apply. Click Update Custom Role to save the changes. Delete Custom Roles Atlas CLI Atlas Administration API Atlas UI To delete a custom database role from your project using the
Atlas CLI, run the following command: atlas customDbRoles delete <roleName> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas customDbRoles delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To delete custom roles through the Atlas Administration API,
see Remove One . Follow these steps to delete a custom role through the
Atlas UI: 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Delete the custom role. Click the Custom Roles tab. Click Delete next to the
role you want to delete. Click Delete in the dialog box to confirm
deletion. You cannot delete a custom role in the following scenarios: When deleting the role would leave one or more child roles with no
parent roles or actions. When deleting the role would leave one or more database users with no roles. Assign Custom Roles You can assign custom roles in the Atlas UI when you add a
database
user or modify a database user . To assign custom roles through the
Atlas Administration API, see Create a Database User or Update a
Database User . Back Built-In Roles and Privileges Next AWS IAM
