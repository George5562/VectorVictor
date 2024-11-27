# Manage Project Access - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization Manage Project Access On this page Create a Project View Projects Move a Project Delete a Project Groups are now projects in the organizations and projects hierarchy. You can create multiple projects in an organization. By having multiple projects within an organization, you can: Isolate different environments (for instance, development/qa/prod
environments) from each other. Associate different users or teams with different environments, or
give different permissions to users in different environments. Maintain separate cluster security configurations. For example: Create/manage different sets of database user credentials for
each project. Isolate networks in different VPCs. Create different alert settings. For example, configure alerts for
Production environments differently than Development environments. Create a Project Prerequisites To create a project for an organization, you must be either an Organization Owner or an Organization Project Creator . When you create a project, you are added as an Project Owner for the project. Procedure Atlas CLI Atlas Administration API Atlas UI To create a new project using the
Atlas CLI, run the following command: atlas projects create <projectName> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas projects create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To create a project for an organization using the API, see Create One Project . To create a project for an organization using the Atlas UI: 1 In Atlas , go to the Projects page for your organization. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Click the Leaf icon in the upper left corner of the
page. Click the Organization Settings icon next to the Organizations menu, then click Projects in the sidebar. Expand the Projects menu in the navigation bar,
then click View All Projects . The Projects page displays. 2 Go to the Create a Project page. Do one of the following steps: Click New Project . Expand the Projects menu in the navigation
bar, then click + New Project . 3 Name your new project. Enter the name for your new project. Important The project name has the following limits: Can't exceed 64 characters. Restricted to letters, numbers, spaces, dashes, and
underscores. Don't include sensitive information in
your project name. Click Next . 4 Add members. For existing Atlas users, enter their username. Usually, this
is the email the person used to register. For new Atlas users, enter their email address to send an
invitation. 5 Specify the access for the members. 6 Click Create Project . View Projects Prerequisites To view a project, you must either: Be an Organization Owner or Project Owner Receive an invitation that grants access to
the project. An Organization Owner or Project Owner can invite users to projects. Important Project Invitation Deprecation The Atlas release on September 13, 2023 deprecates project
invitations. When you invite an organization member to projects within the
organization, the user is automatically granted access to
those projects and doesn't receive any invitations. When you invite a
user to projects in an organization that the user doesn't belong to,
the user receives a single invitation to the organization, which
includes access to all of the projects that you grant them access to.
Invitations expire after 30 days. Procedure Atlas CLI Atlas Administration API Atlas UI To list all projects using the Atlas CLI, run the following command: atlas projects list [options] To return the details for the project you specify using the Atlas CLI, run the following command: atlas projects describe <ID> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas projects list and atlas projects describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view a project using the API, see Return One Project or Return One Project using Its Name . To view projects in the Atlas UI: 1 In Atlas , go to the Projects page for your organization. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Click the Leaf icon in the upper left corner of the
page. Click the Organization Settings icon next to the Organizations menu, then click Projects in the sidebar. Expand the Projects menu in the navigation bar,
then click View All Projects . The Projects page displays. A Backup Compliance Policy icon appears next to each project name that has a Backup Compliance Policy enabled . Move a Project When you move a project to another Atlas organization, Atlas copies the project users and their respective roles to the
same project in the destination organization. However, Atlas doesn't carryover teams assigned to the project because you define
teams at the organization level. When you move projects across organizations, your changes take effect
immediately. The move doesn't: Impact cluster uptime or current cluster configuration. Cause downtime for your cluster or changes to your
connection string. Important Atlas removes existing API Keys after moving the project. You
must create a new API Key after moving the project. Atlas does not migrate any existing App Services applications
to the project in the new organization. After you move the project,
your applications remain, but certain services such
as Triggers and Device Sync might not be supported.
To use your applications again, you must copy the application's configuration files and port them to the new project. Prerequisites To move a project to another Atlas organization, you must be an Organization Owner for both the current and the destination
organization. Procedure To move a project for an organization: 1 In Atlas , go to the Projects page for your organization. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Click the Leaf icon in the upper left corner of the
page. Click the Organization Settings icon next to the Organizations menu, then click Projects in the sidebar. Expand the Projects menu in the navigation bar,
then click View All Projects . The Projects page displays. 2 Select the project you want to move. For the project you want to move: Click . Click Move Project . The Move Project dialog box appears. 3 Select the target organization. Click Next: Confirm to go to the confirmation screen. 4 Click Confirm & Move . Note Billing a Moved Project An Organization Owner of two different Organizations
can move projects between those Organizations at any time. Usage in
any particular project during any particular hour is accrued to the
Organization under which the project was at that time. For example, an Organization Owner owns the Telecomm and Storage Organizations in Atlas . They decide to move
their Backup project from Telecomm to Storage at
11:40 am. The Telecomm project is billed for the full 11:00 to 11:59
am hour. Storage starts getting billed at 12:00 pm. Delete a Project Note If you have a Backup Compliance Policy enabled , you
can't delete the project if any snashots exist. Prerequisites To delete a project for an organization, you must either have the Project Owner role for the project or have the Organization Owner role for the project's organization. You must terminate any Atlas Services apps and/or MongoDB Charts instances. The project has no outstanding invoices. The project has no active clusters. Terminate active clusters or Serverless instances in the project
before you delete it. The project has no configured private endpoint connections . The project has no active federated database instances . Procedure Atlas CLI Atlas Administration API Atlas UI To delete a project using the
Atlas CLI, run the following command: atlas projects delete <ID> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas projects delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To delete a project for an organization using the API, see Remove One Project . To delete a project for an organization using the Atlas UI,
you can delete from the organization's Projects view
or the project's Project Setting view. To delete a project from the organization's Projects view: 1 In Atlas , go to the Projects page for your organization. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Click the Leaf icon in the upper left corner of the
page. Click the Organization Settings icon next to the Organizations menu, then click Projects in the sidebar. Expand the Projects menu in the navigation bar,
then click View All Projects . The Projects page displays. 2 For the project you want to delete, click . 3 Click Delete Project . 4 If Manage Your Multi-Factor Authentication Options is enabled, enter the verification code. After verifying, click Delete Project again. To delete from the project's Project Setting view: 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 In the Delete Project section, click Delete . 3 Click Delete Project to confirm. 4 If Manage Your Multi-Factor Authentication Options is enabled, enter the verification code. After verifying, click Delete Project again. Back Settings Next Projects
