# Manage Organization Teams - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Organization Access Manage Organization Teams On this page Required Access Create a Team View Teams Add Team Members Remove Team Members Rename a Team Delete a Team Next Steps You can create teams at the organization level and add teams to
projects to grant project access roles to multiple users. Add any
number of organization users to a team. Grant a team roles for specific projects. All members of a team share
the same project access. Organization users can belong to multiple
teams. To add teams to a project or edit team roles, see Manage Access to a Project . Required Access To perform any of the following actions, you must have Organization Owner access to Atlas . Create a Team Important Atlas limits the number of users to a maximum of 100 teams per
project and a maximum of 250 teams per organization. Atlas CLI Atlas UI To create one team in your organization using the
Atlas CLI, run the following command: atlas teams create <name> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas teams create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To add users to your team, see Add Team Members . To create a team using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Click Create Team . 3 Enter a name for the team in the Name Your Team box. Note The name must be unique within an organization. 4 Add team members. To add existing organization users to the team, click in the Add Members box and either start typing their Cloud Manager username or click on the name of a user that appears in
the combo box. 5 Click Create Team . View Teams Atlas CLI Atlas UI To list all teams in your organization using the Atlas CLI, run the following command: atlas teams list [options] To return the details for the team you specify using the Atlas CLI, run the following command: atlas teams describe [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas teams list and atlas teams describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view your teams using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Click the Teams tab. Your teams display. Add Team Members Important Atlas limits Atlas user membership to a maximum of 250 Atlas users per team. Atlas CLI Atlas UI To add one user to the team you specify using the
Atlas CLI, run the following command: atlas teams users add <userId>... [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas teams users add . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To add team members using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Click the Teams tab. 3 Click the name of the team you want to modify. 4 Add members to the team. Click Add Members . Type the name or email of the user from the combo box. You can add users that are part of the organization or
users that have been sent an invitation to join the organization. Click Add Members . Remove Team Members Atlas CLI Atlas UI To delete one user from the team you specify using the
Atlas CLI, run the following command: atlas teams users delete <userId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas teams users delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To remove team members using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Click the Teams tab. 3 Click the name of the team you want to modify. 4 Remove members from the team. Click to the right of the user you want to remove
from a team. Removing a member from the team removes the user's project
assignments granted by the team membership. If a user is assigned to a project through both a team and
individual assignment, removing the user from a team does not
remove the user's assignment to that project. Rename a Team Note Atlas CLI Limitation You can't rename a team using the Atlas CLI. 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Click the Teams tab. 3 Rename the team. For the team you want to rename: Click the ellipsis ( ... ) button under the Actions column. Click Rename Team . Enter a new name for the team. The team name must be unique within the organization. Click Rename Team . Delete a Team Atlas CLI Atlas UI To delete one team from your organization using the
Atlas CLI, run the following command: atlas teams delete <teamId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas teams delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To delete a team using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Click the Teams tab. 3 Delete the team. For the team you want to delete: Click the ellipsis ( ... ) button under the Actions column. Click Delete Team . Confirm that you wish to proceed with team deletion. For users belonging to the team, deleting a team removes the
users' project assignments granted by that team membership. Next Steps For the organization users in a team to have access to a project, you
must add the team to the project. To add teams to a project or edit
team roles, see Manage Access to a Project . Back Users Next Settings
