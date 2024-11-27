# Manage Access to a Project - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Project Access Manage Access to a Project On this page Required Access Add Users or Teams to a Project View Who Can Access a Project View User Invitations Cancel or Update User Invitations Remove Users or Teams from a Project Edit a User's or Team's Role in a Project Important Project Invitation Deprecation The Atlas release on September 13, 2023 deprecates project
invitations. When you invite an organization member to projects within the
organization, the user is automatically granted access to
those projects and doesn't receive any invitations. When you invite a
user to projects in an organization that the user doesn't belong to,
the user receives a single invitation to the organization, which
includes access to all of the projects that you grant them access to.
Invitations expire after 30 days. You can grant Atlas users and teams access to Atlas projects.
Assign user roles to enforce permission
levels for Atlas users and teams. Required Access To perform any of the following actions, you must have Project Owner access to Atlas . Add Users or Teams to a Project Important Adding a user to a project also adds that user to the organization. Atlas limits the number of teams to a maximum of: 100 teams per project and 250 teams per organization. Atlas also limits Atlas user membership to a maximum of: 500 per project and 500 per organization, which includes the combined membership of all
projects in the organization. Atlas raises an error if an operation exceeds these limits. For example, if you have an organization with five projects,
such that each project has 100 Atlas users and each user
belongs to only one project, you cannot add any Atlas users to this organization or any project in that organization
without first removing existing Atlas users from the
organization or project membership. To invite a user or team to a project using the Atlas UI: 1 In Atlas , go to the Project Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Select Project Access from the Access Manager menu in the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Access Manager in the sidebar. The Project Access Manager page displays. 2 Click the Users or Teams tab. 3 Click Invite to Project . 4 Add an Atlas user or team. Enter the new user's
email address or Jira username, or an existing team name. If the console finds a connected Jira account, Atlas invites the user to the Atlas project. If the user accepts
the invite, that user is added to the corresponding Jira group. If you want to grant access to a new team, you must first create the team . Press Enter or click on the email
address, Jira username, or team name. Repeat for any additional users or teams. 5 Select roles for the new user or team. By default, each user is given the Project Read Only role. To change or add additional roles for each user or
team, click on the role dropdown menu, then select the checkboxes for
each role you want the user or team to
have in the project. All team members share the roles assigned to the team on this
project. 6 Click Grant Access . Atlas sends an email to the selected users inviting them to join
the project. Invited users do not have access to the project until
they accept the invitation. Invitations expire after 30 days. View Who Can Access a Project Atlas CLI Atlas UI To list all users in the project you specify using the Atlas CLI, run the following command: atlas projects users list [options] To list all teams for a project using the Atlas CLI, run the following command: atlas projects teams list [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas projects users list and atlas projects teams list . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view which users, teams, or API Keys can access a project
using the Atlas UI: 1 In Atlas , go to the Project Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Select Project Access from the Access Manager menu in the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Access Manager in the sidebar. The Project Access Manager page displays. 2 Click the Users , Teams , or API Keys tab. Each tab lists the project's Atlas users, teams, or API Keys
along with their project roles and actions you can take on that user,
team, or API Key. View User Invitations Important Project Invitation Deprecation The Atlas release on September 13, 2023 deprecates project
invitations. When you invite an organization member to projects within the
organization, the user is automatically granted access to
those projects and doesn't receive any invitations. When you invite a
user to projects in an organization that the user doesn't belong to,
the user receives a single invitation to the organization, which
includes access to all of the projects that you grant them access to.
Invitations expire after 30 days. To view user invitations using the Atlas UI: 1 In Atlas , go to the Project Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Select Project Access from the Access Manager menu in the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Access Manager in the sidebar. The Project Access Manager page displays. 2 Click the Users , Teams , or API Keys tab. Each tab lists the project's Atlas users, teams, or API Keys
along with their project roles and actions you can take on that user,
team, or API Key. The Users tab lists any outstanding invitations to
users to join the project and any requests from users who want to join the project. A user can request to join a project when they
first register for Atlas . Individual users are ordered by status. They appear in the
following sequence: Users currently in your project. Users with pending invitations to join your project. Users requesting to join your project. Atlas displays the Name of
users who have not accepted their invitation as Pending User and their role as --invite sent-- . Cancel or Update User Invitations Important Project Invitation Deprecation The Atlas release on September 13, 2023 deprecates project
invitations. When you invite an organization member to projects within the
organization, the user is automatically granted access to
those projects and doesn't receive any invitations. When you invite a
user to projects in an organization that the user doesn't belong to,
the user receives a single invitation to the organization, which
includes access to all of the projects that you grant them access to.
Invitations expire after 30 days. To cancel a user invitation using the Atlas UI: 1 In Atlas , go to the Project Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Select Project Access from the Access Manager menu in the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Access Manager in the sidebar. The Project Access Manager page displays. 2 Click the Users , Teams , or API Keys tab. Each tab lists the project's Atlas users, teams, or API Keys
along with their project roles and actions you can take on that user,
team, or API Key. The Users tab lists any outstanding invitations to
users to join the project and any requests from users who want to join the project. To cancel an invitation, click to the right of the user's name on the Users tab. Remove Users or Teams from a Project Atlas CLI Atlas UI To delete a user from a project using the Atlas CLI, run the following command: atlas projects users delete <ID> [options] To remove a team from the project you specify using the Atlas CLI, run the following command: atlas projects teams delete <teamId> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas projects users delete and atlas projects teams delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To remove a user or team from a project using the Atlas UI: 1 In Atlas , go to the Project Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Select Project Access from the Access Manager menu in the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Access Manager in the sidebar. The Project Access Manager page displays. 2 Click the Users or Teams tab. 3 Remove the Atlas user or team. Click to the right of the Atlas user or
team you want to remove. 4 Confirm the removal. To confirm an Atlas user removal, click Remove User . To confirm a team removal, click Delete Team . To keep the Atlas user or team in the project, click Cancel . Edit a User's or Team's Role in a Project Note You can't edit roles for specific users on the Access Manager page if you configure role mappings for IdP groups. Atlas CLI Atlas UI To update roles for a team in the project you specify using the
Atlas CLI, run the following command: atlas projects teams update <teamId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas projects teams update . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Note Atlas CLI Limitation You can't update a user's role in a project using the
Atlas CLI. To edit the project roles for a user or team using the
Atlas UI: 1 In Atlas , go to the Project Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Select Project Access from the Access Manager menu in the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Access Manager in the sidebar. The Project Access Manager page displays. 2 Edit an Atlas user or team. To edit an Atlas user, click the Users tab. To edit a team, click the Teams tab. 3 Update permissions. In the Actions column, click Edit
Permissions next to the Atlas user or team whose permissions you
want to modify. 4 Select the appropriate role or roles for the Atlas user or team. 5 Click to save. Back Project Access Next Settings
